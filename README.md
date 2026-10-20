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

**xkiro policy:** xkiro models are used **only in `xkiro-best`**. 39 xkiro legs were removed from `all-best` (-18), `qwen-best` (-9), `mistral-best` (-8) and `deepseek-best` (-4).

**Working legs per combo (OK / testable):**

| Combo | OK / testable |
|---|---|
| `combo/all-best` | 64 / 167 |
| `combo/apinex-best` | 1 / 8 |
| `combo/claude-best` | 0 / 33 |
| `combo/claude-code` | 1 / 2 |
| `combo/claude-fast` | 1 / 2 |
| `combo/claude-max` | 1 / 2 |
| `combo/cleanapis-best` | 3 / 23 |
| `combo/codex-best` | 3 / 4 |
| `combo/deepseek-best` | 7 / 46 |
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
| `combo/mistral-best` | 6 / 44 |
| `combo/nara-best` | 1 / 2 |
| `combo/nvidia-best` | 2 / 30 |
| `combo/ollama-best` | 2 / 2 |
| `combo/openrouter-best` | 0 / 9 |
| `combo/qwen-best` | 4 / 45 |
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

_Updated 2026-10-20. **OK** = verified today (live 200 or passing `test-all`); **FAIL ...** = latest `test-all` result; **untested** = no result today. Every leg is listed in priority order: OK first, untested next, failed last; `auto/*` fallback stays at the end. xkiro legs appear only in `xkiro-best`._

