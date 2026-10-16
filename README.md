# Free AI Coding Setup — OmniRoute + OpenCode (Windows)

> One gateway, ~120 provider connections, 27 auto-fallback combos, $0.
> Generated 2026-10-16. All free tiers verified live on this machine.

---

## 1. Install OmniRoute

```powershell
# 1. Node.js LTS (winget)
winget install OpenJS.NodeJS.LTS

# 2. OmniRoute gateway (global)
npm install -g omniroute

# 3. First run (creates C:\Users\<you>\.omniroute, prints dashboard URL)
omniroute

# 4. Save your gateway API key (once)
setx OMNIROUTE_API_KEY "<key-from-dashboard>"
```

Start/stop:

```powershell
# Start (background, port 20128, auto-opens dashboard)
# -> use Desktop shortcut "Start OmniRoute.bat":
omniroute --no-open --port 20128

# Health check
curl.exe http://localhost:20128/health
```

Update (manual — never auto):

```powershell
omniroute update --check
omniroute update --apply --yes   # then restart gateway
```

---

## 2. Connect OpenCode to OmniRoute

```powershell
$key = [System.Environment]::GetEnvironmentVariable('OMNIROUTE_API_KEY','User')
omniroute setup-opencode --port 20128 --api-key $key --model 'auto/best-coding'
```

This writes the `omniroute` provider into
`C:\Users\<you>\.config\opencode\opencode.jsonc`
(`baseURL: http://localhost:20128/v1`, key from env).
**Restart the OpenCode app** after any config change — it reads the picker once at launch.

Refresh picker anytime (double-click):
`Desktop\Refresh OmniRoute Models.bat`
(regenerates catalog → prunes dead → combos on top → validates JSON)

---

## 3. How to use (daily)

- OpenCode model picker → provider **OmniRoute** → pick a `combo/*` (top of list)
- Default daily driver: **`combo/all-best`** (~130 models, Claude-first priority, fails through everything alive)
- Brand combos: `claude-best`, `gemini-best`, `gpt-best`, `grok-best`, `deepseek-best`, `qwen-best`, `nvidia-best`, `mistral-best`, `glm-best`, `kimi-best`, `llama-best`, `gemma-best`, `openrouter/kilocode/trae/codex/xkiro/ollama/kiro/literouter/apinex/nara/cleanapis-best`, `keep-trying`, `steady-coding`, `claude-code/max/fast`
- Single models: `auto/*` routes fan out across all healthy providers

Rules learned the hard way:
- **401/402/403-terminal kills a chain** — never put dead/paid legs early; interleave providers
- Attempt budget is 200/request (max) — big combos are safe
- Quotas fluctuate hourly — combos route around; single models may 429

---

## 4. Providers + free models (all connected here)

Legend: ✅ tested answering · ⏳ quota-flaky (recovers) · ❌ dead/paid · 🔑 needs key/top-up

### API-key free tiers (no login dance)

| Provider | Free models (tested ✅) | Get key |
|----------|------------------------|---------|
| **Gemini (Google AI Studio)** ×8 keys | gemini-3.8-flash, 3.7-flash (+2.5s dead) | https://aistudio.google.com/api-keys |
| **Groq** | gpt-oss-120b/20b, qwen3.8-27b | https://console.groq.com/keys |
| **OpenRouter** (`:free` filter ON) | nemotron super/ultra, north-mini-code, laguna s/xs, gemma, apodex | https://openrouter.ai/keys ($10 top-up = 1000 req/day) |
| **KiloCode** | nemotron ultra/super/lightning `:free`, laguna, north-mini | https://kilocode.ai (OAuth) |
| **NVIDIA NIM** | nemotron/super (rate-limited) | https://build.nvidia.com |
| **Cerebras** | llama-3.1-70b, gpt-oss (1M/day) | https://cloud.cerebras.ai |
| **SiliconFlow** | deepseek-v3.2, qwen (free tier) | https://siliconflow.cn |
| **Mistral** | codestral-latest (tested ✅) | https://console.mistral.ai |
| **Codestral direct** | codestral-2508/latest (0.8s!) | via Mistral key |
| **Together/Fireworks/DeepInfra/SambaNova** | various free models | their consoles |
| **Pollinations** | gpt-oss, llama, claude (no key!) | none needed — https://pollinations.ai |

### OAuth / account bridges (login once, gateway reuses session)

| Provider | Accounts here | Notes |
|----------|---------------|-------|
| **Antigravity** ×11 / **AGY** ×11 | Claude Opus 4.6/Sonnet 4.6 | Bills Anthropic accounts (~$5.79 est. seen) |
| **Claude Web** ×13→1 | Opus/Sonnet/Fable/Haiku | ⚠️ collapsed, mostly 429 — re-add accounts |
| **Codex (ChatGPT)** ×7-8 | gpt-6-luna/sol, 5.6 family | ✅ tested 1.4s |
| **Kiro** ×12 | qwen3-coder-next, glm-5, deepseek, minimax, claude-4.5 | ✅ tested |
| **xKiro** ×6 | qwen max/coder, mistral, sensenova (`:free`) | ✅ tested |
| **Grok CLI** ×10 / **Grok Web** ×13 | grok-4.7, fast | ✅ tested |
| **Kimi (Moonshot)** ×2 | k3, k2d6 | tokens expire — watcher alerts |
| **DeepSeek Web** ×2 | full 14-model lineup | tokens die ~hourly — watcher + 1-min re-auth script |
| **Trae / Qoder / Kilo / Kiro / ClinePass** | assorted | mixed health, fail-through covers |
| **GitHub Copilot** ×2 | claude/gpt via Copilot sub | 400s via gateway (use in IDE instead) |
| **LMArena / Amazon Q / Ollama-cloud** | arena models | flaky/limited |

### Custom OpenAI-compatible gateways (passthrough trick)

| Provider | Base URL | Status |
|----------|----------|--------|
| **CleanAPIs** ×5 keys | https://cleanapis.com/v1 | ✅ tested (claude-5.5, gpt-5.6…) |
| **Apinex** | https://api.apinex.bond/v1 | ⚠️ free quota spent → subscription wall |
| **KiraAI** | https://kiraai.vn/api/v1 | ⚠️ 402, needs top-up |
| **LiteRouter** | (native provider) | ✅ 7 free models tested |
| **NaraRouter** | https://router.bynara.id/v1 | ✅ laguna + nemotron (Telegram link required) |
| **Requesty / AgentRouter / Opper** | various | configured, low usage |

### Dead — do not use

`oc/*` + `opencode/*` (401/402/403 terminal — free pool shut down) · `cxa/*` (needs Codex CLI) · `aug/*` (no CLI) · `cfp/*` (0%) · `ddgw/*` (429 loop) · `dva/*`, `zc/*`, `aihorde`, `veo/*`, `unc/*` · `muse-code`, `huggingface` connections (deleted)

---

## 5. Automation (all in `%USERPROFILE%\.config\opencode\`)

| Script | Schedule | What |
|--------|----------|------|
| `update-allbest.ps1` (+discover/bump/interleave helpers) | `AllBestSyncDaily` 09:00 | rebuilds `all-best` best-first from live catalog |
| `update-omniroute-picker.ps1` (+probe/refresh) | `OmniPickerAM` 09:00, `OmniPickerPM` 21:00 | fresh catalog → prune dead → probe → disable paid → combos on top |
| `update-openrouter-free.ps1` | `OpenRouterFreeSyncDaily` 09:00 | syncs 16-model `:free` whitelist |
| `check-omniroute-update.ps1` | `OmniUpdateCheckWeekly` Mon 09:00 | version check → log only |
| `watch-kimi.ps1` | `KimiWatchDaily` 08:30 | token-expiry detect + alert |
| `watch-deepseek.ps1` | `DeepSeekWatch30m` every 30 min | expiry detect; `refresh-deepseek.ps1` = 1-min re-auth |
| `refresh_omniroute.py` | on demand / via jobs | allowlist prune (combos+auto+chain+`:free` only) |
| Desktop `Refresh OmniRoute Models.bat` | manual | setup-opencode + prune + validate |

