#!/usr/bin/env python3
"""
OmniRoute Combo Auto-Updater
============================
Automatically probes OmniRoute for available providers/models, tests them,
creates/updates combos in OmniRoute, updates combos.md with working/failed status,
updates opencode.jsonc, and optionally pushes to GitHub.

Usage:
    python update_combos.py                          # Dry run (no file changes)
    python update_combos.py --write                  # Update combos.md + opencode.jsonc
    python update_combos.py --write --push           # Update and push to GitHub
    python update_combos.py --test-only              # Only test models, don't update file
    python update_combos.py --sync-combos            # Create/update combos in OmniRoute
    python update_combos.py --sync-combos --write --push  # Full pipeline
    python update_combos.py --init-config            # Create config.yaml template
"""

import argparse
import asyncio
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any

import aiohttp
import yaml

# Optional: openpyxl for reading providers.xlsx
try:
    import openpyxl
    HAS_OPENPYXL = True
except ImportError:
    HAS_OPENPYXL = False


# ============================================================================
# Configuration
# ============================================================================

@dataclass
class Config:
    """Configuration loaded from config file or environment."""
    omniroute_url: str = "http://127.0.0.1:20128"
    api_key: str = ""
    combos_md_path: str = "docs/COMBOS.md"
    opencode_jsonc_path: str = "omniroute-migration/opencode.jsonc"
    providers_xlsx_path: str = "omniroute-providers.xlsx"
    test_timeout: int = 30
    test_concurrency: int = 10
    test_prompt: str = "Say 'OK' if you can respond."
    github_repo: str = ""
    github_branch: str = "main"
    commit_message_prefix: str = "chore: update combos.md"
    auto_create_combos: bool = True
    min_models_for_combo: int = 1
    
    @classmethod
    def from_env(cls) -> "Config":
        cfg = cls()
        cfg.omniroute_url = os.getenv("OMNIROUTE_URL", cfg.omniroute_url)
        cfg.api_key = os.getenv("OMNIROUTE_API_KEY", cfg.api_key)
        cfg.combos_md_path = os.getenv("COMBOS_MD_PATH", cfg.combos_md_path)
        cfg.opencode_jsonc_path = os.getenv("OPENCODE_JSONC_PATH", cfg.opencode_jsonc_path)
        cfg.providers_xlsx_path = os.getenv("PROVIDERS_XLSX_PATH", cfg.providers_xlsx_path)
        cfg.github_repo = os.getenv("GITHUB_REPO", cfg.github_repo)
        cfg.github_branch = os.getenv("GITHUB_BRANCH", cfg.github_branch)
        return cfg
    
    @classmethod
    def from_file(cls, path: Path) -> "Config":
        if path.suffix in ('.yaml', '.yml'):
            with open(path) as f:
                data = yaml.safe_load(f) or {}
        elif path.suffix == '.json':
            with open(path) as f:
                data = json.load(f)
        else:
            raise ValueError(f"Unsupported config format: {path.suffix}")
        
        cfg = cls()
        for key, value in data.items():
            if hasattr(cfg, key):
                setattr(cfg, key, value)
        return cfg


# ============================================================================
# Data Models
# ============================================================================

@dataclass
class ModelInfo:
    id: str
    provider: str
    owned_by: str
    context_length: int = 0
    max_output_tokens: int = 0
    capabilities: Dict = field(default_factory=dict)


@dataclass
class TestResult:
    model_id: str
    success: bool
    latency_ms: float
    error: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))


@dataclass
class ComboDefinition:
    name: str
    strategy: str = "priority"
    max_global_attempts: int = 200
    models: List[str] = field(default_factory=list)  # model IDs in priority order
    description: str = ""
    display_name: str = ""
    
    def to_omniroute_payload(self) -> Dict[str, Any]:
        """Convert to OmniRoute API payload."""
        return {
            "name": self.name.replace("combo/", ""),
            "strategy": self.strategy,
            "models": [
                {"kind": "model", "model": m, "providerId": m.split("/")[0] if "/" in m else "auto"}
                for m in self.models
            ],
            "config": {"maxGlobalAttempts": self.max_global_attempts},
            "description": self.description,
            "displayName": self.display_name or self.name,
        }


@dataclass
class ProviderInfo:
    name: str
    active_connections: int
    total_models: int
    models: List[str]
    has_combo: bool = False


# ============================================================================
# OmniRoute Client
# ============================================================================

