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

## 8. Combo catalog (30 combos, all priority strategy)

Generated live from the gateway. Attempt budget 200 each. Fail-through order = listed order (Claude-first where noted).

### `combo/all-best` (130 legs)

- `codestral/codestral-latest`
- `codestral/codestral-2508`
- `antigravity/claude-opus-4-6-thinking-low`
- `antigravity/claude-opus-4-6-thinking`
- `antigravity/claude-sonnet-4-6-low`
- `agy/claude-opus-4-6-thinking-low`
- `agy/claude-sonnet-4-6-low`
- `claude-web/claude-opus-4-6`
- `claude-web/claude-sonnet-4-6-low`
- `claude-web/claude-opus-5-low`
- `deepseek-web/deepseek-chat`
- `gemini/gemini-3.8-flash-lite-tts`
- `groq/openai/gpt-oss-120b`
- `openrouter/nvidia/nemotron-3-super-120b-a12b:free`
- `kilocode/nvidia/nemotron-3.5-lightning:free`
- `auto/coding:free`
- `codex/gpt-6-luna`
- `kiro/qwen3-coder-next`
- `mistral/codestral-latest`
- `literouter/glm-5:free`
- `xkiro/qwen/qwen3-coder-plus:free`
- `ollama-cloud/nemotron-3-super`
- `zai-web/glm-5.3`
- `grok-web/fast`
- `grok-cli/grok-4.7-low`
- `deepseek-web/DeepSeek-V3.2`
- `groq/qwen/qwen3.8-27b`
- `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free`
- `kilocode/poolside/laguna-s-2.1:free`
- `codex/gpt-5.6-luna`
- `kiro/glm-5`
- `literouter/glm-5.3-flash:free`
- `xkiro/qwen/qwen3-max:free`
- `ollama-cloud/gemma4:31b`
- `zai-web/glm-5.3-flash`
- `grok-cli/grok-4.7`
- `deepseek-web/deepseek-reasoner`
- `groq/openai/gpt-oss-20b`
- `openrouter/cohere/north-mini-code:free`
- `kilocode/poolside/laguna-xs-2.1:free`
- `codex/gpt-5.5`
- `kiro/deepseek-3.2`
- `literouter/deepseek-v3.2:free`
- `xkiro/mistralai/codestral-2508`
- `zai-web/glm-5.2`
- `grok-cli/grok-4.7-medium`
- `deepseek-web/deepseek-v4-flash`
- `openrouter/poolside/laguna-s-2.1:free`
- `kilocode/nvidia/nemotron-3-super-120b-a12b:free`
- `codex/gpt-5.6-terra`
- `kiro/minimax-m2.1`
- `literouter/gpt-oss-120b:free`
- `xkiro/mistralai/mistral-small-2603`
- `grok-cli/grok-4.7-high`
- `deepseek-web/deepseek-v4-pro`
- `openrouter/poolside/laguna-xs-2.1:free`
- `kilocode/cohere/north-mini-code:free`
- `kiro/minimax-m2.5`
- `literouter/kimi-k2.7-code-cheap:free`
- `xkiro/qwen/qwen3.8-max:free`
- `deepseek-web/deepseek-v4-pro-think`
- `openrouter/nvidia/nemotron-3.5-lightning:free`
- `literouter/qwen3-coder-next:free`
- `xkiro/qwen/qwen3.7-max:free`
- `deepseek-web/deepseek-v4-pro-search`
- `literouter/llama-3.3-70b-instruct-turbo:free`
- `xkiro/qwen/qwen3.6-max-preview:free`
- `deepseek-web/deepseek-v4-pro-think-search`
- `literouter/ministral-3b-2512:free`
- `xkiro/mistralai/mistral-large-2512`
- `deepseek-web/deepseek-v4-flash-think`
- `literouter/ministral-3-8b-instruct:free`
- `xkiro/qwen/qwen3.5-plus:free`
- `deepseek-web/deepseek-v4-flash-search`
- `literouter/deepseek-v3.1`
- `xkiro/sensenova/sensenova-6.8-flash-lite`
- `deepseek-web/deepseek-v4-flash-think-search`
- `literouter/deepseek-v3.1:free`
- `xkiro/mistralai/devstral-medium`
- `deepseek-web/DeepSeek-R1`
- `literouter/deepseek-v3.2`
- `xkiro/mistralai/mistral-medium-3.5`
- `deepseek-web/DeepSeek-R1-Search`
- `literouter/deepseek-v4-flash`
- `xkiro/mistralai/ministral-8b`
- `deepseek-web/DeepSeek-Search`
- `literouter/deepseek-v4-flash-cheap`
- `literouter/deepseek-v4-flash-cheap:free`
- `literouter/deepseek-v4-flash-stable`
- `literouter/deepseek-v4-flash:free`
- `literouter/deepseek-v4-pro`
- `literouter/deepseek-v4-pro-cheap`
- `literouter/deepseek-v4-pro-cheap:free`
- `literouter/deepseek-v4.1-flash`
- `literouter/deepseek-v4.1-flash-cheap`
- `literouter/deepseek-v4.1-flash-cheap:free`
- `literouter/deepseek-v4.1-flash-stable`
- `literouter/deepseek-v4.1-flash-stable:free`
- `literouter/deepseek-v4.1-flash:free`
- `literouter/gemini-2.5-flash-lite:free`
- `literouter/glm-4.5`
- `literouter/glm-4.5-air`
- `literouter/glm-4.5-air:free`
- `literouter/glm-4.5:free`
- `literouter/glm-4.6`
- `literouter/glm-4.6:free`
- `literouter/glm-4.7`
- `literouter/glm-4.7-flash`
- `literouter/glm-4.7-flash-heretic`
- `literouter/glm-4.7-flash-heretic:free`
- `literouter/glm-4.7-flash:free`
- `literouter/glm-4.7:free`
- `literouter/glm-5`
- `literouter/glm-5.1`
- `literouter/glm-5.1-cheap:free`
- `literouter/glm-5.1:free`
- `literouter/glm-5.2`
- `literouter/glm-5.2-cheap`
- `literouter/glm-5.2-cheap:free`
- `literouter/glm-5.2:free`
- `literouter/glm-5.3`
- `literouter/glm-5.3-cheap`
- `literouter/glm-5.3-flash`
- `literouter/glm-5.3-flash-cheap`
- `literouter/glm-5.3-flash-cheap:free`
- `literouter/gpt-5-mini`
- `literouter/gpt-5-mini-stable`
- `nara/laguna-s-2.1`
- `nara/nemotron-3.5-lightning-free`
- `auto/best-coding`