Key rules encoded: 401/402 = durable-dead (auto-disable), 403/429/5xx = transient (leave for recovery), attempt budget 200, Claude-first priority, interleave providers (anti-circuit), `:free` modelFilter on OpenRouter.

---

## 6. Files map

- Gateway data: `C:\Users\<you>\.omniroute\` (storage.sqlite, .env — **contains encryption key**)
- OpenCode: `%USERPROFILE%\.config\opencode\opencode.jsonc`, `%USERPROFILE%\.local\share\opencode\auth.json`
- This folder: guide PDFs, `BEST_50_MODELS.txt`, `FREE_CODING_MODELS.txt`, `setup-omniroute-windows.bat`, `omniroute-migration\` (full export + restore guide), `omniroute-providers.xlsx` (**contains plaintext keys — move to USB, delete here**)

---

## 7. Troubleshooting

| Symptom | Cause → fix |
|---------|-------------|
| Combo 403/401 terminal, stops early | Dead leg first — probe legs, drop 401/402s, interleave providers |
| "Maximum combo attempts exceeded" | Budget hit — bump `maxGlobalAttempts` (cap 200) |
| `trae/kimi/deepseek 401` | Token expired — re-auth account, re-probe |
| OpenRouter 403 budget | $0.60 workspace cap spent — add 2nd key or wait reset |
| Picker missing combos | App restart (reads config once); check JSON validity |
| Gateway spins (`ECONNREFUSED`) | Gateway down — run `Start OmniRoute.bat`; kill duplicate node processes |
| Costs page shows $ | Estimates at list price, not bills (only Anthropic actual) |

## 8. Combo catalog (live)

_Status per model from last live probe: **active** = answered, **dead (CODE)** = terminal failure, **untested** = in rotation, never directly probed, **router** = auto-route (fans out live). Generated 2026-10-16._

### `combo/all-best` — priority, 130 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `codestral/codestral-latest` | active |
| 2 | `codestral/codestral-2508` | active |
| 3 | `antigravity/claude-opus-4-6-thinking-low` | dead (FAIL) |
| 4 | `antigravity/claude-opus-4-6-thinking` | active |
| 5 | `antigravity/claude-sonnet-4-6-low` | dead (FAIL) |
| 6 | `agy/claude-opus-4-6-thinking-low` | dead (FAIL) |
| 7 | `agy/claude-sonnet-4-6-low` | dead (FAIL) |
| 8 | `claude-web/claude-opus-4-6` | dead (FAIL-429) |
| 9 | `claude-web/claude-sonnet-4-6-low` | dead (FAIL-429) |
| 10 | `claude-web/claude-opus-5-low` | active |
| 11 | `deepseek-web/deepseek-chat` | active |
| 12 | `gemini/gemini-3.8-flash-lite-tts` | untested |
| 13 | `groq/openai/gpt-oss-120b` | active |
| 14 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | active |
| 15 | `kilocode/nvidia/nemotron-3.5-lightning:free` | active |
| 16 | `auto/coding:free` | active |
| 17 | `codex/gpt-6-luna` | active |
| 18 | `kiro/qwen3-coder-next` | active |
| 19 | `mistral/codestral-latest` | active |
| 20 | `literouter/glm-5:free` | active |
| 21 | `xkiro/qwen/qwen3-coder-plus:free` | active |
| 22 | `ollama-cloud/nemotron-3-super` | active |
| 23 | `zai-web/glm-5.3` | untested |
| 24 | `grok-web/fast` | active |
| 25 | `grok-cli/grok-4.7-low` | active |
| 26 | `deepseek-web/DeepSeek-V3.2` | active |
| 27 | `groq/qwen/qwen3.8-27b` | active |
| 28 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | active |
| 29 | `kilocode/poolside/laguna-s-2.1:free` | active |
| 30 | `codex/gpt-5.6-luna` | active |
| 31 | `kiro/glm-5` | active |
| 32 | `literouter/glm-5.3-flash:free` | active |
| 33 | `xkiro/qwen/qwen3-max:free` | active |
| 34 | `ollama-cloud/gemma4:31b` | active |
| 35 | `zai-web/glm-5.3-flash` | untested |
| 36 | `grok-cli/grok-4.7` | active |
| 37 | `deepseek-web/deepseek-reasoner` | active |
| 38 | `groq/openai/gpt-oss-20b` | active |
| 39 | `openrouter/cohere/north-mini-code:free` | active |
| 40 | `kilocode/poolside/laguna-xs-2.1:free` | active |
| 41 | `codex/gpt-5.5` | active |
| 42 | `kiro/deepseek-3.2` | untested |
| 43 | `literouter/deepseek-v3.2:free` | active |
| 44 | `xkiro/mistralai/codestral-2508` | active |
| 45 | `zai-web/glm-5.2` | active |
| 46 | `grok-cli/grok-4.7-medium` | active |
| 47 | `deepseek-web/deepseek-v4-flash` | active |
| 48 | `openrouter/poolside/laguna-s-2.1:free` | active |
| 49 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | active |
| 50 | `codex/gpt-5.6-terra` | active |
| 51 | `kiro/minimax-m2.1` | untested |
| 52 | `literouter/gpt-oss-120b:free` | active |
| 53 | `xkiro/mistralai/mistral-small-2603` | active |
| 54 | `grok-cli/grok-4.7-high` | active |
| 55 | `deepseek-web/deepseek-v4-pro` | active |
| 56 | `openrouter/poolside/laguna-xs-2.1:free` | untested |
| 57 | `kilocode/cohere/north-mini-code:free` | active |
| 58 | `kiro/minimax-m2.5` | untested |
| 59 | `literouter/kimi-k2.7-code-cheap:free` | active |
| 60 | `xkiro/qwen/qwen3.8-max:free` | active |
| 61 | `deepseek-web/deepseek-v4-pro-think` | active |
| 62 | `openrouter/nvidia/nemotron-3.5-lightning:free` | active |
| 63 | `literouter/qwen3-coder-next:free` | active |
| 64 | `xkiro/qwen/qwen3.7-max:free` | active |
| 65 | `deepseek-web/deepseek-v4-pro-search` | active |
| 66 | `literouter/llama-3.3-70b-instruct-turbo:free` | active |
| 67 | `xkiro/qwen/qwen3.6-max-preview:free` | active |
| 68 | `deepseek-web/deepseek-v4-pro-think-search` | active |
| 69 | `literouter/ministral-3b-2512:free` | untested |
| 70 | `xkiro/mistralai/mistral-large-2512` | active |
| 71 | `deepseek-web/deepseek-v4-flash-think` | active |
| 72 | `literouter/ministral-3-8b-instruct:free` | untested |
| 73 | `xkiro/qwen/qwen3.5-plus:free` | active |
| 74 | `deepseek-web/deepseek-v4-flash-search` | active |
| 75 | `literouter/deepseek-v3.1` | untested |
| 76 | `xkiro/sensenova/sensenova-6.8-flash-lite` | active |
| 77 | `deepseek-web/deepseek-v4-flash-think-search` | active |
| 78 | `literouter/deepseek-v3.1:free` | untested |
| 79 | `xkiro/mistralai/devstral-medium` | active |
| 80 | `deepseek-web/DeepSeek-R1` | active |
| 81 | `literouter/deepseek-v3.2` | untested |
| 82 | `xkiro/mistralai/mistral-medium-3.5` | active |
| 83 | `deepseek-web/DeepSeek-R1-Search` | active |
| 84 | `literouter/deepseek-v4-flash` | untested |
| 85 | `xkiro/mistralai/ministral-8b` | untested |
| 86 | `deepseek-web/DeepSeek-Search` | active |
| 87 | `literouter/deepseek-v4-flash-cheap` | untested |
| 88 | `literouter/deepseek-v4-flash-cheap:free` | untested |
| 89 | `literouter/deepseek-v4-flash-stable` | untested |
| 90 | `literouter/deepseek-v4-flash:free` | untested |
| 91 | `literouter/deepseek-v4-pro` | untested |
| 92 | `literouter/deepseek-v4-pro-cheap` | untested |
| 93 | `literouter/deepseek-v4-pro-cheap:free` | untested |
| 94 | `literouter/deepseek-v4.1-flash` | untested |
| 95 | `literouter/deepseek-v4.1-flash-cheap` | untested |
| 96 | `literouter/deepseek-v4.1-flash-cheap:free` | untested |
| 97 | `literouter/deepseek-v4.1-flash-stable` | untested |
| 98 | `literouter/deepseek-v4.1-flash-stable:free` | untested |
| 99 | `literouter/deepseek-v4.1-flash:free` | untested |
| 100 | `literouter/gemini-2.5-flash-lite:free` | untested |
| 101 | `literouter/glm-4.5` | untested |
| 102 | `literouter/glm-4.5-air` | untested |
| 103 | `literouter/glm-4.5-air:free` | untested |
| 104 | `literouter/glm-4.5:free` | untested |
| 105 | `literouter/glm-4.6` | untested |
| 106 | `literouter/glm-4.6:free` | untested |
| 107 | `literouter/glm-4.7` | untested |
| 108 | `literouter/glm-4.7-flash` | untested |
| 109 | `literouter/glm-4.7-flash-heretic` | untested |
| 110 | `literouter/glm-4.7-flash-heretic:free` | untested |
| 111 | `literouter/glm-4.7-flash:free` | untested |
| 112 | `literouter/glm-4.7:free` | untested |
| 113 | `literouter/glm-5` | untested |
| 114 | `literouter/glm-5.1` | untested |
| 115 | `literouter/glm-5.1-cheap:free` | untested |
| 116 | `literouter/glm-5.1:free` | untested |
| 117 | `literouter/glm-5.2` | untested |
| 118 | `literouter/glm-5.2-cheap` | untested |
| 119 | `literouter/glm-5.2-cheap:free` | untested |
| 120 | `literouter/glm-5.2:free` | untested |
| 121 | `literouter/glm-5.3` | untested |
| 122 | `literouter/glm-5.3-cheap` | untested |
| 123 | `literouter/glm-5.3-flash` | untested |
| 124 | `literouter/glm-5.3-flash-cheap` | untested |
| 125 | `literouter/glm-5.3-flash-cheap:free` | untested |
| 126 | `literouter/gpt-5-mini` | untested |
| 127 | `literouter/gpt-5-mini-stable` | untested |
| 128 | `nara/laguna-s-2.1` | untested |
| 129 | `nara/nemotron-3.5-lightning-free` | untested |
| 130 | `auto/best-coding` | router (live) |

### `combo/apinex-best` — priority, 9 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | active |
| 2 | `openai/free/gpt-6-luna` | untested |
| 3 | `openai/free/glm-5.3-flash` | untested |
| 4 | `openai/free/deepseek-v4.1-flash` | untested |
| 5 | `openai/free/qwen-3.8-max` | untested |
| 6 | `openai/free/mimo-v2.6-pro` | untested |
| 7 | `openai/free/deepseek-v4-pro-0813` | untested |
| 8 | `openai/free/deepseek-v4-flash-0731` | untested |
| 9 | `auto/best-coding` | router (live) |

### `combo/claude-best` — priority, 34 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `openai/claude-opus-5.5` | untested |
| 2 | `openai/claude-sonnet-5` | untested |
| 3 | `claude-web/claude-opus-5-low` | active |
| 4 | `cline/anthropic/claude-opus-4.8-low` | active |
| 5 | `claude-web/claude-opus-5-high` | untested |
| 6 | `claude-web/claude-opus-5-xhigh` | untested |
| 7 | `claude-web/claude-opus-5-medium` | untested |
| 8 | `antigravity/claude-opus-4-6-thinking` | active |
| 9 | `claude-web/claude-opus-4-6` | dead (FAIL-429) |
| 10 | `agy/claude-opus-4-6-thinking-low` | dead (FAIL) |
| 11 | `antigravity/claude-opus-4-6-thinking-low` | dead (FAIL) |
| 12 | `claude-web/claude-opus-4-6-low` | dead (FAIL) |
| 13 | `claude-web/claude-opus-4-7-low` | dead (FAIL-429) |
| 14 | `claude-web/claude-opus-4-8-low` | dead (FAIL-429) |
| 15 | `claude-web/claude-opus-5` | untested |
| 16 | `claude-web/claude-sonnet-5-high` | untested |
| 17 | `claude-web/claude-sonnet-5-xhigh` | untested |
| 18 | `claude-web/claude-sonnet-5-medium` | untested |
| 19 | `claude-web/claude-sonnet-5-low` | dead (FAIL-429) |
| 20 | `kiro/claude-sonnet-4.5` | dead (FAIL-429) |
| 21 | `agy/claude-sonnet-4-6` | untested |
| 22 | `antigravity/claude-sonnet-4-6` | untested |
| 23 | `claude-web/claude-sonnet-4-6` | untested |
| 24 | `agy/claude-sonnet-4-6-low` | dead (FAIL) |
| 25 | `antigravity/claude-sonnet-4-6-low` | dead (FAIL) |
| 26 | `claude-web/claude-sonnet-4-6-low` | dead (FAIL-429) |
| 27 | `claude-web/claude-sonnet-5` | dead (FAIL-429) |
| 28 | `cline/anthropic/claude-sonnet-5` | untested |
| 29 | `claude-web/claude-fable-5-1-low` | dead (FAIL-429) |
| 30 | `claude-web/claude-fable-5-low` | dead (FAIL-429) |
| 31 | `cline/anthropic/claude-fable-5-low` | untested |
| 32 | `kiro/claude-haiku-4.5` | untested |
| 33 | `claude-web/claude-haiku-4-5-20251001-low` | dead (FAIL-429) |
| 34 | `auto/best-coding` | router (live) |

### `combo/claude-code` — priority, 4 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | active |
| 2 | `auto/claude-sonnet` | router (live) |
| 3 | `gemini/gemini-3.8-flash` | dead (FAIL) |
| 4 | `auto/best-coding` | router (live) |

### `combo/claude-fast` — priority, 4 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | active |
| 2 | `gemini/gemini-3.8-flash` | dead (FAIL) |
| 3 | `auto/best-fast` | router (live) |
| 4 | `auto/best-coding` | router (live) |

### `combo/claude-max` — priority, 5 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `auto/claude-opus` | active |
| 2 | `groq/openai/gpt-oss-120b` | active |
| 3 | `auto/claude-sonnet` | router (live) |
| 4 | `gemini/gemini-3.8-flash` | dead (FAIL) |
| 5 | `auto/best-coding` | router (live) |

### `combo/cleanapis-best` — priority, 24 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `openai/claude-sonnet-5` | untested |
| 2 | `groq/openai/gpt-oss-120b` | active |
| 3 | `openai/claude-opus-5.5` | untested |
| 4 | `gemini/gemini-3.8-flash` | dead (FAIL) |
| 5 | `openai/kimi-k3` | untested |
| 6 | `groq/qwen/qwen3.8-27b` | active |
| 7 | `openai/glm-5.3` | untested |
| 8 | `openrouter/cohere/north-mini-code:free` | active |
| 9 | `openai/deepseek-v4-pro-max` | untested |
| 10 | `kilocode/cohere/north-mini-code:free` | active |
| 11 | `openai/free/qwen-3.8-max` | untested |
| 12 | `groq/openai/gpt-oss-20b` | active |
| 13 | `openai/free/deepseek-v4.1-flash` | untested |
| 14 | `openrouter/poolside/laguna-s-2.1:free` | active |
| 15 | `openai/free/deepseek-v4-flash-0731` | untested |
| 16 | `kilocode/poolside/laguna-s-2.1:free` | active |
| 17 | `openai/free/deepseek-v4-pro-0813` | untested |
| 18 | `gemini/gemini-3.7-flash` | active |
| 19 | `openai/free/gpt-6-luna` | untested |
| 20 | `openrouter/poolside/laguna-xs-2.1:free` | untested |
| 21 | `openai/free/glm-5.3-flash` | untested |
| 22 | `kilocode/poolside/laguna-xs-2.1:free` | active |
| 23 | `openai/free/mimo-v2.6-pro` | untested |
| 24 | `auto/best-coding` | router (live) |

### `combo/codex-best` — priority, 5 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `codex/gpt-6-luna` | active |
| 2 | `codex/gpt-5.6-luna` | active |
| 3 | `codex/gpt-5.6-terra` | active |
| 4 | `codex/gpt-5.5` | active |
| 5 | `auto/best-coding` | router (live) |

### `combo/deepseek-best` — priority, 44 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `openai/deepseek-v4-pro-max` | untested |
| 2 | `deepseek-web/DeepSeek-V3.2` | active |
| 3 | `deepseek-web/deepseek-v4-pro` | active |
| 4 | `deepseek-web/deepseek-v4-pro-search` | active |
| 5 | `deepseek-web/deepseek-v4-pro-think` | active |
| 6 | `deepseek-web/deepseek-v4-pro-think-search` | active |
| 7 | `deepseek-web/DeepSeek-R1` | active |
| 8 | `deepseek-web/DeepSeek-R1-Search` | active |
| 9 | `deepseek-web/DeepSeek-Search` | active |
| 10 | `deepseek-web/deepseek-chat` | active |
| 11 | `deepseek-web/deepseek-reasoner` | active |
| 12 | `deepseek-web/deepseek-v4-flash` | active |
| 13 | `deepseek-web/deepseek-v4-flash-search` | active |
| 14 | `deepseek-web/deepseek-v4-flash-think` | active |
| 15 | `deepseek-web/deepseek-v4-flash-think-search` | active |
| 16 | `nvidia/deepseek-ai/deepseek-coder-6.7b-instruct` | untested |
| 17 | `cline/deepseek/deepseek-v4.1-flash` | untested |
| 18 | `cline/deepseek/deepseek-v4.1-flash:batch` | untested |
| 19 | `nvidia/deepseek-ai/deepseek-v4.1-flash` | dead (FAIL) |
| 20 | `cline/deepseek/deepseek-v3.2` | untested |
| 21 | `cline/deepseek/deepseek-v3.2-exp` | untested |
| 22 | `kiro/deepseek-3.2` | untested |
| 23 | `xkiro/deepseek/deepseek-v3.2` | dead (FAIL) |
| 24 | `cline/deepseek/deepseek-chat-v3.1` | untested |
| 25 | `cline/deepseek/deepseek-v3.1-terminus` | untested |
| 26 | `xkiro/deepseek/deepseek-chat-v3.1` | untested |
| 27 | `cfp/deepseek-ai/deepseek-v4-pro-0813` | untested |
| 28 | `cline/deepseek/deepseek-v4-pro` | untested |
| 29 | `cline/deepseek/deepseek-v4-pro-0813` | untested |
| 30 | `cline/~deepseek/deepseek-pro-latest` | untested |
| 31 | `xkiro/deepseek/deepseek-v4-pro` | dead (FAIL) |
| 32 | `cfp/deepseek-ai/deepseek-r1-distill-qwen-32b` | untested |
| 33 | `cfp/deepseek-ai/deepseek-v4-flash-0731` | untested |
| 34 | `cline/deepseek/deepseek-chat` | untested |
| 35 | `cline/deepseek/deepseek-chat-v3-0324` | untested |
| 36 | `cline/deepseek/deepseek-r1` | untested |
| 37 | `cline/deepseek/deepseek-r1-0528` | untested |
| 38 | `cline/deepseek/deepseek-v4-flash` | untested |
| 39 | `cline/deepseek/deepseek-v4-flash-0731` | untested |
| 40 | `cline/deepseek/deepseek-v4-flash-vision-exp` | untested |
| 41 | `cline/~deepseek/deepseek-flash-latest` | untested |
| 42 | `cline/~deepseek/deepseek-v4-flash-latest` | untested |
| 43 | `xkiro/deepseek/deepseek-v4-flash` | dead (FAIL) |
| 44 | `auto/best-coding` | router (live) |

### `combo/gemini-best` — priority, 30 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `gemini/gemini-3.7-flash` | active |
| 2 | `agy/gemini-3.8-flash-low` | untested |
| 3 | `cline/google/gemini-3.8-flash` | untested |
| 4 | `gemini/gemini-3.8-flash` | dead (FAIL) |
| 5 | `agy/gemini-3.7-flash-low` | untested |
| 6 | `cline/google/gemini-3.7-flash` | untested |
| 7 | `agy/gemini-3.6-flash-low` | untested |
| 8 | `cline/google/gemini-3.6-flash` | untested |
| 9 | `agy/gemini-3.5-flash-lite` | untested |
| 10 | `antigravity/gemini-3.5-flash-lite` | untested |
| 11 | `cline/google/gemini-3.5-flash` | untested |
| 12 | `cline/google/gemini-3.5-flash-lite` | untested |
| 13 | `agy/gemini-3.1-pro-low` | untested |
| 14 | `antigravity/gemini-3.1-pro-low` | untested |
| 15 | `agy/gemini-3.1-flash-lite` | untested |
| 16 | `antigravity/gemini-3.1-flash-lite` | untested |
| 17 | `cline/google/gemini-3.1-flash-lite` | untested |
| 18 | `gemini/gemini-3.1-flash-lite` | dead (FAIL) |
| 19 | `agy/gemini-3-flash` | untested |
| 20 | `antigravity/gemini-3-flash` | untested |
| 21 | `gemini/gemini-3-flash-preview` | untested |
| 22 | `cline/google/gemini-2.5-pro` | untested |
| 23 | `cline/google/gemini-2.5-flash` | untested |
| 24 | `cline/google/gemini-2.5-flash-lite` | untested |
| 25 | `gemini/gemini-2.5-flash-lite` | untested |
| 26 | `agy/gemini-pro-agent` | untested |
| 27 | `antigravity/gemini-pro-agent` | untested |
| 28 | `cline/~google/gemini-pro-latest` | untested |
| 29 | `cline/~google/gemini-flash-latest` | untested |
| 30 | `auto/best-coding` | router (live) |

### `combo/gemma-best` — priority, 21 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `cfp/google/gemma-4-26b-a4b-it` | untested |
| 2 | `cline/google/gemma-4-26b-a4b-it` | untested |
| 3 | `cline/google/gemma-4-26b-a4b-it:free` | untested |
| 4 | `cline/google/gemma-4-31b-it` | untested |
| 5 | `cline/google/gemma-4-31b-it:free` | dead (FAIL-500) |
| 6 | `nvidia/google/gemma-4-31b-it` | untested |
| 7 | `openrouter/google/gemma-4-26b-a4b-it:free` | untested |
| 8 | `openrouter/google/gemma-4-31b-it:free` | dead (FAIL-429) |
| 9 | `cline/google/gemma-3-12b-it` | untested |
| 10 | `cline/google/gemma-3-27b-it` | untested |
| 11 | `cline/google/gemma-3-4b-it` | untested |
| 12 | `nvidia/google/gemma-3-12b-it` | untested |
| 13 | `nvidia/google/gemma-3-4b-it` | untested |
| 14 | `cline/google/gemma-2-27b-it` | untested |
| 15 | `nvidia/google/codegemma-1.1-7b` | untested |
| 16 | `cfp/aisingapore/gemma-sea-lion-v4-27b-it` | untested |
| 17 | `ddgw/tinfoil/gemma4-31b` | untested |
| 18 | `nvidia/google/codegemma-7b` | dead (FAIL) |
| 19 | `nvidia/google/gemma-2b` | untested |
| 20 | `nvidia/google/recurrentgemma-2b` | untested |
| 21 | `auto/best-coding` | router (live) |

### `combo/glm-best` — priority, 39 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `openai/glm-5.3` | untested |
| 2 | `cline/z-ai/glm-5.3` | active |
| 3 | `zai-web/glm-5.2` | active |
| 4 | `kiro/glm-5` | active |
| 5 | `zai-web/glm-5.3-flash-max` | untested |
| 6 | `zai-web/glm-5.3-max` | untested |
| 7 | `zai-web/glm-5.3-flash-high` | untested |
| 8 | `zai-web/glm-5.3-high` | untested |
| 9 | `cline/z-ai/glm-5.3-flash` | untested |
| 10 | `cline/z-ai/glm-5.3-flash:batch` | untested |
| 11 | `cline/z-ai/glm-5.3-flashx` | untested |
| 12 | `cline/z-ai/glm-5.3-prime` | untested |
| 13 | `cline/z-ai/glm-5.3:batch` | untested |
| 14 | `nvidia/z-ai/glm-5.3` | untested |
| 15 | `nvidia/z-ai/glm-5.3-flash` | untested |
| 16 | `zai-web/glm-5.3` | untested |
| 17 | `zai-web/glm-5.3-flash` | untested |
| 18 | `zai-web/glm-5.3-flash-low` | dead (FAIL) |
| 19 | `zai-web/glm-5.3-low` | dead (FAIL) |
| 20 | `zai-web/glm-5.2-max` | untested |
| 21 | `zai-web/glm-5.2-high` | untested |
| 22 | `aug/glm-5.2` | untested |
| 23 | `cfp/zai-org/glm-5.2` | untested |
| 24 | `cline/z-ai/glm-5.2` | untested |
| 25 | `cline/z-ai/glm-5.1` | untested |
| 26 | `cline/z-ai/glm-5-turbo` | untested |
| 27 | `cfp/zai-org/glm-4.7-flash` | untested |
| 28 | `cline/z-ai/glm-4.7` | untested |
| 29 | `cline/z-ai/glm-4.7-flash` | untested |
| 30 | `cline/z-ai/glm-4.6` | untested |
| 31 | `cline/z-ai/glm-4.6v` | untested |
| 32 | `cline/z-ai/glm-4.5` | untested |
| 33 | `cline/z-ai/glm-4.5-air` | untested |
| 34 | `cline/z-ai/glm-4.5v` | untested |
| 35 | `cline/z-ai/glm-5` | untested |
| 36 | `cline/z-ai/glm-5v-turbo` | untested |
| 37 | `cline/~z-ai/glm-flash-latest` | untested |
| 38 | `cline/~z-ai/glm-latest` | untested |
| 39 | `auto/best-coding` | router (live) |

### `combo/gpt-best` — priority, 127 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `codex/gpt-6-luna` | active |
| 2 | `cline/openai/gpt-5.6-sol` | active |
| 3 | `codex/gpt-5.6-luna` | active |
| 4 | `codex/gpt-5.6-terra` | active |
| 5 | `codex/gpt-5.5` | active |
| 6 | `cline/openai/gpt-5.4-mini` | active |
| 7 | `groq/openai/gpt-oss-120b` | active |
| 8 | `groq/openai/gpt-oss-20b` | active |
| 9 | `cline/openai/gpt-4o-2024-05-13` | untested |
| 10 | `cline/openai/gpt-4o-2024-08-06` | untested |
| 11 | `cline/openai/gpt-4o-2024-11-20` | untested |
| 12 | `cline/openai/gpt-4o-mini-2024-07-18` | untested |
| 13 | `cline/openai/gpt-6.1-sol-pro` | untested |
| 14 | `cline/openai/gpt-6.1-sol-pro:batch` | untested |
| 15 | `cline/openai/gpt-6.1-sol` | untested |
| 16 | `cline/openai/gpt-6.1-sol:batch` | untested |
| 17 | `codex/gpt-6-astra-max` | untested |
| 18 | `codex/gpt-6-astra-ultra` | untested |
| 19 | `codex/gpt-6-luna-max` | untested |
| 20 | `codex/gpt-6-sol-max` | untested |
| 21 | `codex/gpt-6-sol-ultra` | untested |
| 22 | `cline/openai/gpt-6-astra-pro` | untested |
| 23 | `cline/openai/gpt-6-astra-pro:batch` | untested |
| 24 | `cline/openai/gpt-6-luna-pro` | untested |
| 25 | `cline/openai/gpt-6-luna-pro:batch` | untested |
| 26 | `cline/openai/gpt-6-sol-pro` | untested |
| 27 | `cline/openai/gpt-6-sol-pro:batch` | untested |
| 28 | `codex/gpt-6-astra-high` | untested |
| 29 | `codex/gpt-6-astra-xhigh` | untested |
| 30 | `codex/gpt-6-luna-high` | untested |
| 31 | `codex/gpt-6-luna-xhigh` | untested |
| 32 | `codex/gpt-6-sol-high` | untested |
| 33 | `codex/gpt-6-sol-xhigh` | untested |
| 34 | `cline/openai/gpt-6-astra` | untested |
| 35 | `cline/openai/gpt-6-astra:batch` | untested |
| 36 | `cline/openai/gpt-6-luna` | untested |
| 37 | `cline/openai/gpt-6-luna:batch` | untested |
| 38 | `cline/openai/gpt-6-sol` | untested |
| 39 | `cline/openai/gpt-6-sol:batch` | untested |
| 40 | `codex/gpt-6-astra` | untested |
| 41 | `codex/gpt-6-sol` | dead (FAIL) |
| 42 | `codex/gpt-6-astra-medium` | untested |
| 43 | `codex/gpt-6-luna-medium` | untested |
| 44 | `codex/gpt-6-sol-medium` | untested |
| 45 | `codex/gpt-6-astra-low` | dead (FAIL) |
| 46 | `codex/gpt-6-luna-low` | active |
| 47 | `codex/gpt-6-sol-low` | dead (FAIL) |
| 48 | `codex/gpt-5.6-luna-max` | untested |
| 49 | `codex/gpt-5.6-sol-max` | untested |
| 50 | `codex/gpt-5.6-sol-ultra` | untested |
| 51 | `codex/gpt-5.6-terra-max` | untested |
| 52 | `codex/gpt-5.6-terra-ultra` | untested |
| 53 | `cline/openai/gpt-5.6-luna-pro` | untested |
| 54 | `cline/openai/gpt-5.6-luna-pro:batch` | untested |
| 55 | `cline/openai/gpt-5.6-sol-pro` | untested |
| 56 | `cline/openai/gpt-5.6-sol-pro:batch` | untested |
| 57 | `cline/openai/gpt-5.6-terra-pro` | untested |
| 58 | `cline/openai/gpt-5.6-terra-pro:batch` | untested |
| 59 | `codex/gpt-5.6-luna-high` | untested |
| 60 | `codex/gpt-5.6-luna-xhigh` | untested |
| 61 | `codex/gpt-5.6-sol-high` | untested |
| 62 | `codex/gpt-5.6-sol-xhigh` | untested |
| 63 | `codex/gpt-5.6-terra-high` | untested |
| 64 | `codex/gpt-5.6-terra-xhigh` | untested |
| 65 | `cline/openai/gpt-5.6-luna` | untested |
| 66 | `cline/openai/gpt-5.6-luna:batch` | untested |
| 67 | `cline/openai/gpt-5.6-sol:batch` | untested |
| 68 | `cline/openai/gpt-5.6-terra` | untested |
| 69 | `cline/openai/gpt-5.6-terra:batch` | untested |
| 70 | `codex/gpt-5.6-sol` | dead (FAIL) |
| 71 | `ddgw/gpt-5.6-luna` | untested |
| 72 | `kiro/gpt-5.6-luna` | dead (FAIL) |
| 73 | `kiro/gpt-5.6-sol` | untested |
| 74 | `kiro/gpt-5.6-terra` | untested |
| 75 | `codex/gpt-5.6-luna-medium` | untested |
| 76 | `codex/gpt-5.6-sol-medium` | untested |
| 77 | `codex/gpt-5.6-terra-medium` | untested |
| 78 | `codex/gpt-5.6-luna-low` | untested |
| 79 | `codex/gpt-5.6-sol-low` | untested |
| 80 | `codex/gpt-5.6-terra-low` | untested |
| 81 | `cline/openai/gpt-5.5-pro` | untested |
| 82 | `cline/openai/gpt-5.5-pro:batch` | untested |
| 83 | `codex/gpt-5.5-high` | untested |
| 84 | `codex/gpt-5.5-xhigh` | untested |
| 85 | `cline/openai/gpt-5.5` | untested |
| 86 | `cline/openai/gpt-5.5:batch` | untested |
| 87 | `codex/gpt-5.5-medium` | untested |
| 88 | `codex/gpt-5.5-low` | untested |
| 89 | `cline/openai/gpt-5.4-pro` | untested |
| 90 | `cline/openai/gpt-5.4-pro:batch` | untested |
| 91 | `cline/openai/gpt-5.4` | untested |
| 92 | `cline/openai/gpt-5.4:batch` | untested |
| 93 | `cline/openai/gpt-5.4-nano` | untested |
| 94 | `cline/openai/gpt-5.4-nano:batch` | untested |
| 95 | `cline/openai/gpt-5.4-mini:batch` | untested |
| 96 | `ddgw/gpt-5.4-mini` | untested |
| 97 | `cline/openai/gpt-5.3-codex` | untested |
| 98 | `cline/openai/gpt-5.2-pro` | untested |
| 99 | `cline/openai/gpt-5.2-pro:batch` | untested |
| 100 | `cline/openai/gpt-5.2` | untested |
| 101 | `cline/openai/gpt-5.2-chat` | untested |
| 102 | `cline/openai/gpt-5.2:batch` | untested |
| 103 | `cline/openai/gpt-5.1` | untested |
| 104 | `cline/openai/gpt-5.1:batch` | untested |
| 105 | `cline/openai/gpt-5-pro` | untested |
| 106 | `cline/openai/gpt-5-pro:batch` | untested |
| 107 | `cline/openai/gpt-5-nano` | untested |
| 108 | `cline/openai/gpt-5-nano:batch` | untested |
| 109 | `cline/openai/gpt-5-mini` | untested |
| 110 | `cline/openai/gpt-5-mini:batch` | untested |
| 111 | `cfp/openai/gpt-oss-120b` | untested |
| 112 | `cfp/openai/gpt-oss-20b` | untested |
| 113 | `cline/openai/gpt-4o` | untested |
| 114 | `cline/openai/gpt-4o:batch` | untested |
| 115 | `cline/openai/gpt-5` | untested |
| 116 | `cline/openai/gpt-5:batch` | untested |
| 117 | `cline/openai/gpt-oss-120b` | untested |
| 118 | `cline/openai/gpt-oss-120b:batch` | untested |
| 119 | `cline/openai/gpt-oss-20b` | untested |
| 120 | `cline/openai/gpt-oss-20b:batch` | untested |
| 121 | `ddgw/tinfoil/gpt-oss-120b` | untested |
| 122 | `nvidia/openai/gpt-oss-20b` | untested |
| 123 | `agy/gpt-oss-120b-medium` | untested |
| 124 | `antigravity/gpt-oss-120b-medium` | untested |
| 125 | `cline/openai/gpt-4o-mini` | untested |
| 126 | `cline/openai/gpt-4o-mini:batch` | untested |
| 127 | `auto/best-coding` | router (live) |

### `combo/grok-best` — priority, 18 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `grok-cli/grok-4.7-high` | active |
| 2 | `grok-cli/grok-4.7-medium` | active |
| 3 | `grok-cli/grok-4.7-low` | active |
| 4 | `cline/x-ai/grok-4.5` | active |
| 5 | `grok-web/fast` | active |
| 6 | `cline/x-ai/grok-4.20` | untested |
| 7 | `cline/x-ai/grok-4.20-multi-agent` | untested |
| 8 | `grok-cli/grok-4.7-xhigh` | untested |
| 9 | `cline/x-ai/grok-4.7` | untested |
| 10 | `grok-cli/grok-4.7` | active |
| 11 | `cline/x-ai/grok-4.6` | untested |
| 12 | `cline/x-ai/grok-4.3` | untested |
| 13 | `cline/x-ai/grok-4.3:batch` | untested |
| 14 | `cline/x-ai/grok-build-0.1` | untested |
| 15 | `cline/~x-ai/grok-latest` | untested |
| 16 | `grok-web/expert` | dead (FAIL-403) |
| 17 | `grok-web/heavy` | dead (FAIL-403) |
| 18 | `auto/best-coding` | router (live) |

### `combo/keep-trying` — priority, 5 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | active |
| 2 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | active |
| 3 | `groq/openai/gpt-oss-120b` | active |
| 4 | `gemini/gemini-3.8-flash` | dead (FAIL) |
| 5 | `auto/best-coding` | router (live) |

### `combo/kilocode-best` — priority, 7 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `kilocode/nvidia/nemotron-3.5-lightning:free` | active |
| 2 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | active |
| 3 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | active |
| 4 | `kilocode/poolside/laguna-s-2.1:free` | active |
| 5 | `kilocode/poolside/laguna-xs-2.1:free` | active |
| 6 | `kilocode/cohere/north-mini-code:free` | active |
| 7 | `auto/best-coding` | router (live) |

### `combo/kimi-best` — priority, 18 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `openai/kimi-k3` | untested |
| 2 | `cline/moonshotai/kimi-k3` | active |
| 3 | `aug/kimi-k2.7` | untested |
| 4 | `cfp/moonshotai/kimi-k2.7-code` | untested |
| 5 | `cline/moonshotai/kimi-k2.7-code` | untested |
| 6 | `aug/kimi-k2.6` | untested |
| 7 | `cfp/moonshotai/kimi-k2.6` | untested |
| 8 | `cline/moonshotai/kimi-k2.6` | untested |
| 9 | `nvidia/moonshotai/kimi-k2.6` | untested |
| 10 | `ollama-cloud/kimi-k2.6` | dead (FAIL-402) |
| 11 | `cline/moonshotai/kimi-k2.5` | untested |
| 12 | `cline/moonshotai/kimi-k2` | untested |
| 13 | `cline/moonshotai/kimi-k2-0905` | untested |
| 14 | `cline/moonshotai/kimi-k2-thinking` | untested |
| 15 | `cline/moonshotai/kimi-k3:batch` | untested |
| 16 | `cline/~moonshotai/kimi-latest` | untested |
| 17 | `nvidia/moonshotai/kimi-k3` | untested |
| 18 | `auto/best-coding` | router (live) |

### `combo/kiro-best` — priority, 8 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `kiro/glm-5` | active |
| 2 | `kiro/qwen3-coder-next` | active |
| 3 | `kiro/claude-sonnet-4.5` | dead (FAIL-429) |
| 4 | `kiro/claude-haiku-4.5` | untested |
| 5 | `kiro/deepseek-3.2` | untested |
| 6 | `kiro/minimax-m2.5` | untested |
| 7 | `kiro/minimax-m2.1` | untested |
| 8 | `auto/best-coding` | router (live) |

### `combo/literouter-best` — priority, 14 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `literouter/glm-5.3-flash:free` | active |
| 2 | `groq/qwen/qwen3.8-27b` | active |
| 3 | `literouter/llama-3.3-70b-instruct-turbo:free` | active |
| 4 | `literouter/deepseek-v3.2:free` | active |
| 5 | `literouter/kimi-k2.7-code-cheap:free` | active |
| 6 | `groq/openai/gpt-oss-120b` | active |
| 7 | `groq/openai/gpt-oss-20b` | active |
| 8 | `kilocode/cohere/north-mini-code:free` | active |
| 9 | `literouter/glm-5:free` | active |
| 10 | `literouter/gpt-oss-120b:free` | active |
| 11 | `literouter/qwen3-coder-next:free` | active |
| 12 | `openrouter/cohere/north-mini-code:free` | active |
| 13 | `gemini/gemini-3.8-flash` | dead (FAIL) |
| 14 | `auto/best-coding` | router (live) |

### `combo/llama-best` — priority, 21 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `ollama-cloud/gemma4:31b` | active |
| 2 | `cfp/meta/llama-4-scout-17b-16e-instruct` | untested |
| 3 | `cline/meta-llama/llama-4-maverick` | untested |
| 4 | `cline/meta-llama/llama-4-scout` | untested |
| 5 | `cfp/meta-llama/llama-3.3-70b-instruct-fp8-fast` | untested |
| 6 | `cline/meta-llama/llama-3.3-70b-instruct` | untested |
| 7 | `cline/meta-llama/llama-3.2-1b-instruct` | untested |
| 8 | `cline/meta-llama/llama-3.2-3b-instruct` | untested |
| 9 | `nvidia/meta/llama-3.2-11b-vision-instruct` | untested |
| 10 | `nvidia/meta/llama-3.2-90b-vision-instruct` | untested |
| 11 | `cfp/meta/llama-3.1-8b-instruct-fp8` | untested |
| 12 | `cline/aion-labs/aion-rp-llama-3.1-8b` | untested |
| 13 | `cline/meta-llama/llama-3.1-70b-instruct` | untested |
| 14 | `cline/meta-llama/llama-3.1-8b-instruct` | untested |
| 15 | `cline/nousresearch/hermes-3-llama-3.1-405b` | untested |
| 16 | `cline/nousresearch/hermes-3-llama-3.1-70b` | untested |
| 17 | `ollama-cloud/minimax-m2.7` | dead (FAIL-402) |
| 18 | `nvidia/nvidia/llama3-chatqa-1.5-70b` | untested |
| 19 | `nvidia/meta/codellama-70b` | untested |
| 20 | `nvidia/meta/llama2-70b` | untested |
| 21 | `auto/best-coding` | router (live) |

### `combo/mistral-best` — priority, 50 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `codestral/codestral-latest` | active |
| 2 | `codestral/codestral-2508` | active |
| 3 | `xkiro/mistralai/mistral-medium-3.5` | active |
| 4 | `xkiro/mistralai/codestral-2508` | active |
| 5 | `xkiro/mistralai/mistral-large-2512` | active |
| 6 | `xkiro/mistralai/mistral-small-2603` | active |
| 7 | `xkiro/mistralai/devstral-medium` | active |
| 8 | `cline/mistralai/mistral-large-4-0` | untested |
| 9 | `cline/mistralai/mistral-small-3.2-24b-instruct` | untested |
| 10 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | untested |
| 11 | `cline/mistralai/mistral-small-3.1-24b-instruct` | untested |
| 12 | `cline/mistralai/mistral-medium-3.1` | untested |
| 13 | `cline/mistralai/mistral-medium-3.1:batch` | untested |
| 14 | `cline/mistralai/mistral-medium-3-5` | untested |
| 15 | `cline/mistralai/mistral-medium-3-5:batch` | untested |
| 16 | `literouter/ministral-3-8b-instruct:free` | untested |
| 17 | `nvidia/mistralai/mistral-large-2-instruct` | untested |
| 18 | `nvidia/mistralai/mistral-7b-instruct-v0.3` | untested |
| 19 | `nvidia/mistralai/codestral-22b-instruct-v0.1` | dead (FAIL) |
| 20 | `nvidia/mistralai/mixtral-8x22b-v0.1` | untested |
| 21 | `cline/cognitivecomputations/dolphin-mistral-24b-venice-edition` | untested |
| 22 | `cline/mistralai/codestral-2508` | untested |
| 23 | `cline/mistralai/codestral-2508:batch` | untested |
| 24 | `cline/mistralai/devstral-2512` | untested |
| 25 | `cline/mistralai/mistral-large` | untested |
| 26 | `cline/mistralai/mistral-large-2407` | untested |
| 27 | `cline/mistralai/mistral-large-2512` | untested |
| 28 | `cline/mistralai/mistral-large-2512:batch` | untested |
| 29 | `cline/mistralai/mistral-nemo` | untested |
| 30 | `cline/mistralai/mistral-saba` | untested |
| 31 | `cline/mistralai/mistral-small-24b-instruct-2501` | untested |
| 32 | `cline/mistralai/mistral-small-2603` | untested |
| 33 | `cline/mistralai/mistral-small-2603:batch` | untested |
| 34 | `cline/mistralai/mixtral-8x22b-instruct` | untested |
| 35 | `cline/mistralai/voxtral-small-24b-2507` | untested |
| 36 | `ddgw/mistral-small-2603` | untested |
| 37 | `mistral/codestral-latest` | active |
| 38 | `nvidia/mistralai/mistral-large` | untested |
| 39 | `nvidia/nv-mistralai/mistral-nemo-12b-instruct` | untested |
| 40 | `cline/mistralai/mistral-medium-3` | untested |
| 41 | `cline/mistralai/ministral-14b-2512` | untested |
| 42 | `cline/mistralai/ministral-3b-2512` | untested |
| 43 | `cline/mistralai/ministral-8b-2512` | untested |
| 44 | `cline/mistralai/ministral-8b-2512:batch` | untested |
| 45 | `literouter/ministral-3b-2512:free` | untested |
| 46 | `nvidia/nvidia/mistral-nemo-minitron-8b-8k-instruct` | untested |
| 47 | `xkiro/mistralai/ministral-14b` | active |
| 48 | `xkiro/mistralai/ministral-3b` | active |
| 49 | `xkiro/mistralai/ministral-8b` | untested |
| 50 | `auto/best-coding` | router (live) |

### `combo/nara-best` — priority, 3 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `nara/laguna-s-2.1` | untested |
| 2 | `nara/nemotron-3.5-lightning-free` | untested |
| 3 | `auto/best-coding` | router (live) |

### `combo/nvidia-best` — priority, 33 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `cline/nvidia/nemotron-3.5-lightning:free` | active |
| 2 | `kilocode/nvidia/nemotron-3.5-content-safety:free` | active |
| 3 | `kilocode/nvidia/nemotron-3.5-lightning:free` | active |
| 4 | `openrouter/nvidia/nemotron-3.5-lightning:free` | active |
| 5 | `cline/nvidia/nemotron-3-ultra-550b-a55b:free` | active |
| 6 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | active |
| 7 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | active |
| 8 | `ollama-cloud/nemotron-3-super` | active |
| 9 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | active |
| 10 | `nvidia/nvidia/nemotron-4-340b-instruct` | dead (FAIL) |
| 11 | `nvidia/nvidia/nemotron-4-340b-reward` | untested |
| 12 | `cline/nvidia/nemotron-3.5-content-safety` | untested |
| 13 | `cline/nvidia/nemotron-3.5-content-safety:free` | untested |
| 14 | `cline/nvidia/nemotron-3.5-lightning` | untested |
| 15 | `nvidia/nvidia/nemotron-3.5-content-safety` | active |
| 16 | `nvidia/nvidia/nemotron-3.5-lightning-30b-a3b` | untested |
| 17 | `openrouter/nvidia/nemotron-3.5-content-safety:free` | untested |
| 18 | `nvidia/nvidia/llama-3.1-nemotron-ultra-253b-v1` | untested |
| 19 | `nvidia/nvidia/llama-3.1-nemotron-51b-instruct` | untested |
| 20 | `nvidia/nvidia/llama-3.1-nemotron-70b-instruct` | untested |
| 21 | `cline/nvidia/nemotron-3-ultra-550b-a55b` | untested |
| 22 | `nvidia/nvidia/nemotron-3-ultra-550b-a55b` | dead (FAIL) |
| 23 | `cfp/nvidia/nemotron-3-120b-a12b` | untested |
| 24 | `cline/nvidia/nemotron-3-super-120b-a12b` | untested |
| 25 | `cline/nvidia/nemotron-3-super-120b-a12b:free` | untested |
| 26 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | active |
| 27 | `cline/nvidia/nemotron-3-nano-30b-a3b` | untested |
| 28 | `cline/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | untested |
| 29 | `nvidia/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | untested |
| 30 | `nvidia/nvidia/nemotron-nano-3-30b-a3b` | untested |
| 31 | `nvidia/nvidia/nemotron-parse-2.0` | untested |
| 32 | `nvidia/nvidia/nemotron-parse` | untested |
| 33 | `auto/best-coding` | router (live) |

### `combo/ollama-best` — priority, 3 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `ollama-cloud/nemotron-3-super` | active |
| 2 | `ollama-cloud/gemma4:31b` | active |
| 3 | `auto/best-coding` | router (live) |

### `combo/openrouter-best` — priority, 10 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `openrouter/nvidia/nemotron-3.5-lightning:free` | active |
| 2 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | active |
| 3 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | active |
| 4 | `openrouter/poolside/laguna-s-2.1:free` | active |
| 5 | `openrouter/apodex/apodex-1.1-mini:free` | active |
| 6 | `openrouter/cohere/north-mini-code:free` | active |
| 7 | `openrouter/google/gemma-4-31b-it:free` | dead (FAIL-429) |
| 8 | `openrouter/liquid/lfm-2.5-2.6b:free` | untested |
| 9 | `openrouter/poolside/laguna-xs-2.1:free` | untested |
| 10 | `auto/best-coding` | router (live) |

### `combo/qwen-best` — priority, 58 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `xkiro/qwen/qwen3.8-max:free` | active |
| 2 | `groq/qwen/qwen3.8-27b` | active |
| 3 | `xkiro/qwen/qwen3.7-max:free` | active |
| 4 | `xkiro/qwen/qwen3.5-plus:free` | active |
| 5 | `xkiro/qwen/qwen3-max:free` | active |
| 6 | `cline/qwen/qwen3-coder-next` | active |
| 7 | `kiro/qwen3-coder-next` | active |
| 8 | `xkiro/qwen/qwen3-coder-plus:free` | active |
| 9 | `xkiro/qwen/qwen-plus-2025-07-28:free` | active |
| 10 | `cline/qwen/qwen3.8-max-0902` | untested |
| 11 | `cline/qwen/qwen3.8-max-prime` | untested |
| 12 | `cline/qwen/qwen3.8-2.4t-a95b` | untested |
| 13 | `cline/qwen/qwen3.8-27b` | untested |
| 14 | `cline/qwen/qwen3.8-flash` | untested |
| 15 | `cline/qwen/qwen3.8-omni-flash` | untested |
| 16 | `cline/qwen/qwen3.7-max` | untested |
| 17 | `cline/qwen/qwen3.7-flash` | untested |
| 18 | `cline/qwen/qwen3.7-plus` | untested |
| 19 | `xkiro/qwen/qwen3.7-plus:free` | active |
| 20 | `cline/qwen/qwen3.6-27b` | untested |
| 21 | `cline/qwen/qwen3.6-35b-a3b` | untested |
| 22 | `cline/qwen/qwen3.6-flash` | untested |
| 23 | `cline/qwen/qwen3.6-plus` | untested |
| 24 | `xkiro/qwen/qwen3.6-27b:free` | active |
| 25 | `xkiro/qwen/qwen3.6-35b-a3b:free` | untested |
| 26 | `xkiro/qwen/qwen3.6-plus:free` | untested |
| 27 | `cline/qwen/qwen3.5-122b-a10b` | untested |
| 28 | `cline/qwen/qwen3.5-27b` | untested |
| 29 | `cline/qwen/qwen3.5-35b-a3b` | untested |
| 30 | `cline/qwen/qwen3.5-397b-a17b` | untested |
| 31 | `cline/qwen/qwen3.5-9b` | untested |
| 32 | `cline/qwen/qwen3.5-flash-02-23` | untested |
| 33 | `cline/qwen/qwen3.5-plus-02-15` | untested |
| 34 | `cline/qwen/qwen3.5-plus-20260420` | untested |
| 35 | `xkiro/qwen/qwen3.5-397b-a17b:free` | untested |
| 36 | `xkiro/qwen/qwen3.5-flash:free` | active |
| 37 | `xkiro/qwen/qwen3.5-omni-flash:free` | untested |
| 38 | `xkiro/qwen/qwen3.5-omni-plus:free` | untested |
| 39 | `cfp/qwen/qwen2.5-coder-32b-instruct` | untested |
| 40 | `cline/qwen/qwen-2.5-72b-instruct` | untested |
| 41 | `cline/qwen/qwen-2.5-7b-instruct` | untested |
| 42 | `cline/qwen/qwen-2.5-coder-32b-instruct` | untested |
| 43 | `cfp/qwen/qwen3-30b-a3b-fp8` | untested |
| 44 | `cfp/qwen/qwq-32b` | untested |
| 45 | `cline/qwen/qwen-plus` | untested |
| 46 | `cline/qwen/qwen3-14b` | untested |
| 47 | `cline/qwen/qwen3-235b-a22b-2507` | untested |
| 48 | `cline/qwen/qwen3-235b-a22b-thinking-2507` | untested |
| 49 | `cline/qwen/qwen3-30b-a3b` | untested |
| 50 | `cline/qwen/qwen3-30b-a3b-instruct-2507` | untested |
| 51 | `cline/qwen/qwen3-32b` | untested |
| 52 | `cline/qwen/qwen3-coder` | untested |
| 53 | `cline/qwen/qwen3-coder-30b-a3b-instruct` | untested |
| 54 | `cline/qwen/qwen3-coder-flash` | untested |
| 55 | `cline/qwen/qwen3-next-80b-a3b-instruct` | untested |
| 56 | `cline/qwen/qwen3-next-80b-a3b-thinking` | untested |
| 57 | `xkiro/qwen/qwen3-omni-flash:free` | untested |
| 58 | `auto/best-coding` | router (live) |

### `combo/steady-coding` — priority, 3 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | active |
| 2 | `gemini/gemini-3.8-flash` | dead (FAIL) |
| 3 | `auto/best-coding` | router (live) |

### `combo/trae-best` — priority, 3 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `trae/gpt-5.4` | active |
| 2 | `trae/gpt-5.2` | active |
| 3 | `auto/best-coding` | router (live) |

### `combo/xkiro-best` — priority, 36 legs

| # | Model | Status |
|---|-------|--------|
| 1 | `xkiro/qwen/qwen3-coder-plus:free` | active |
| 2 | `groq/qwen/qwen3.8-27b` | active |
| 3 | `xkiro/mistralai/codestral-2508` | active |
| 4 | `openrouter/cohere/north-mini-code:free` | active |
| 5 | `xkiro/mistralai/devstral-medium` | active |
| 6 | `groq/openai/gpt-oss-20b` | active |
| 7 | `xkiro/qwen/qwen3-max:free` | active |
| 8 | `kilocode/cohere/north-mini-code:free` | active |
| 9 | `xkiro/qwen/qwen3.8-max:free` | active |
| 10 | `groq/openai/gpt-oss-120b` | active |
| 11 | `xkiro/qwen/qwen3.7-max:free` | active |
| 12 | `openrouter/poolside/laguna-s-2.1:free` | active |
| 13 | `xkiro/qwen/qwen3.6-max-preview:free` | active |
| 14 | `kilocode/poolside/laguna-s-2.1:free` | active |
| 15 | `xkiro/qwen/qwen3.5-plus:free` | active |
| 16 | `openrouter/poolside/laguna-xs-2.1:free` | untested |
| 17 | `xkiro/qwen/qwen3.7-plus:free` | active |
| 18 | `kilocode/poolside/laguna-xs-2.1:free` | active |
| 19 | `xkiro/qwen/qwen3.6-27b:free` | active |
| 20 | `gemini/gemini-3.8-flash` | dead (FAIL) |
| 21 | `xkiro/qwen/qwen-plus-2025-07-28:free` | active |
| 22 | `gemini/gemini-3.7-flash` | active |
| 23 | `xkiro/mistralai/mistral-large-2512` | active |
| 24 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | active |
| 25 | `xkiro/mistralai/mistral-medium-3.5` | active |
| 26 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | active |
| 27 | `xkiro/mistralai/mistral-small-2603` | active |
| 28 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | active |
| 29 | `xkiro/mistralai/ministral-14b` | active |
| 30 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | active |
| 31 | `xkiro/mistralai/ministral-8b` | untested |
| 32 | `openrouter/nvidia/nemotron-3.5-lightning:free` | active |
| 33 | `xkiro/mistralai/ministral-3b` | active |
| 34 | `kilocode/nvidia/nemotron-3.5-lightning:free` | active |
| 35 | `xkiro/sensenova/sensenova-6.8-flash-lite` | active |
| 36 | `auto/best-coding` | router (live) |

_Total routed legs: 766 across 29 combos_