class OmniRouteClient:
    def __init__(self, config: Config):
        self.config = config
        self.session: Optional[aiohttp.ClientSession] = None
        self.headers = {"Authorization": f"Bearer {config.api_key}"} if config.api_key else {}
    
    async def __aenter__(self):
        timeout = aiohttp.ClientTimeout(total=self.config.test_timeout)
        self.session = aiohttp.ClientSession(timeout=timeout, headers=self.headers)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def get_models(self) -> List[ModelInfo]:
        """Fetch all models from OmniRoute /v1/models endpoint."""
        async with self.session.get(f"{self.config.omniroute_url}/v1/models") as resp:
            resp.raise_for_status()
            data = await resp.json()
        
        models = []
        for m in data.get("data", []):
            model_id = m.get("id", "")
            parts = model_id.split("/", 1)
            provider = parts[0] if len(parts) > 1 else "unknown"
            models.append(ModelInfo(
                id=model_id,
                provider=provider,
                owned_by=m.get("owned_by", ""),
                context_length=m.get("context_length", 0),
                max_output_tokens=m.get("max_output_tokens", 0),
                capabilities=m.get("capabilities", {}),
            ))
        return models
    
    async def test_model(self, model_id: str) -> TestResult:
        """Test a single model with a simple prompt."""
        start = time.time()
        try:
            payload = {
                "model": model_id,
                "messages": [{"role": "user", "content": self.config.test_prompt}],
                "max_tokens": 10,
                "temperature": 0,
            }
            async with self.session.post(
                f"{self.config.omniroute_url}/v1/chat/completions",
                json=payload
            ) as resp:
                latency = (time.time() - start) * 1000
                if resp.status == 200:
                    data = await resp.json()
                    if data.get("choices") and data["choices"][0].get("message", {}).get("content"):
                        return TestResult(model_id=model_id, success=True, latency_ms=latency)
                    return TestResult(model_id=model_id, success=False, latency_ms=latency, error="Empty response")
                else:
                    error_text = await resp.text()
                    return TestResult(model_id=model_id, success=False, latency_ms=latency, error=f"HTTP {resp.status}: {error_text[:200]}")
        except asyncio.TimeoutError:
            return TestResult(model_id=model_id, success=False, latency_ms=self.config.test_timeout * 1000, error="Timeout")
        except Exception as e:
            latency = (time.time() - start) * 1000
            return TestResult(model_id=model_id, success=False, latency_ms=latency, error=str(e))
    
    async def test_models(self, model_ids: List[str]) -> List[TestResult]:
        """Test multiple models concurrently."""
        semaphore = asyncio.Semaphore(self.config.test_concurrency)
        
        async def test_with_sem(model_id: str) -> TestResult:
            async with semaphore:
                return await self.test_model(model_id)
        
        tasks = [test_with_sem(mid) for mid in model_ids]
        return await asyncio.gather(*tasks)
    
    # Combo Management API
    async def get_combos(self) -> List[Dict[str, Any]]:
        """Fetch all combos from OmniRoute."""
        async with self.session.get(f"{self.config.omniroute_url}/api/combos") as resp:
            resp.raise_for_status()
            data = await resp.json()
        return data.get("combos", [])
    
    async def get_combo_by_name(self, combo_name: str) -> Optional[Dict[str, Any]]:
        """Fetch a specific combo by name (searches all combos)."""
        combos = await self.get_combos()
        for combo in combos:
            if combo.get("name") == combo_name:
                return combo
        return None
    
    async def get_combo_by_id(self, combo_id: str) -> Optional[Dict[str, Any]]:
        """Fetch a specific combo by ID."""
        async with self.session.get(f"{self.config.omniroute_url}/api/combos/{combo_id}") as resp:
            if resp.status == 404:
                return None
            resp.raise_for_status()
            return await resp.json()
    
    async def create_combo(self, combo: ComboDefinition) -> Dict[str, Any]:
        """Create a new combo in OmniRoute."""
        payload = combo.to_omniroute_payload()
        async with self.session.post(
            f"{self.config.omniroute_url}/api/combos",
            json=payload
        ) as resp:
            resp.raise_for_status()
            return await resp.json()
    
    async def update_combo(self, combo_id: str, combo: ComboDefinition) -> Dict[str, Any]:
        """Update an existing combo in OmniRoute."""
        payload = combo.to_omniroute_payload()
        payload["id"] = combo_id
        async with self.session.put(
            f"{self.config.omniroute_url}/api/combos/{combo_id}",
            json=payload
        ) as resp:
            resp.raise_for_status()
            return await resp.json()
    
    async def upsert_combo(self, combo: ComboDefinition) -> Tuple[Dict[str, Any], bool]:
        """Create or update a combo. Returns (combo_data, created_flag)."""
        # First check if combo exists by name (strip "combo/" prefix)
        combo_name = combo.name.replace("combo/", "")
        existing = await self.get_combo_by_name(combo_name)
        if existing:
            combo_id = existing.get("id")
            result = await self.update_combo(combo_id, combo)
            return result, False
        else:
            result = await self.create_combo(combo)
            return result, True
    
    async def delete_combo(self, combo_id: str) -> bool:
        """Delete a combo from OmniRoute."""
        async with self.session.delete(f"{self.config.omniroute_url}/api/combos/{combo_id}") as resp:
            return resp.status == 200


# ============================================================================
# Provider Discovery
# ============================================================================

class ProviderDiscovery:
    def __init__(self, config: Config):
        self.config = config
    
    def get_active_providers_from_xlsx(self) -> Dict[str, ProviderInfo]:
        """Read providers.xlsx and return providers with active connections."""
        if not HAS_OPENPYXL:
            print("[WARN] openpyxl not installed, skipping providers.xlsx discovery")
            return {}
        
        if not Path(self.config.providers_xlsx_path).exists():
            print(f"[WARN] providers.xlsx not found at {self.config.providers_xlsx_path}")
            return {}
        
        wb = openpyxl.load_workbook(self.config.providers_xlsx_path)
        providers: Dict[str, ProviderInfo] = {}
        
        for sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            active_count = 0
            rows_data = list(ws.iter_rows(values_only=True))
            
            if not rows_data:
                continue
            
            # First row is header
            for row in rows_data[1:]:
                if not row or not row[0]:
                    continue
                conn_name = str(row[0])
                active = row[2] if len(row) > 2 else False
                if active is True and not conn_name.startswith("MISSING:"):
                    active_count += 1
            
            if active_count > 0:
                providers[sheet_name] = ProviderInfo(
                    name=sheet_name,
                    active_connections=active_count,
                    total_models=0,  # Will be filled later
                    models=[],
                )
        
        return providers
    
    def enrich_with_models(self, providers: Dict[str, ProviderInfo], models: List[ModelInfo]) -> Dict[str, ProviderInfo]:
        """Add model information to providers."""
        model_by_provider: Dict[str, List[str]] = {}
        for m in models:
            if m.owned_by != "combo":
                if m.provider not in model_by_provider:
                    model_by_provider[m.provider] = []
                model_by_provider[m.provider].append(m.id)
        
        for name, info in providers.items():
            info.models = model_by_provider.get(name, [])
            info.total_models = len(info.models)
        
        return providers
    
    def discover_new_providers(self, providers: Dict[str, ProviderInfo], builtin_combos: Dict[str, ComboDefinition]) -> List[ProviderInfo]:
        """Find providers with active connections but no combo defined."""
        # Extract provider names that already have combos
        combo_providers = set()
        for combo in builtin_combos.values():
            for model in combo.models:
                if "/" in model:
                    provider = model.split("/")[0]
                    combo_providers.add(provider)
        
        # Also check combo names for provider hints
        for combo_id in builtin_combos.keys():
            if combo_id.endswith("-best"):
                provider_hint = combo_id.replace("-best", "")
                combo_providers.add(provider_hint)
        
        new_providers = []
        for name, info in providers.items():
            if name not in combo_providers and info.total_models >= self.config.min_models_for_combo:
                info.has_combo = False
                new_providers.append(info)
            elif name in combo_providers:
                info.has_combo = True
        
        return new_providers