### `combo/apinex-best` (9 legs)

- `groq/openai/gpt-oss-120b`
- `openai/free/gpt-6-luna`
- `openai/free/glm-5.3-flash`
- `openai/free/deepseek-v4.1-flash`
- `openai/free/qwen-3.8-max`
- `openai/free/mimo-v2.6-pro`
- `openai/free/deepseek-v4-pro-0813`
- `openai/free/deepseek-v4-flash-0731`
- `auto/best-coding`

### `combo/claude-best` (34 legs)

- `openai/claude-opus-5.5`
- `openai/claude-sonnet-5`
- `claude-web/claude-opus-5-low`
- `cline/anthropic/claude-opus-4.8-low`
- `claude-web/claude-opus-5-high`
- `claude-web/claude-opus-5-xhigh`
- `claude-web/claude-opus-5-medium`
- `antigravity/claude-opus-4-6-thinking`
- `claude-web/claude-opus-4-6`
- `agy/claude-opus-4-6-thinking-low`
- `antigravity/claude-opus-4-6-thinking-low`
- `claude-web/claude-opus-4-6-low`
- `claude-web/claude-opus-4-7-low`
- `claude-web/claude-opus-4-8-low`
- `claude-web/claude-opus-5`
- `claude-web/claude-sonnet-5-high`
- `claude-web/claude-sonnet-5-xhigh`
- `claude-web/claude-sonnet-5-medium`
- `claude-web/claude-sonnet-5-low`
- `kiro/claude-sonnet-4.5`
- `agy/claude-sonnet-4-6`
- `antigravity/claude-sonnet-4-6`
- `claude-web/claude-sonnet-4-6`
- `agy/claude-sonnet-4-6-low`
- `antigravity/claude-sonnet-4-6-low`
- `claude-web/claude-sonnet-4-6-low`
- `claude-web/claude-sonnet-5`
- `cline/anthropic/claude-sonnet-5`
- `claude-web/claude-fable-5-1-low`
- `claude-web/claude-fable-5-low`
- `cline/anthropic/claude-fable-5-low`
- `kiro/claude-haiku-4.5`
- `claude-web/claude-haiku-4-5-20251001-low`
- `auto/best-coding`

### `combo/claude-code` (4 legs)

- `groq/openai/gpt-oss-120b`
- `auto/claude-sonnet`
- `gemini/gemini-3.8-flash`
- `auto/best-coding`

### `combo/claude-fast` (4 legs)

- `groq/openai/gpt-oss-120b`
- `gemini/gemini-3.8-flash`
- `auto/best-fast`
- `auto/best-coding`

### `combo/claude-max` (5 legs)

- `auto/claude-opus`
- `groq/openai/gpt-oss-120b`
- `auto/claude-sonnet`
- `gemini/gemini-3.8-flash`
- `auto/best-coding`

### `combo/cleanapis-best` (24 legs)

- `openai/claude-sonnet-5`
- `groq/openai/gpt-oss-120b`
- `openai/claude-opus-5.5`
- `gemini/gemini-3.8-flash`
- `openai/kimi-k3`
- `groq/qwen/qwen3.8-27b`
- `openai/glm-5.3`
- `openrouter/cohere/north-mini-code:free`
- `openai/deepseek-v4-pro-max`
- `kilocode/cohere/north-mini-code:free`
- `openai/free/qwen-3.8-max`
- `groq/openai/gpt-oss-20b`
- `openai/free/deepseek-v4.1-flash`
- `openrouter/poolside/laguna-s-2.1:free`
- `openai/free/deepseek-v4-flash-0731`
- `kilocode/poolside/laguna-s-2.1:free`
- `openai/free/deepseek-v4-pro-0813`
- `gemini/gemini-3.7-flash`
- `openai/free/gpt-6-luna`
- `openrouter/poolside/laguna-xs-2.1:free`
- `openai/free/glm-5.3-flash`
- `kilocode/poolside/laguna-xs-2.1:free`
- `openai/free/mimo-v2.6-pro`
- `auto/best-coding`

