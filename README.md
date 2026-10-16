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


### Also connected (minor/dead/tool providers)

| Provider | Status |
|----------|--------|
| morph | ✅ `morph-v3-fast` tested, in `all-best` |
| kimi-web | ✅ k3/k2d6 (tokens expire — watcher alerts) |
| llm7 | ❌ 402, needs top-up |
| gemini-web | tool bridge, no chat models |
| ollama-search | search tool, no LLMs |
| tinyfish / firecrawl | search tools, no LLMs |
| adobe-firefly | image/video only (own Adobe credits), not in chat combos |
| amazon-q / lmarena / copilot-web | 400s, need login/setup |
| api-airforce / arcee-ai | connected, no usable free models |
| bazaarlink / orcarouter | free pools spent |
| opencode / oc pool | terminal dead (401/402/403) |
| devin / openference / muse-spark-web | connections removed |
| xai-oauth / zed-hosted / zenmux(-free) / clinepass | connected, marginal use |
| qoder / cerebras / siliconflow / together / pollinations | cataloged free tiers, not yet connected |



## Provider status snapshot (2026-10-17)

135 connections, 42 families. Smoke: 17/27 combos answering.
Failing now: glm-best (timeout), trae-best (503 dead conn),
xkiro/literouter/apinex-best (403 throttled), claude-code/max/fast
+ steady-coding (429/403 quota wave). Inactive conns (27): kimi x2,
trae, adobe, lmarena, copilot-web, 3x token-refresh-failed
(agy/antigravity), orcarouter (out of credits), 2x xai-oauth,
grok-web x1, gemini x3, rest user-disabled. Costs: only the known
~$5.84 Antigravity estimate, nothing new.


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

_Smoke-tested 2026-10-17. Status = this run: **OK via X** = answered, **FAIL** = error. Per-model Status from probe history._