# ============================================================================
# Auto Combo Generator
# ============================================================================

class AutoComboGenerator:
    """Generate combo definitions for newly discovered providers."""
    
    # Provider-specific model sorting/priority rules
    PROVIDER_PRIORITY_RULES = {
        "aug": {
            "priority_keywords": ["sonnet", "opus", "haiku"],
            "sort_order": ["opus", "sonnet", "haiku", "fable"],
        },
        "gemini-web": {
            "priority_keywords": ["pro", "flash"],
            "sort_order": ["pro", "flash"],
        },
        "ollama-cloud": {
            "priority_keywords": ["ultra", "super", "nemotron"],
            "sort_order": ["nemotron-3-ultra", "nemotron-3-super", "gemma", "beam"],
        },
        "cx": {
            "priority_keywords": ["gpt-6", "gpt-5"],
            "sort_order": ["gpt-6", "gpt-5"],
        },
        "cxa": {
            "priority_keywords": ["gpt-6", "astra", "sol"],
            "sort_order": ["gpt-6-astra", "gpt-6-sol", "gpt-5"],
        },
        "dva": {
            "priority_keywords": ["opus", "sonnet"],
            "sort_order": ["opus", "sonnet"],
        },
        "zc": {
            "priority_keywords": ["glm"],
            "sort_order": ["glm"],
        },
    }
    
    @classmethod
    def generate_combo_for_provider(cls, provider: ProviderInfo) -> ComboDefinition:
        """Generate a combo definition for a provider."""
        models = provider.models
        
        # Apply provider-specific sorting
        rules = cls.PROVIDER_PRIORITY_RULES.get(provider.name, {})
        sort_order = rules.get("sort_order", [])
        
        def sort_key(model: str) -> Tuple[int, str]:
            model_lower = model.lower()
            for i, keyword in enumerate(sort_order):
                if keyword.lower() in model_lower:
                    return (i, model)
            return (len(sort_order), model)
        
        sorted_models = sorted(models, key=sort_key)
        
        # Create display name
        display_name = provider.name.replace("-", " ").replace("_", " ").title()
        display_name = display_name.replace("Ai", "AI").replace("Cli", "CLI").replace("Web", "Web")
        
        return ComboDefinition(
            name=f"combo/{provider.name}-best",
            strategy="priority",
            max_global_attempts=200,
            models=sorted_models,
            description=f"Auto-discovered {display_name} models",
            display_name=f"{display_name} Best (auto-discovered)",
        )


# ============================================================================
# OpenCode Config Updater
# ============================================================================

class OpenCodeConfigUpdater:
    def __init__(self, config: Config):
        self.config = config
        self.path = Path(config.opencode_jsonc_path)
    
    def read_config(self) -> Dict[str, Any]:
        """Read and parse opencode.jsonc (strip comments)."""
        content = self.path.read_text(encoding="utf-8")
        # Simple JSONC parsing - remove line comments, but handle URLs with //
        lines = []
        for line in content.split("\n"):
            # Remove inline comments but keep strings intact
            in_string = False
            escaped = False
            cleaned = ""
            i = 0
            while i < len(line):
                ch = line[i]
                if not in_string and ch == '"' and not escaped:
                    in_string = True
                elif in_string and ch == '"' and not escaped:
                    in_string = False
                elif in_string and ch == "\\" and not escaped:
                    escaped = True
                    cleaned += ch
                    i += 1
                    continue
                elif not in_string and ch == "/" and i + 1 < len(line) and line[i + 1] == "/":
                    # Check if this is a URL protocol (http:// or https://)
                    if i >= 5 and line[i-5:i] in ("http:", "https:"):
                        cleaned += ch
                    else:
                        break
                cleaned += ch
                escaped = False
                i += 1
            lines.append(cleaned)
        return json.loads("\n".join(lines))
    
    def write_config(self, data: Dict[str, Any]) -> None:
        """Write config with preserved formatting."""
        # Use json.dumps with indent, then add back comments if needed
        content = json.dumps(data, indent=2)
        self.path.write_text(content + "\n", encoding="utf-8")
        print(f"[OK] Updated {self.path}")
    
    def update_model_entries(self, combos: Dict[str, ComboDefinition]) -> Tuple[int, int]:
        """Add/update model entries in opencode.jsonc for combos. Returns (added, updated)."""
        data = self.read_config()
        
        # Combo models are under provider.omniroute.models
        if "provider" not in data:
            data["provider"] = {}
        if "omniroute" not in data["provider"]:
            data["provider"]["omniroute"] = {}
        if "models" not in data["provider"]["omniroute"]:
            data["provider"]["omniroute"]["models"] = {}
        
        models_dict = data["provider"]["omniroute"]["models"]
        
        added = 0
        updated = 0
        
        for combo_id, combo in combos.items():
            model_key = combo.name  # e.g., "combo/gemini-web-best"
            
            # Build model config
            model_config = {
                "name": combo.display_name or combo.name,
                "attachment": True,
                "reasoning": True,
                "temperature": True,
                "tool_call": True,
                "limit": {
                    "context": 131072,
                    "output": 32768,
                    "input": 131072
                }
            }
            
            if model_key in models_dict:
                # Preserve any existing custom fields
                existing = models_dict[model_key]
                for k, v in existing.items():
                    if k not in model_config:
                        model_config[k] = v
                updated += 1
            else:
                added += 1
            
            models_dict[model_key] = model_config
        
        self.write_config(data)
        return added, updated


# ============================================================================
# Combo Markdown Generator
# ============================================================================