### `combo/codex-best` (5 legs)

- `codex/gpt-6-luna`
- `codex/gpt-5.6-luna`
- `codex/gpt-5.6-terra`
- `codex/gpt-5.5`
- `auto/best-coding`

### `combo/deepseek-best` (44 legs)

- `openai/deepseek-v4-pro-max`
- `deepseek-web/DeepSeek-V3.2`
- `deepseek-web/deepseek-v4-pro`
- `deepseek-web/deepseek-v4-pro-search`
- `deepseek-web/deepseek-v4-pro-think`
- `deepseek-web/deepseek-v4-pro-think-search`
- `deepseek-web/DeepSeek-R1`
- `deepseek-web/DeepSeek-R1-Search`
- `deepseek-web/DeepSeek-Search`
- `deepseek-web/deepseek-chat`
- `deepseek-web/deepseek-reasoner`
- `deepseek-web/deepseek-v4-flash`
- `deepseek-web/deepseek-v4-flash-search`
- `deepseek-web/deepseek-v4-flash-think`
- `deepseek-web/deepseek-v4-flash-think-search`
- `nvidia/deepseek-ai/deepseek-coder-6.7b-instruct`
- `cline/deepseek/deepseek-v4.1-flash`
- `cline/deepseek/deepseek-v4.1-flash:batch`
- `nvidia/deepseek-ai/deepseek-v4.1-flash`
- `cline/deepseek/deepseek-v3.2`
- `cline/deepseek/deepseek-v3.2-exp`
- `kiro/deepseek-3.2`
- `xkiro/deepseek/deepseek-v3.2`
- `cline/deepseek/deepseek-chat-v3.1`
- `cline/deepseek/deepseek-v3.1-terminus`
- `xkiro/deepseek/deepseek-chat-v3.1`
- `cfp/deepseek-ai/deepseek-v4-pro-0813`
- `cline/deepseek/deepseek-v4-pro`
- `cline/deepseek/deepseek-v4-pro-0813`
- `cline/~deepseek/deepseek-pro-latest`
- `xkiro/deepseek/deepseek-v4-pro`
- `cfp/deepseek-ai/deepseek-r1-distill-qwen-32b`
- `cfp/deepseek-ai/deepseek-v4-flash-0731`
- `cline/deepseek/deepseek-chat`
- `cline/deepseek/deepseek-chat-v3-0324`
- `cline/deepseek/deepseek-r1`
- `cline/deepseek/deepseek-r1-0528`
- `cline/deepseek/deepseek-v4-flash`
- `cline/deepseek/deepseek-v4-flash-0731`
- `cline/deepseek/deepseek-v4-flash-vision-exp`
- `cline/~deepseek/deepseek-flash-latest`
- `cline/~deepseek/deepseek-v4-flash-latest`
- `xkiro/deepseek/deepseek-v4-flash`
- `auto/best-coding`

### `combo/gemini-best` (30 legs)

- `gemini/gemini-3.7-flash`
- `agy/gemini-3.8-flash-low`
- `cline/google/gemini-3.8-flash`
- `gemini/gemini-3.8-flash`
- `agy/gemini-3.7-flash-low`
- `cline/google/gemini-3.7-flash`
- `agy/gemini-3.6-flash-low`
- `cline/google/gemini-3.6-flash`
- `agy/gemini-3.5-flash-lite`
- `antigravity/gemini-3.5-flash-lite`
- `cline/google/gemini-3.5-flash`
- `cline/google/gemini-3.5-flash-lite`
- `agy/gemini-3.1-pro-low`
- `antigravity/gemini-3.1-pro-low`
- `agy/gemini-3.1-flash-lite`
- `antigravity/gemini-3.1-flash-lite`
- `cline/google/gemini-3.1-flash-lite`
- `gemini/gemini-3.1-flash-lite`
- `agy/gemini-3-flash`
- `antigravity/gemini-3-flash`
- `gemini/gemini-3-flash-preview`
- `cline/google/gemini-2.5-pro`
- `cline/google/gemini-2.5-flash`
- `cline/google/gemini-2.5-flash-lite`
- `gemini/gemini-2.5-flash-lite`
- `agy/gemini-pro-agent`
- `antigravity/gemini-pro-agent`
- `cline/~google/gemini-pro-latest`
- `cline/~google/gemini-flash-latest`
- `auto/best-coding`

### `combo/gemma-best` (21 legs)

- `cfp/google/gemma-4-26b-a4b-it`
- `cline/google/gemma-4-26b-a4b-it`
- `cline/google/gemma-4-26b-a4b-it:free`
- `cline/google/gemma-4-31b-it`
- `cline/google/gemma-4-31b-it:free`
- `nvidia/google/gemma-4-31b-it`
- `openrouter/google/gemma-4-26b-a4b-it:free`
- `openrouter/google/gemma-4-31b-it:free`
- `cline/google/gemma-3-12b-it`
- `cline/google/gemma-3-27b-it`
- `cline/google/gemma-3-4b-it`
- `nvidia/google/gemma-3-12b-it`
- `nvidia/google/gemma-3-4b-it`
- `cline/google/gemma-2-27b-it`
- `nvidia/google/codegemma-1.1-7b`
- `cfp/aisingapore/gemma-sea-lion-v4-27b-it`
- `ddgw/tinfoil/gemma4-31b`
- `nvidia/google/codegemma-7b`
- `nvidia/google/gemma-2b`
- `nvidia/google/recurrentgemma-2b`
- `auto/best-coding`

