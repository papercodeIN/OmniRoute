# Free AI Coding Setup — OmniRoute + OpenCode (Windows)

> One gateway, ~120 provider connections, 27 auto-fallback combos, $0.
> Generated 2026-10-20. All free tiers verified live on this machine.

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
| exa-search / zenmux-free | connected utility providers (search / free pool) |



## Provider status snapshot (2026-10-20)

**Probe run (today, live):** 592 `test-all` calls across 275 unique models - **0 OK**, 535 error, 31 rate-limited (429), 26 timeout (30 s). The Claude catalogue (800 entries) remains largely unavailable: quota exhaustion on `agy`/`antigravity`, 401 auth on `claude-web`/`cline`, 404/402 elsewhere.

**xkiro combo probe (today):** all **18/18 legs of `xkiro-best` returned `ok`** via `test-all` (latency 0.9-4.9 s, connections rotated across 12 active accounts). Every Qwen, Mistral and SenseNova leg is healthy.

**Connection health (today):** 2,603 `/api/providers/test` calls - 2,416 returned 200. Healthy: `codex` (40), `grok-cli` (44), `grok-web` (48), `xkiro` (47), `kiro` (33), `codestral` (39), `gemini` (20), `agy` (16), `antigravity` (16), `groq` (16), `mistral` (16), `nara` (16), `claude-web` (11). Failing: `cline` (18 x 401), `openai` (3 x 503), `literouter` (2 x 401), `arcee-ai`/`nvidia` (1 x 401 each).

**Verified working combos today:**

| Combo | Working model(s) | Evidence |
|---|---|---|
| `xkiro-best` | all 18 legs | test-all OK |
| `codex-best` | `codex/gpt-6-luna` | 388 live 200s |
| `ollama-best` | `ollama-cloud/nemotron-3-super` | 10 live 200s |
| `grok-best` | `grok-cli/grok-4.7` | 2 live 200s |

All other combos had no successful live request today; their legs are rate-limited, failing, or untested. Durable failures (401/402/404) are auto-disabled; transient ones (429/5xx/timeout) recover.

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

_Updated 2026-10-20. **OK** = verified today (live 200 or passing `test-all`); **FAIL ...** = latest `test-all` result; **untested** = no result today. Legs are shown in current priority order (free / preferred providers first)._