class ComboMarkdownGenerator:
    def __init__(self, config: Config):
        self.config = config
        self.path = Path(config.combos_md_path)
    
    def generate(self, combos: Dict[str, ComboDefinition], results: Dict[str, TestResult]) -> str:
        """Generate the full COMBOS.md content."""
        lines = []
        
        # Header
        lines.append("# Combos - full leg lists")
        lines.append("")
        lines.append("[Back to README](../README.md)")
        lines.append("")
        lines.append("Every OmniRoute combo on this machine, with each leg and its 30-day success rate.")
        lines.append("A `priority` combo stops at the **first leg that answers**, so leg order is the ranking.")
        lines.append("")
        lines.append(f"> **Updated {datetime.now(timezone.utc).strftime('%Y-%m-%d')}:** Auto-generated from live OmniRoute catalog.")
        lines.append("")
        
        # Combo index
        lines.append("## Combo index")
        lines.append("")
        for combo_id in sorted(combos.keys()):
            lines.append(f"- [`{combos[combo_id].name}`](#combo{combo_id.replace('-', '-')})")
        lines.append("")
        
        # Summary table
        lines.append("---")
        lines.append("")
        lines.append("| Combo | Legs | Working | Failed | Status |")
        lines.append("|---|---:|---:|---:|---|")
        
        for combo_id in sorted(combos.keys()):
            combo = combos[combo_id]
            working = sum(1 for m in combo.models if results.get(m, TestResult(m, False, 0, "not tested")).success)
            failed = sum(1 for m in combo.models if not results.get(m, TestResult(m, False, 0, "not tested")).success)
            status_icon = "✅" if failed == 0 else ("⚠️" if working > 0 else "❌")
            lines.append(f"| `{combo.name}` | {len(combo.models)} | {working} | {failed} | {status_icon} |")
        
        lines.append("")
        
        # Detailed combo sections
        for combo_id in sorted(combos.keys()):
            combo = combos[combo_id]
            lines.append(f"<a id=\"combo{combo_id.replace('-', '-')}\"></a>")
            lines.append(f"### {combo.name}")
            lines.append("")
            
            # Strategy info
            if combo.strategy != "priority" or combo.max_global_attempts != 200:
                lines.append(f"**Strategy** `{combo.strategy}` · **maxGlobalAttempts** {combo.max_global_attempts}")
                lines.append("")
            
            if combo.description:
                lines.append(combo.description)
                lines.append("")
            
            # Model table
            lines.append("| # | Model | Status | Latency |")
            lines.append("|---|-------|--------|---------|")
            
            for i, model_id in enumerate(combo.models, 1):
                result = results.get(model_id, TestResult(model_id, False, 0, "not tested"))
                status = "✅" if result.success else "❌"
                latency = f"{result.latency_ms:.0f}ms" if result.latency_ms > 0 else "-"
                
                # Strike through failed models
                model_display = f"`{model_id}`" if result.success else f"~~`{model_id}`~~"
                if not result.success and result.error and result.error != "not tested":
                    status += f" - {result.error[:60]}"
                
                lines.append(f"| {i} | {model_display} | {status} | {latency} |")
            
            lines.append("")
        
        return "\n".join(lines)
    
    def write(self, content: str) -> None:
        """Write content to combos.md."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(content, encoding="utf-8")
        print(f"[OK] Written to {self.path}")


# ============================================================================
# Git Operations
# ============================================================================

class GitOperator:
    def __init__(self, repo_path: Path, config: Config):
        self.repo_path = repo_path
        self.config = config
    
    def is_git_repo(self) -> bool:
        return (self.repo_path / ".git").exists()
    
    def get_status(self) -> str:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=self.repo_path, capture_output=True, text=True
        )
        return result.stdout.strip()
    
    def add(self, files: List[str]) -> bool:
        result = subprocess.run(
            ["git", "add"] + files,
            cwd=self.repo_path, capture_output=True, text=True
        )
        return result.returncode == 0
    
    def commit(self, message: str) -> bool:
        result = subprocess.run(
            ["git", "commit", "-m", message],
            cwd=self.repo_path, capture_output=True, text=True
        )
        return result.returncode == 0
    
    def push(self, remote: str = "origin", branch: str = "") -> bool:
        branch = branch or self.config.github_branch
        result = subprocess.run(
            ["git", "push", remote, branch],
            cwd=self.repo_path, capture_output=True, text=True
        )
        return result.returncode == 0
    
    def get_current_branch(self) -> str:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=self.repo_path, capture_output=True, text=True
        )
        return result.stdout.strip()
    
    def get_remote_url(self, remote: str = "origin") -> str:
        result = subprocess.run(
            ["git", "remote", "get-url", remote],
            cwd=self.repo_path, capture_output=True, text=True
        )
        return result.stdout.strip()


# ============================================================================
# Built-in Combo Definitions
# ============================================================================

BUILTIN_COMBOS: Dict[str, ComboDefinition] = {
    "agy-antigravity-best": ComboDefinition(
        name="combo/agy-antigravity-best",
        strategy="priority",
        models=[
            "antigravity/claude-opus-4-6-thinking",
            "agy/claude-opus-4-6-thinking",
            "antigravity/claude-sonnet-4-6",
            "agy/claude-sonnet-4-6",
            "antigravity/gemini-3.8-flash-tiered",
            "agy/gemini-3.8-flash-tiered",
            "agy/gemini-3.8-flash-medium",
            "agy/gemini-3.8-flash-high",
            "agy/gemini-3.8-flash-low",
            "agy/gemini-3.1-flash-lite",
            "agy/gemini-3.5-flash-lite",
            "agy/gemini-3-flash",
            "antigravity/gemini-3.1-flash-lite",
            "antigravity/gemini-3-flash",
            "antigravity/gemini-3.5-flash-lite",
        ],
        description="AGY + Antigravity Claude and Gemini",
        display_name="AGY + Antigravity Best",
    ),
    "claude-best": ComboDefinition(
        name="combo/claude-best",
        strategy="priority",
        models=[
            "antigravity/claude-opus-4-6-thinking",
            "agy/claude-opus-4-6-thinking",
            "antigravity/claude-sonnet-4-6",
            "agy/claude-sonnet-4-6",
            "auto/best-coding",
        ],
        description="Best Claude models via antigravity and agy",
        display_name="Claude Best",
    ),
    "cloudflare-best": ComboDefinition(
        name="combo/cloudflare-best",
        strategy="priority",
        models=[
            "cloudflare-ai/@cf/qwen/qwen2.5-coder-32b-instruct",
            "cloudflare-ai/@cf/qwen/qwq-32b",
            "cloudflare-ai/@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "cfp/qwen/qwq-32b",
            "cfp/qwen/qwen3-30b-a3b-fp8",
            "cfp/deepseek-ai/deepseek-r1-distill-qwen-32b",
            "cfp/mistralai/mistral-small-3.1-24b-instruct",
            "cloudflare-ai/@cf/mistral/mistral-7b-instruct-v0.2-lora",
            "cloudflare-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "cloudflare-ai/@cf/google/gemma-4-26b-a4b-it",
            "cfp/google/gemma-4-26b-a4b-it",
            "cfp/aisingapore/gemma-sea-lion-v4-27b-it",
            "cfp/mistralai/mistral-small-3.1-24b-instruct",
            "cloudflare-ai/@cf/meta/llama-3.2-3b-instruct",
            "cloudflare-ai/@cf/mistral/mistral-7b-instruct-v0.2-lora",
        ],
        description="Cloudflare Workers AI + CFP models",
        display_name="Cloudflare Best",
    ),
    "codex-best": ComboDefinition(
        name="combo/codex-best",
        strategy="priority",
        models=[
            "codex/gpt-6-luna-max",
            "codex/gpt-6-luna-xhigh",
            "codex/gpt-6-luna-high",
            "codex/gpt-6-luna",
            "codex/gpt-6-luna-medium",
            "codex/gpt-6-luna-low",
            "codex/gpt-5.6-terra-max",
            "codex/gpt-5.6-terra-xhigh",
            "codex/gpt-5.6-terra-high",
            "codex/gpt-5.6-terra",
            "codex/gpt-5.6-terra-medium",
            "codex/gpt-5.6-terra-low",
            "codex/gpt-5.6-luna-max",
            "codex/gpt-5.6-luna-xhigh",
            "codex/gpt-5.6-luna-high",
            "codex/gpt-5.6-luna",
            "codex/gpt-5.6-luna-medium",
            "codex/gpt-5.6-luna-low",
            "codex/gpt-reserve-max",
            "codex/gpt-reserve-xhigh",
            "codex/gpt-reserve-high",
            "codex/gpt-reserve",
            "codex/gpt-reserve-medium",
            "codex/gpt-reserve-low",
            "codex/codex-auto-review-max",
            "codex/codex-auto-review-xhigh",
            "codex/codex-auto-review-high",
            "codex/codex-auto-review",
            "codex/codex-auto-review-medium",
            "codex/codex-auto-review-low",
        ],
        description="Codex GPT models",
        display_name="Codex Best",
    ),
    "coding-elite": ComboDefinition(
        name="combo/coding-elite",
        strategy="priority",
        models=[
            "codestral/codestral-latest",
            "mistral/mistral-code-fim-latest",
            "codestral/codestral-2508",
            "mistral/codestral-2508",
            "mistral/codestral-latest",
            "cloudflare-ai/@cf/qwen/qwen2.5-coder-32b-instruct",
            "mistral/mistral-code-latest",
            "free-ai/qwen3-coder",
            "free-ai/qwen-coder",
            "codex/gpt-6-luna",
            "antigravity/claude-opus-4-6-thinking",
            "agy/claude-opus-4-6-thinking",
            "antigravity/claude-sonnet-4-6",
            "agy/claude-sonnet-4-6",
            "codex/gpt-reserve",
            "codex/gpt-5.6-terra",
            "codex/gpt-5.6-luna",
            "openadapter/GPT-6-Luna",
            "grok-cli/grok-4.7-xhigh",
            "openadapter/0G-DeepSeek-v4-Flash",
            "openadapter/DeepSeek-V4.1-Flash",
            "openadapter/DeepSeek-V4-Flash",
            "openadapter/0G-DeepSeek-V3",
            "openadapter/Qwen3.8-27B",
            "openadapter/Kimi-K2-Think",
            "openadapter/GLM-5.3-Flash",
            "openadapter/GLM-4.7-Flash",
            "openadapter/MiMo-V2.6-Pro",
            "openadapter/MiMo-V2.6-Flash",
            "openadapter/gpt-oss-120b",
            "openadapter/Llama-3.1-405B",
            "antigravity/gemini-3.8-flash-tiered",
            "antigravity/gemini-3.8-flash-medium",
            "antigravity/gemini-3.8-flash-high",
            "agy/gemini-3.8-flash-tiered",
            "agy/gemini-3.8-flash-medium",
            "agy/gemini-3.8-flash-high",
            "antigravity/gemini-3.5-flash-lite",
            "agy/gemini-3.5-flash-lite",
            "antigravity/gemini-3.1-flash-lite",
            "agy/gemini-3.1-flash-lite",
            "codex/codex-auto-review",
            "nvidia/poolside/laguna-xs-2.1",
            "mistral/ministral-14b-latest",
            "openadapter/MiMo-V2.5-Pro",
            "mistral/mistral-large-4",
            "cloudflare-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast",
            "cloudflare-ai/@cf/qwen/qwq-32b",
            "antigravity/gemini-3-flash",
            "ollama-cloud/gemma4:31b",
            "openadapter/Gemma-4-31B-TEE",
            "openadapter/Hermes-4-14B",
            "openadapter/gemma-4-31b-it",
            "mistral/ministral-8b-latest",
            "openadapter/Gemma-3-27B",
            "free-ai/mistral",
        ],
        description="Daily driver - best coding models ranked by quality",
        display_name="Coding Elite",
    ),
    "free-ai-best": ComboDefinition(
        name="combo/free-ai-best",
        strategy="priority",
        models=[
            "free-ai/qwen3-coder",
            "free-ai/qwen-coder",
            "free-ai/deepseek-r1",
            "free-ai/mistral",
            "free-ai/qwen3-8b",
            "free-ai/qwen7b",
            "free-ai/deepseek-r1-7b",
        ],
        description="Completely free models across multiple providers",
        display_name="Free AI Best",
    ),
    "gemini-best": ComboDefinition(
        name="combo/gemini-best",
        strategy="priority",
        models=[
            "agy/gemini-3.8-flash-tiered",
            "agy/gemini-3.8-flash-medium",
            "antigravity/gemini-3.8-flash-tiered",
            "agy/gemini-3.8-flash-high",
            "agy/gemini-3.8-flash-low",
            "agy/gemini-3.5-flash-lite",
            "antigravity/gemini-3.5-flash-lite",
            "agy/gemini-3.1-flash-lite",
            "antigravity/gemini-3.1-flash-lite",
            "agy/gemini-3-flash",
            "antigravity/gemini-3-flash",
        ],
        description="Best Gemini models via antigravity and agy",
        display_name="Gemini Best",
    ),
    "gemini-web-best": ComboDefinition(
        name="combo/gemini-web-best",
        strategy="priority",
        models=[
            "gemini-web/gemini-3.7-flash",
            "gemini-web/gemini-3.1-pro",
            "gemini-web/gemini-3.1-flash-lite",
        ],
        description="Gemini Web free models",
        display_name="Gemini Web Best",
    ),
    "gpt-best": ComboDefinition(
        name="combo/gpt-best",
        strategy="priority",
        models=[
            "codex/gpt-6-luna",
            "codex/gpt-5.6-luna",
            "codex/gpt-5.6-terra",
            "codex/gpt-6-luna-max",
            "codex/gpt-6-luna-high",
            "codex/gpt-6-luna-xhigh",
            "codex/gpt-6-luna-medium",
            "codex/gpt-6-luna-low",
            "codex/gpt-5.6-luna-max",
            "codex/gpt-5.6-terra-max",
            "codex/gpt-5.6-luna-high",
            "codex/gpt-5.6-luna-xhigh",
            "codex/gpt-5.6-terra-high",
            "codex/gpt-5.6-terra-xhigh",
            "codex/gpt-5.6-luna-medium",
            "codex/gpt-5.6-luna-low",
            "codex/gpt-5.6-terra-low",
            "codex/gpt-5.6-terra-ultra",
            "codex/gpt-5.6-terra-medium",
            "nvidia/openai/gpt-oss-20b",
            "agy/gpt-oss-120b-medium",
            "antigravity/gpt-oss-120b-medium",
            "ddgw/gpt-5.6-luna",
            "ddgw/gpt-5.4-mini",
            "cfp/openai/gpt-oss-120b",
            "cfp/openai/gpt-oss-20b",
            "ddgw/tinfoil/gpt-oss-120b",
        ],
        description="GPT models via CX + Codex",
        display_name="GPT Best",
    ),
    "grok-best": ComboDefinition(
        name="combo/grok-best",
        strategy="priority",
        models=[
            "grok-cli/grok-4.7-high",
            "grok-cli/grok-4.7-low",
            "grok-cli/grok-4.7-xhigh",
            "grok-cli/grok-4.7",
            "grok-cli/grok-4.7-medium",
            "grok-web/fast",
            "auto/best-coding",
        ],
        description="Grok CLI + Web models",
        display_name="Grok Best",
    ),
    "groq-best": ComboDefinition(
        name="combo/groq-best",
        strategy="priority",
        models=[
            "groq/openai/gpt-oss-120b",
            "groq/qwen/qwen3.8-27b",
            "groq/openai/gpt-oss-20b",
            "groq/openai/gpt-oss-safeguard-20b",
            "groq/allam-2-7b",
            "auto/best-coding",
        ],
        description="Groq fast inference models",
        display_name="Groq Best",
    ),
    "inceptionai-best": ComboDefinition(
        name="combo/inceptionai-best",
        strategy="priority",
        models=[
            "inceptionai/mercury-3",
        ],
        description="Inception Labs Mercury-3",
        display_name="Inception Labs Best",
    ),
    "kilocode-best": ComboDefinition(
        name="combo/kilocode-best",
        strategy="priority",
        models=[
            "kilocode/nvidia/nemotron-3-ultra-550b-a55b:free",
            "kilocode/stealth/glyph-cluster",
            "kilocode/reflection/beam-free",
            "kilocode/cohere/north-mini-code:free",
            "kilocode/nvidia/nemotron-3.5-super-vl:free",
            "kilocode/nvidia/nemotron-3.5-lightning:free",
            "kilocode/dots-studio/dots-3-note-preview:free",
            "kilocode/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
            "kilocode/kilo-auto/small",
            "kilocode/kilo-auto/free",
            "kilocode/openrouter/free",
        ],
        description="KiloCode free models ranked by coding quality",
        display_name="KiloCode Best (free)",
    ),
    "mistral-best": ComboDefinition(
        name="combo/mistral-best",
        strategy="priority",
        models=[
            "codestral/codestral-latest",
            "codestral/codestral-2508",
            "mistral/codestral-latest",
            "mistral/codestral-2508",
            "mistral/mistral-code-latest",
            "mistral/mistral-code-fim-latest",
            "mistral/ministral-14b-latest",
            "mistral/ministral-8b-latest",
            "mistral/ministral-3b-latest",
            "mistral/ministral-3b-2512",
            "mistral/ministral-8b-2512",
            "mistral/ministral-14b-2512",
        ],
        description="Mistral AI models via mistral and codestral",
        display_name="Mistral Best",
    ),
    "morph-best": ComboDefinition(
        name="combo/morph-best",
        strategy="priority",
        models=[
            "morph/morph-v3-fast",
            "morph/morph-v3-large",
        ],
        description="Morph fast reasoning and coding",
        display_name="Morph Best",
    ),
    "nvidia-best": ComboDefinition(
        name="combo/nvidia-best",
        strategy="priority",
        models=[
            "nvidia/nvidia/nemotron-3.5-content-safety",
            "openrouter/nvidia/nemotron-3.5-lightning:free",
            "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free",
            "openrouter/nvidia/nemotron-3.5-content-safety:free",
            "kilocode/nvidia/nemotron-3.5-lightning:free",
            "kilocode/nvidia/nemotron-3.5-content-safety:free",
            "auto/best-coding",
        ],
        description="NVIDIA NIM models",
        display_name="NVIDIA Best",
    ),
    "ollama-cloud-best": ComboDefinition(
        name="combo/ollama-cloud-best",
        strategy="priority",
        models=[
            "ollama-cloud/nemotron-3-ultra",
            "ollama-cloud/nemotron-3-super",
            "ollama-cloud/beam",
            "ollama-cloud/gemma4:31b",
        ],
        description="Ollama Cloud Nemotron + Gemma",
        display_name="Ollama Cloud Best",
    ),
    "openrouter-best": ComboDefinition(
        name="combo/openrouter-best",
        strategy="priority",
        models=[
            "openrouter/cohere/north-mini-code:free",
            "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free",
            "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free-high",
            "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free-medium",
            "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free-none",
            "openrouter/nvidia/nemotron-3.5-lightning:free",
            "openrouter/nvidia/nemotron-3.5-super-vl:free",
            "openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
            "openrouter/dots-studio/dots-3-note-preview:free",
            "openrouter/liquid/lfm-2.5-2.6b:free",
            "auto/best-coding",
        ],
        description="OpenRouter free coding/reasoning models",
        display_name="OpenRouter Best (free)",
    ),
    "orcarouter-best": ComboDefinition(
        name="combo/orcarouter-best",
        strategy="priority",
        models=[
            "orcarouter/orcarouter/free",
            "orcarouter/deepseek/deepseek-v4.1-flash-free",
            "orcarouter/deepseek/deepseek-v4-flash-free",
            "orcarouter/z-ai/glm-5.3-flash-free",
        ],
        description="OrcaRouter models",
        display_name="OrcaRouter Best",
    ),
}


# ============================================================================
# Main Orchestrator
# ============================================================================

class ComboUpdater:
    def __init__(self, config: Config):
        self.config = config
        self.client = OmniRouteClient(config)
        self.generator = ComboMarkdownGenerator(config)
        self.git = GitOperator(Path.cwd(), config)
        self.discovery = ProviderDiscovery(config)
        self.opencode_updater = OpenCodeConfigUpdater(config)
    
    async def run(
        self,
        write: bool = False,
        push: bool = False,
        test_only: bool = False,
        sync_combos: bool = False,
        discover_only: bool = False,
    ) -> int:
        """Main entry point."""
        print(f"[INFO] Connecting to OmniRoute at {self.config.omniroute_url}...")
        
        async with self.client:
            # Fetch all models
            print("[INFO] Fetching models from OmniRoute...")
            models = await self.client.get_models()
            print(f"   Found {len(models)} total models")
            
            # Discover providers from providers.xlsx
            print("[INFO] Discovering active providers from providers.xlsx...")
            xlsx_providers = self.discovery.get_active_providers_from_xlsx()
            xlsx_providers = self.discovery.enrich_with_models(xlsx_providers, models)
            
            # Discover new providers needing combos (sets has_combo flag)
            new_providers = self.discovery.discover_new_providers(xlsx_providers, BUILTIN_COMBOS)
            
            print(f"   Found {len(xlsx_providers)} providers with active connections:")
            for name, info in sorted(xlsx_providers.items()):
                combo_status = "[OK] has combo" if info.has_combo else "[MISSING] NO COMBO"
                print(f"     {name}: {info.active_connections} conn, {info.total_models} models - {combo_status}")
            
            if new_providers:
                print(f"\n[NEW] Discovered {len(new_providers)} new providers needing combos:")
                for p in new_providers:
                    print(f"     {p.name}: {p.total_models} models - {p.models[:5]}{'...' if len(p.models) > 5 else ''}")
            else:
                print("\n[OK] All active providers already have combos defined")
            
            if discover_only:
                return 0
            
            # Generate combos for new providers
            all_combos = dict(BUILTIN_COMBOS)
            if self.config.auto_create_combos and new_providers:
                print("\n[INFO] Auto-generating combos for new providers...")
                for provider in new_providers:
                    combo = AutoComboGenerator.generate_combo_for_provider(provider)
                    all_combos[provider.name + "-best"] = combo
                    print(f"   [OK] Generated {combo.name} with {len(combo.models)} models")
            
            # Get unique model IDs from all combos
            all_combo_models = set()
            for combo in all_combos.values():
                all_combo_models.update(combo.models)
            
            # Filter to only models that exist in OmniRoute
            available_model_ids = {m.id for m in models if m.owned_by != "combo"}
            models_to_test = list(all_combo_models & available_model_ids)
            
            missing_models = all_combo_models - available_model_ids
            if missing_models:
                print(f"\n[WARN] {len(missing_models)} combo models not found in OmniRoute:")
                for m in sorted(missing_models)[:20]:
                    print(f"     {m}")
                if len(missing_models) > 20:
                    print(f"     ... and {len(missing_models) - 20} more")
            
            print(f"\n[INFO] Testing {len(models_to_test)} models in defined combos...")
            
            results = await self.client.test_models(models_to_test)
            result_map = {r.model_id: r for r in results}
            
            # Print summary
            working = sum(1 for r in results if r.success)
            failed = sum(1 for r in results if not r.success)
            print(f"\n[RESULTS] Test Results: {working} working, {failed} failed")
            
            if test_only:
                self._print_detailed_results(results)
                return 0
            
            # Sync combos to OmniRoute
            if sync_combos:
                print("\n[INFO] Syncing combos to OmniRoute...")
                synced = 0
                created = 0
                for combo_id, combo in all_combos.items():
                    try:
                        result, was_created = await self.client.upsert_combo(combo)
                        action = "created" if was_created else "updated"
                        print(f"   {action}: {combo.name} (ID: {result.get('id', 'unknown')})")
                        synced += 1
                        if was_created:
                            created += 1
                    except Exception as e:
                        print(f"   [FAIL] Failed to sync {combo.name}: {e}")
                print(f"\n[OK] Synced {synced} combos ({created} new, {synced - created} updated)")
            
            # Generate markdown
            print("\n[INFO] Generating combos.md...")
            content = self.generator.generate(all_combos, result_map)
            
            # Update opencode.jsonc
            print("[INFO] Updating opencode.jsonc...")
            added, updated = self.opencode_updater.update_model_entries(all_combos)
            print(f"   Added {added} new, updated {updated} existing model entries")
            
            if write:
                self.generator.write(content)
                
                if push:
                    if not self.git.is_git_repo():
                        print("[WARN] Not a git repository, skipping push")
                        return 0
                    
                    print("[INFO] Pushing to GitHub...")
                    files_to_add = [self.config.combos_md_path, self.config.opencode_jsonc_path]
                    if self.git.add(files_to_add):
                        msg = f"{self.config.commit_message_prefix} - {datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
                        if self.git.commit(msg):
                            if self.git.push():
                                print("[OK] Pushed to GitHub")
                            else:
                                print("[FAIL] Push failed")
                                return 1
                        else:
                            print("[WARN] Commit failed (no changes?)")
                    else:
                        print("[FAIL] Git add failed")
                        return 1
            else:
                print("\n--- DRY RUN: combos.md preview ---")
                print(content[:3000] + ("..." if len(content) > 3000 else ""))
                print("--- End preview ---")
                print("\nRun with --write to update files, --write --push to also push to GitHub")
                print("Run with --sync-combos to create/update combos in OmniRoute")
        
        return 0
    
    def _print_detailed_results(self, results: List[TestResult]) -> None:
        """Print detailed test results grouped by provider."""
        by_provider: Dict[str, List[TestResult]] = {}
        for r in results:
            provider = r.model_id.split("/")[0] if "/" in r.model_id else "unknown"
            if provider not in by_provider:
                by_provider[provider] = []
            by_provider[provider].append(r)
        
        for provider in sorted(by_provider.keys()):
            provider_results = by_provider[provider]
            working = sum(1 for r in provider_results if r.success)
            total = len(provider_results)
            print(f"\n  {provider}: {working}/{total} working")
            for r in provider_results:
                status = "[OK]" if r.success else "[FAIL]"
                error = f" ({r.error[:50]})" if not r.success and r.error else ""
                print(f"    {status} {r.model_id} - {r.latency_ms:.0f}ms{error}")


# ============================================================================
# Config File Template
# ============================================================================

CONFIG_TEMPLATE = """# OmniRoute Combo Updater Configuration
# Save as config.yaml or config.json