### `combo/glm-best` (39 legs)

- `openai/glm-5.3`
- `cline/z-ai/glm-5.3`
- `zai-web/glm-5.2`
- `kiro/glm-5`
- `zai-web/glm-5.3-flash-max`
- `zai-web/glm-5.3-max`
- `zai-web/glm-5.3-flash-high`
- `zai-web/glm-5.3-high`
- `cline/z-ai/glm-5.3-flash`
- `cline/z-ai/glm-5.3-flash:batch`
- `cline/z-ai/glm-5.3-flashx`
- `cline/z-ai/glm-5.3-prime`
- `cline/z-ai/glm-5.3:batch`
- `nvidia/z-ai/glm-5.3`
- `nvidia/z-ai/glm-5.3-flash`
- `zai-web/glm-5.3`
- `zai-web/glm-5.3-flash`
- `zai-web/glm-5.3-flash-low`
- `zai-web/glm-5.3-low`
- `zai-web/glm-5.2-max`
- `zai-web/glm-5.2-high`
- `aug/glm-5.2`
- `cfp/zai-org/glm-5.2`
- `cline/z-ai/glm-5.2`
- `cline/z-ai/glm-5.1`
- `cline/z-ai/glm-5-turbo`
- `cfp/zai-org/glm-4.7-flash`
- `cline/z-ai/glm-4.7`
- `cline/z-ai/glm-4.7-flash`
- `cline/z-ai/glm-4.6`
- `cline/z-ai/glm-4.6v`
- `cline/z-ai/glm-4.5`
- `cline/z-ai/glm-4.5-air`
- `cline/z-ai/glm-4.5v`
- `cline/z-ai/glm-5`
- `cline/z-ai/glm-5v-turbo`
- `cline/~z-ai/glm-flash-latest`
- `cline/~z-ai/glm-latest`
- `auto/best-coding`

### `combo/gpt-best` (127 legs)