| Combo | Legs | OK / testable |
|---|---|---|
| [`combo/all-best`](#comboall-best) | 169 | 64 / 167 |
| [`combo/apinex-best`](#comboapinex-best) | 9 | 1 / 8 |
| [`combo/claude-best`](#comboclaude-best) | 34 | 0 / 33 |
| [`combo/claude-code`](#comboclaude-code) | 4 | 1 / 2 |
| [`combo/claude-fast`](#comboclaude-fast) | 4 | 1 / 2 |
| [`combo/claude-max`](#comboclaude-max) | 5 | 1 / 2 |
| [`combo/cleanapis-best`](#combocleanapis-best) | 24 | 3 / 23 |
| [`combo/codex-best`](#combocodex-best) | 5 | 3 / 4 |
| [`combo/deepseek-best`](#combodeepseek-best) | 47 | 7 / 46 |
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
| [`combo/mistral-best`](#combomistral-best) | 45 | 6 / 44 |
| [`combo/nara-best`](#combonara-best) | 3 | 1 / 2 |
| [`combo/nvidia-best`](#combonvidia-best) | 31 | 2 / 30 |
| [`combo/ollama-best`](#comboollama-best) | 3 | 2 / 2 |
| [`combo/openrouter-best`](#comboopenrouter-best) | 10 | 0 / 9 |
| [`combo/qwen-best`](#comboqwen-best) | 46 | 4 / 45 |
| [`combo/spark-best`](#combospark-best) | 6 | 0 / 5 |
| [`combo/steady-coding`](#combosteady-coding) | 3 | 1 / 2 |
| [`combo/trae-best`](#combotrae-best) | 3 | 0 / 2 |
| [`combo/xkiro-best`](#comboxkiro-best) | 18 | 18 / 18 |

<a id="comboall-best"></a>
### combo/all-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 64 / 167 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `mistral/ministral-3b-latest` | OK |
| 2 | `mistral/mistral-code-latest` | OK |
| 3 | `mistral/ministral-8b-latest` | OK |
| 4 | `codex/gpt-5.6-luna-high` | OK |
| 5 | `codex/gpt-6-luna-low` | OK |
| 6 | `codex/gpt-5.6-terra-low` | OK |
| 7 | `codex/gpt-5.6-luna-medium` | OK |
| 8 | `codex/gpt-5.6-luna-low` | OK |
| 9 | `gemini/gemini-3-flash-preview` | OK |
| 10 | `codex/gpt-5.6-terra-xhigh` | OK |
| 11 | `codex/gpt-5.6-luna-xhigh` | OK |
| 12 | `codex/gpt-6-luna-max` | OK |
| 13 | `cline/google/gemma-4-31b-it:free` | OK |
| 14 | `codex/gpt-5.6-terra-max` | OK |
| 15 | `agy/gemini-3-flash` | OK |
| 16 | `cline/nvidia/nemotron-3-ultra-550b-a55b:free` | OK |
| 17 | `codex/gpt-6-luna-high` | OK |
| 18 | `codex/gpt-6-luna-medium` | OK |
| 19 | `antigravity/gemini-3.1-flash-lite` | OK |
| 20 | `codex/gpt-5.6-luna-max` | OK |
| 21 | `antigravity/gemini-3-flash` | OK |
| 22 | `literouter/qwen3-coder:free` | OK |
| 23 | `agy/gemini-3.8-flash-tiered` | OK |
| 24 | `literouter/qwen3-32b:free` | OK |
| 25 | `agy/gemini-3.8-flash-medium` | OK |
| 26 | `antigravity/gemini-3.5-flash-lite` | OK |
| 27 | `antigravity/gemini-3.8-flash-tiered` | OK |
| 28 | `agy/gemini-3.1-flash-lite` | OK |
| 29 | `literouter/deepseek-v4-flash-stable:free` | OK |
| 30 | `agy/gemini-3.5-flash-lite` | OK |
| 31 | `codex/gpt-6-luna-xhigh` | OK |
| 32 | `grok-cli/grok-4.7-xhigh` | OK |
| 33 | `agy/gemini-3.8-flash-high` | OK |
| 34 | `agy/gemini-3.8-flash-low` | OK |
| 35 | `literouter/qwen3.5-9b:free` | OK |
| 36 | `literouter/deepseek-v4.1-flash-1017:free` | OK |
| 37 | `literouter/kimi-k2.8` | OK |
| 38 | `codex/gpt-5.6-terra-high` | OK |
| 39 | `gemini/gemini-3.1-flash-lite` | OK |
| 40 | `literouter/llama-3.3-70b-instruct-turbo:free` | OK |
| 41 | `literouter/deepseek-v3.1:free` | OK |
| 42 | `literouter/deepseek-v4-pro-cheap:free` | OK |
| 43 | `literouter/glm-4.5-air:free` | OK |
| 44 | `literouter/glm-5.3-flash-cheap:free` | OK |
| 45 | `literouter/deepseek-v3.1` | OK |
| 46 | `literouter/deepseek-v3.2` | OK |
| 47 | `literouter/deepseek-v4-pro-cheap` | OK |
| 48 | `literouter/glm-5.2` | OK |
| 49 | `groq/openai/gpt-oss-120b` | OK |
| 50 | `groq/qwen/qwen3.8-27b` | OK |
| 51 | `groq/openai/gpt-oss-20b` | OK |
| 52 | `codestral/codestral-latest` | OK |
| 53 | `codestral/codestral-2508` | OK |
| 54 | `codex/gpt-6-luna` | OK |
| 55 | `mistral/codestral-latest` | OK |
| 56 | `ollama-cloud/nemotron-3-super` | OK |
| 57 | `grok-cli/grok-4.7-low` | OK |
| 58 | `codex/gpt-5.6-luna` | OK |
| 59 | `ollama-cloud/gemma4:31b` | OK |
| 60 | `grok-cli/grok-4.7` | OK |
| 61 | `codex/gpt-5.6-terra` | OK |
| 62 | `grok-cli/grok-4.7-high` | OK |
| 63 | `nara/laguna-s-2.1` | OK |
| 64 | `morph/morph-v3-fast` | OK |
| 65 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 66 | `kilocode/nvidia/nemotron-3.5-lightning:free` | FAIL error |
| 67 | `literouter/glm-5:free` | FAIL error |
| 68 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | FAIL error |
| 69 | `kilocode/poolside/laguna-s-2.1:free` | FAIL error |
| 70 | `literouter/glm-5.3-flash:free` | FAIL error |
| 71 | `openrouter/cohere/north-mini-code:free` | FAIL error |
| 72 | `kilocode/poolside/laguna-xs-2.1:free` | FAIL error |
| 73 | `literouter/deepseek-v3.2:free` | FAIL error |
| 74 | `openrouter/poolside/laguna-s-2.1:free` | FAIL error |
| 75 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 76 | `literouter/gpt-oss-120b:free` | FAIL error |
| 77 | `openrouter/poolside/laguna-xs-2.1:free` | FAIL error |
| 78 | `kilocode/cohere/north-mini-code:free` | FAIL error |
| 79 | `literouter/kimi-k2.7-code-cheap:free` | FAIL error |
| 80 | `openrouter/nvidia/nemotron-3.5-lightning:free` | FAIL error |
| 81 | `literouter/qwen3-coder-next:free` | FAIL error |
| 82 | `literouter/ministral-3b-2512:free` | FAIL error |
| 83 | `literouter/ministral-3-8b-instruct:free` | FAIL error |
| 84 | `literouter/deepseek-v4-flash-cheap:free` | FAIL error |
| 85 | `literouter/deepseek-v4-flash:free` | FAIL error |
| 86 | `literouter/deepseek-v4.1-flash-cheap:free` | FAIL error |
| 87 | `literouter/deepseek-v4.1-flash-stable:free` | FAIL error |
| 88 | `literouter/deepseek-v4.1-flash:free` | FAIL error |
| 89 | `literouter/gemini-2.5-flash-lite:free` | FAIL error |
| 90 | `literouter/glm-4.5:free` | FAIL error |
| 91 | `literouter/glm-4.6:free` | FAIL error |
| 92 | `literouter/glm-4.7-flash-heretic:free` | FAIL error |
| 93 | `literouter/glm-4.7-flash:free` | FAIL error |
| 94 | `literouter/glm-4.7:free` | FAIL error |
| 95 | `literouter/glm-5.1-cheap:free` | FAIL error |
| 96 | `literouter/glm-5.1:free` | FAIL error |
| 97 | `literouter/glm-5.2-cheap:free` | FAIL error |
| 98 | `literouter/glm-5.2:free` | FAIL error |
| 99 | `nara/nemotron-3.5-lightning-free` | FAIL error |
| 100 | `literouter/deepseek-v4-flash` | FAIL error |
| 101 | `literouter/deepseek-v4-flash-cheap` | FAIL error |
| 102 | `literouter/deepseek-v4-flash-stable` | FAIL error |
| 103 | `literouter/deepseek-v4-pro` | FAIL error |
| 104 | `literouter/deepseek-v4.1-flash` | FAIL error |
| 105 | `literouter/deepseek-v4.1-flash-cheap` | FAIL error |
| 106 | `literouter/deepseek-v4.1-flash-stable` | FAIL error |
| 107 | `literouter/glm-4.5` | FAIL error |
| 108 | `literouter/glm-4.5-air` | FAIL error |
| 109 | `literouter/glm-4.6` | FAIL error |
| 110 | `literouter/glm-4.7` | FAIL error |
| 111 | `literouter/glm-4.7-flash` | FAIL error |
| 112 | `literouter/glm-4.7-flash-heretic` | FAIL error |
| 113 | `literouter/glm-5` | FAIL error |
| 114 | `literouter/glm-5.1` | FAIL error |
| 115 | `literouter/glm-5.2-cheap` | FAIL error |
| 116 | `literouter/glm-5.3` | FAIL error |
| 117 | `literouter/glm-5.3-cheap` | FAIL error |
| 118 | `literouter/glm-5.3-flash` | FAIL error |
| 119 | `literouter/glm-5.3-flash-cheap` | FAIL error |
| 120 | `literouter/gpt-5-mini` | FAIL error |
| 121 | `literouter/gpt-5-mini-stable` | FAIL error |
| 122 | `antigravity/claude-opus-4-6-thinking-low` | FAIL error |
| 123 | `antigravity/claude-opus-4-6-thinking` | FAIL error |
| 124 | `antigravity/claude-sonnet-4-6-low` | FAIL error |
| 125 | `agy/claude-opus-4-6-thinking-low` | FAIL error |
| 126 | `agy/claude-sonnet-4-6-low` | FAIL error |
| 127 | `claude-web/claude-opus-4-6` | FAIL error |
| 128 | `claude-web/claude-sonnet-4-6-low` | FAIL error |
| 129 | `claude-web/claude-opus-5-low` | FAIL error |
| 130 | `deepseek-web/deepseek-chat` | FAIL error |
| 131 | `gemini/gemini-3.8-flash-lite-tts` | FAIL error |
| 132 | `kiro/qwen3-coder-next` | FAIL error |
| 133 | `zai-web/glm-5.3` | FAIL error |
| 134 | `grok-web/fast` | FAIL error |
| 135 | `deepseek-web/DeepSeek-V3.2` | FAIL error |
| 136 | `kiro/glm-5` | FAIL error |
| 137 | `zai-web/glm-5.3-flash` | FAIL error |
| 138 | `deepseek-web/deepseek-reasoner` | FAIL error |
| 139 | `codex/gpt-5.5` | FAIL error |
| 140 | `kiro/deepseek-3.2` | FAIL error |
| 141 | `zai-web/glm-5.2` | FAIL error |
| 142 | `grok-cli/grok-4.7-medium` | FAIL error |
| 143 | `deepseek-web/deepseek-v4-flash` | FAIL error |
| 144 | `kiro/minimax-m2.1` | FAIL error |
| 145 | `deepseek-web/deepseek-v4-pro` | FAIL error |
| 146 | `kiro/minimax-m2.5` | FAIL error |
| 147 | `deepseek-web/deepseek-v4-pro-think` | FAIL error |
| 148 | `deepseek-web/deepseek-v4-pro-search` | FAIL error |
| 149 | `deepseek-web/deepseek-v4-pro-think-search` | FAIL error |
| 150 | `deepseek-web/deepseek-v4-flash-think` | FAIL error |
| 151 | `deepseek-web/deepseek-v4-flash-search` | FAIL error |
| 152 | `deepseek-web/deepseek-v4-flash-think-search` | FAIL error |
| 153 | `deepseek-web/DeepSeek-R1` | FAIL error |
| 154 | `deepseek-web/DeepSeek-R1-Search` | FAIL error |
| 155 | `deepseek-web/DeepSeek-Search` | FAIL error |
| 156 | `cline/meta/muse-spark-1.1` | FAIL error |
| 157 | `cline/meta/muse-spark-1.3-contributor` | FAIL error |
| 158 | `cline/meta/muse-spark-1.2-contributor` | FAIL error |
| 159 | `cline/deepseek/deepseek-r1` | FAIL error |
| 160 | `cline/qwen/qwen3-coder-30b-a3b-instruct` | FAIL error |
| 161 | `cline/google/gemini-3.8-flash` | FAIL error |
| 162 | `cline/meta-llama/llama-3.3-70b-instruct` | FAIL error |
| 163 | `cline/mistralai/codestral-2508` | FAIL error |
| 164 | `cline/z-ai/glm-5.2` | FAIL error |
| 165 | `cline/moonshotai/kimi-k2.5` | FAIL error |
| 166 | `cline/openai/gpt-oss-20b` | FAIL error |
| 167 | `cline/google/gemma-3-27b-it` | FAIL error |
| 168 | `auto/coding:free` | untested |
| 169 | `auto/best-coding` | untested |

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
| 9 | `auto/best-coding` | untested |

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
| 9 | `claude-web/claude-opus-4-6` | FAIL error |
| 10 | `agy/claude-opus-4-6-thinking-low` | FAIL error |
| 11 | `antigravity/claude-opus-4-6-thinking-low` | FAIL error |
| 12 | `claude-web/claude-opus-4-6-low` | FAIL error |
| 13 | `claude-web/claude-opus-4-7-low` | FAIL error |
| 14 | `claude-web/claude-opus-4-8-low` | FAIL error |
| 15 | `claude-web/claude-opus-5` | FAIL error |
| 16 | `claude-web/claude-sonnet-5-high` | FAIL error |
| 17 | `claude-web/claude-sonnet-5-xhigh` | FAIL error |
| 18 | `claude-web/claude-sonnet-5-medium` | FAIL error |
| 19 | `claude-web/claude-sonnet-5-low` | FAIL error |
| 20 | `kiro/claude-sonnet-4.5` | FAIL error |
| 21 | `agy/claude-sonnet-4-6` | FAIL error |
| 22 | `antigravity/claude-sonnet-4-6` | FAIL error |
| 23 | `claude-web/claude-sonnet-4-6` | FAIL error |
| 24 | `agy/claude-sonnet-4-6-low` | FAIL error |
| 25 | `antigravity/claude-sonnet-4-6-low` | FAIL error |
| 26 | `claude-web/claude-sonnet-4-6-low` | FAIL error |
| 27 | `claude-web/claude-sonnet-5` | FAIL error |
| 28 | `cline/anthropic/claude-sonnet-5` | FAIL error |
| 29 | `claude-web/claude-fable-5-1-low` | FAIL error |
| 30 | `claude-web/claude-fable-5-low` | FAIL error |
| 31 | `cline/anthropic/claude-fable-5-low` | FAIL error |
| 32 | `kiro/claude-haiku-4.5` | FAIL error |
| 33 | `claude-web/claude-haiku-4-5-20251001-low` | FAIL error |
| 34 | `auto/best-coding` | untested |

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
| 9 | `openai/free/deepseek-v4-flash-0731` | FAIL error |
| 10 | `kilocode/poolside/laguna-s-2.1:free` | FAIL error |
| 11 | `openai/free/deepseek-v4-pro-0813` | FAIL error |
| 12 | `openai/free/gpt-6-luna` | FAIL error |
| 13 | `openrouter/poolside/laguna-xs-2.1:free` | FAIL error |
| 14 | `openai/free/glm-5.3-flash` | FAIL error |
| 15 | `kilocode/poolside/laguna-xs-2.1:free` | FAIL error |
| 16 | `openai/free/mimo-v2.6-pro` | FAIL error |
| 17 | `openai/claude-sonnet-5` | FAIL error |
| 18 | `openai/claude-opus-5.5` | FAIL error |
| 19 | `gemini/gemini-3.8-flash` | FAIL error |
| 20 | `openai/kimi-k3` | FAIL error |
| 21 | `openai/glm-5.3` | FAIL error |
| 22 | `openai/deepseek-v4-pro-max` | FAIL error |
| 23 | `gemini/gemini-3.7-flash` | FAIL error |
| 24 | `auto/best-coding` | untested |

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

**Working legs today:** 7 / 46 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `literouter/deepseek-v3.1` | OK |
| 2 | `literouter/deepseek-v4-flash-stable:free` | OK |
| 3 | `literouter/deepseek-v3.2` | OK |
| 4 | `literouter/deepseek-v3.1:free` | OK |
| 5 | `literouter/deepseek-v4-pro-cheap:free` | OK |
| 6 | `literouter/deepseek-v4-pro-cheap` | OK |
| 7 | `literouter/deepseek-v4.1-flash-1017:free` | OK |
| 8 | `openai/deepseek-v4-pro-max` | FAIL error |
| 9 | `deepseek-web/DeepSeek-V3.2` | FAIL error |
| 10 | `deepseek-web/deepseek-v4-pro` | FAIL error |
| 11 | `deepseek-web/deepseek-v4-pro-search` | FAIL error |
| 12 | `deepseek-web/deepseek-v4-pro-think` | FAIL error |
| 13 | `deepseek-web/deepseek-v4-pro-think-search` | FAIL error |
| 14 | `deepseek-web/DeepSeek-R1` | FAIL error |
| 15 | `deepseek-web/DeepSeek-R1-Search` | FAIL error |
| 16 | `deepseek-web/DeepSeek-Search` | FAIL error |
| 17 | `deepseek-web/deepseek-chat` | FAIL error |
| 18 | `deepseek-web/deepseek-reasoner` | FAIL error |
| 19 | `deepseek-web/deepseek-v4-flash` | FAIL error |
| 20 | `deepseek-web/deepseek-v4-flash-search` | FAIL error |
| 21 | `deepseek-web/deepseek-v4-flash-think` | FAIL error |
| 22 | `deepseek-web/deepseek-v4-flash-think-search` | FAIL error |
| 23 | `nvidia/deepseek-ai/deepseek-coder-6.7b-instruct` | FAIL error |
| 24 | `cline/deepseek/deepseek-v4.1-flash` | FAIL error |
| 25 | `cline/deepseek/deepseek-v4.1-flash:batch` | FAIL error |
| 26 | `nvidia/deepseek-ai/deepseek-v4.1-flash` | FAIL error |
| 27 | `cline/deepseek/deepseek-v3.2` | FAIL error |
| 28 | `cline/deepseek/deepseek-v3.2-exp` | FAIL error |
| 29 | `kiro/deepseek-3.2` | FAIL error |
| 30 | `cline/deepseek/deepseek-chat-v3.1` | FAIL error |
| 31 | `cline/deepseek/deepseek-v3.1-terminus` | FAIL error |
| 32 | `cline/deepseek/deepseek-v4-pro` | FAIL error |
| 33 | `cline/deepseek/deepseek-v4-pro-0813` | FAIL error |
| 34 | `cline/~deepseek/deepseek-pro-latest` | FAIL error |
| 35 | `cline/deepseek/deepseek-chat` | FAIL error |
| 36 | `cline/deepseek/deepseek-chat-v3-0324` | FAIL error |
| 37 | `cline/deepseek/deepseek-r1` | FAIL error |
| 38 | `cline/deepseek/deepseek-r1-0528` | FAIL error |
| 39 | `cline/deepseek/deepseek-v4-flash` | FAIL error |
| 40 | `cline/deepseek/deepseek-v4-flash-0731` | FAIL error |
| 41 | `cline/deepseek/deepseek-v4-flash-vision-exp` | FAIL error |
| 42 | `cline/~deepseek/deepseek-flash-latest` | FAIL error |
| 43 | `cline/~deepseek/deepseek-v4-flash-latest` | FAIL error |
| 44 | `cfp/deepseek-ai/deepseek-v4-pro-0813` | no connection |
| 45 | `cfp/deepseek-ai/deepseek-r1-distill-qwen-32b` | no connection |
| 46 | `cfp/deepseek-ai/deepseek-v4-flash-0731` | no connection |
| 47 | `auto/best-coding` | untested |

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
| 9 | `antigravity/gemini-3.1-flash-lite` | OK |
| 10 | `gemini/gemini-3.1-flash-lite` | OK |
| 11 | `agy/gemini-3-flash` | OK |
| 12 | `antigravity/gemini-3-flash` | OK |
| 13 | `gemini/gemini-3-flash-preview` | OK |
| 14 | `gemini/gemini-3.7-flash` | FAIL error |
| 15 | `cline/google/gemini-3.8-flash` | FAIL error |
| 16 | `gemini/gemini-3.8-flash` | FAIL error |
| 17 | `agy/gemini-3.7-flash-low` | FAIL error |
| 18 | `cline/google/gemini-3.7-flash` | FAIL error |
| 19 | `agy/gemini-3.6-flash-low` | FAIL error |
| 20 | `cline/google/gemini-3.6-flash` | FAIL error |
| 21 | `cline/google/gemini-3.5-flash` | FAIL error |
| 22 | `cline/google/gemini-3.5-flash-lite` | FAIL error |
| 23 | `agy/gemini-3.1-pro-low` | FAIL error |
| 24 | `antigravity/gemini-3.1-pro-low` | FAIL error |
| 25 | `cline/google/gemini-3.1-flash-lite` | FAIL error |
| 26 | `cline/google/gemini-2.5-pro` | FAIL error |
| 27 | `cline/google/gemini-2.5-flash` | FAIL error |
| 28 | `cline/google/gemini-2.5-flash-lite` | FAIL error |
| 29 | `gemini/gemini-2.5-flash-lite` | FAIL error |
| 30 | `agy/gemini-pro-agent` | FAIL error |
| 31 | `antigravity/gemini-pro-agent` | FAIL error |
| 32 | `cline/~google/gemini-pro-latest` | FAIL error |
| 33 | `cline/~google/gemini-flash-latest` | FAIL error |
| 34 | `auto/best-coding` | untested |

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
| 9 | `cline/google/gemma-3-12b-it` | FAIL error |
| 10 | `cline/google/gemma-3-27b-it` | FAIL error |
| 11 | `cline/google/gemma-3-4b-it` | FAIL error |
| 12 | `nvidia/google/gemma-3-12b-it` | FAIL error |
| 13 | `nvidia/google/gemma-3-4b-it` | FAIL error |
| 14 | `cline/google/gemma-2-27b-it` | FAIL error |
| 15 | `nvidia/google/codegemma-1.1-7b` | FAIL error |
| 16 | `nvidia/google/codegemma-7b` | FAIL error |
| 17 | `nvidia/google/gemma-2b` | FAIL error |
| 18 | `nvidia/google/recurrentgemma-2b` | FAIL error |
| 19 | `cfp/google/gemma-4-26b-a4b-it` | no connection |
| 20 | `cfp/aisingapore/gemma-sea-lion-v4-27b-it` | no connection |
| 21 | `ddgw/tinfoil/gemma4-31b` | no connection |
| 22 | `auto/best-coding` | untested |

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
| 9 | `cline/z-ai/glm-5.3:batch` | FAIL error |
| 10 | `cline/z-ai/glm-5.2` | FAIL error |
| 11 | `cline/z-ai/glm-5.1` | FAIL error |
| 12 | `cline/z-ai/glm-5-turbo` | FAIL error |
| 13 | `cline/z-ai/glm-4.7` | FAIL error |
| 14 | `cline/z-ai/glm-4.7-flash` | FAIL error |
| 15 | `cline/z-ai/glm-4.6` | FAIL error |
| 16 | `cline/z-ai/glm-4.6v` | FAIL error |
| 17 | `cline/z-ai/glm-4.5` | FAIL error |
| 18 | `cline/z-ai/glm-4.5-air` | FAIL error |
| 19 | `cline/z-ai/glm-4.5v` | FAIL error |
| 20 | `cline/z-ai/glm-5` | FAIL error |
| 21 | `cline/z-ai/glm-5v-turbo` | FAIL error |
| 22 | `cline/~z-ai/glm-flash-latest` | FAIL error |
| 23 | `cline/~z-ai/glm-latest` | FAIL error |
| 24 | `kiro/glm-5` | FAIL error |
| 25 | `zai-web/glm-5.2` | FAIL error |
| 26 | `zai-web/glm-5.3-flash-max` | FAIL error |
| 27 | `zai-web/glm-5.3-max` | FAIL error |
| 28 | `zai-web/glm-5.3-flash-high` | FAIL error |
| 29 | `zai-web/glm-5.3-high` | FAIL error |
| 30 | `nvidia/z-ai/glm-5.3` | FAIL error |
| 31 | `nvidia/z-ai/glm-5.3-flash` | FAIL error |
| 32 | `zai-web/glm-5.3` | FAIL error |
| 33 | `zai-web/glm-5.3-flash` | FAIL error |
| 34 | `zai-web/glm-5.3-flash-low` | FAIL error |
| 35 | `zai-web/glm-5.3-low` | FAIL error |
| 36 | `zai-web/glm-5.2-max` | FAIL error |
| 37 | `zai-web/glm-5.2-high` | FAIL error |
| 38 | `openai/glm-5.3` | FAIL error |
| 39 | `cfp/zai-org/glm-4.7-flash` | no connection |
| 40 | `cfp/zai-org/glm-5.2` | no connection |
| 41 | `aug/glm-5.2` | no connection |
| 42 | `auto/best-coding` | untested |

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
| 9 | `codex/gpt-6-luna-medium` | OK |
| 10 | `codex/gpt-6-luna-low` | OK |
| 11 | `codex/gpt-5.6-luna-max` | OK |
| 12 | `codex/gpt-5.6-terra-max` | OK |
| 13 | `codex/gpt-5.6-luna-high` | OK |
| 14 | `codex/gpt-5.6-luna-xhigh` | OK |
| 15 | `codex/gpt-5.6-terra-high` | OK |
| 16 | `codex/gpt-5.6-terra-xhigh` | OK |
| 17 | `codex/gpt-5.6-luna-medium` | OK |
| 18 | `codex/gpt-5.6-luna-low` | OK |
| 19 | `codex/gpt-5.6-terra-low` | OK |
| 20 | `cline/openai/gpt-5.6-sol` | FAIL error |
| 21 | `codex/gpt-5.5` | FAIL error |
| 22 | `cline/openai/gpt-5.4-mini` | FAIL error |
| 23 | `cline/openai/gpt-4o-2024-05-13` | FAIL error |
| 24 | `cline/openai/gpt-4o-2024-08-06` | FAIL error |
| 25 | `cline/openai/gpt-4o-2024-11-20` | FAIL error |
| 26 | `cline/openai/gpt-4o-mini-2024-07-18` | FAIL error |
| 27 | `cline/openai/gpt-6.1-sol-pro` | FAIL error |
| 28 | `cline/openai/gpt-6.1-sol-pro:batch` | FAIL error |
| 29 | `cline/openai/gpt-6.1-sol` | FAIL error |
| 30 | `cline/openai/gpt-6.1-sol:batch` | FAIL error |
| 31 | `codex/gpt-6-astra-max` | FAIL error |
| 32 | `codex/gpt-6-astra-ultra` | FAIL error |
| 33 | `codex/gpt-6-sol-max` | FAIL error |
| 34 | `codex/gpt-6-sol-ultra` | FAIL error |
| 35 | `cline/openai/gpt-6-astra-pro` | FAIL error |
| 36 | `cline/openai/gpt-6-astra-pro:batch` | FAIL error |
| 37 | `cline/openai/gpt-6-luna-pro` | FAIL error |
| 38 | `cline/openai/gpt-6-luna-pro:batch` | FAIL error |
| 39 | `cline/openai/gpt-6-sol-pro` | FAIL error |
| 40 | `cline/openai/gpt-6-sol-pro:batch` | FAIL error |
| 41 | `codex/gpt-6-astra-high` | FAIL error |
| 42 | `codex/gpt-6-astra-xhigh` | FAIL error |
| 43 | `codex/gpt-6-sol-high` | FAIL error |
| 44 | `codex/gpt-6-sol-xhigh` | FAIL error |
| 45 | `cline/openai/gpt-6-astra` | FAIL error |
| 46 | `cline/openai/gpt-6-astra:batch` | FAIL error |
| 47 | `cline/openai/gpt-6-luna` | FAIL error |
| 48 | `cline/openai/gpt-6-luna:batch` | FAIL error |
| 49 | `cline/openai/gpt-6-sol` | FAIL error |
| 50 | `cline/openai/gpt-6-sol:batch` | FAIL error |
| 51 | `codex/gpt-6-astra` | FAIL error |
| 52 | `codex/gpt-6-sol` | FAIL error |
| 53 | `codex/gpt-6-astra-medium` | FAIL error |
| 54 | `codex/gpt-6-sol-medium` | FAIL error |
| 55 | `codex/gpt-6-astra-low` | FAIL error |
| 56 | `codex/gpt-6-sol-low` | FAIL error |
| 57 | `codex/gpt-5.6-sol-max` | FAIL error |
| 58 | `codex/gpt-5.6-sol-ultra` | FAIL error |
| 59 | `codex/gpt-5.6-terra-ultra` | FAIL error |
| 60 | `cline/openai/gpt-5.6-luna-pro` | FAIL error |
| 61 | `cline/openai/gpt-5.6-luna-pro:batch` | FAIL error |
| 62 | `cline/openai/gpt-5.6-sol-pro` | FAIL error |
| 63 | `cline/openai/gpt-5.6-sol-pro:batch` | FAIL error |
| 64 | `cline/openai/gpt-5.6-terra-pro` | FAIL error |
| 65 | `cline/openai/gpt-5.6-terra-pro:batch` | FAIL error |
| 66 | `codex/gpt-5.6-sol-high` | FAIL error |
| 67 | `codex/gpt-5.6-sol-xhigh` | FAIL error |
| 68 | `cline/openai/gpt-5.6-luna` | FAIL error |
| 69 | `cline/openai/gpt-5.6-luna:batch` | FAIL error |
| 70 | `cline/openai/gpt-5.6-sol:batch` | FAIL error |
| 71 | `cline/openai/gpt-5.6-terra` | FAIL error |
| 72 | `cline/openai/gpt-5.6-terra:batch` | FAIL error |
| 73 | `codex/gpt-5.6-sol` | FAIL error |
| 74 | `kiro/gpt-5.6-luna` | FAIL error |
| 75 | `kiro/gpt-5.6-sol` | FAIL error |
| 76 | `kiro/gpt-5.6-terra` | FAIL error |
| 77 | `codex/gpt-5.6-sol-medium` | FAIL error |
| 78 | `codex/gpt-5.6-terra-medium` | FAIL error |
| 79 | `codex/gpt-5.6-sol-low` | FAIL error |
| 80 | `cline/openai/gpt-5.5-pro` | FAIL error |
| 81 | `cline/openai/gpt-5.5-pro:batch` | FAIL error |
| 82 | `codex/gpt-5.5-high` | FAIL error |
| 83 | `codex/gpt-5.5-xhigh` | FAIL error |
| 84 | `cline/openai/gpt-5.5` | FAIL error |
| 85 | `cline/openai/gpt-5.5:batch` | FAIL error |
| 86 | `codex/gpt-5.5-medium` | FAIL error |
| 87 | `codex/gpt-5.5-low` | FAIL error |
| 88 | `cline/openai/gpt-5.4-pro` | FAIL error |
| 89 | `cline/openai/gpt-5.4-pro:batch` | FAIL error |
| 90 | `cline/openai/gpt-5.4` | FAIL error |
| 91 | `cline/openai/gpt-5.4:batch` | FAIL error |
| 92 | `cline/openai/gpt-5.4-nano` | FAIL error |
| 93 | `cline/openai/gpt-5.4-nano:batch` | FAIL error |
| 94 | `cline/openai/gpt-5.4-mini:batch` | FAIL error |
| 95 | `cline/openai/gpt-5.3-codex` | FAIL error |
| 96 | `cline/openai/gpt-5.2-pro` | FAIL error |
| 97 | `cline/openai/gpt-5.2-pro:batch` | FAIL error |
| 98 | `cline/openai/gpt-5.2` | FAIL error |
| 99 | `cline/openai/gpt-5.2-chat` | FAIL error |
| 100 | `cline/openai/gpt-5.2:batch` | FAIL error |
| 101 | `cline/openai/gpt-5.1` | FAIL error |
| 102 | `cline/openai/gpt-5.1:batch` | FAIL error |
| 103 | `cline/openai/gpt-5-pro` | FAIL error |
| 104 | `cline/openai/gpt-5-pro:batch` | FAIL error |
| 105 | `cline/openai/gpt-5-nano` | FAIL error |
| 106 | `cline/openai/gpt-5-nano:batch` | FAIL error |
| 107 | `cline/openai/gpt-5-mini` | FAIL error |
| 108 | `cline/openai/gpt-5-mini:batch` | FAIL error |
| 109 | `cline/openai/gpt-4o` | FAIL error |
| 110 | `cline/openai/gpt-4o:batch` | FAIL error |
| 111 | `cline/openai/gpt-5` | FAIL error |
| 112 | `cline/openai/gpt-5:batch` | FAIL error |
| 113 | `cline/openai/gpt-oss-120b` | FAIL error |
| 114 | `cline/openai/gpt-oss-120b:batch` | FAIL error |
| 115 | `cline/openai/gpt-oss-20b` | FAIL error |
| 116 | `cline/openai/gpt-oss-20b:batch` | FAIL error |
| 117 | `nvidia/openai/gpt-oss-20b` | FAIL error |
| 118 | `agy/gpt-oss-120b-medium` | FAIL error |
| 119 | `antigravity/gpt-oss-120b-medium` | FAIL error |
| 120 | `cline/openai/gpt-4o-mini` | FAIL error |
| 121 | `cline/openai/gpt-4o-mini:batch` | FAIL error |
| 122 | `ddgw/gpt-5.6-luna` | no connection |
| 123 | `ddgw/gpt-5.4-mini` | no connection |
| 124 | `cfp/openai/gpt-oss-120b` | no connection |
| 125 | `cfp/openai/gpt-oss-20b` | no connection |
| 126 | `ddgw/tinfoil/gpt-oss-120b` | no connection |
| 127 | `auto/best-coding` | untested |

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
| 9 | `cline/x-ai/grok-4.20-multi-agent` | FAIL error |
| 10 | `cline/x-ai/grok-4.7` | FAIL error |
| 11 | `cline/x-ai/grok-4.6` | FAIL error |
| 12 | `cline/x-ai/grok-4.3` | FAIL error |
| 13 | `cline/x-ai/grok-4.3:batch` | FAIL error |
| 14 | `cline/x-ai/grok-build-0.1` | FAIL error |
| 15 | `cline/~x-ai/grok-latest` | FAIL error |
| 16 | `grok-web/expert` | FAIL error |
| 17 | `grok-web/heavy` | FAIL error |
| 18 | `auto/best-coding` | untested |

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
| 9 | `cline/moonshotai/kimi-k2` | FAIL error |
| 10 | `cline/moonshotai/kimi-k2-0905` | FAIL error |
| 11 | `cline/moonshotai/kimi-k2-thinking` | FAIL error |
| 12 | `cline/moonshotai/kimi-k3:batch` | FAIL error |
| 13 | `cline/~moonshotai/kimi-latest` | FAIL error |
| 14 | `nvidia/moonshotai/kimi-k3` | FAIL error |
| 15 | `aug/kimi-k2.7` | no connection |
| 16 | `cfp/moonshotai/kimi-k2.7-code` | no connection |
| 17 | `aug/kimi-k2.6` | no connection |
| 18 | `cfp/moonshotai/kimi-k2.6` | no connection |
| 19 | `auto/best-coding` | untested |

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
| 9 | `cline/meta-llama/llama-3.2-3b-instruct` | FAIL error |
| 10 | `nvidia/meta/llama-3.2-11b-vision-instruct` | FAIL error |
| 11 | `nvidia/meta/llama-3.2-90b-vision-instruct` | FAIL error |
| 12 | `cline/aion-labs/aion-rp-llama-3.1-8b` | FAIL error |
| 13 | `cline/meta-llama/llama-3.1-70b-instruct` | FAIL error |
| 14 | `cline/meta-llama/llama-3.1-8b-instruct` | FAIL error |
| 15 | `cline/nousresearch/hermes-3-llama-3.1-405b` | FAIL error |
| 16 | `cline/nousresearch/hermes-3-llama-3.1-70b` | FAIL error |
| 17 | `ollama-cloud/minimax-m2.7` | FAIL error |
| 18 | `nvidia/nvidia/llama3-chatqa-1.5-70b` | FAIL error |
| 19 | `nvidia/meta/codellama-70b` | FAIL error |
| 20 | `nvidia/meta/llama2-70b` | FAIL error |
| 21 | `cfp/meta/llama-4-scout-17b-16e-instruct` | no connection |
| 22 | `cfp/meta-llama/llama-3.3-70b-instruct-fp8-fast` | no connection |
| 23 | `cfp/meta/llama-3.1-8b-instruct-fp8` | no connection |
| 24 | `auto/best-coding` | untested |

<a id="combomistral-best"></a>
### combo/mistral-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 6 / 44 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `mistral/ministral-3b-latest` | OK |
| 2 | `mistral/mistral-code-latest` | OK |
| 3 | `mistral/ministral-8b-latest` | OK |
| 4 | `codestral/codestral-latest` | OK |
| 5 | `codestral/codestral-2508` | OK |
| 6 | `mistral/codestral-latest` | OK |
| 7 | `literouter/ministral-3-8b-instruct:free` | FAIL error |
| 8 | `literouter/ministral-3b-2512:free` | FAIL error |
| 9 | `cline/mistralai/mistral-large-4-0` | FAIL error |
| 10 | `cline/mistralai/mistral-small-3.2-24b-instruct` | FAIL error |
| 11 | `cline/mistralai/mistral-small-3.1-24b-instruct` | FAIL error |
| 12 | `cline/mistralai/mistral-medium-3.1` | FAIL error |
| 13 | `cline/mistralai/mistral-medium-3.1:batch` | FAIL error |
| 14 | `cline/mistralai/mistral-medium-3-5` | FAIL error |
| 15 | `cline/mistralai/mistral-medium-3-5:batch` | FAIL error |
| 16 | `nvidia/mistralai/mistral-large-2-instruct` | FAIL error |
| 17 | `nvidia/mistralai/mistral-7b-instruct-v0.3` | FAIL error |
| 18 | `nvidia/mistralai/codestral-22b-instruct-v0.1` | FAIL error |
| 19 | `nvidia/mistralai/mixtral-8x22b-v0.1` | FAIL error |
| 20 | `cline/cognitivecomputations/dolphin-mistral-24b-venice-edition` | FAIL error |
| 21 | `cline/mistralai/codestral-2508` | FAIL error |
| 22 | `cline/mistralai/codestral-2508:batch` | FAIL error |
| 23 | `cline/mistralai/devstral-2512` | FAIL error |
| 24 | `cline/mistralai/mistral-large` | FAIL error |
| 25 | `cline/mistralai/mistral-large-2407` | FAIL error |
| 26 | `cline/mistralai/mistral-large-2512` | FAIL error |
| 27 | `cline/mistralai/mistral-large-2512:batch` | FAIL error |
| 28 | `cline/mistralai/mistral-nemo` | FAIL error |
| 29 | `cline/mistralai/mistral-saba` | FAIL error |
| 30 | `cline/mistralai/mistral-small-24b-instruct-2501` | FAIL error |
| 31 | `cline/mistralai/mistral-small-2603` | FAIL error |
| 32 | `cline/mistralai/mistral-small-2603:batch` | FAIL error |
| 33 | `cline/mistralai/mixtral-8x22b-instruct` | FAIL error |
| 34 | `cline/mistralai/voxtral-small-24b-2507` | FAIL error |
| 35 | `nvidia/mistralai/mistral-large` | FAIL error |
| 36 | `nvidia/nv-mistralai/mistral-nemo-12b-instruct` | FAIL error |
| 37 | `cline/mistralai/mistral-medium-3` | FAIL error |
| 38 | `cline/mistralai/ministral-14b-2512` | FAIL error |
| 39 | `cline/mistralai/ministral-3b-2512` | FAIL error |
| 40 | `cline/mistralai/ministral-8b-2512` | FAIL error |
| 41 | `cline/mistralai/ministral-8b-2512:batch` | FAIL error |
| 42 | `nvidia/nvidia/mistral-nemo-minitron-8b-8k-instruct` | FAIL error |
| 43 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | no connection |
| 44 | `ddgw/mistral-small-2603` | no connection |
| 45 | `auto/best-coding` | untested |

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
| 9 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | FAIL error |
| 10 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 11 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 12 | `cline/nvidia/nemotron-3.5-content-safety:free` | FAIL error |
| 13 | `openrouter/nvidia/nemotron-3.5-content-safety:free` | FAIL error |
| 14 | `cline/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 15 | `cline/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | FAIL error |
| 16 | `nvidia/nvidia/nemotron-4-340b-instruct` | FAIL error |
| 17 | `cline/nvidia/nemotron-3.5-content-safety` | FAIL error |
| 18 | `cline/nvidia/nemotron-3.5-lightning` | FAIL error |
| 19 | `nvidia/nvidia/nemotron-3.5-content-safety` | FAIL error |
| 20 | `nvidia/nvidia/nemotron-3.5-lightning-30b-a3b` | FAIL error |
| 21 | `nvidia/nvidia/llama-3.1-nemotron-ultra-253b-v1` | FAIL error |
| 22 | `nvidia/nvidia/llama-3.1-nemotron-51b-instruct` | FAIL error |
| 23 | `nvidia/nvidia/llama-3.1-nemotron-70b-instruct` | FAIL error |
| 24 | `cline/nvidia/nemotron-3-ultra-550b-a55b` | FAIL error |
| 25 | `nvidia/nvidia/nemotron-3-ultra-550b-a55b` | FAIL error |
| 26 | `cline/nvidia/nemotron-3-super-120b-a12b` | FAIL error |
| 27 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | FAIL error |
| 28 | `cline/nvidia/nemotron-3-nano-30b-a3b` | FAIL error |
| 29 | `nvidia/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | FAIL error |
| 30 | `cfp/nvidia/nemotron-3-120b-a12b` | no connection |
| 31 | `auto/best-coding` | untested |

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
| 9 | `openrouter/poolside/laguna-xs-2.1:free` | FAIL error |
| 10 | `auto/best-coding` | untested |

<a id="comboqwen-best"></a>
### combo/qwen-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 4 / 45 testable

| # | Model | Status |
|---|-------|--------|
| 1 | `literouter/qwen3-coder:free` | OK |
| 2 | `literouter/qwen3-32b:free` | OK |
| 3 | `literouter/qwen3.5-9b:free` | OK |
| 4 | `groq/qwen/qwen3.8-27b` | OK |
| 5 | `cline/qwen/qwen3-coder-next` | FAIL error |
| 6 | `kiro/qwen3-coder-next` | FAIL error |
| 7 | `cline/qwen/qwen3.8-max-0902` | FAIL error |
| 8 | `cline/qwen/qwen3.8-max-prime` | FAIL error |
| 9 | `cline/qwen/qwen3.8-2.4t-a95b` | FAIL error |
| 10 | `cline/qwen/qwen3.8-27b` | FAIL error |
| 11 | `cline/qwen/qwen3.8-flash` | FAIL error |
| 12 | `cline/qwen/qwen3.8-omni-flash` | FAIL error |
| 13 | `cline/qwen/qwen3.7-max` | FAIL error |
| 14 | `cline/qwen/qwen3.7-flash` | FAIL error |
| 15 | `cline/qwen/qwen3.7-plus` | FAIL error |
| 16 | `cline/qwen/qwen3.6-27b` | FAIL error |
| 17 | `cline/qwen/qwen3.6-35b-a3b` | FAIL error |
| 18 | `cline/qwen/qwen3.6-flash` | FAIL error |
| 19 | `cline/qwen/qwen3.6-plus` | FAIL error |
| 20 | `cline/qwen/qwen3.5-122b-a10b` | FAIL error |
| 21 | `cline/qwen/qwen3.5-27b` | FAIL error |
| 22 | `cline/qwen/qwen3.5-35b-a3b` | FAIL error |
| 23 | `cline/qwen/qwen3.5-397b-a17b` | FAIL error |
| 24 | `cline/qwen/qwen3.5-9b` | FAIL error |
| 25 | `cline/qwen/qwen3.5-flash-02-23` | FAIL error |
| 26 | `cline/qwen/qwen3.5-plus-02-15` | FAIL error |
| 27 | `cline/qwen/qwen3.5-plus-20260420` | FAIL error |
| 28 | `cline/qwen/qwen-2.5-72b-instruct` | FAIL error |
| 29 | `cline/qwen/qwen-2.5-7b-instruct` | FAIL error |
| 30 | `cline/qwen/qwen-2.5-coder-32b-instruct` | FAIL error |
| 31 | `cline/qwen/qwen-plus` | FAIL error |
| 32 | `cline/qwen/qwen3-14b` | FAIL error |
| 33 | `cline/qwen/qwen3-235b-a22b-2507` | FAIL error |
| 34 | `cline/qwen/qwen3-235b-a22b-thinking-2507` | FAIL error |
| 35 | `cline/qwen/qwen3-30b-a3b` | FAIL error |
| 36 | `cline/qwen/qwen3-30b-a3b-instruct-2507` | FAIL error |
| 37 | `cline/qwen/qwen3-32b` | FAIL error |
| 38 | `cline/qwen/qwen3-coder` | FAIL error |
| 39 | `cline/qwen/qwen3-coder-30b-a3b-instruct` | FAIL error |
| 40 | `cline/qwen/qwen3-coder-flash` | FAIL error |
| 41 | `cline/qwen/qwen3-next-80b-a3b-instruct` | FAIL error |
| 42 | `cline/qwen/qwen3-next-80b-a3b-thinking` | FAIL error |
| 43 | `cfp/qwen/qwen2.5-coder-32b-instruct` | no connection |
| 44 | `cfp/qwen/qwen3-30b-a3b-fp8` | no connection |
| 45 | `cfp/qwen/qwq-32b` | no connection |
| 46 | `auto/best-coding` | untested |

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