omniroute_url: "http://127.0.0.1:20128"
api_key: "${OMNIROUTE_API_KEY}"  # Or set via environment variable
combos_md_path: "docs/COMBOS.md"
opencode_jsonc_path: "omniroute-migration/opencode.jsonc"
providers_xlsx_path: "omniroute-providers.xlsx"

# Test settings
test_timeout: 30          # seconds per model
test_concurrency: 10      # parallel test requests
test_prompt: "Say 'OK' if you can respond."

# Auto-discovery settings
auto_create_combos: true  # Automatically create combos for new providers
min_models_for_combo: 1   # Minimum models needed to create a combo

# GitHub settings (optional)
github_repo: ""           # e.g., "username/repo"
github_branch: "main"
commit_message_prefix: "chore: update combos.md"
"""


# ============================================================================
# CLI Entry Point
# ============================================================================

def create_config_template(path: Path) -> None:
    """Create a config template file."""
    path.write_text(CONFIG_TEMPLATE)
    print(f"[OK] Created config template at {path}")


def main():
    parser = argparse.ArgumentParser(
        description="OmniRoute Combo Auto-Updater",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python update_combos.py                              # Dry run (discover + test)
  python update_combos.py --write                      # Update combos.md + opencode.jsonc
  python update_combos.py --write --push               # Update and push to GitHub
  python update_combos.py --test-only                  # Only test models, show results
  python update_combos.py --sync-combos                # Create/update combos in OmniRoute
  python update_combos.py --sync-combos --write --push # Full pipeline: sync + write + push
  python update_combos.py --discover-only              # Only show provider discovery
  python update_combos.py --init-config                # Create config.yaml template

Environment variables:
  OMNIROUTE_API_KEY         Your OmniRoute API key
  OMNIROUTE_URL             OmniRoute server URL (default: http://127.0.0.1:20128)
  COMBOS_MD_PATH            Path to combos.md (default: docs/COMBOS.md)
  OPENCODE_JSONC_PATH       Path to opencode.jsonc (default: omniroute-migration/opencode.jsonc)
  PROVIDERS_XLSX_PATH       Path to providers.xlsx (default: omniroute-providers.xlsx)
  GITHUB_REPO               GitHub repo for pushing (e.g., user/repo)
  GITHUB_BRANCH             Branch to push to (default: main)

Requirements:
  pip install aiohttp pyyaml openpyxl
        """
    )
    
    parser.add_argument("--write", action="store_true", help="Write changes to combos.md and opencode.jsonc")
    parser.add_argument("--push", action="store_true", help="Push to GitHub after writing")
    parser.add_argument("--test-only", action="store_true", help="Only test models, don't update files")
    parser.add_argument("--sync-combos", action="store_true", help="Create/update combos in OmniRoute")
    parser.add_argument("--discover-only", action="store_true", help="Only run provider discovery, no testing")
    parser.add_argument("--init-config", action="store_true", help="Create config.yaml template")
    parser.add_argument("--config", type=Path, help="Path to config file (YAML or JSON)")
    parser.add_argument("--url", help="OmniRoute URL (overrides config/env)")
    parser.add_argument("--api-key", help="OmniRoute API key (overrides config/env)")
    parser.add_argument("--concurrency", type=int, help="Test concurrency (default: 10)")
    parser.add_argument("--timeout", type=int, help="Test timeout in seconds (default: 30)")
    
    args = parser.parse_args()
    
    if args.init_config:
        create_config_template(Path("config.yaml"))
        return 0
    
    # Load config
    config = Config.from_env()
    if args.config and args.config.exists():
        config = Config.from_file(args.config)
    
    # Override from CLI
    if args.url:
        config.omniroute_url = args.url
    if args.api_key:
        config.api_key = args.api_key
    if args.concurrency:
        config.test_concurrency = args.concurrency
    if args.timeout:
        config.test_timeout = args.timeout
    
    if not config.api_key:
        print("[FAIL] Error: OMNIROUTE_API_KEY not set. Set it in environment, config file, or --api-key")
        return 1
    
    # Run
    updater = ComboUpdater(config)
    try:
        return asyncio.run(updater.run(
            write=args.write,
            push=args.push,
            test_only=args.test_only,
            sync_combos=args.sync_combos,
            discover_only=args.discover_only,
        ))
    except KeyboardInterrupt:
        print("[WARN] Interrupted")
        return 130
    except Exception as e:
        print(f"\n[FAIL] Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())