- `codex/gpt-6-luna`
- `cline/openai/gpt-5.6-sol`
- `codex/gpt-5.6-luna`
- `codex/gpt-5.6-terra`
- `codex/gpt-5.5`
- `cline/openai/gpt-5.4-mini`
- `groq/openai/gpt-oss-120b`
- `groq/openai/gpt-oss-20b`
- `cline/openai/gpt-4o-2024-05-13`
- `cline/openai/gpt-4o-2024-08-06`
- `cline/openai/gpt-4o-2024-11-20`
- `cline/openai/gpt-4o-mini-2024-07-18`
- `cline/openai/gpt-6.1-sol-pro`
- `cline/openai/gpt-6.1-sol-pro:batch`
- `cline/openai/gpt-6.1-sol`
- `cline/openai/gpt-6.1-sol:batch`
- `codex/gpt-6-astra-max`
- `codex/gpt-6-astra-ultra`
- `codex/gpt-6-luna-max`
- `codex/gpt-6-sol-max`
- `codex/gpt-6-sol-ultra`
- `cline/openai/gpt-6-astra-pro`
- `cline/openai/gpt-6-astra-pro:batch`
- `cline/openai/gpt-6-luna-pro`
- `cline/openai/gpt-6-luna-pro:batch`
- `cline/openai/gpt-6-sol-pro`
- `cline/openai/gpt-6-sol-pro:batch`
- `codex/gpt-6-astra-high`
- `codex/gpt-6-astra-xhigh`
- `codex/gpt-6-luna-high`
- `codex/gpt-6-luna-xhigh`
- `codex/gpt-6-sol-high`
- `codex/gpt-6-sol-xhigh`
- `cline/openai/gpt-6-astra`
- `cline/openai/gpt-6-astra:batch`
- `cline/openai/gpt-6-luna`
- `cline/openai/gpt-6-luna:batch`
- `cline/openai/gpt-6-sol`
- `cline/openai/gpt-6-sol:batch`
- `codex/gpt-6-astra`
- `codex/gpt-6-sol`
- `codex/gpt-6-astra-medium`
- `codex/gpt-6-luna-medium`
- `codex/gpt-6-sol-medium`
- `codex/gpt-6-astra-low`
- `codex/gpt-6-luna-low`
- `codex/gpt-6-sol-low`
- `codex/gpt-5.6-luna-max`
- `codex/gpt-5.6-sol-max`
- `codex/gpt-5.6-sol-ultra`
- `codex/gpt-5.6-terra-max`
- `codex/gpt-5.6-terra-ultra`
- `cline/openai/gpt-5.6-luna-pro`
- `cline/openai/gpt-5.6-luna-pro:batch`
- `cline/openai/gpt-5.6-sol-pro`
- `cline/openai/gpt-5.6-sol-pro:batch`
- `cline/openai/gpt-5.6-terra-pro`
- `cline/openai/gpt-5.6-terra-pro:batch`
- `codex/gpt-5.6-luna-high`
- `codex/gpt-5.6-luna-xhigh`
- `codex/gpt-5.6-sol-high`
- `codex/gpt-5.6-sol-xhigh`
- `codex/gpt-5.6-terra-high`
- `codex/gpt-5.6-terra-xhigh`
- `cline/openai/gpt-5.6-luna`
- `cline/openai/gpt-5.6-luna:batch`
- `cline/openai/gpt-5.6-sol:batch`
- `cline/openai/gpt-5.6-terra`
- `cline/openai/gpt-5.6-terra:batch`
- `codex/gpt-5.6-sol`
- `ddgw/gpt-5.6-luna`
- `kiro/gpt-5.6-luna`
- `kiro/gpt-5.6-sol`
- `kiro/gpt-5.6-terra`
- `codex/gpt-5.6-luna-medium`
- `codex/gpt-5.6-sol-medium`
- `codex/gpt-5.6-terra-medium`
- `codex/gpt-5.6-luna-low`
- `codex/gpt-5.6-sol-low`
- `codex/gpt-5.6-terra-low`
- `cline/openai/gpt-5.5-pro`
- `cline/openai/gpt-5.5-pro:batch`
- `codex/gpt-5.5-high`
- `codex/gpt-5.5-xhigh`
- `cline/openai/gpt-5.5`
- `cline/openai/gpt-5.5:batch`
- `codex/gpt-5.5-medium`
- `codex/gpt-5.5-low`
- `cline/openai/gpt-5.4-pro`
- `cline/openai/gpt-5.4-pro:batch`
- `cline/openai/gpt-5.4`
- `cline/openai/gpt-5.4:batch`
- `cline/openai/gpt-5.4-nano`
- `cline/openai/gpt-5.4-nano:batch`
- `cline/openai/gpt-5.4-mini:batch`
- `ddgw/gpt-5.4-mini`
- `cline/openai/gpt-5.3-codex`
- `cline/openai/gpt-5.2-pro`
- `cline/openai/gpt-5.2-pro:batch`
- `cline/openai/gpt-5.2`
- `cline/openai/gpt-5.2-chat`
- `cline/openai/gpt-5.2:batch`
- `cline/openai/gpt-5.1`
- `cline/openai/gpt-5.1:batch`
- `cline/openai/gpt-5-pro`
- `cline/openai/gpt-5-pro:batch`
- `cline/openai/gpt-5-nano`
- `cline/openai/gpt-5-nano:batch`
- `cline/openai/gpt-5-mini`
- `cline/openai/gpt-5-mini:batch`
- `cfp/openai/gpt-oss-120b`
- `cfp/openai/gpt-oss-20b`
- `cline/openai/gpt-4o`
- `cline/openai/gpt-4o:batch`
- `cline/openai/gpt-5`
- `cline/openai/gpt-5:batch`
- `cline/openai/gpt-oss-120b`
- `cline/openai/gpt-oss-120b:batch`
- `cline/openai/gpt-oss-20b`
- `cline/openai/gpt-oss-20b:batch`
- `ddgw/tinfoil/gpt-oss-120b`
- `nvidia/openai/gpt-oss-20b`
- `agy/gpt-oss-120b-medium`
- `antigravity/gpt-oss-120b-medium`
- `cline/openai/gpt-4o-mini`
- `cline/openai/gpt-4o-mini:batch`
- `auto/best-coding`

### `combo/grok-best` (18 legs)

- `grok-cli/grok-4.7-high`
- `grok-cli/grok-4.7-medium`
- `grok-cli/grok-4.7-low`
- `cline/x-ai/grok-4.5`
- `grok-web/fast`
- `cline/x-ai/grok-4.20`
- `cline/x-ai/grok-4.20-multi-agent`
- `grok-cli/grok-4.7-xhigh`
- `cline/x-ai/grok-4.7`
- `grok-cli/grok-4.7`
- `cline/x-ai/grok-4.6`
- `cline/x-ai/grok-4.3`
- `cline/x-ai/grok-4.3:batch`
- `cline/x-ai/grok-build-0.1`
- `cline/~x-ai/grok-latest`
- `grok-web/expert`
- `grok-web/heavy`
- `auto/best-coding`

### `combo/keep-trying` (5 legs)

- `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free`
- `openrouter/nvidia/nemotron-3-super-120b-a12b:free`
- `groq/openai/gpt-oss-120b`
- `gemini/gemini-3.8-flash`
- `auto/best-coding`

### `combo/kilocode-best` (7 legs)

- `kilocode/nvidia/nemotron-3.5-lightning:free`
- `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free`
- `kilocode/nvidia/nemotron-3-super-120b-a12b:free`
- `kilocode/poolside/laguna-s-2.1:free`
- `kilocode/poolside/laguna-xs-2.1:free`
- `kilocode/cohere/north-mini-code:free`
- `auto/best-coding`

### `combo/kimi-best` (18 legs)