| Combo | Legs | Smoke |
|---|---|---|
| [`combo/all-best`](#comboall-best) | 131 | OK via codestral/codestral-latest |
| [`combo/apinex-best`](#comboapinex-best) | 9 | FAIL: HTTP Error 403: Forbidden |
| [`combo/claude-best`](#comboclaude-best) | 34 | OK via antigravity/claude-opus-4-6-thinking |
| [`combo/claude-code`](#comboclaude-code) | 4 | FAIL: HTTP Error 403: Forbidden |
| [`combo/claude-fast`](#comboclaude-fast) | 4 | FAIL: HTTP Error 403: Forbidden |
| [`combo/claude-max`](#comboclaude-max) | 5 | FAIL: HTTP Error 429: Too Many Requests |
| [`combo/cleanapis-best`](#combocleanapis-best) | 24 | ? |
| [`combo/codex-best`](#combocodex-best) | 5 | OK via codex/gpt-6-luna |
| [`combo/deepseek-best`](#combodeepseek-best) | 44 | OK via cloudflare-playground/deepseek-ai/deepseek-v4-pro-0813 |
| [`combo/gemini-best`](#combogemini-best) | 30 | OK via antigravity/gemini-3.8-flash-low |
| [`combo/gemma-best`](#combogemma-best) | 21 | OK via cloudflare-playground/google/gemma-4-26b-a4b-it |
| [`combo/glm-best`](#comboglm-best) | 39 | FAIL: timed out |
| [`combo/gpt-best`](#combogpt-best) | 127 | OK via codex/gpt-6-luna |
| [`combo/grok-best`](#combogrok-best) | 18 | OK via grok-cli/grok-4.7 |
| [`combo/keep-trying`](#combokeep-trying) | 5 | OK via openrouter/nvidia/nemotron-3-super-120b-a12b:free |
| [`combo/kilocode-best`](#combokilocode-best) | 7 | OK via kilocode/nvidia/nemotron-3.5-lightning:free |
| [`combo/kimi-best`](#combokimi-best) | 18 | OK via cloudflare-playground/moonshotai/kimi-k2.7-code |
| [`combo/kiro-best`](#combokiro-best) | 8 | FAIL: HTTP Error 503: Service Unavailable |
| [`combo/literouter-best`](#comboliterouter-best) | 7 | FAIL: HTTP Error 403: Forbidden |
| [`combo/llama-best`](#combollama-best) | 21 | OK via ollama-cloud/gemma4:31b |
| [`combo/mistral-best`](#combomistral-best) | 50 | OK via codestral/codestral-latest |
| [`combo/nara-best`](#combonara-best) | 3 | ? |
| [`combo/nvidia-best`](#combonvidia-best) | 33 | OK via kilocode/nvidia/nemotron-3.5-content-safety:free |
| [`combo/ollama-best`](#comboollama-best) | 3 | OK via ollama-cloud/nemotron-3-super |
| [`combo/openrouter-best`](#comboopenrouter-best) | 10 | OK via openrouter/nvidia/nemotron-3.5-lightning:free |
| [`combo/qwen-best`](#comboqwen-best) | 58 | OK via cloudflare-playground/qwen/qwen2.5-coder-32b-instruct |
| [`combo/steady-coding`](#combosteady-coding) | 3 | FAIL: HTTP Error 403: Forbidden |
| [`combo/trae-best`](#combotrae-best) | 3 | FAIL: HTTP Error 503: Service Unavailable |
| [`combo/xkiro-best`](#comboxkiro-best) | 18 | FAIL: HTTP Error 403: Forbidden |

<a id="combo-all-best"></a>
### combo/all-best · [back to list](#8-combo-catalog-live)

Smoke: OK via codestral/codestral-latest

| # | Model |
|---|-------|
| 1 | `codestral/codestral-latest` |
| 2 | `codestral/codestral-2508` |
| 3 | `antigravity/claude-opus-4-6-thinking-low` |
| 4 | `antigravity/claude-opus-4-6-thinking` |
| 5 | `antigravity/claude-sonnet-4-6-low` |
| 6 | `agy/claude-opus-4-6-thinking-low` |
| 7 | `agy/claude-sonnet-4-6-low` |
| 8 | `claude-web/claude-opus-4-6` |
| 9 | `claude-web/claude-sonnet-4-6-low` |
| 10 | `claude-web/claude-opus-5-low` |
| 11 | `deepseek-web/deepseek-chat` |
| 12 | `gemini/gemini-3.8-flash-lite-tts` |
| 13 | `groq/openai/gpt-oss-120b` |
| 14 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` |
| 15 | `kilocode/nvidia/nemotron-3.5-lightning:free` |
| 16 | `auto/coding:free` |
| 17 | `codex/gpt-6-luna` |
| 18 | `kiro/qwen3-coder-next` |
| 19 | `mistral/codestral-latest` |
| 20 | `literouter/glm-5:free` |
| 21 | `xkiro/qwen/qwen3-coder-plus:free` |
| 22 | `ollama-cloud/nemotron-3-super` |
| 23 | `zai-web/glm-5.3` |
| 24 | `grok-web/fast` |
| 25 | `grok-cli/grok-4.7-low` |
| 26 | `deepseek-web/DeepSeek-V3.2` |
| 27 | `groq/qwen/qwen3.8-27b` |
| 28 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` |
| 29 | `kilocode/poolside/laguna-s-2.1:free` |
| 30 | `codex/gpt-5.6-luna` |
| 31 | `kiro/glm-5` |
| 32 | `literouter/glm-5.3-flash:free` |
| 33 | `xkiro/qwen/qwen3-max:free` |
| 34 | `ollama-cloud/gemma4:31b` |
| 35 | `zai-web/glm-5.3-flash` |
| 36 | `grok-cli/grok-4.7` |
| 37 | `deepseek-web/deepseek-reasoner` |
| 38 | `groq/openai/gpt-oss-20b` |
| 39 | `openrouter/cohere/north-mini-code:free` |
| 40 | `kilocode/poolside/laguna-xs-2.1:free` |
| 41 | `codex/gpt-5.5` |
| 42 | `kiro/deepseek-3.2` |
| 43 | `literouter/deepseek-v3.2:free` |
| 44 | `xkiro/mistralai/codestral-2508` |
| 45 | `zai-web/glm-5.2` |
| 46 | `grok-cli/grok-4.7-medium` |
| 47 | `deepseek-web/deepseek-v4-flash` |
| 48 | `openrouter/poolside/laguna-s-2.1:free` |
| 49 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` |
| 50 | `codex/gpt-5.6-terra` |
| 51 | `kiro/minimax-m2.1` |
| 52 | `literouter/gpt-oss-120b:free` |
| 53 | `xkiro/mistralai/mistral-small-2603` |
| 54 | `grok-cli/grok-4.7-high` |
| 55 | `deepseek-web/deepseek-v4-pro` |
| 56 | `openrouter/poolside/laguna-xs-2.1:free` |
| 57 | `kilocode/cohere/north-mini-code:free` |
| 58 | `kiro/minimax-m2.5` |
| 59 | `literouter/kimi-k2.7-code-cheap:free` |
| 60 | `xkiro/qwen/qwen3.8-max:free` |
| 61 | `deepseek-web/deepseek-v4-pro-think` |
| 62 | `openrouter/nvidia/nemotron-3.5-lightning:free` |
| 63 | `literouter/qwen3-coder-next:free` |
| 64 | `xkiro/qwen/qwen3.7-max:free` |
| 65 | `deepseek-web/deepseek-v4-pro-search` |
| 66 | `literouter/llama-3.3-70b-instruct-turbo:free` |
| 67 | `xkiro/qwen/qwen3.6-max-preview:free` |
| 68 | `deepseek-web/deepseek-v4-pro-think-search` |
| 69 | `literouter/ministral-3b-2512:free` |
| 70 | `xkiro/mistralai/mistral-large-2512` |
| 71 | `deepseek-web/deepseek-v4-flash-think` |
| 72 | `literouter/ministral-3-8b-instruct:free` |
| 73 | `xkiro/qwen/qwen3.5-plus:free` |
| 74 | `deepseek-web/deepseek-v4-flash-search` |
| 75 | `literouter/deepseek-v3.1` |
| 76 | `xkiro/sensenova/sensenova-6.8-flash-lite` |
| 77 | `deepseek-web/deepseek-v4-flash-think-search` |
| 78 | `literouter/deepseek-v3.1:free` |
| 79 | `xkiro/mistralai/devstral-medium` |
| 80 | `deepseek-web/DeepSeek-R1` |
| 81 | `literouter/deepseek-v3.2` |
| 82 | `xkiro/mistralai/mistral-medium-3.5` |
| 83 | `deepseek-web/DeepSeek-R1-Search` |
| 84 | `literouter/deepseek-v4-flash` |
| 85 | `xkiro/mistralai/ministral-8b` |
| 86 | `deepseek-web/DeepSeek-Search` |
| 87 | `literouter/deepseek-v4-flash-cheap` |
| 88 | `literouter/deepseek-v4-flash-cheap:free` |
| 89 | `literouter/deepseek-v4-flash-stable` |
| 90 | `literouter/deepseek-v4-flash:free` |
| 91 | `literouter/deepseek-v4-pro` |
| 92 | `literouter/deepseek-v4-pro-cheap` |
| 93 | `literouter/deepseek-v4-pro-cheap:free` |
| 94 | `literouter/deepseek-v4.1-flash` |
| 95 | `literouter/deepseek-v4.1-flash-cheap` |
| 96 | `literouter/deepseek-v4.1-flash-cheap:free` |
| 97 | `literouter/deepseek-v4.1-flash-stable` |
| 98 | `literouter/deepseek-v4.1-flash-stable:free` |
| 99 | `literouter/deepseek-v4.1-flash:free` |
| 100 | `literouter/gemini-2.5-flash-lite:free` |
| 101 | `literouter/glm-4.5` |
| 102 | `literouter/glm-4.5-air` |
| 103 | `literouter/glm-4.5-air:free` |
| 104 | `literouter/glm-4.5:free` |
| 105 | `literouter/glm-4.6` |
| 106 | `literouter/glm-4.6:free` |
| 107 | `literouter/glm-4.7` |
| 108 | `literouter/glm-4.7-flash` |
| 109 | `literouter/glm-4.7-flash-heretic` |
| 110 | `literouter/glm-4.7-flash-heretic:free` |
| 111 | `literouter/glm-4.7-flash:free` |
| 112 | `literouter/glm-4.7:free` |
| 113 | `literouter/glm-5` |
| 114 | `literouter/glm-5.1` |
| 115 | `literouter/glm-5.1-cheap:free` |
| 116 | `literouter/glm-5.1:free` |
| 117 | `literouter/glm-5.2` |
| 118 | `literouter/glm-5.2-cheap` |
| 119 | `literouter/glm-5.2-cheap:free` |
| 120 | `literouter/glm-5.2:free` |
| 121 | `literouter/glm-5.3` |
| 122 | `literouter/glm-5.3-cheap` |
| 123 | `literouter/glm-5.3-flash` |
| 124 | `literouter/glm-5.3-flash-cheap` |
| 125 | `literouter/glm-5.3-flash-cheap:free` |
| 126 | `literouter/gpt-5-mini` |
| 127 | `literouter/gpt-5-mini-stable` |
| 128 | `nara/laguna-s-2.1` |
| 129 | `nara/nemotron-3.5-lightning-free` |
| 130 | `morph/morph-v3-fast` |
| 131 | `auto/best-coding` |

<a id="combo-apinex-best"></a>
### combo/apinex-best · [back to list](#8-combo-catalog-live)

Smoke: FAIL: HTTP Error 403: Forbidden

| # | Model |
|---|-------|
| 1 | `groq/openai/gpt-oss-120b` |
| 2 | `openai/free/gpt-6-luna` |
| 3 | `openai/free/glm-5.3-flash` |
| 4 | `openai/free/deepseek-v4.1-flash` |
| 5 | `openai/free/qwen-3.8-max` |
| 6 | `openai/free/mimo-v2.6-pro` |
| 7 | `openai/free/deepseek-v4-pro-0813` |
| 8 | `openai/free/deepseek-v4-flash-0731` |
| 9 | `auto/best-coding` |

<a id="combo-claude-best"></a>
### combo/claude-best · [back to list](#8-combo-catalog-live)

Smoke: OK via antigravity/claude-opus-4-6-thinking

| # | Model |
|---|-------|
| 1 | `openai/claude-opus-5.5` |
| 2 | `openai/claude-sonnet-5` |
| 3 | `claude-web/claude-opus-5-low` |
| 4 | `cline/anthropic/claude-opus-4.8-low` |
| 5 | `claude-web/claude-opus-5-high` |
| 6 | `claude-web/claude-opus-5-xhigh` |
| 7 | `claude-web/claude-opus-5-medium` |
| 8 | `antigravity/claude-opus-4-6-thinking` |
| 9 | `claude-web/claude-opus-4-6` |
| 10 | `agy/claude-opus-4-6-thinking-low` |
| 11 | `antigravity/claude-opus-4-6-thinking-low` |
| 12 | `claude-web/claude-opus-4-6-low` |
| 13 | `claude-web/claude-opus-4-7-low` |
| 14 | `claude-web/claude-opus-4-8-low` |
| 15 | `claude-web/claude-opus-5` |
| 16 | `claude-web/claude-sonnet-5-high` |
| 17 | `claude-web/claude-sonnet-5-xhigh` |
| 18 | `claude-web/claude-sonnet-5-medium` |
| 19 | `claude-web/claude-sonnet-5-low` |
| 20 | `kiro/claude-sonnet-4.5` |
| 21 | `agy/claude-sonnet-4-6` |
| 22 | `antigravity/claude-sonnet-4-6` |
| 23 | `claude-web/claude-sonnet-4-6` |
| 24 | `agy/claude-sonnet-4-6-low` |
| 25 | `antigravity/claude-sonnet-4-6-low` |
| 26 | `claude-web/claude-sonnet-4-6-low` |
| 27 | `claude-web/claude-sonnet-5` |
| 28 | `cline/anthropic/claude-sonnet-5` |
| 29 | `claude-web/claude-fable-5-1-low` |
| 30 | `claude-web/claude-fable-5-low` |
| 31 | `cline/anthropic/claude-fable-5-low` |
| 32 | `kiro/claude-haiku-4.5` |
| 33 | `claude-web/claude-haiku-4-5-20251001-low` |
| 34 | `auto/best-coding` |

<a id="combo-claude-code"></a>
### combo/claude-code · [back to list](#8-combo-catalog-live)

Smoke: FAIL: HTTP Error 403: Forbidden

| # | Model |
|---|-------|
| 1 | `groq/openai/gpt-oss-120b` |
| 2 | `auto/claude-sonnet` |
| 3 | `gemini/gemini-3.8-flash` |
| 4 | `auto/best-coding` |

<a id="combo-claude-fast"></a>
### combo/claude-fast · [back to list](#8-combo-catalog-live)

Smoke: FAIL: HTTP Error 403: Forbidden

| # | Model |
|---|-------|
| 1 | `groq/openai/gpt-oss-120b` |
| 2 | `gemini/gemini-3.8-flash` |
| 3 | `auto/best-fast` |
| 4 | `auto/best-coding` |

<a id="combo-claude-max"></a>
### combo/claude-max · [back to list](#8-combo-catalog-live)

Smoke: FAIL: HTTP Error 429: Too Many Requests

| # | Model |
|---|-------|
| 1 | `auto/claude-opus` |
| 2 | `groq/openai/gpt-oss-120b` |
| 3 | `auto/claude-sonnet` |
| 4 | `gemini/gemini-3.8-flash` |
| 5 | `auto/best-coding` |

<a id="combo-cleanapis-best"></a>
### combo/cleanapis-best · [back to list](#8-combo-catalog-live)

Smoke: not tested

| # | Model |
|---|-------|
| 1 | `openai/claude-sonnet-5` |
| 2 | `groq/openai/gpt-oss-120b` |
| 3 | `openai/claude-opus-5.5` |
| 4 | `gemini/gemini-3.8-flash` |
| 5 | `openai/kimi-k3` |
| 6 | `groq/qwen/qwen3.8-27b` |
| 7 | `openai/glm-5.3` |
| 8 | `openrouter/cohere/north-mini-code:free` |
| 9 | `openai/deepseek-v4-pro-max` |
| 10 | `kilocode/cohere/north-mini-code:free` |
| 11 | `openai/free/qwen-3.8-max` |
| 12 | `groq/openai/gpt-oss-20b` |
| 13 | `openai/free/deepseek-v4.1-flash` |
| 14 | `openrouter/poolside/laguna-s-2.1:free` |
| 15 | `openai/free/deepseek-v4-flash-0731` |
| 16 | `kilocode/poolside/laguna-s-2.1:free` |
| 17 | `openai/free/deepseek-v4-pro-0813` |
| 18 | `gemini/gemini-3.7-flash` |
| 19 | `openai/free/gpt-6-luna` |
| 20 | `openrouter/poolside/laguna-xs-2.1:free` |
| 21 | `openai/free/glm-5.3-flash` |
| 22 | `kilocode/poolside/laguna-xs-2.1:free` |
| 23 | `openai/free/mimo-v2.6-pro` |
| 24 | `auto/best-coding` |

<a id="combo-codex-best"></a>
### combo/codex-best · [back to list](#8-combo-catalog-live)

Smoke: OK via codex/gpt-6-luna

| # | Model |
|---|-------|
| 1 | `codex/gpt-6-luna` |
| 2 | `codex/gpt-5.6-luna` |
| 3 | `codex/gpt-5.6-terra` |
| 4 | `codex/gpt-5.5` |
| 5 | `auto/best-coding` |

<a id="combo-deepseek-best"></a>
### combo/deepseek-best · [back to list](#8-combo-catalog-live)

Smoke: OK via cloudflare-playground/deepseek-ai/deepseek-v4-pro-0813

| # | Model |
|---|-------|
| 1 | `openai/deepseek-v4-pro-max` |
| 2 | `deepseek-web/DeepSeek-V3.2` |
| 3 | `deepseek-web/deepseek-v4-pro` |
| 4 | `deepseek-web/deepseek-v4-pro-search` |
| 5 | `deepseek-web/deepseek-v4-pro-think` |
| 6 | `deepseek-web/deepseek-v4-pro-think-search` |
| 7 | `deepseek-web/DeepSeek-R1` |
| 8 | `deepseek-web/DeepSeek-R1-Search` |
| 9 | `deepseek-web/DeepSeek-Search` |
| 10 | `deepseek-web/deepseek-chat` |
| 11 | `deepseek-web/deepseek-reasoner` |
| 12 | `deepseek-web/deepseek-v4-flash` |
| 13 | `deepseek-web/deepseek-v4-flash-search` |
| 14 | `deepseek-web/deepseek-v4-flash-think` |
| 15 | `deepseek-web/deepseek-v4-flash-think-search` |
| 16 | `nvidia/deepseek-ai/deepseek-coder-6.7b-instruct` |
| 17 | `cline/deepseek/deepseek-v4.1-flash` |
| 18 | `cline/deepseek/deepseek-v4.1-flash:batch` |
| 19 | `nvidia/deepseek-ai/deepseek-v4.1-flash` |
| 20 | `cline/deepseek/deepseek-v3.2` |
| 21 | `cline/deepseek/deepseek-v3.2-exp` |
| 22 | `kiro/deepseek-3.2` |
| 23 | `xkiro/deepseek/deepseek-v3.2` |
| 24 | `cline/deepseek/deepseek-chat-v3.1` |
| 25 | `cline/deepseek/deepseek-v3.1-terminus` |
| 26 | `xkiro/deepseek/deepseek-chat-v3.1` |
| 27 | `cfp/deepseek-ai/deepseek-v4-pro-0813` |
| 28 | `cline/deepseek/deepseek-v4-pro` |
| 29 | `cline/deepseek/deepseek-v4-pro-0813` |
| 30 | `cline/~deepseek/deepseek-pro-latest` |
| 31 | `xkiro/deepseek/deepseek-v4-pro` |
| 32 | `cfp/deepseek-ai/deepseek-r1-distill-qwen-32b` |
| 33 | `cfp/deepseek-ai/deepseek-v4-flash-0731` |
| 34 | `cline/deepseek/deepseek-chat` |
| 35 | `cline/deepseek/deepseek-chat-v3-0324` |
| 36 | `cline/deepseek/deepseek-r1` |
| 37 | `cline/deepseek/deepseek-r1-0528` |
| 38 | `cline/deepseek/deepseek-v4-flash` |
| 39 | `cline/deepseek/deepseek-v4-flash-0731` |
| 40 | `cline/deepseek/deepseek-v4-flash-vision-exp` |
| 41 | `cline/~deepseek/deepseek-flash-latest` |
| 42 | `cline/~deepseek/deepseek-v4-flash-latest` |
| 43 | `xkiro/deepseek/deepseek-v4-flash` |
| 44 | `auto/best-coding` |

<a id="combo-gemini-best"></a>
### combo/gemini-best · [back to list](#8-combo-catalog-live)

Smoke: OK via antigravity/gemini-3.8-flash-low

| # | Model |
|---|-------|
| 1 | `gemini/gemini-3.7-flash` |
| 2 | `agy/gemini-3.8-flash-low` |
| 3 | `cline/google/gemini-3.8-flash` |
| 4 | `gemini/gemini-3.8-flash` |
| 5 | `agy/gemini-3.7-flash-low` |
| 6 | `cline/google/gemini-3.7-flash` |
| 7 | `agy/gemini-3.6-flash-low` |
| 8 | `cline/google/gemini-3.6-flash` |
| 9 | `agy/gemini-3.5-flash-lite` |
| 10 | `antigravity/gemini-3.5-flash-lite` |
| 11 | `cline/google/gemini-3.5-flash` |
| 12 | `cline/google/gemini-3.5-flash-lite` |
| 13 | `agy/gemini-3.1-pro-low` |
| 14 | `antigravity/gemini-3.1-pro-low` |
| 15 | `agy/gemini-3.1-flash-lite` |
| 16 | `antigravity/gemini-3.1-flash-lite` |
| 17 | `cline/google/gemini-3.1-flash-lite` |
| 18 | `gemini/gemini-3.1-flash-lite` |
| 19 | `agy/gemini-3-flash` |
| 20 | `antigravity/gemini-3-flash` |
| 21 | `gemini/gemini-3-flash-preview` |
| 22 | `cline/google/gemini-2.5-pro` |
| 23 | `cline/google/gemini-2.5-flash` |
| 24 | `cline/google/gemini-2.5-flash-lite` |
| 25 | `gemini/gemini-2.5-flash-lite` |
| 26 | `agy/gemini-pro-agent` |
| 27 | `antigravity/gemini-pro-agent` |
| 28 | `cline/~google/gemini-pro-latest` |
| 29 | `cline/~google/gemini-flash-latest` |
| 30 | `auto/best-coding` |

<a id="combo-gemma-best"></a>
### combo/gemma-best · [back to list](#8-combo-catalog-live)

Smoke: OK via cloudflare-playground/google/gemma-4-26b-a4b-it

| # | Model |
|---|-------|
| 1 | `cfp/google/gemma-4-26b-a4b-it` |
| 2 | `cline/google/gemma-4-26b-a4b-it` |
| 3 | `cline/google/gemma-4-26b-a4b-it:free` |
| 4 | `cline/google/gemma-4-31b-it` |
| 5 | `cline/google/gemma-4-31b-it:free` |
| 6 | `nvidia/google/gemma-4-31b-it` |
| 7 | `openrouter/google/gemma-4-26b-a4b-it:free` |
| 8 | `openrouter/google/gemma-4-31b-it:free` |
| 9 | `cline/google/gemma-3-12b-it` |
| 10 | `cline/google/gemma-3-27b-it` |
| 11 | `cline/google/gemma-3-4b-it` |
| 12 | `nvidia/google/gemma-3-12b-it` |
| 13 | `nvidia/google/gemma-3-4b-it` |
| 14 | `cline/google/gemma-2-27b-it` |
| 15 | `nvidia/google/codegemma-1.1-7b` |
| 16 | `cfp/aisingapore/gemma-sea-lion-v4-27b-it` |
| 17 | `ddgw/tinfoil/gemma4-31b` |
| 18 | `nvidia/google/codegemma-7b` |
| 19 | `nvidia/google/gemma-2b` |
| 20 | `nvidia/google/recurrentgemma-2b` |
| 21 | `auto/best-coding` |

<a id="combo-glm-best"></a>
### combo/glm-best · [back to list](#8-combo-catalog-live)

Smoke: FAIL: timed out

| # | Model |
|---|-------|
| 1 | `openai/glm-5.3` |
| 2 | `cline/z-ai/glm-5.3` |
| 3 | `zai-web/glm-5.2` |
| 4 | `kiro/glm-5` |
| 5 | `zai-web/glm-5.3-flash-max` |
| 6 | `zai-web/glm-5.3-max` |
| 7 | `zai-web/glm-5.3-flash-high` |
| 8 | `zai-web/glm-5.3-high` |
| 9 | `cline/z-ai/glm-5.3-flash` |
| 10 | `cline/z-ai/glm-5.3-flash:batch` |
| 11 | `cline/z-ai/glm-5.3-flashx` |
| 12 | `cline/z-ai/glm-5.3-prime` |
| 13 | `cline/z-ai/glm-5.3:batch` |
| 14 | `nvidia/z-ai/glm-5.3` |
| 15 | `nvidia/z-ai/glm-5.3-flash` |
| 16 | `zai-web/glm-5.3` |
| 17 | `zai-web/glm-5.3-flash` |
| 18 | `zai-web/glm-5.3-flash-low` |
| 19 | `zai-web/glm-5.3-low` |
| 20 | `zai-web/glm-5.2-max` |
| 21 | `zai-web/glm-5.2-high` |
| 22 | `aug/glm-5.2` |
| 23 | `cfp/zai-org/glm-5.2` |
| 24 | `cline/z-ai/glm-5.2` |
| 25 | `cline/z-ai/glm-5.1` |
| 26 | `cline/z-ai/glm-5-turbo` |
| 27 | `cfp/zai-org/glm-4.7-flash` |
| 28 | `cline/z-ai/glm-4.7` |
| 29 | `cline/z-ai/glm-4.7-flash` |
| 30 | `cline/z-ai/glm-4.6` |
| 31 | `cline/z-ai/glm-4.6v` |
| 32 | `cline/z-ai/glm-4.5` |
| 33 | `cline/z-ai/glm-4.5-air` |
| 34 | `cline/z-ai/glm-4.5v` |
| 35 | `cline/z-ai/glm-5` |
| 36 | `cline/z-ai/glm-5v-turbo` |
| 37 | `cline/~z-ai/glm-flash-latest` |
| 38 | `cline/~z-ai/glm-latest` |
| 39 | `auto/best-coding` |

<a id="combo-gpt-best"></a>
### combo/gpt-best · [back to list](#8-combo-catalog-live)

Smoke: OK via codex/gpt-6-luna

| # | Model |
|---|-------|
| 1 | `codex/gpt-6-luna` |
| 2 | `cline/openai/gpt-5.6-sol` |
| 3 | `codex/gpt-5.6-luna` |
| 4 | `codex/gpt-5.6-terra` |
| 5 | `codex/gpt-5.5` |
| 6 | `cline/openai/gpt-5.4-mini` |
| 7 | `groq/openai/gpt-oss-120b` |
| 8 | `groq/openai/gpt-oss-20b` |
| 9 | `cline/openai/gpt-4o-2024-05-13` |
| 10 | `cline/openai/gpt-4o-2024-08-06` |
| 11 | `cline/openai/gpt-4o-2024-11-20` |
| 12 | `cline/openai/gpt-4o-mini-2024-07-18` |
| 13 | `cline/openai/gpt-6.1-sol-pro` |
| 14 | `cline/openai/gpt-6.1-sol-pro:batch` |
| 15 | `cline/openai/gpt-6.1-sol` |
| 16 | `cline/openai/gpt-6.1-sol:batch` |
| 17 | `codex/gpt-6-astra-max` |
| 18 | `codex/gpt-6-astra-ultra` |
| 19 | `codex/gpt-6-luna-max` |
| 20 | `codex/gpt-6-sol-max` |
| 21 | `codex/gpt-6-sol-ultra` |
| 22 | `cline/openai/gpt-6-astra-pro` |
| 23 | `cline/openai/gpt-6-astra-pro:batch` |
| 24 | `cline/openai/gpt-6-luna-pro` |
| 25 | `cline/openai/gpt-6-luna-pro:batch` |
| 26 | `cline/openai/gpt-6-sol-pro` |
| 27 | `cline/openai/gpt-6-sol-pro:batch` |
| 28 | `codex/gpt-6-astra-high` |
| 29 | `codex/gpt-6-astra-xhigh` |
| 30 | `codex/gpt-6-luna-high` |
| 31 | `codex/gpt-6-luna-xhigh` |
| 32 | `codex/gpt-6-sol-high` |
| 33 | `codex/gpt-6-sol-xhigh` |
| 34 | `cline/openai/gpt-6-astra` |
| 35 | `cline/openai/gpt-6-astra:batch` |
| 36 | `cline/openai/gpt-6-luna` |
| 37 | `cline/openai/gpt-6-luna:batch` |
| 38 | `cline/openai/gpt-6-sol` |
| 39 | `cline/openai/gpt-6-sol:batch` |
| 40 | `codex/gpt-6-astra` |
| 41 | `codex/gpt-6-sol` |
| 42 | `codex/gpt-6-astra-medium` |
| 43 | `codex/gpt-6-luna-medium` |
| 44 | `codex/gpt-6-sol-medium` |
| 45 | `codex/gpt-6-astra-low` |
| 46 | `codex/gpt-6-luna-low` |
| 47 | `codex/gpt-6-sol-low` |
| 48 | `codex/gpt-5.6-luna-max` |
| 49 | `codex/gpt-5.6-sol-max` |
| 50 | `codex/gpt-5.6-sol-ultra` |
| 51 | `codex/gpt-5.6-terra-max` |
| 52 | `codex/gpt-5.6-terra-ultra` |
| 53 | `cline/openai/gpt-5.6-luna-pro` |
| 54 | `cline/openai/gpt-5.6-luna-pro:batch` |
| 55 | `cline/openai/gpt-5.6-sol-pro` |
| 56 | `cline/openai/gpt-5.6-sol-pro:batch` |
| 57 | `cline/openai/gpt-5.6-terra-pro` |
| 58 | `cline/openai/gpt-5.6-terra-pro:batch` |
| 59 | `codex/gpt-5.6-luna-high` |
| 60 | `codex/gpt-5.6-luna-xhigh` |
| 61 | `codex/gpt-5.6-sol-high` |
| 62 | `codex/gpt-5.6-sol-xhigh` |
| 63 | `codex/gpt-5.6-terra-high` |
| 64 | `codex/gpt-5.6-terra-xhigh` |
| 65 | `cline/openai/gpt-5.6-luna` |
| 66 | `cline/openai/gpt-5.6-luna:batch` |
| 67 | `cline/openai/gpt-5.6-sol:batch` |
| 68 | `cline/openai/gpt-5.6-terra` |
| 69 | `cline/openai/gpt-5.6-terra:batch` |
| 70 | `codex/gpt-5.6-sol` |
| 71 | `ddgw/gpt-5.6-luna` |
| 72 | `kiro/gpt-5.6-luna` |
| 73 | `kiro/gpt-5.6-sol` |
| 74 | `kiro/gpt-5.6-terra` |
| 75 | `codex/gpt-5.6-luna-medium` |
| 76 | `codex/gpt-5.6-sol-medium` |
| 77 | `codex/gpt-5.6-terra-medium` |
| 78 | `codex/gpt-5.6-luna-low` |
| 79 | `codex/gpt-5.6-sol-low` |
| 80 | `codex/gpt-5.6-terra-low` |
| 81 | `cline/openai/gpt-5.5-pro` |
| 82 | `cline/openai/gpt-5.5-pro:batch` |
| 83 | `codex/gpt-5.5-high` |
| 84 | `codex/gpt-5.5-xhigh` |
| 85 | `cline/openai/gpt-5.5` |
| 86 | `cline/openai/gpt-5.5:batch` |
| 87 | `codex/gpt-5.5-medium` |
| 88 | `codex/gpt-5.5-low` |
| 89 | `cline/openai/gpt-5.4-pro` |
| 90 | `cline/openai/gpt-5.4-pro:batch` |
| 91 | `cline/openai/gpt-5.4` |
| 92 | `cline/openai/gpt-5.4:batch` |
| 93 | `cline/openai/gpt-5.4-nano` |
| 94 | `cline/openai/gpt-5.4-nano:batch` |
| 95 | `cline/openai/gpt-5.4-mini:batch` |
| 96 | `ddgw/gpt-5.4-mini` |
| 97 | `cline/openai/gpt-5.3-codex` |
| 98 | `cline/openai/gpt-5.2-pro` |
| 99 | `cline/openai/gpt-5.2-pro:batch` |
| 100 | `cline/openai/gpt-5.2` |
| 101 | `cline/openai/gpt-5.2-chat` |
| 102 | `cline/openai/gpt-5.2:batch` |
| 103 | `cline/openai/gpt-5.1` |
| 104 | `cline/openai/gpt-5.1:batch` |
| 105 | `cline/openai/gpt-5-pro` |
| 106 | `cline/openai/gpt-5-pro:batch` |
| 107 | `cline/openai/gpt-5-nano` |
| 108 | `cline/openai/gpt-5-nano:batch` |
| 109 | `cline/openai/gpt-5-mini` |
| 110 | `cline/openai/gpt-5-mini:batch` |
| 111 | `cfp/openai/gpt-oss-120b` |
| 112 | `cfp/openai/gpt-oss-20b` |
| 113 | `cline/openai/gpt-4o` |
| 114 | `cline/openai/gpt-4o:batch` |
| 115 | `cline/openai/gpt-5` |
| 116 | `cline/openai/gpt-5:batch` |
| 117 | `cline/openai/gpt-oss-120b` |
| 118 | `cline/openai/gpt-oss-120b:batch` |
| 119 | `cline/openai/gpt-oss-20b` |
| 120 | `cline/openai/gpt-oss-20b:batch` |
| 121 | `ddgw/tinfoil/gpt-oss-120b` |
| 122 | `nvidia/openai/gpt-oss-20b` |
| 123 | `agy/gpt-oss-120b-medium` |
| 124 | `antigravity/gpt-oss-120b-medium` |
| 125 | `cline/openai/gpt-4o-mini` |
| 126 | `cline/openai/gpt-4o-mini:batch` |
| 127 | `auto/best-coding` |

<a id="combo-grok-best"></a>
### combo/grok-best · [back to list](#8-combo-catalog-live)

Smoke: OK via grok-cli/grok-4.7

| # | Model |
|---|-------|
| 1 | `grok-cli/grok-4.7-high` |
| 2 | `grok-cli/grok-4.7-medium` |
| 3 | `grok-cli/grok-4.7-low` |
| 4 | `cline/x-ai/grok-4.5` |
| 5 | `grok-web/fast` |
| 6 | `cline/x-ai/grok-4.20` |
| 7 | `cline/x-ai/grok-4.20-multi-agent` |
| 8 | `grok-cli/grok-4.7-xhigh` |
| 9 | `cline/x-ai/grok-4.7` |
| 10 | `grok-cli/grok-4.7` |
| 11 | `cline/x-ai/grok-4.6` |
| 12 | `cline/x-ai/grok-4.3` |
| 13 | `cline/x-ai/grok-4.3:batch` |
| 14 | `cline/x-ai/grok-build-0.1` |
| 15 | `cline/~x-ai/grok-latest` |
| 16 | `grok-web/expert` |
| 17 | `grok-web/heavy` |
| 18 | `auto/best-coding` |

<a id="combo-keep-trying"></a>
### combo/keep-trying · [back to list](#8-combo-catalog-live)

Smoke: OK via openrouter/nvidia/nemotron-3-super-120b-a12b:free

| # | Model |
|---|-------|
| 1 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` |
| 2 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` |
| 3 | `groq/openai/gpt-oss-120b` |
| 4 | `gemini/gemini-3.8-flash` |
| 5 | `auto/best-coding` |

<a id="combo-kilocode-best"></a>
### combo/kilocode-best · [back to list](#8-combo-catalog-live)

Smoke: OK via kilocode/nvidia/nemotron-3.5-lightning:free

| # | Model |
|---|-------|
| 1 | `kilocode/nvidia/nemotron-3.5-lightning:free` |
| 2 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` |
| 3 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` |
| 4 | `kilocode/poolside/laguna-s-2.1:free` |
| 5 | `kilocode/poolside/laguna-xs-2.1:free` |
| 6 | `kilocode/cohere/north-mini-code:free` |
| 7 | `auto/best-coding` |

<a id="combo-kimi-best"></a>
### combo/kimi-best · [back to list](#8-combo-catalog-live)

Smoke: OK via cloudflare-playground/moonshotai/kimi-k2.7-code

| # | Model |
|---|-------|
| 1 | `openai/kimi-k3` |
| 2 | `cline/moonshotai/kimi-k3` |
| 3 | `aug/kimi-k2.7` |
| 4 | `cfp/moonshotai/kimi-k2.7-code` |
| 5 | `cline/moonshotai/kimi-k2.7-code` |
| 6 | `aug/kimi-k2.6` |
| 7 | `cfp/moonshotai/kimi-k2.6` |
| 8 | `cline/moonshotai/kimi-k2.6` |
| 9 | `nvidia/moonshotai/kimi-k2.6` |
| 10 | `ollama-cloud/kimi-k2.6` |
| 11 | `cline/moonshotai/kimi-k2.5` |
| 12 | `cline/moonshotai/kimi-k2` |
| 13 | `cline/moonshotai/kimi-k2-0905` |
| 14 | `cline/moonshotai/kimi-k2-thinking` |
| 15 | `cline/moonshotai/kimi-k3:batch` |
| 16 | `cline/~moonshotai/kimi-latest` |
| 17 | `nvidia/moonshotai/kimi-k3` |
| 18 | `auto/best-coding` |

<a id="combo-kiro-best"></a>
### combo/kiro-best · [back to list](#8-combo-catalog-live)

Smoke: FAIL: HTTP Error 503: Service Unavailable

| # | Model |
|---|-------|
| 1 | `kiro/glm-5` |
| 2 | `kiro/qwen3-coder-next` |
| 3 | `kiro/claude-sonnet-4.5` |
| 4 | `kiro/claude-haiku-4.5` |
| 5 | `kiro/deepseek-3.2` |
| 6 | `kiro/minimax-m2.5` |
| 7 | `kiro/minimax-m2.1` |
| 8 | `auto/best-coding` |

<a id="combo-literouter-best"></a>
### combo/literouter-best · [back to list](#8-combo-catalog-live)

Smoke: FAIL: HTTP Error 403: Forbidden

| # | Model |
|---|-------|
| 1 | `literouter/glm-5.3-flash:free` |
| 2 | `literouter/llama-3.3-70b-instruct-turbo:free` |
| 3 | `literouter/deepseek-v3.2:free` |
| 4 | `literouter/kimi-k2.7-code-cheap:free` |
| 5 | `literouter/glm-5:free` |
| 6 | `literouter/gpt-oss-120b:free` |
| 7 | `literouter/qwen3-coder-next:free` |

<a id="combo-llama-best"></a>
### combo/llama-best · [back to list](#8-combo-catalog-live)

Smoke: OK via ollama-cloud/gemma4:31b

| # | Model |
|---|-------|
| 1 | `ollama-cloud/gemma4:31b` |
| 2 | `cfp/meta/llama-4-scout-17b-16e-instruct` |
| 3 | `cline/meta-llama/llama-4-maverick` |
| 4 | `cline/meta-llama/llama-4-scout` |
| 5 | `cfp/meta-llama/llama-3.3-70b-instruct-fp8-fast` |
| 6 | `cline/meta-llama/llama-3.3-70b-instruct` |
| 7 | `cline/meta-llama/llama-3.2-1b-instruct` |
| 8 | `cline/meta-llama/llama-3.2-3b-instruct` |
| 9 | `nvidia/meta/llama-3.2-11b-vision-instruct` |
| 10 | `nvidia/meta/llama-3.2-90b-vision-instruct` |
| 11 | `cfp/meta/llama-3.1-8b-instruct-fp8` |
| 12 | `cline/aion-labs/aion-rp-llama-3.1-8b` |
| 13 | `cline/meta-llama/llama-3.1-70b-instruct` |
| 14 | `cline/meta-llama/llama-3.1-8b-instruct` |
| 15 | `cline/nousresearch/hermes-3-llama-3.1-405b` |
| 16 | `cline/nousresearch/hermes-3-llama-3.1-70b` |
| 17 | `ollama-cloud/minimax-m2.7` |
| 18 | `nvidia/nvidia/llama3-chatqa-1.5-70b` |
| 19 | `nvidia/meta/codellama-70b` |
| 20 | `nvidia/meta/llama2-70b` |
| 21 | `auto/best-coding` |

<a id="combo-mistral-best"></a>
### combo/mistral-best · [back to list](#8-combo-catalog-live)

Smoke: OK via codestral/codestral-latest

| # | Model |
|---|-------|
| 1 | `codestral/codestral-latest` |
| 2 | `codestral/codestral-2508` |
| 3 | `xkiro/mistralai/mistral-medium-3.5` |
| 4 | `xkiro/mistralai/codestral-2508` |
| 5 | `xkiro/mistralai/mistral-large-2512` |
| 6 | `xkiro/mistralai/mistral-small-2603` |
| 7 | `xkiro/mistralai/devstral-medium` |
| 8 | `cline/mistralai/mistral-large-4-0` |
| 9 | `cline/mistralai/mistral-small-3.2-24b-instruct` |
| 10 | `cfp/mistralai/mistral-small-3.1-24b-instruct` |
| 11 | `cline/mistralai/mistral-small-3.1-24b-instruct` |
| 12 | `cline/mistralai/mistral-medium-3.1` |
| 13 | `cline/mistralai/mistral-medium-3.1:batch` |
| 14 | `cline/mistralai/mistral-medium-3-5` |
| 15 | `cline/mistralai/mistral-medium-3-5:batch` |
| 16 | `literouter/ministral-3-8b-instruct:free` |
| 17 | `nvidia/mistralai/mistral-large-2-instruct` |
| 18 | `nvidia/mistralai/mistral-7b-instruct-v0.3` |
| 19 | `nvidia/mistralai/codestral-22b-instruct-v0.1` |
| 20 | `nvidia/mistralai/mixtral-8x22b-v0.1` |
| 21 | `cline/cognitivecomputations/dolphin-mistral-24b-venice-edition` |
| 22 | `cline/mistralai/codestral-2508` |
| 23 | `cline/mistralai/codestral-2508:batch` |
| 24 | `cline/mistralai/devstral-2512` |
| 25 | `cline/mistralai/mistral-large` |
| 26 | `cline/mistralai/mistral-large-2407` |
| 27 | `cline/mistralai/mistral-large-2512` |
| 28 | `cline/mistralai/mistral-large-2512:batch` |
| 29 | `cline/mistralai/mistral-nemo` |
| 30 | `cline/mistralai/mistral-saba` |
| 31 | `cline/mistralai/mistral-small-24b-instruct-2501` |
| 32 | `cline/mistralai/mistral-small-2603` |
| 33 | `cline/mistralai/mistral-small-2603:batch` |
| 34 | `cline/mistralai/mixtral-8x22b-instruct` |
| 35 | `cline/mistralai/voxtral-small-24b-2507` |
| 36 | `ddgw/mistral-small-2603` |
| 37 | `mistral/codestral-latest` |
| 38 | `nvidia/mistralai/mistral-large` |
| 39 | `nvidia/nv-mistralai/mistral-nemo-12b-instruct` |
| 40 | `cline/mistralai/mistral-medium-3` |
| 41 | `cline/mistralai/ministral-14b-2512` |
| 42 | `cline/mistralai/ministral-3b-2512` |
| 43 | `cline/mistralai/ministral-8b-2512` |
| 44 | `cline/mistralai/ministral-8b-2512:batch` |
| 45 | `literouter/ministral-3b-2512:free` |
| 46 | `nvidia/nvidia/mistral-nemo-minitron-8b-8k-instruct` |
| 47 | `xkiro/mistralai/ministral-14b` |
| 48 | `xkiro/mistralai/ministral-3b` |
| 49 | `xkiro/mistralai/ministral-8b` |
| 50 | `auto/best-coding` |

<a id="combo-nara-best"></a>
### combo/nara-best · [back to list](#8-combo-catalog-live)

Smoke: not tested

| # | Model |
|---|-------|
| 1 | `nara/laguna-s-2.1` |
| 2 | `nara/nemotron-3.5-lightning-free` |
| 3 | `auto/best-coding` |

<a id="combo-nvidia-best"></a>
### combo/nvidia-best · [back to list](#8-combo-catalog-live)

Smoke: OK via kilocode/nvidia/nemotron-3.5-content-safety:free

| # | Model |
|---|-------|
| 1 | `cline/nvidia/nemotron-3.5-lightning:free` |
| 2 | `kilocode/nvidia/nemotron-3.5-content-safety:free` |
| 3 | `kilocode/nvidia/nemotron-3.5-lightning:free` |
| 4 | `openrouter/nvidia/nemotron-3.5-lightning:free` |
| 5 | `cline/nvidia/nemotron-3-ultra-550b-a55b:free` |
| 6 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` |
| 7 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` |
| 8 | `ollama-cloud/nemotron-3-super` |
| 9 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` |
| 10 | `nvidia/nvidia/nemotron-4-340b-instruct` |
| 11 | `nvidia/nvidia/nemotron-4-340b-reward` |
| 12 | `cline/nvidia/nemotron-3.5-content-safety` |
| 13 | `cline/nvidia/nemotron-3.5-content-safety:free` |
| 14 | `cline/nvidia/nemotron-3.5-lightning` |
| 15 | `nvidia/nvidia/nemotron-3.5-content-safety` |
| 16 | `nvidia/nvidia/nemotron-3.5-lightning-30b-a3b` |
| 17 | `openrouter/nvidia/nemotron-3.5-content-safety:free` |
| 18 | `nvidia/nvidia/llama-3.1-nemotron-ultra-253b-v1` |
| 19 | `nvidia/nvidia/llama-3.1-nemotron-51b-instruct` |
| 20 | `nvidia/nvidia/llama-3.1-nemotron-70b-instruct` |
| 21 | `cline/nvidia/nemotron-3-ultra-550b-a55b` |
| 22 | `nvidia/nvidia/nemotron-3-ultra-550b-a55b` |
| 23 | `cfp/nvidia/nemotron-3-120b-a12b` |
| 24 | `cline/nvidia/nemotron-3-super-120b-a12b` |
| 25 | `cline/nvidia/nemotron-3-super-120b-a12b:free` |
| 26 | `nvidia/nvidia/nemotron-3-super-120b-a12b` |
| 27 | `cline/nvidia/nemotron-3-nano-30b-a3b` |
| 28 | `cline/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` |
| 29 | `nvidia/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` |
| 30 | `nvidia/nvidia/nemotron-nano-3-30b-a3b` |
| 31 | `nvidia/nvidia/nemotron-parse-2.0` |
| 32 | `nvidia/nvidia/nemotron-parse` |
| 33 | `auto/best-coding` |

<a id="combo-ollama-best"></a>
### combo/ollama-best · [back to list](#8-combo-catalog-live)

Smoke: OK via ollama-cloud/nemotron-3-super

| # | Model |
|---|-------|
| 1 | `ollama-cloud/nemotron-3-super` |
| 2 | `ollama-cloud/gemma4:31b` |
| 3 | `auto/best-coding` |

<a id="combo-openrouter-best"></a>
### combo/openrouter-best · [back to list](#8-combo-catalog-live)

Smoke: OK via openrouter/nvidia/nemotron-3.5-lightning:free

| # | Model |
|---|-------|
| 1 | `openrouter/nvidia/nemotron-3.5-lightning:free` |
| 2 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` |
| 3 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` |
| 4 | `openrouter/poolside/laguna-s-2.1:free` |
| 5 | `openrouter/apodex/apodex-1.1-mini:free` |
| 6 | `openrouter/cohere/north-mini-code:free` |
| 7 | `openrouter/google/gemma-4-31b-it:free` |
| 8 | `openrouter/liquid/lfm-2.5-2.6b:free` |
| 9 | `openrouter/poolside/laguna-xs-2.1:free` |
| 10 | `auto/best-coding` |

<a id="combo-qwen-best"></a>
### combo/qwen-best · [back to list](#8-combo-catalog-live)

Smoke: OK via cloudflare-playground/qwen/qwen2.5-coder-32b-instruct

| # | Model |
|---|-------|
| 1 | `xkiro/qwen/qwen3.8-max:free` |
| 2 | `groq/qwen/qwen3.8-27b` |
| 3 | `xkiro/qwen/qwen3.7-max:free` |
| 4 | `xkiro/qwen/qwen3.5-plus:free` |
| 5 | `xkiro/qwen/qwen3-max:free` |
| 6 | `cline/qwen/qwen3-coder-next` |
| 7 | `kiro/qwen3-coder-next` |
| 8 | `xkiro/qwen/qwen3-coder-plus:free` |
| 9 | `xkiro/qwen/qwen-plus-2025-07-28:free` |
| 10 | `cline/qwen/qwen3.8-max-0902` |
| 11 | `cline/qwen/qwen3.8-max-prime` |
| 12 | `cline/qwen/qwen3.8-2.4t-a95b` |
| 13 | `cline/qwen/qwen3.8-27b` |
| 14 | `cline/qwen/qwen3.8-flash` |
| 15 | `cline/qwen/qwen3.8-omni-flash` |
| 16 | `cline/qwen/qwen3.7-max` |
| 17 | `cline/qwen/qwen3.7-flash` |
| 18 | `cline/qwen/qwen3.7-plus` |
| 19 | `xkiro/qwen/qwen3.7-plus:free` |
| 20 | `cline/qwen/qwen3.6-27b` |
| 21 | `cline/qwen/qwen3.6-35b-a3b` |
| 22 | `cline/qwen/qwen3.6-flash` |
| 23 | `cline/qwen/qwen3.6-plus` |
| 24 | `xkiro/qwen/qwen3.6-27b:free` |
| 25 | `xkiro/qwen/qwen3.6-35b-a3b:free` |
| 26 | `xkiro/qwen/qwen3.6-plus:free` |
| 27 | `cline/qwen/qwen3.5-122b-a10b` |
| 28 | `cline/qwen/qwen3.5-27b` |
| 29 | `cline/qwen/qwen3.5-35b-a3b` |
| 30 | `cline/qwen/qwen3.5-397b-a17b` |
| 31 | `cline/qwen/qwen3.5-9b` |
| 32 | `cline/qwen/qwen3.5-flash-02-23` |
| 33 | `cline/qwen/qwen3.5-plus-02-15` |
| 34 | `cline/qwen/qwen3.5-plus-20260420` |
| 35 | `xkiro/qwen/qwen3.5-397b-a17b:free` |
| 36 | `xkiro/qwen/qwen3.5-flash:free` |
| 37 | `xkiro/qwen/qwen3.5-omni-flash:free` |
| 38 | `xkiro/qwen/qwen3.5-omni-plus:free` |
| 39 | `cfp/qwen/qwen2.5-coder-32b-instruct` |
| 40 | `cline/qwen/qwen-2.5-72b-instruct` |
| 41 | `cline/qwen/qwen-2.5-7b-instruct` |
| 42 | `cline/qwen/qwen-2.5-coder-32b-instruct` |
| 43 | `cfp/qwen/qwen3-30b-a3b-fp8` |
| 44 | `cfp/qwen/qwq-32b` |
| 45 | `cline/qwen/qwen-plus` |
| 46 | `cline/qwen/qwen3-14b` |
| 47 | `cline/qwen/qwen3-235b-a22b-2507` |
| 48 | `cline/qwen/qwen3-235b-a22b-thinking-2507` |
| 49 | `cline/qwen/qwen3-30b-a3b` |
| 50 | `cline/qwen/qwen3-30b-a3b-instruct-2507` |
| 51 | `cline/qwen/qwen3-32b` |
| 52 | `cline/qwen/qwen3-coder` |
| 53 | `cline/qwen/qwen3-coder-30b-a3b-instruct` |
| 54 | `cline/qwen/qwen3-coder-flash` |
| 55 | `cline/qwen/qwen3-next-80b-a3b-instruct` |
| 56 | `cline/qwen/qwen3-next-80b-a3b-thinking` |
| 57 | `xkiro/qwen/qwen3-omni-flash:free` |
| 58 | `auto/best-coding` |

<a id="combo-steady-coding"></a>
### combo/steady-coding · [back to list](#8-combo-catalog-live)

Smoke: FAIL: HTTP Error 403: Forbidden

| # | Model |
|---|-------|
| 1 | `groq/openai/gpt-oss-120b` |
| 2 | `gemini/gemini-3.8-flash` |
| 3 | `auto/best-coding` |

<a id="combo-trae-best"></a>
### combo/trae-best · [back to list](#8-combo-catalog-live)

Smoke: FAIL: HTTP Error 503: Service Unavailable

| # | Model |
|---|-------|
| 1 | `trae/gpt-5.4` |
| 2 | `trae/gpt-5.2` |
| 3 | `auto/best-coding` |

<a id="combo-xkiro-best"></a>
### combo/xkiro-best · [back to list](#8-combo-catalog-live)

Smoke: FAIL: HTTP Error 403: Forbidden

| # | Model |
|---|-------|
| 1 | `xkiro/qwen/qwen3-coder-plus:free` |
| 2 | `xkiro/mistralai/codestral-2508` |
| 3 | `xkiro/mistralai/devstral-medium` |
| 4 | `xkiro/qwen/qwen3-max:free` |
| 5 | `xkiro/qwen/qwen3.8-max:free` |
| 6 | `xkiro/qwen/qwen3.7-max:free` |
| 7 | `xkiro/qwen/qwen3.6-max-preview:free` |
| 8 | `xkiro/qwen/qwen3.5-plus:free` |
| 9 | `xkiro/qwen/qwen3.7-plus:free` |
| 10 | `xkiro/qwen/qwen3.6-27b:free` |
| 11 | `xkiro/qwen/qwen-plus-2025-07-28:free` |
| 12 | `xkiro/mistralai/mistral-large-2512` |
| 13 | `xkiro/mistralai/mistral-medium-3.5` |
| 14 | `xkiro/mistralai/mistral-small-2603` |
| 15 | `xkiro/mistralai/ministral-14b` |
| 16 | `xkiro/mistralai/ministral-8b` |
| 17 | `xkiro/mistralai/ministral-3b` |
| 18 | `xkiro/sensenova/sensenova-6.8-flash-lite` |

_Total routed legs: 742 across 29 combos_