| Combo | Legs | Verified working today |
|---|---|---|
| [`combo/all-best`](#comboall-best) | 143 | `xkiro/qwen/qwen3-coder-plus:free`, `xkiro/qwen/qwen3-max:free`, `xkiro/qwen/qwen3.8-max:free`, `xkiro/qwen/qwen3.7-max:free`, `xkiro/qwen/qwen3.6-max-preview:free`, `xkiro/qwen/qwen3.5-plus:free` (+10 more) |
| [`combo/apinex-best`](#comboapinex-best) | 9 | none |
| [`combo/claude-best`](#comboclaude-best) | 34 | none |
| [`combo/claude-code`](#comboclaude-code) | 4 | none |
| [`combo/claude-fast`](#comboclaude-fast) | 4 | none |
| [`combo/claude-max`](#comboclaude-max) | 5 | none |
| [`combo/cleanapis-best`](#combocleanapis-best) | 24 | none |
| [`combo/codex-best`](#combocodex-best) | 5 | `codex/gpt-6-luna` |
| [`combo/deepseek-best`](#combodeepseek-best) | 44 | none |
| [`combo/gemini-best`](#combogemini-best) | 30 | none |
| [`combo/gemma-best`](#combogemma-best) | 21 | none |
| [`combo/glm-best`](#comboglm-best) | 39 | none |
| [`combo/gpt-best`](#combogpt-best) | 127 | `codex/gpt-6-luna` |
| [`combo/grok-best`](#combogrok-best) | 18 | `grok-cli/grok-4.7` |
| [`combo/keep-trying`](#combokeep-trying) | 5 | none |
| [`combo/kilocode-best`](#combokilocode-best) | 7 | none |
| [`combo/kimi-best`](#combokimi-best) | 18 | none |
| [`combo/kiro-best`](#combokiro-best) | 8 | none |
| [`combo/literouter-best`](#comboliterouter-best) | 7 | none |
| [`combo/llama-best`](#combollama-best) | 21 | none |
| [`combo/mistral-best`](#combomistral-best) | 50 | `xkiro/mistralai/mistral-medium-3.5`, `xkiro/mistralai/codestral-2508`, `xkiro/mistralai/mistral-large-2512`, `xkiro/mistralai/mistral-small-2603`, `xkiro/mistralai/devstral-medium`, `xkiro/mistralai/ministral-14b` (+2 more) |
| [`combo/nara-best`](#combonara-best) | 3 | none |
| [`combo/nvidia-best`](#combonvidia-best) | 33 | `ollama-cloud/nemotron-3-super` |
| [`combo/ollama-best`](#comboollama-best) | 3 | `ollama-cloud/nemotron-3-super` |
| [`combo/openrouter-best`](#comboopenrouter-best) | 10 | none |
| [`combo/qwen-best`](#comboqwen-best) | 43 | none |
| [`combo/spark-best`](#combospark-best) | 6 | none |
| [`combo/steady-coding`](#combosteady-coding) | 3 | none |
| [`combo/trae-best`](#combotrae-best) | 3 | none |
| [`combo/xkiro-best`](#comboxkiro-best) | 18 | all 18 legs OK |

<a id="comboall-best"></a>
### combo/all-best - [back to list](#8-combo-catalog-live)

**Verified working today:** `xkiro/qwen/qwen3-coder-plus:free`, `xkiro/qwen/qwen3-max:free`, `xkiro/qwen/qwen3.8-max:free`, `xkiro/qwen/qwen3.7-max:free`, `xkiro/qwen/qwen3.6-max-preview:free`, `xkiro/qwen/qwen3.5-plus:free`, `xkiro/mistralai/codestral-2508`, `xkiro/mistralai/mistral-small-2603`, `xkiro/mistralai/mistral-large-2512`, `xkiro/sensenova/sensenova-6.8-flash-lite`, `xkiro/mistralai/devstral-medium`, `xkiro/mistralai/mistral-medium-3.5`, `xkiro/mistralai/ministral-8b`, `codex/gpt-6-luna`, `ollama-cloud/nemotron-3-super`, `grok-cli/grok-4.7`

| # | Model | Status |
|---|-------|--------|
| 1 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | untested |
| 2 | `kilocode/nvidia/nemotron-3.5-lightning:free` | untested |
| 3 | `auto/coding:free` | untested |
| 4 | `literouter/glm-5:free` | untested |
| 5 | `xkiro/qwen/qwen3-coder-plus:free` | OK |
| 6 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | untested |
| ... | _137 more legs_ | |

<a id="comboapinex-best"></a>
### combo/apinex-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `openai/free/gpt-6-luna` | untested |
| 2 | `openai/free/glm-5.3-flash` | untested |
| 3 | `openai/free/deepseek-v4.1-flash` | untested |
| 4 | `openai/free/qwen-3.8-max` | untested |
| 5 | `openai/free/mimo-v2.6-pro` | untested |
| 6 | `openai/free/deepseek-v4-pro-0813` | untested |
| ... | _3 more legs_ | |

<a id="comboclaude-best"></a>
### combo/claude-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `openai/claude-opus-5.5` | untested |
| 2 | `openai/claude-sonnet-5` | untested |
| 3 | `claude-web/claude-opus-5-low` | untested |
| 4 | `cline/anthropic/claude-opus-4.8-low` | untested |
| 5 | `claude-web/claude-opus-5-high` | untested |
| 6 | `claude-web/claude-opus-5-xhigh` | untested |
| ... | _28 more legs_ | |

<a id="comboclaude-code"></a>
### combo/claude-code - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | untested |
| 2 | `auto/claude-sonnet` | untested |
| 3 | `gemini/gemini-3.8-flash` | untested |
| 4 | `auto/best-coding` | untested |

<a id="comboclaude-fast"></a>
### combo/claude-fast - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | untested |
| 2 | `gemini/gemini-3.8-flash` | untested |
| 3 | `auto/best-fast` | untested |
| 4 | `auto/best-coding` | untested |

<a id="comboclaude-max"></a>
### combo/claude-max - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | untested |
| 2 | `auto/claude-opus` | untested |
| 3 | `auto/claude-sonnet` | untested |
| 4 | `gemini/gemini-3.8-flash` | untested |
| 5 | `auto/best-coding` | untested |

<a id="combocleanapis-best"></a>
### combo/cleanapis-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `openrouter/cohere/north-mini-code:free` | untested |
| 2 | `kilocode/cohere/north-mini-code:free` | untested |
| 3 | `openai/free/qwen-3.8-max` | untested |
| 4 | `openai/free/deepseek-v4.1-flash` | untested |
| 5 | `openrouter/poolside/laguna-s-2.1:free` | untested |
| 6 | `openai/free/deepseek-v4-flash-0731` | untested |
| ... | _18 more legs_ | |

<a id="combocodex-best"></a>
### combo/codex-best - [back to list](#8-combo-catalog-live)

**Verified working today:** `codex/gpt-6-luna`

| # | Model | Status |
|---|-------|--------|
| 1 | `codex/gpt-6-luna` | OK |
| 2 | `codex/gpt-5.6-luna` | untested |
| 3 | `codex/gpt-5.6-terra` | untested |
| 4 | `codex/gpt-5.5` | untested |
| 5 | `auto/best-coding` | untested |

<a id="combodeepseek-best"></a>
### combo/deepseek-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `xkiro/deepseek/deepseek-v3.2` | untested |
| 2 | `xkiro/deepseek/deepseek-chat-v3.1` | untested |
| 3 | `xkiro/deepseek/deepseek-v4-pro` | untested |
| 4 | `xkiro/deepseek/deepseek-v4-flash` | untested |
| 5 | `openai/deepseek-v4-pro-max` | untested |
| 6 | `deepseek-web/DeepSeek-V3.2` | untested |
| ... | _38 more legs_ | |

<a id="combogemini-best"></a>
### combo/gemini-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `gemini/gemini-3.7-flash` | untested |
| 2 | `agy/gemini-3.8-flash-low` | untested |
| 3 | `cline/google/gemini-3.8-flash` | untested |
| 4 | `gemini/gemini-3.8-flash` | untested |
| 5 | `agy/gemini-3.7-flash-low` | untested |
| 6 | `cline/google/gemini-3.7-flash` | untested |
| ... | _24 more legs_ | |

<a id="combogemma-best"></a>
### combo/gemma-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `cline/google/gemma-4-26b-a4b-it:free` | untested |
| 2 | `cline/google/gemma-4-31b-it:free` | untested |
| 3 | `openrouter/google/gemma-4-26b-a4b-it:free` | untested |
| 4 | `openrouter/google/gemma-4-31b-it:free` | untested |
| 5 | `cfp/google/gemma-4-26b-a4b-it` | untested |
| 6 | `cline/google/gemma-4-26b-a4b-it` | untested |
| ... | _15 more legs_ | |

<a id="comboglm-best"></a>
### combo/glm-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `cfp/zai-org/glm-4.7-flash` | untested |
| 2 | `cfp/zai-org/glm-5.2` | untested |
| 3 | `auto/best-coding` | untested |
| 4 | `cline/z-ai/glm-5.3` | untested |
| 5 | `cline/z-ai/glm-5.3-flash` | untested |
| 6 | `cline/z-ai/glm-5.3-flash:batch` | untested |
| ... | _33 more legs_ | |

<a id="combogpt-best"></a>
### combo/gpt-best - [back to list](#8-combo-catalog-live)

**Verified working today:** `codex/gpt-6-luna`

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | untested |
| 2 | `groq/openai/gpt-oss-20b` | untested |
| 3 | `codex/gpt-6-luna` | OK |
| 4 | `cline/openai/gpt-5.6-sol` | untested |
| 5 | `codex/gpt-5.6-luna` | untested |
| 6 | `codex/gpt-5.6-terra` | untested |
| ... | _121 more legs_ | |

<a id="combogrok-best"></a>
### combo/grok-best - [back to list](#8-combo-catalog-live)

**Verified working today:** `grok-cli/grok-4.7`

| # | Model | Status |
|---|-------|--------|
| 1 | `grok-cli/grok-4.7-high` | untested |
| 2 | `grok-cli/grok-4.7-medium` | untested |
| 3 | `grok-cli/grok-4.7-low` | untested |
| 4 | `cline/x-ai/grok-4.5` | untested |
| 5 | `grok-web/fast` | untested |
| 6 | `cline/x-ai/grok-4.20` | untested |
| ... | _12 more legs_ | |

<a id="combokeep-trying"></a>
### combo/keep-trying - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | untested |
| 2 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | untested |
| 3 | `groq/openai/gpt-oss-120b` | untested |
| 4 | `gemini/gemini-3.8-flash` | untested |
| 5 | `auto/best-coding` | untested |

<a id="combokilocode-best"></a>
### combo/kilocode-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `kilocode/nvidia/nemotron-3.5-lightning:free` | untested |
| 2 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | untested |
| 3 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | untested |
| 4 | `kilocode/poolside/laguna-s-2.1:free` | untested |
| 5 | `kilocode/poolside/laguna-xs-2.1:free` | untested |
| 6 | `kilocode/cohere/north-mini-code:free` | untested |
| ... | _1 more legs_ | |

<a id="combokimi-best"></a>
### combo/kimi-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `openai/kimi-k3` | untested |
| 2 | `cline/moonshotai/kimi-k3` | untested |
| 3 | `aug/kimi-k2.7` | untested |
| 4 | `cfp/moonshotai/kimi-k2.7-code` | untested |
| 5 | `cline/moonshotai/kimi-k2.7-code` | untested |
| 6 | `aug/kimi-k2.6` | untested |
| ... | _12 more legs_ | |

<a id="combokiro-best"></a>
### combo/kiro-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `kiro/glm-5` | untested |
| 2 | `kiro/qwen3-coder-next` | untested |
| 3 | `kiro/claude-sonnet-4.5` | FAIL error |
| 4 | `kiro/claude-haiku-4.5` | FAIL rate-limited |
| 5 | `kiro/deepseek-3.2` | untested |
| 6 | `kiro/minimax-m2.5` | untested |
| ... | _2 more legs_ | |

<a id="comboliterouter-best"></a>
### combo/literouter-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `literouter/glm-5.3-flash:free` | untested |
| 2 | `literouter/llama-3.3-70b-instruct-turbo:free` | untested |
| 3 | `literouter/deepseek-v3.2:free` | untested |
| 4 | `literouter/kimi-k2.7-code-cheap:free` | untested |
| 5 | `literouter/glm-5:free` | untested |
| 6 | `literouter/gpt-oss-120b:free` | untested |
| ... | _1 more legs_ | |

<a id="combollama-best"></a>
### combo/llama-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `ollama-cloud/gemma4:31b` | untested |
| 2 | `cfp/meta/llama-4-scout-17b-16e-instruct` | untested |
| 3 | `cline/meta-llama/llama-4-maverick` | untested |
| 4 | `cline/meta-llama/llama-4-scout` | untested |
| 5 | `cfp/meta-llama/llama-3.3-70b-instruct-fp8-fast` | untested |
| 6 | `cline/meta-llama/llama-3.3-70b-instruct` | untested |
| ... | _15 more legs_ | |

<a id="combomistral-best"></a>
### combo/mistral-best - [back to list](#8-combo-catalog-live)

**Verified working today:** `xkiro/mistralai/mistral-medium-3.5`, `xkiro/mistralai/codestral-2508`, `xkiro/mistralai/mistral-large-2512`, `xkiro/mistralai/mistral-small-2603`, `xkiro/mistralai/devstral-medium`, `xkiro/mistralai/ministral-14b`, `xkiro/mistralai/ministral-3b`, `xkiro/mistralai/ministral-8b`

| # | Model | Status |
|---|-------|--------|
| 1 | `literouter/ministral-3-8b-instruct:free` | untested |
| 2 | `literouter/ministral-3b-2512:free` | untested |
| 3 | `xkiro/mistralai/mistral-medium-3.5` | OK |
| 4 | `xkiro/mistralai/codestral-2508` | OK |
| 5 | `xkiro/mistralai/mistral-large-2512` | OK |
| 6 | `xkiro/mistralai/mistral-small-2603` | OK |
| ... | _44 more legs_ | |

<a id="combonara-best"></a>
### combo/nara-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `nara/nemotron-3.5-lightning-free` | untested |
| 2 | `nara/laguna-s-2.1` | untested |
| 3 | `auto/best-coding` | untested |

<a id="combonvidia-best"></a>
### combo/nvidia-best - [back to list](#8-combo-catalog-live)

**Verified working today:** `ollama-cloud/nemotron-3-super`

| # | Model | Status |
|---|-------|--------|
| 1 | `cline/nvidia/nemotron-3.5-lightning:free` | untested |
| 2 | `kilocode/nvidia/nemotron-3.5-content-safety:free` | untested |
| 3 | `kilocode/nvidia/nemotron-3.5-lightning:free` | untested |
| 4 | `openrouter/nvidia/nemotron-3.5-lightning:free` | untested |
| 5 | `cline/nvidia/nemotron-3-ultra-550b-a55b:free` | untested |
| 6 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | untested |
| ... | _27 more legs_ | |

<a id="comboollama-best"></a>
### combo/ollama-best - [back to list](#8-combo-catalog-live)

**Verified working today:** `ollama-cloud/nemotron-3-super`

| # | Model | Status |
|---|-------|--------|
| 1 | `ollama-cloud/nemotron-3-super` | OK |
| 2 | `ollama-cloud/gemma4:31b` | untested |
| 3 | `auto/best-coding` | untested |

<a id="comboopenrouter-best"></a>
### combo/openrouter-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `openrouter/nvidia/nemotron-3.5-lightning:free` | untested |
| 2 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | untested |
| 3 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | untested |
| 4 | `openrouter/poolside/laguna-s-2.1:free` | untested |
| 5 | `openrouter/apodex/apodex-1.1-mini:free` | untested |
| 6 | `openrouter/cohere/north-mini-code:free` | untested |
| ... | _4 more legs_ | |

<a id="comboqwen-best"></a>
### combo/qwen-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/qwen/qwen3.8-27b` | untested |
| 2 | `cline/qwen/qwen3-coder-next` | untested |
| 3 | `kiro/qwen3-coder-next` | untested |
| 4 | `cline/qwen/qwen3.8-max-0902` | untested |
| 5 | `cline/qwen/qwen3.8-max-prime` | untested |
| 6 | `cline/qwen/qwen3.8-2.4t-a95b` | untested |
| ... | _37 more legs_ | |

<a id="combospark-best"></a>
### combo/spark-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `cline/meta/muse-spark-1.3` | untested |
| 2 | `cline/meta/muse-spark-1.2` | untested |
| 3 | `cline/meta/muse-spark-1.1` | untested |
| 4 | `cline/meta/muse-spark-1.3-contributor` | untested |
| 5 | `cline/meta/muse-spark-1.2-contributor` | untested |
| 6 | `auto/best-coding` | untested |

<a id="combosteady-coding"></a>
### combo/steady-coding - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | untested |
| 2 | `gemini/gemini-3.8-flash` | untested |
| 3 | `auto/best-coding` | untested |

<a id="combotrae-best"></a>
### combo/trae-best - [back to list](#8-combo-catalog-live)

**Verified working today:** none

| # | Model | Status |
|---|-------|--------|
| 1 | `trae/gpt-5.4` | untested |
| 2 | `trae/gpt-5.2` | untested |
| 3 | `auto/best-coding` | untested |

<a id="comboxkiro-best"></a>
### combo/xkiro-best - [back to list](#8-combo-catalog-live)

**Verified working today:** all 18 legs OK

| # | Model | Status |
|---|-------|--------|
| 1 | `xkiro/qwen/qwen3-coder-plus:free` | OK |
| 2 | `xkiro/qwen/qwen3-max:free` | OK |
| 3 | `xkiro/qwen/qwen3.8-max:free` | OK |
| 4 | `xkiro/qwen/qwen3.7-max:free` | OK |
| 5 | `xkiro/qwen/qwen3.6-max-preview:free` | OK |
| 6 | `xkiro/qwen/qwen3.5-plus:free` | OK |
| 7 | `xkiro/qwen/qwen3.7-plus:free` | OK |
| 8 | `xkiro/qwen/qwen3.6-27b:free` | OK |
| 9 | `xkiro/qwen/qwen-plus-2025-07-28:free` | OK |
| 10 | `xkiro/mistralai/codestral-2508` | OK |
| 11 | `xkiro/mistralai/devstral-medium` | OK |
| 12 | `xkiro/mistralai/mistral-large-2512` | OK |
| 13 | `xkiro/mistralai/mistral-medium-3.5` | OK |
| 14 | `xkiro/mistralai/mistral-small-2603` | OK |
| 15 | `xkiro/mistralai/ministral-14b` | OK |
| 16 | `xkiro/mistralai/ministral-8b` | OK |
| 17 | `xkiro/mistralai/ministral-3b` | OK |
| 18 | `xkiro/sensenova/sensenova-6.8-flash-lite` | OK |