- `openai/kimi-k3`
- `cline/moonshotai/kimi-k3`
- `aug/kimi-k2.7`
- `cfp/moonshotai/kimi-k2.7-code`
- `cline/moonshotai/kimi-k2.7-code`
- `aug/kimi-k2.6`
- `cfp/moonshotai/kimi-k2.6`
- `cline/moonshotai/kimi-k2.6`
- `nvidia/moonshotai/kimi-k2.6`
- `ollama-cloud/kimi-k2.6`
- `cline/moonshotai/kimi-k2.5`
- `cline/moonshotai/kimi-k2`
- `cline/moonshotai/kimi-k2-0905`
- `cline/moonshotai/kimi-k2-thinking`
- `cline/moonshotai/kimi-k3:batch`
- `cline/~moonshotai/kimi-latest`
- `nvidia/moonshotai/kimi-k3`
- `auto/best-coding`

### `combo/kiro-best` (8 legs)

- `kiro/glm-5`
- `kiro/qwen3-coder-next`
- `kiro/claude-sonnet-4.5`
- `kiro/claude-haiku-4.5`
- `kiro/deepseek-3.2`
- `kiro/minimax-m2.5`
- `kiro/minimax-m2.1`
- `auto/best-coding`

### `combo/literouter-best` (14 legs)

- `literouter/glm-5.3-flash:free`
- `groq/qwen/qwen3.8-27b`
- `literouter/llama-3.3-70b-instruct-turbo:free`
- `literouter/deepseek-v3.2:free`
- `literouter/kimi-k2.7-code-cheap:free`
- `groq/openai/gpt-oss-120b`
- `groq/openai/gpt-oss-20b`
- `kilocode/cohere/north-mini-code:free`
- `literouter/glm-5:free`
- `literouter/gpt-oss-120b:free`
- `literouter/qwen3-coder-next:free`
- `openrouter/cohere/north-mini-code:free`
- `gemini/gemini-3.8-flash`
- `auto/best-coding`

### `combo/llama-best` (21 legs)

- `ollama-cloud/gemma4:31b`
- `cfp/meta/llama-4-scout-17b-16e-instruct`
- `cline/meta-llama/llama-4-maverick`
- `cline/meta-llama/llama-4-scout`
- `cfp/meta-llama/llama-3.3-70b-instruct-fp8-fast`
- `cline/meta-llama/llama-3.3-70b-instruct`
- `cline/meta-llama/llama-3.2-1b-instruct`
- `cline/meta-llama/llama-3.2-3b-instruct`
- `nvidia/meta/llama-3.2-11b-vision-instruct`
- `nvidia/meta/llama-3.2-90b-vision-instruct`
- `cfp/meta/llama-3.1-8b-instruct-fp8`
- `cline/aion-labs/aion-rp-llama-3.1-8b`
- `cline/meta-llama/llama-3.1-70b-instruct`
- `cline/meta-llama/llama-3.1-8b-instruct`
- `cline/nousresearch/hermes-3-llama-3.1-405b`
- `cline/nousresearch/hermes-3-llama-3.1-70b`
- `ollama-cloud/minimax-m2.7`
- `nvidia/nvidia/llama3-chatqa-1.5-70b`
- `nvidia/meta/codellama-70b`
- `nvidia/meta/llama2-70b`
- `auto/best-coding`

### `combo/mistral-best` (50 legs)

- `codestral/codestral-latest`
- `codestral/codestral-2508`
- `xkiro/mistralai/mistral-medium-3.5`
- `xkiro/mistralai/codestral-2508`
- `xkiro/mistralai/mistral-large-2512`
- `xkiro/mistralai/mistral-small-2603`
- `xkiro/mistralai/devstral-medium`
- `cline/mistralai/mistral-large-4-0`
- `cline/mistralai/mistral-small-3.2-24b-instruct`
- `cfp/mistralai/mistral-small-3.1-24b-instruct`
- `cline/mistralai/mistral-small-3.1-24b-instruct`
- `cline/mistralai/mistral-medium-3.1`
- `cline/mistralai/mistral-medium-3.1:batch`
- `cline/mistralai/mistral-medium-3-5`
- `cline/mistralai/mistral-medium-3-5:batch`
- `literouter/ministral-3-8b-instruct:free`
- `nvidia/mistralai/mistral-large-2-instruct`
- `nvidia/mistralai/mistral-7b-instruct-v0.3`
- `nvidia/mistralai/codestral-22b-instruct-v0.1`
- `nvidia/mistralai/mixtral-8x22b-v0.1`
- `cline/cognitivecomputations/dolphin-mistral-24b-venice-edition`
- `cline/mistralai/codestral-2508`
- `cline/mistralai/codestral-2508:batch`
- `cline/mistralai/devstral-2512`
- `cline/mistralai/mistral-large`
- `cline/mistralai/mistral-large-2407`
- `cline/mistralai/mistral-large-2512`
- `cline/mistralai/mistral-large-2512:batch`
- `cline/mistralai/mistral-nemo`
- `cline/mistralai/mistral-saba`
- `cline/mistralai/mistral-small-24b-instruct-2501`
- `cline/mistralai/mistral-small-2603`
- `cline/mistralai/mistral-small-2603:batch`
- `cline/mistralai/mixtral-8x22b-instruct`
- `cline/mistralai/voxtral-small-24b-2507`
- `ddgw/mistral-small-2603`
- `mistral/codestral-latest`
- `nvidia/mistralai/mistral-large`
- `nvidia/nv-mistralai/mistral-nemo-12b-instruct`
- `cline/mistralai/mistral-medium-3`
- `cline/mistralai/ministral-14b-2512`
- `cline/mistralai/ministral-3b-2512`
- `cline/mistralai/ministral-8b-2512`
- `cline/mistralai/ministral-8b-2512:batch`
- `literouter/ministral-3b-2512:free`
- `nvidia/nvidia/mistral-nemo-minitron-8b-8k-instruct`
- `xkiro/mistralai/ministral-14b`
- `xkiro/mistralai/ministral-3b`
- `xkiro/mistralai/ministral-8b`
- `auto/best-coding`

