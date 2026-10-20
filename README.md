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

**Full combo probe (today, live):** all 30 combos, 557 unique provider/model legs tested via `test-all` (8 workers, 40 s timeout) - **70 OK**, 455 error, 3 slow, 29 no active connection.

**New-model scan:** 73 catalogue models not yet in any combo were tested (free/latest models across claude, gpt, grok, gemini, qwen, kimi, glm, deepseek, llama, mistral, nvidia) - **13 OK** and added to their brand combos.

**Combos updated:** 80 working legs added across `gemini-best` (+4), `gemma-best` (+1), `qwen-best` (+12), `kimi-best` (+1), `glm-best` (+3), `deepseek-best` (+7), `llama-best` (+4), `mistral-best` (+3) and `all-best` (+45). Every combo was then re-sorted: OK legs first, untested next, failed legs last (auto fallback stays at the end).

**Working legs per combo (OK / testable):**

| Combo | OK / testable |
|---|---|
| `combo/all-best` | 82 / 185 |
| `combo/apinex-best` | 1 / 8 |
| `combo/claude-best` | 0 / 33 |
| `combo/claude-code` | 1 / 2 |
| `combo/claude-fast` | 1 / 2 |
| `combo/claude-max` | 1 / 2 |
| `combo/cleanapis-best` | 3 / 23 |
| `combo/codex-best` | 3 / 4 |
| `combo/deepseek-best` | 7 / 50 |
| `combo/gemini-best` | 13 / 33 |
| `combo/gemma-best` | 2 / 21 |
| `combo/glm-best` | 3 / 41 |
| `combo/gpt-best` | 19 / 126 |
| `combo/grok-best` | 4 / 17 |
| `combo/keep-trying` | 1 / 4 |
| `combo/kilocode-best` | 0 / 6 |
| `combo/kimi-best` | 1 / 18 |
| `combo/kiro-best` | 0 / 7 |
| `combo/literouter-best` | 1 / 7 |
| `combo/llama-best` | 4 / 23 |
| `combo/mistral-best` | 14 / 52 |
| `combo/nara-best` | 1 / 2 |
| `combo/nvidia-best` | 2 / 30 |
| `combo/ollama-best` | 2 / 2 |
| `combo/openrouter-best` | 0 / 9 |
| `combo/qwen-best` | 13 / 54 |
| `combo/spark-best` | 0 / 5 |
| `combo/steady-coding` | 1 / 2 |
| `combo/trae-best` | 0 / 2 |
| `combo/xkiro-best` | 18 / 18 |

Durable failures (401/402/404) are auto-disabled; transient ones (429/5xx/timeout) recover.

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

_Updated 2026-10-20. **OK** = verified today (live 200 or passing `test-all`); **FAIL ...** = latest `test-all` result; **untested** = no result today. Legs are in priority order: OK first, untested next, failed last; `auto/*` fallback stays at the end._