### `combo/nara-best` (3 legs)

- `nara/laguna-s-2.1`
- `nara/nemotron-3.5-lightning-free`
- `auto/best-coding`

### `combo/nvidia-best` (33 legs)

- `cline/nvidia/nemotron-3.5-lightning:free`
- `kilocode/nvidia/nemotron-3.5-content-safety:free`
- `kilocode/nvidia/nemotron-3.5-lightning:free`
- `openrouter/nvidia/nemotron-3.5-lightning:free`
- `cline/nvidia/nemotron-3-ultra-550b-a55b:free`
- `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free`
- `kilocode/nvidia/nemotron-3-super-120b-a12b:free`
- `ollama-cloud/nemotron-3-super`
- `openrouter/nvidia/nemotron-3-super-120b-a12b:free`
- `nvidia/nvidia/nemotron-4-340b-instruct`
- `nvidia/nvidia/nemotron-4-340b-reward`
- `cline/nvidia/nemotron-3.5-content-safety`
- `cline/nvidia/nemotron-3.5-content-safety:free`
- `cline/nvidia/nemotron-3.5-lightning`
- `nvidia/nvidia/nemotron-3.5-content-safety`
- `nvidia/nvidia/nemotron-3.5-lightning-30b-a3b`
- `openrouter/nvidia/nemotron-3.5-content-safety:free`
- `nvidia/nvidia/llama-3.1-nemotron-ultra-253b-v1`
- `nvidia/nvidia/llama-3.1-nemotron-51b-instruct`
- `nvidia/nvidia/llama-3.1-nemotron-70b-instruct`
- `cline/nvidia/nemotron-3-ultra-550b-a55b`
- `nvidia/nvidia/nemotron-3-ultra-550b-a55b`
- `cfp/nvidia/nemotron-3-120b-a12b`
- `cline/nvidia/nemotron-3-super-120b-a12b`
- `cline/nvidia/nemotron-3-super-120b-a12b:free`
- `nvidia/nvidia/nemotron-3-super-120b-a12b`
- `cline/nvidia/nemotron-3-nano-30b-a3b`
- `cline/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- `nvidia/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`
- `nvidia/nvidia/nemotron-nano-3-30b-a3b`
- `nvidia/nvidia/nemotron-parse-2.0`
- `nvidia/nvidia/nemotron-parse`
- `auto/best-coding`

### `combo/ollama-best` (3 legs)

- `ollama-cloud/nemotron-3-super`
- `ollama-cloud/gemma4:31b`
- `auto/best-coding`

### `combo/openrouter-best` (10 legs)

- `openrouter/nvidia/nemotron-3.5-lightning:free`
- `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free`
- `openrouter/nvidia/nemotron-3-super-120b-a12b:free`
- `openrouter/poolside/laguna-s-2.1:free`
- `openrouter/apodex/apodex-1.1-mini:free`
- `openrouter/cohere/north-mini-code:free`
- `openrouter/google/gemma-4-31b-it:free`
- `openrouter/liquid/lfm-2.5-2.6b:free`
- `openrouter/poolside/laguna-xs-2.1:free`
- `auto/best-coding`

### `combo/qwen-best` (58 legs)

- `xkiro/qwen/qwen3.8-max:free`
- `groq/qwen/qwen3.8-27b`
- `xkiro/qwen/qwen3.7-max:free`
- `xkiro/qwen/qwen3.5-plus:free`
- `xkiro/qwen/qwen3-max:free`
- `cline/qwen/qwen3-coder-next`
- `kiro/qwen3-coder-next`
- `xkiro/qwen/qwen3-coder-plus:free`
- `xkiro/qwen/qwen-plus-2025-07-28:free`
- `cline/qwen/qwen3.8-max-0902`
- `cline/qwen/qwen3.8-max-prime`
- `cline/qwen/qwen3.8-2.4t-a95b`
- `cline/qwen/qwen3.8-27b`
- `cline/qwen/qwen3.8-flash`
- `cline/qwen/qwen3.8-omni-flash`
- `cline/qwen/qwen3.7-max`
- `cline/qwen/qwen3.7-flash`
- `cline/qwen/qwen3.7-plus`
- `xkiro/qwen/qwen3.7-plus:free`
- `cline/qwen/qwen3.6-27b`
- `cline/qwen/qwen3.6-35b-a3b`
- `cline/qwen/qwen3.6-flash`
- `cline/qwen/qwen3.6-plus`
- `xkiro/qwen/qwen3.6-27b:free`
- `xkiro/qwen/qwen3.6-35b-a3b:free`
- `xkiro/qwen/qwen3.6-plus:free`
- `cline/qwen/qwen3.5-122b-a10b`
- `cline/qwen/qwen3.5-27b`
- `cline/qwen/qwen3.5-35b-a3b`
- `cline/qwen/qwen3.5-397b-a17b`
- `cline/qwen/qwen3.5-9b`
- `cline/qwen/qwen3.5-flash-02-23`
- `cline/qwen/qwen3.5-plus-02-15`
- `cline/qwen/qwen3.5-plus-20260420`
- `xkiro/qwen/qwen3.5-397b-a17b:free`
- `xkiro/qwen/qwen3.5-flash:free`
- `xkiro/qwen/qwen3.5-omni-flash:free`
- `xkiro/qwen/qwen3.5-omni-plus:free`
- `cfp/qwen/qwen2.5-coder-32b-instruct`
- `cline/qwen/qwen-2.5-72b-instruct`
- `cline/qwen/qwen-2.5-7b-instruct`
- `cline/qwen/qwen-2.5-coder-32b-instruct`
- `cfp/qwen/qwen3-30b-a3b-fp8`
- `cfp/qwen/qwq-32b`
- `cline/qwen/qwen-plus`
- `cline/qwen/qwen3-14b`
- `cline/qwen/qwen3-235b-a22b-2507`
- `cline/qwen/qwen3-235b-a22b-thinking-2507`
- `cline/qwen/qwen3-30b-a3b`
- `cline/qwen/qwen3-30b-a3b-instruct-2507`
- `cline/qwen/qwen3-32b`
- `cline/qwen/qwen3-coder`
- `cline/qwen/qwen3-coder-30b-a3b-instruct`
- `cline/qwen/qwen3-coder-flash`
- `cline/qwen/qwen3-next-80b-a3b-instruct`
- `cline/qwen/qwen3-next-80b-a3b-thinking`
- `xkiro/qwen/qwen3-omni-flash:free`
- `auto/best-coding`

### `combo/steady-coding` (3 legs)

- `groq/openai/gpt-oss-120b`
- `gemini/gemini-3.8-flash`
- `auto/best-coding`

### `combo/trae-best` (3 legs)

- `trae/gpt-5.4`
- `trae/gpt-5.2`
- `auto/best-coding`

### `combo/xkiro-best` (36 legs)

- `xkiro/qwen/qwen3-coder-plus:free`
- `groq/qwen/qwen3.8-27b`
- `xkiro/mistralai/codestral-2508`
- `openrouter/cohere/north-mini-code:free`
- `xkiro/mistralai/devstral-medium`
- `groq/openai/gpt-oss-20b`
- `xkiro/qwen/qwen3-max:free`
- `kilocode/cohere/north-mini-code:free`
- `xkiro/qwen/qwen3.8-max:free`
- `groq/openai/gpt-oss-120b`
- `xkiro/qwen/qwen3.7-max:free`
- `openrouter/poolside/laguna-s-2.1:free`
- `xkiro/qwen/qwen3.6-max-preview:free`
- `kilocode/poolside/laguna-s-2.1:free`
- `xkiro/qwen/qwen3.5-plus:free`
- `openrouter/poolside/laguna-xs-2.1:free`
- `xkiro/qwen/qwen3.7-plus:free`
- `kilocode/poolside/laguna-xs-2.1:free`
- `xkiro/qwen/qwen3.6-27b:free`
- `gemini/gemini-3.8-flash`
- `xkiro/qwen/qwen-plus-2025-07-28:free`
- `gemini/gemini-3.7-flash`
- `xkiro/mistralai/mistral-large-2512`
- `openrouter/nvidia/nemotron-3-super-120b-a12b:free`
- `xkiro/mistralai/mistral-medium-3.5`
- `kilocode/nvidia/nemotron-3-super-120b-a12b:free`
- `xkiro/mistralai/mistral-small-2603`
- `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free`
- `xkiro/mistralai/ministral-14b`
- `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free`
- `xkiro/mistralai/ministral-8b`
- `openrouter/nvidia/nemotron-3.5-lightning:free`
- `xkiro/mistralai/ministral-3b`
- `kilocode/nvidia/nemotron-3.5-lightning:free`
- `xkiro/sensenova/sensenova-6.8-flash-lite`
- `auto/best-coding`

### `combo/xkiro-best-copy` (20 legs)

- `xkiro/sensenova/sensenova-6.8-flash-lite`
- `xkiro/qwen/qwen3.8-max:free`
- `groq/qwen/qwen3.8-27b`
- `xkiro/qwen/qwen3.7-max:free`
- `xkiro/qwen/qwen3.6-max-preview:free`
- `xkiro/qwen/qwen3.5-plus:free`
- `xkiro/mistralai/mistral-medium-3.5`
- `xkiro/qwen/qwen3-max:free`
- `groq/openai/gpt-oss-120b`
- `groq/openai/gpt-oss-20b`
- `xkiro/mistralai/codestral-2508`
- `xkiro/mistralai/mistral-large-2512`
- `xkiro/mistralai/mistral-small-2603`
- `xkiro/qwen/qwen3-coder-plus:free`
- `xkiro/mistralai/devstral-medium`
- `kilocode/cohere/north-mini-code:free`
- `openrouter/cohere/north-mini-code:free`
- `gemini/gemini-3.8-flash`
- `xkiro/mistralai/ministral-8b`
- `auto/best-coding`

_Total routed legs: 786_