| Combo | Legs | OK / testable |
|---|---|---|
| [`combo/all-best`](#comboall-best) | 187 | 82 / 185 |
| [`combo/apinex-best`](#comboapinex-best) | 9 | 1 / 8 |
| [`combo/claude-best`](#comboclaude-best) | 34 | 0 / 33 |
| [`combo/claude-code`](#comboclaude-code) | 4 | 1 / 2 |
| [`combo/claude-fast`](#comboclaude-fast) | 4 | 1 / 2 |
| [`combo/claude-max`](#comboclaude-max) | 5 | 1 / 2 |
| [`combo/cleanapis-best`](#combocleanapis-best) | 24 | 3 / 23 |
| [`combo/codex-best`](#combocodex-best) | 5 | 3 / 4 |
| [`combo/deepseek-best`](#combodeepseek-best) | 51 | 7 / 50 |
| [`combo/gemini-best`](#combogemini-best) | 34 | 13 / 33 |
| [`combo/gemma-best`](#combogemma-best) | 22 | 2 / 21 |
| [`combo/glm-best`](#comboglm-best) | 42 | 3 / 41 |
| [`combo/gpt-best`](#combogpt-best) | 127 | 19 / 126 |
| [`combo/grok-best`](#combogrok-best) | 18 | 4 / 17 |
| [`combo/keep-trying`](#combokeep-trying) | 5 | 1 / 4 |
| [`combo/kilocode-best`](#combokilocode-best) | 7 | 0 / 6 |
| [`combo/kimi-best`](#combokimi-best) | 19 | 1 / 18 |
| [`combo/kiro-best`](#combokiro-best) | 8 | 0 / 7 |
| [`combo/literouter-best`](#comboliterouter-best) | 7 | 1 / 7 |
| [`combo/llama-best`](#combollama-best) | 24 | 4 / 23 |
| [`combo/mistral-best`](#combomistral-best) | 53 | 14 / 52 |
| [`combo/nara-best`](#combonara-best) | 3 | 1 / 2 |
| [`combo/nvidia-best`](#combonvidia-best) | 31 | 2 / 30 |
| [`combo/ollama-best`](#comboollama-best) | 3 | 2 / 2 |
| [`combo/openrouter-best`](#comboopenrouter-best) | 10 | 0 / 9 |
| [`combo/qwen-best`](#comboqwen-best) | 55 | 13 / 54 |
| [`combo/spark-best`](#combospark-best) | 6 | 0 / 5 |
| [`combo/steady-coding`](#combosteady-coding) | 3 | 1 / 2 |
| [`combo/trae-best`](#combotrae-best) | 3 | 0 / 2 |
| [`combo/xkiro-best`](#comboxkiro-best) | 18 | 18 / 18 |

<a id="comboall-best"></a>
### combo/all-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 82 / 185 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `mistral/ministral-3b-latest` | OK |
| 2 | `mistral/mistral-code-latest` | OK |
| 3 | `xkiro/mistralai/ministral-3b` | OK |
| 4 | `mistral/ministral-8b-latest` | OK |
| 5 | `xkiro/mistralai/ministral-14b` | OK |
| 6 | `codex/gpt-5.6-luna-high` | OK |
| 7 | `codex/gpt-6-luna-low` | OK |
| 8 | `codex/gpt-5.6-terra-low` | OK |
| ... | _179 more legs_ | |

<a id="comboapinex-best"></a>
### combo/apinex-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 8 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `openai/free/gpt-6-luna` | FAIL error |
| 3 | `openai/free/glm-5.3-flash` | FAIL error |
| 4 | `openai/free/deepseek-v4.1-flash` | FAIL error |
| 5 | `openai/free/qwen-3.8-max` | FAIL error |
| 6 | `openai/free/mimo-v2.6-pro` | FAIL error |
| 7 | `openai/free/deepseek-v4-pro-0813` | FAIL error |
| 8 | `openai/free/deepseek-v4-flash-0731` | FAIL error |
| ... | _1 more legs_ | |

<a id="comboclaude-best"></a>
### combo/claude-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 0 / 33 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `openai/claude-opus-5.5` | FAIL error |
| 2 | `openai/claude-sonnet-5` | FAIL error |
| 3 | `claude-web/claude-opus-5-low` | FAIL error |
| 4 | `cline/anthropic/claude-opus-4.8-low` | FAIL error |
| 5 | `claude-web/claude-opus-5-high` | FAIL error |
| 6 | `claude-web/claude-opus-5-xhigh` | FAIL error |
| 7 | `claude-web/claude-opus-5-medium` | FAIL error |
| 8 | `antigravity/claude-opus-4-6-thinking` | FAIL error |
| ... | _26 more legs_ | |

<a id="comboclaude-code"></a>
### combo/claude-code - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 2 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `gemini/gemini-3.8-flash` | FAIL error |
| 3 | `auto/claude-sonnet` | untested |
| 4 | `auto/best-coding` | untested |

<a id="comboclaude-fast"></a>
### combo/claude-fast - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 2 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `gemini/gemini-3.8-flash` | FAIL error |
| 3 | `auto/best-fast` | untested |
| 4 | `auto/best-coding` | untested |

<a id="comboclaude-max"></a>
### combo/claude-max - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 2 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `gemini/gemini-3.8-flash` | FAIL error |
| 3 | `auto/claude-opus` | untested |
| 4 | `auto/claude-sonnet` | untested |
| 5 | `auto/best-coding` | untested |

<a id="combocleanapis-best"></a>
### combo/cleanapis-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 3 / 23 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `groq/qwen/qwen3.8-27b` | OK |
| 3 | `groq/openai/gpt-oss-20b` | OK |
| 4 | `openrouter/cohere/north-mini-code:free` | FAIL error |
| 5 | `kilocode/cohere/north-mini-code:free` | FAIL error |
| 6 | `openai/free/qwen-3.8-max` | FAIL error |
| 7 | `openai/free/deepseek-v4.1-flash` | FAIL error |
| 8 | `openrouter/poolside/laguna-s-2.1:free` | FAIL error |
| ... | _16 more legs_ | |

<a id="combocodex-best"></a>
### combo/codex-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 3 / 4 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `codex/gpt-6-luna` | OK |
| 2 | `codex/gpt-5.6-luna` | OK |
| 3 | `codex/gpt-5.6-terra` | OK |
| 4 | `codex/gpt-5.5` | FAIL error |
| 5 | `auto/best-coding` | untested |

<a id="combodeepseek-best"></a>
### combo/deepseek-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 7 / 50 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `literouter/deepseek-v3.1` | OK |
| 2 | `literouter/deepseek-v4-flash-stable:free` | OK |
| 3 | `literouter/deepseek-v3.2` | OK |
| 4 | `literouter/deepseek-v3.1:free` | OK |
| 5 | `literouter/deepseek-v4-pro-cheap:free` | OK |
| 6 | `literouter/deepseek-v4-pro-cheap` | OK |
| 7 | `literouter/deepseek-v4.1-flash-1017:free` | OK |
| 8 | `xkiro/deepseek/deepseek-v3.2` | FAIL error |
| ... | _43 more legs_ | |

<a id="combogemini-best"></a>
### combo/gemini-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 13 / 33 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `agy/gemini-3.8-flash-tiered` | OK |
| 2 | `agy/gemini-3.8-flash-medium` | OK |
| 3 | `antigravity/gemini-3.8-flash-tiered` | OK |
| 4 | `agy/gemini-3.8-flash-high` | OK |
| 5 | `agy/gemini-3.8-flash-low` | OK |
| 6 | `agy/gemini-3.5-flash-lite` | OK |
| 7 | `antigravity/gemini-3.5-flash-lite` | OK |
| 8 | `agy/gemini-3.1-flash-lite` | OK |
| ... | _26 more legs_ | |

<a id="combogemma-best"></a>
### combo/gemma-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 2 / 21 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `ollama-cloud/gemma4:31b` | OK |
| 2 | `cline/google/gemma-4-31b-it:free` | OK |
| 3 | `cline/google/gemma-4-26b-a4b-it:free` | FAIL error |
| 4 | `openrouter/google/gemma-4-26b-a4b-it:free` | FAIL error |
| 5 | `openrouter/google/gemma-4-31b-it:free` | FAIL error |
| 6 | `cline/google/gemma-4-26b-a4b-it` | FAIL error |
| 7 | `cline/google/gemma-4-31b-it` | FAIL error |
| 8 | `nvidia/google/gemma-4-31b-it` | FAIL error |
| ... | _14 more legs_ | |

<a id="comboglm-best"></a>
### combo/glm-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 3 / 41 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `literouter/glm-5.2` | OK |
| 2 | `literouter/glm-5.3-flash-cheap:free` | OK |
| 3 | `literouter/glm-4.5-air:free` | OK |
| 4 | `cline/z-ai/glm-5.3` | FAIL error |
| 5 | `cline/z-ai/glm-5.3-flash` | FAIL error |
| 6 | `cline/z-ai/glm-5.3-flash:batch` | FAIL error |
| 7 | `cline/z-ai/glm-5.3-flashx` | FAIL error |
| 8 | `cline/z-ai/glm-5.3-prime` | FAIL error |
| ... | _34 more legs_ | |

<a id="combogpt-best"></a>
### combo/gpt-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 19 / 126 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `groq/openai/gpt-oss-20b` | OK |
| 3 | `codex/gpt-6-luna` | OK |
| 4 | `codex/gpt-5.6-luna` | OK |
| 5 | `codex/gpt-5.6-terra` | OK |
| 6 | `codex/gpt-6-luna-max` | OK |
| 7 | `codex/gpt-6-luna-high` | OK |
| 8 | `codex/gpt-6-luna-xhigh` | OK |
| ... | _119 more legs_ | |

<a id="combogrok-best"></a>
### combo/grok-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 4 / 17 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `grok-cli/grok-4.7-high` | OK |
| 2 | `grok-cli/grok-4.7-low` | OK |
| 3 | `grok-cli/grok-4.7-xhigh` | OK |
| 4 | `grok-cli/grok-4.7` | OK |
| 5 | `grok-cli/grok-4.7-medium` | FAIL error |
| 6 | `cline/x-ai/grok-4.5` | FAIL error |
| 7 | `grok-web/fast` | FAIL error |
| 8 | `cline/x-ai/grok-4.20` | FAIL error |
| ... | _10 more legs_ | |

<a id="combokeep-trying"></a>
### combo/keep-trying - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 4 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | FAIL error |
| 3 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 4 | `gemini/gemini-3.8-flash` | FAIL error |
| 5 | `auto/best-coding` | untested |

<a id="combokilocode-best"></a>
### combo/kilocode-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 0 / 6 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `kilocode/nvidia/nemotron-3.5-lightning:free` | FAIL error |
| 2 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | FAIL error |
| 3 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 4 | `kilocode/poolside/laguna-s-2.1:free` | FAIL error |
| 5 | `kilocode/poolside/laguna-xs-2.1:free` | FAIL error |
| 6 | `kilocode/cohere/north-mini-code:free` | FAIL error |
| 7 | `auto/best-coding` | untested |

<a id="combokimi-best"></a>
### combo/kimi-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 18 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `literouter/kimi-k2.8` | OK |
| 2 | `openai/kimi-k3` | FAIL error |
| 3 | `cline/moonshotai/kimi-k3` | FAIL error |
| 4 | `cline/moonshotai/kimi-k2.7-code` | FAIL error |
| 5 | `cline/moonshotai/kimi-k2.6` | FAIL error |
| 6 | `nvidia/moonshotai/kimi-k2.6` | FAIL error |
| 7 | `ollama-cloud/kimi-k2.6` | FAIL error |
| 8 | `cline/moonshotai/kimi-k2.5` | FAIL error |
| ... | _11 more legs_ | |

<a id="combokiro-best"></a>
### combo/kiro-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 0 / 7 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `kiro/glm-5` | FAIL error |
| 2 | `kiro/qwen3-coder-next` | FAIL error |
| 3 | `kiro/claude-sonnet-4.5` | FAIL error |
| 4 | `kiro/claude-haiku-4.5` | FAIL error |
| 5 | `kiro/deepseek-3.2` | FAIL error |
| 6 | `kiro/minimax-m2.5` | FAIL error |
| 7 | `kiro/minimax-m2.1` | FAIL error |
| 8 | `auto/best-coding` | untested |

<a id="comboliterouter-best"></a>
### combo/literouter-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 7 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `literouter/llama-3.3-70b-instruct-turbo:free` | OK |
| 2 | `literouter/glm-5.3-flash:free` | FAIL error |
| 3 | `literouter/deepseek-v3.2:free` | FAIL error |
| 4 | `literouter/kimi-k2.7-code-cheap:free` | FAIL error |
| 5 | `literouter/glm-5:free` | FAIL error |
| 6 | `literouter/gpt-oss-120b:free` | FAIL error |
| 7 | `literouter/qwen3-coder-next:free` | FAIL error |

<a id="combollama-best"></a>
### combo/llama-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 4 / 23 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `cline/nvidia/nemotron-3-ultra-550b-a55b:free` | OK |
| 2 | `ollama-cloud/nemotron-3-super` | OK |
| 3 | `literouter/llama-3.3-70b-instruct-turbo:free` | OK |
| 4 | `ollama-cloud/gemma4:31b` | OK |
| 5 | `cline/meta-llama/llama-4-maverick` | FAIL error |
| 6 | `cline/meta-llama/llama-4-scout` | FAIL error |
| 7 | `cline/meta-llama/llama-3.3-70b-instruct` | FAIL error |
| 8 | `cline/meta-llama/llama-3.2-1b-instruct` | FAIL error |
| ... | _16 more legs_ | |

<a id="combomistral-best"></a>
### combo/mistral-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 14 / 52 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `mistral/ministral-3b-latest` | OK |
| 2 | `mistral/mistral-code-latest` | OK |
| 3 | `mistral/ministral-8b-latest` | OK |
| 4 | `xkiro/mistralai/mistral-medium-3.5` | OK |
| 5 | `xkiro/mistralai/codestral-2508` | OK |
| 6 | `xkiro/mistralai/mistral-large-2512` | OK |
| 7 | `xkiro/mistralai/mistral-small-2603` | OK |
| 8 | `xkiro/mistralai/devstral-medium` | OK |
| ... | _45 more legs_ | |

<a id="combonara-best"></a>
### combo/nara-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 2 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `nara/laguna-s-2.1` | OK |
| 2 | `nara/nemotron-3.5-lightning-free` | FAIL error |
| 3 | `auto/best-coding` | untested |

<a id="combonvidia-best"></a>
### combo/nvidia-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 2 / 30 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `cline/nvidia/nemotron-3-ultra-550b-a55b:free` | OK |
| 2 | `ollama-cloud/nemotron-3-super` | OK |
| 3 | `nvidia/nvidia/nemotron-4-340b-reward` | FAIL timeout |
| 4 | `nvidia/nvidia/nemotron-nano-3-30b-a3b` | FAIL timeout |
| 5 | `cline/nvidia/nemotron-3.5-lightning:free` | FAIL error |
| 6 | `kilocode/nvidia/nemotron-3.5-content-safety:free` | FAIL error |
| 7 | `kilocode/nvidia/nemotron-3.5-lightning:free` | FAIL error |
| 8 | `openrouter/nvidia/nemotron-3.5-lightning:free` | FAIL error |
| ... | _23 more legs_ | |

<a id="comboollama-best"></a>
### combo/ollama-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 2 / 2 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `ollama-cloud/nemotron-3-super` | OK |
| 2 | `ollama-cloud/gemma4:31b` | OK |
| 3 | `auto/best-coding` | untested |

<a id="comboopenrouter-best"></a>
### combo/openrouter-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 0 / 9 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `openrouter/nvidia/nemotron-3.5-lightning:free` | FAIL error |
| 2 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | FAIL error |
| 3 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 4 | `openrouter/poolside/laguna-s-2.1:free` | FAIL error |
| 5 | `openrouter/apodex/apodex-1.1-mini:free` | FAIL error |
| 6 | `openrouter/cohere/north-mini-code:free` | FAIL error |
| 7 | `openrouter/google/gemma-4-31b-it:free` | FAIL error |
| 8 | `openrouter/liquid/lfm-2.5-2.6b:free` | FAIL error |
| ... | _2 more legs_ | |

<a id="comboqwen-best"></a>
### combo/qwen-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 13 / 54 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `xkiro/qwen/qwen3.6-max-preview:free` | OK |
| 2 | `xkiro/qwen/qwen3.8-max:free` | OK |
| 3 | `literouter/qwen3-coder:free` | OK |
| 4 | `xkiro/qwen/qwen3.5-plus:free` | OK |
| 5 | `literouter/qwen3-32b:free` | OK |
| 6 | `xkiro/qwen/qwen3.7-max:free` | OK |
| 7 | `xkiro/qwen/qwen3.7-plus:free` | OK |
| 8 | `xkiro/qwen/qwen3.6-27b:free` | OK |
| ... | _47 more legs_ | |

<a id="combospark-best"></a>
### combo/spark-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 0 / 5 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `cline/meta/muse-spark-1.3` | FAIL error |
| 2 | `cline/meta/muse-spark-1.2` | FAIL error |
| 3 | `cline/meta/muse-spark-1.1` | FAIL error |
| 4 | `cline/meta/muse-spark-1.3-contributor` | FAIL error |
| 5 | `cline/meta/muse-spark-1.2-contributor` | FAIL error |
| 6 | `auto/best-coding` | untested |

<a id="combosteady-coding"></a>
### combo/steady-coding - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 2 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `gemini/gemini-3.8-flash` | FAIL error |
| 3 | `auto/best-coding` | untested |

<a id="combotrae-best"></a>
### combo/trae-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 0 / 2 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `trae/gpt-5.4` | no connection |
| 2 | `trae/gpt-5.2` | no connection |
| 3 | `auto/best-coding` | untested |

<a id="comboxkiro-best"></a>
### combo/xkiro-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 18 / 18 testable

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

