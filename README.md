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
| exa-search / zenmux-free | connected utility providers (search / free pool) |



## Provider status snapshot (2026-10-19)

Live sweep of all 30 combos: 562 unique models probed, 120 responded OK.

Combos with at least one working leg (24): all-best, apinex-best, claude-code, claude-fast, claude-max, cleanapis-best, deepseek-best, gemini-best, gemma-best, glm-best, gpt-best, grok-best, keep-trying, kilocode-best, literouter-best, llama-best, mistral-best, nara-best, nvidia-best, ollama-best, openrouter-best, qwen-best, steady-coding, xkiro-best.

Combos currently with zero working legs (6): claude-best, codex-best, kimi-best, kiro-best, spark-best, trae-best.

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

_Per-model probe status 2026-10-17: **OK** = answered live, **FAIL** = failed probe (kept: may recover), **untested** = never directly probed. Dead rows removed._

| Combo | Legs |
|---|---|
| [`combo/all-best`](#comboall-best) | 143 |
| [`combo/apinex-best`](#comboapinex-best) | 9 |
| [`combo/claude-best`](#comboclaude-best) | 34 |
| [`combo/claude-code`](#comboclaude-code) | 4 |
| [`combo/claude-fast`](#comboclaude-fast) | 4 |
| [`combo/claude-max`](#comboclaude-max) | 5 |
| [`combo/cleanapis-best`](#combocleanapis-best) | 24 |
| [`combo/codex-best`](#combocodex-best) | 5 |
| [`combo/deepseek-best`](#combodeepseek-best) | 44 |
| [`combo/gemini-best`](#combogemini-best) | 30 |
| [`combo/gemma-best`](#combogemma-best) | 21 |
| [`combo/glm-best`](#comboglm-best) | 39 |
| [`combo/gpt-best`](#combogpt-best) | 127 |
| [`combo/grok-best`](#combogrok-best) | 18 |
| [`combo/keep-trying`](#combokeep-trying) | 5 |
| [`combo/kilocode-best`](#combokilocode-best) | 7 |
| [`combo/kimi-best`](#combokimi-best) | 18 |
| [`combo/kiro-best`](#combokiro-best) | 8 |
| [`combo/literouter-best`](#comboliterouter-best) | 7 |
| [`combo/llama-best`](#combollama-best) | 21 |
| [`combo/mistral-best`](#combomistral-best) | 50 |
| [`combo/nara-best`](#combonara-best) | 3 |
| [`combo/nvidia-best`](#combonvidia-best) | 33 |
| [`combo/ollama-best`](#comboollama-best) | 3 |
| [`combo/openrouter-best`](#comboopenrouter-best) | 10 |
| [`combo/qwen-best`](#comboqwen-best) | 43 |
| [`combo/spark-best`](#combospark-best) | 6 |
| [`combo/steady-coding`](#combosteady-coding) | 3 |
| [`combo/trae-best`](#combotrae-best) | 3 |
| [`combo/xkiro-best`](#comboxkiro-best) | 18 |

<a id="comboall-best"></a>
### combo/all-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `codestral/codestral-latest` | OK |
| 2 | `codestral/codestral-2508` | OK |
| 3 | `antigravity/claude-opus-4-6-thinking-low` | FAIL 400 |
| 4 | `antigravity/claude-opus-4-6-thinking` | FAIL timeout |
| 5 | `antigravity/claude-sonnet-4-6-low` | FAIL 400 |
| 6 | `agy/claude-opus-4-6-thinking-low` | FAIL 400 |
| 7 | `agy/claude-sonnet-4-6-low` | FAIL 400 |
| 8 | `claude-web/claude-opus-4-6` | FAIL 403 |
| 9 | `claude-web/claude-sonnet-4-6-low` | FAIL 400 |
| 10 | `claude-web/claude-opus-5-low` | FAIL 400 |
| 11 | `deepseek-web/deepseek-chat` | FAIL 502 |
| 12 | `gemini/gemini-3.8-flash-lite-tts` | FAIL 400 |
| 13 | `groq/openai/gpt-oss-120b` | OK |
| 14 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | FAIL timeout |
| 15 | `kilocode/nvidia/nemotron-3.5-lightning:free` | OK |
| 16 | `auto/coding:free` | router (live) |
| 17 | `codex/gpt-6-luna` | FAIL timeout |
| 18 | `kiro/qwen3-coder-next` | FAIL 429 quota |
| 19 | `mistral/codestral-latest` | OK |
| 20 | `literouter/glm-5:free` | FAIL 400 |
| 21 | `xkiro/qwen/qwen3-coder-plus:free` | OK |
| 22 | `ollama-cloud/nemotron-3-super` | OK |
| 23 | `zai-web/glm-5.3` | FAIL timeout |
| 24 | `grok-web/fast` | OK |
| 25 | `grok-cli/grok-4.7-low` | OK |
| 26 | `deepseek-web/DeepSeek-V3.2` | OK |
| 27 | `groq/qwen/qwen3.8-27b` | OK |
| 28 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | OK |
| 29 | `kilocode/poolside/laguna-s-2.1:free` | OK |
| 30 | `codex/gpt-5.6-luna` | FAIL timeout |
| 31 | `kiro/glm-5` | FAIL 429 quota |
| 32 | `literouter/glm-5.3-flash:free` | OK |
| 33 | `xkiro/qwen/qwen3-max:free` | OK |
| 34 | `ollama-cloud/gemma4:31b` | OK |
| 35 | `zai-web/glm-5.3-flash` | FAIL timeout |
| 36 | `grok-cli/grok-4.7` | OK |
| 37 | `deepseek-web/deepseek-reasoner` | FAIL 502 |
| 38 | `groq/openai/gpt-oss-20b` | FAIL timeout |
| 39 | `openrouter/cohere/north-mini-code:free` | OK |
| 40 | `kilocode/poolside/laguna-xs-2.1:free` | OK |
| 41 | `codex/gpt-5.5` | FAIL timeout |
| 42 | `kiro/deepseek-3.2` | FAIL 429 quota |
| 43 | `literouter/deepseek-v3.2:free` | OK |
| 44 | `xkiro/mistralai/codestral-2508` | OK |
| 45 | `zai-web/glm-5.2` | FAIL timeout |
| 46 | `grok-cli/grok-4.7-medium` | OK |
| 47 | `deepseek-web/deepseek-v4-flash` | OK |
| 48 | `openrouter/poolside/laguna-s-2.1:free` | OK |
| 49 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | OK |
| 50 | `codex/gpt-5.6-terra` | FAIL timeout |
| 51 | `kiro/minimax-m2.1` | FAIL 429 quota |
| 52 | `literouter/gpt-oss-120b:free` | FAIL 403 |
| 53 | `xkiro/mistralai/mistral-small-2603` | OK |
| 54 | `grok-cli/grok-4.7-high` | OK |
| 55 | `deepseek-web/deepseek-v4-pro` | OK |
| 56 | `openrouter/poolside/laguna-xs-2.1:free` | OK |
| 57 | `kilocode/cohere/north-mini-code:free` | OK |
| 58 | `kiro/minimax-m2.5` | FAIL 429 quota |
| 59 | `literouter/kimi-k2.7-code-cheap:free` | FAIL 403 |
| 60 | `xkiro/qwen/qwen3.8-max:free` | OK |
| 61 | `deepseek-web/deepseek-v4-pro-think` | OK |
| 62 | `openrouter/nvidia/nemotron-3.5-lightning:free` | OK |
| 63 | `literouter/qwen3-coder-next:free` | FAIL 403 |
| 64 | `xkiro/qwen/qwen3.7-max:free` | OK |
| 65 | `deepseek-web/deepseek-v4-pro-search` | OK |
| 66 | `literouter/llama-3.3-70b-instruct-turbo:free` | OK |
| 67 | `xkiro/qwen/qwen3.6-max-preview:free` | OK |
| 68 | `deepseek-web/deepseek-v4-pro-think-search` | OK |
| 69 | `literouter/ministral-3b-2512:free` | OK |
| 70 | `xkiro/mistralai/mistral-large-2512` | OK |
| 71 | `deepseek-web/deepseek-v4-flash-think` | FAIL 502 |
| 72 | `literouter/ministral-3-8b-instruct:free` | OK |
| 73 | `xkiro/qwen/qwen3.5-plus:free` | OK |
| 74 | `deepseek-web/deepseek-v4-flash-search` | OK |
| 75 | `literouter/deepseek-v3.1` | OK |
| 76 | `xkiro/sensenova/sensenova-6.8-flash-lite` | OK |
| 77 | `deepseek-web/deepseek-v4-flash-think-search` | FAIL 502 |
| 78 | `literouter/deepseek-v3.1:free` | OK |
| 79 | `xkiro/mistralai/devstral-medium` | OK |
| 80 | `deepseek-web/DeepSeek-R1` | OK |
| 81 | `literouter/deepseek-v3.2` | FAIL 403 |
| 82 | `xkiro/mistralai/mistral-medium-3.5` | OK |
| 83 | `deepseek-web/DeepSeek-R1-Search` | OK |
| 84 | `literouter/deepseek-v4-flash` | FAIL 403 |
| 85 | `xkiro/mistralai/ministral-8b` | OK |
| 86 | `deepseek-web/DeepSeek-Search` | OK |
| 87 | `literouter/deepseek-v4-flash-cheap` | OK |
| 88 | `literouter/deepseek-v4-flash-cheap:free` | OK |
| 89 | `literouter/deepseek-v4-flash-stable` | FAIL 403 |
| 90 | `literouter/deepseek-v4-flash:free` | FAIL 403 |
| 91 | `literouter/deepseek-v4-pro` | FAIL 403 |
| 92 | `literouter/deepseek-v4-pro-cheap` | FAIL 403 |
| 93 | `literouter/deepseek-v4-pro-cheap:free` | FAIL 403 |
| 94 | `literouter/deepseek-v4.1-flash` | FAIL 403 |
| 95 | `literouter/deepseek-v4.1-flash-cheap` | FAIL 403 |
| 96 | `literouter/deepseek-v4.1-flash-cheap:free` | FAIL 403 |
| 97 | `literouter/deepseek-v4.1-flash-stable` | OK |
| 98 | `literouter/deepseek-v4.1-flash-stable:free` | FAIL 403 |
| 99 | `literouter/deepseek-v4.1-flash:free` | OK |
| 100 | `literouter/gemini-2.5-flash-lite:free` | FAIL 400 |
| 101 | `literouter/glm-4.5` | FAIL timeout |
| 102 | `literouter/glm-4.5-air` | FAIL 403 |
| 103 | `literouter/glm-4.5-air:free` | FAIL 403 |
| 104 | `literouter/glm-4.5:free` | FAIL 403 |
| 105 | `literouter/glm-4.6` | FAIL 403 |
| 106 | `literouter/glm-4.6:free` | FAIL 400 |
| 107 | `literouter/glm-4.7` | FAIL 403 |
| 108 | `literouter/glm-4.7-flash` | FAIL 403 |
| 109 | `literouter/glm-4.7-flash-heretic` | FAIL timeout |
| 110 | `literouter/glm-4.7-flash-heretic:free` | FAIL 403 |
| 111 | `literouter/glm-4.7-flash:free` | OK |
| 112 | `literouter/glm-4.7:free` | FAIL 400 |
| 113 | `literouter/glm-5` | FAIL 403 |
| 114 | `literouter/glm-5.1` | FAIL 403 |
| 115 | `literouter/glm-5.1-cheap:free` | FAIL 403 |
| 116 | `literouter/glm-5.1:free` | FAIL 400 |
| 117 | `literouter/glm-5.2` | FAIL 403 |
| 118 | `literouter/glm-5.2-cheap` | FAIL 403 |
| 119 | `literouter/glm-5.2-cheap:free` | FAIL 403 |
| 120 | `literouter/glm-5.2:free` | FAIL 400 |
| 121 | `literouter/glm-5.3` | OK |
| 122 | `literouter/glm-5.3-cheap` | FAIL 403 |
| 123 | `literouter/glm-5.3-flash` | FAIL 403 |
| 124 | `literouter/glm-5.3-flash-cheap` | FAIL 403 |
| 125 | `literouter/glm-5.3-flash-cheap:free` | OK |
| 126 | `literouter/gpt-5-mini` | FAIL timeout |
| 127 | `literouter/gpt-5-mini-stable` | FAIL timeout |
| 128 | `nara/laguna-s-2.1` | OK |
| 129 | `nara/nemotron-3.5-lightning-free` | FAIL 400 |
| 130 | `morph/morph-v3-fast` | OK |
| 131 | `cline/meta/muse-spark-1.1` | FAIL 402 credits |
| 132 | `cline/meta/muse-spark-1.3-contributor` | FAIL 402 credits |
| 133 | `cline/meta/muse-spark-1.2-contributor` | FAIL 402 credits |
| 134 | `cline/deepseek/deepseek-r1` | FAIL 400 |
| 135 | `cline/qwen/qwen3-coder-30b-a3b-instruct` | FAIL 402 credits |
| 136 | `cline/google/gemini-3.8-flash` | FAIL 402 credits |
| 137 | `cline/meta-llama/llama-3.3-70b-instruct` | FAIL 402 credits |
| 138 | `cline/mistralai/codestral-2508` | FAIL 402 credits |
| 139 | `cline/z-ai/glm-5.2` | FAIL 402 credits |
| 140 | `cline/moonshotai/kimi-k2.5` | FAIL 402 credits |
| 141 | `cline/openai/gpt-oss-20b` | FAIL 402 credits |
| 142 | `cline/google/gemma-3-27b-it` | FAIL 402 credits |
| 143 | `auto/best-coding` | router (live) |

<a id="comboapinex-best"></a>
### combo/apinex-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `openai/free/gpt-6-luna` | FAIL 404 |
| 3 | `openai/free/glm-5.3-flash` | FAIL 404 |
| 4 | `openai/free/deepseek-v4.1-flash` | FAIL 404 |
| 5 | `openai/free/qwen-3.8-max` | FAIL 404 |
| 6 | `openai/free/mimo-v2.6-pro` | FAIL 404 |
| 7 | `openai/free/deepseek-v4-pro-0813` | FAIL 404 |
| 8 | `openai/free/deepseek-v4-flash-0731` | FAIL 404 |
| 9 | `auto/best-coding` | router (live) |

<a id="comboclaude-best"></a>
### combo/claude-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `openai/claude-opus-5.5` | FAIL 404 |
| 2 | `openai/claude-sonnet-5` | FAIL 404 |
| 3 | `claude-web/claude-opus-5-low` | FAIL 400 |
| 4 | `cline/anthropic/claude-opus-4.8-low` | FAIL 402 credits |
| 5 | `claude-web/claude-opus-5-high` | FAIL 400 |
| 6 | `claude-web/claude-opus-5-xhigh` | FAIL 400 |
| 7 | `claude-web/claude-opus-5-medium` | FAIL 400 |
| 8 | `antigravity/claude-opus-4-6-thinking` | FAIL timeout |
| 9 | `claude-web/claude-opus-4-6` | FAIL 403 |
| 10 | `agy/claude-opus-4-6-thinking-low` | FAIL 400 |
| 11 | `antigravity/claude-opus-4-6-thinking-low` | FAIL 400 |
| 12 | `claude-web/claude-opus-4-6-low` | FAIL 400 |
| 13 | `claude-web/claude-opus-4-7-low` | FAIL 400 |
| 14 | `claude-web/claude-opus-4-8-low` | FAIL 400 |
| 15 | `claude-web/claude-opus-5` | FAIL 429 quota |
| 16 | `claude-web/claude-sonnet-5-high` | FAIL 400 |
| 17 | `claude-web/claude-sonnet-5-xhigh` | FAIL 400 |
| 18 | `claude-web/claude-sonnet-5-medium` | FAIL 400 |
| 19 | `claude-web/claude-sonnet-5-low` | FAIL 400 |
| 20 | `kiro/claude-sonnet-4.5` | FAIL 429 quota |
| 21 | `agy/claude-sonnet-4-6` | FAIL timeout |
| 22 | `antigravity/claude-sonnet-4-6` | FAIL timeout |
| 23 | `claude-web/claude-sonnet-4-6` | FAIL 429 quota |
| 24 | `agy/claude-sonnet-4-6-low` | FAIL 400 |
| 25 | `antigravity/claude-sonnet-4-6-low` | FAIL 400 |
| 26 | `claude-web/claude-sonnet-4-6-low` | FAIL 400 |
| 27 | `claude-web/claude-sonnet-5` | FAIL 429 quota |
| 28 | `cline/anthropic/claude-sonnet-5` | FAIL 402 credits |
| 29 | `claude-web/claude-fable-5-1-low` | FAIL 429 quota |
| 30 | `claude-web/claude-fable-5-low` | FAIL 400 |
| 31 | `cline/anthropic/claude-fable-5-low` | FAIL 400 |
| 32 | `kiro/claude-haiku-4.5` | FAIL 429 quota |
| 33 | `claude-web/claude-haiku-4-5-20251001-low` | FAIL 400 |
| 34 | `auto/best-coding` | router (live) |

<a id="comboclaude-code"></a>
### combo/claude-code - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `auto/claude-sonnet` | router (live) |
| 3 | `gemini/gemini-3.8-flash` | FAIL 400 |
| 4 | `auto/best-coding` | router (live) |

<a id="comboclaude-fast"></a>
### combo/claude-fast - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `gemini/gemini-3.8-flash` | FAIL 400 |
| 3 | `auto/best-fast` | router (live) |
| 4 | `auto/best-coding` | router (live) |

<a id="comboclaude-max"></a>
### combo/claude-max - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `auto/claude-opus` | router (live) |
| 2 | `groq/openai/gpt-oss-120b` | OK |
| 3 | `auto/claude-sonnet` | router (live) |
| 4 | `gemini/gemini-3.8-flash` | FAIL 400 |
| 5 | `auto/best-coding` | router (live) |

<a id="combocleanapis-best"></a>
### combo/cleanapis-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `openai/claude-sonnet-5` | FAIL 404 |
| 2 | `groq/openai/gpt-oss-120b` | OK |
| 3 | `openai/claude-opus-5.5` | FAIL 404 |
| 4 | `gemini/gemini-3.8-flash` | FAIL 400 |
| 5 | `openai/kimi-k3` | FAIL 404 |
| 6 | `groq/qwen/qwen3.8-27b` | OK |
| 7 | `openai/glm-5.3` | FAIL 404 |
| 8 | `openrouter/cohere/north-mini-code:free` | OK |
| 9 | `openai/deepseek-v4-pro-max` | FAIL 404 |
| 10 | `kilocode/cohere/north-mini-code:free` | OK |
| 11 | `openai/free/qwen-3.8-max` | FAIL 404 |
| 12 | `groq/openai/gpt-oss-20b` | FAIL timeout |
| 13 | `openai/free/deepseek-v4.1-flash` | FAIL 404 |
| 14 | `openrouter/poolside/laguna-s-2.1:free` | OK |
| 15 | `openai/free/deepseek-v4-flash-0731` | FAIL 404 |
| 16 | `kilocode/poolside/laguna-s-2.1:free` | OK |
| 17 | `openai/free/deepseek-v4-pro-0813` | FAIL 404 |
| 18 | `gemini/gemini-3.7-flash` | FAIL 400 |
| 19 | `openai/free/gpt-6-luna` | FAIL 404 |
| 20 | `openrouter/poolside/laguna-xs-2.1:free` | OK |
| 21 | `openai/free/glm-5.3-flash` | FAIL 404 |
| 22 | `kilocode/poolside/laguna-xs-2.1:free` | OK |
| 23 | `openai/free/mimo-v2.6-pro` | FAIL 404 |
| 24 | `auto/best-coding` | router (live) |

<a id="combocodex-best"></a>
### combo/codex-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `codex/gpt-6-luna` | FAIL timeout |
| 2 | `codex/gpt-5.6-luna` | FAIL timeout |
| 3 | `codex/gpt-5.6-terra` | FAIL timeout |
| 4 | `codex/gpt-5.5` | FAIL timeout |
| 5 | `auto/best-coding` | router (live) |

<a id="combodeepseek-best"></a>
### combo/deepseek-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `openai/deepseek-v4-pro-max` | FAIL 404 |
| 2 | `deepseek-web/DeepSeek-V3.2` | OK |
| 3 | `deepseek-web/deepseek-v4-pro` | OK |
| 4 | `deepseek-web/deepseek-v4-pro-search` | OK |
| 5 | `deepseek-web/deepseek-v4-pro-think` | OK |
| 6 | `deepseek-web/deepseek-v4-pro-think-search` | OK |
| 7 | `deepseek-web/DeepSeek-R1` | OK |
| 8 | `deepseek-web/DeepSeek-R1-Search` | OK |
| 9 | `deepseek-web/DeepSeek-Search` | OK |
| 10 | `deepseek-web/deepseek-chat` | FAIL 502 |
| 11 | `deepseek-web/deepseek-reasoner` | FAIL 502 |
| 12 | `deepseek-web/deepseek-v4-flash` | OK |
| 13 | `deepseek-web/deepseek-v4-flash-search` | OK |
| 14 | `deepseek-web/deepseek-v4-flash-think` | FAIL 502 |
| 15 | `deepseek-web/deepseek-v4-flash-think-search` | FAIL 502 |
| 16 | `nvidia/deepseek-ai/deepseek-coder-6.7b-instruct` | FAIL 404 |
| 17 | `cline/deepseek/deepseek-v4.1-flash` | FAIL 402 credits |
| 18 | `cline/deepseek/deepseek-v4.1-flash:batch` | FAIL 402 credits |
| 19 | `nvidia/deepseek-ai/deepseek-v4.1-flash` | FAIL timeout |
| 20 | `cline/deepseek/deepseek-v3.2` | FAIL 402 credits |
| 21 | `cline/deepseek/deepseek-v3.2-exp` | FAIL 402 credits |
| 22 | `kiro/deepseek-3.2` | FAIL 429 quota |
| 23 | `xkiro/deepseek/deepseek-v3.2` | FAIL 404 |
| 24 | `cline/deepseek/deepseek-chat-v3.1` | FAIL 402 credits |
| 25 | `cline/deepseek/deepseek-v3.1-terminus` | FAIL 402 credits |
| 26 | `xkiro/deepseek/deepseek-chat-v3.1` | FAIL 404 |
| 27 | `cfp/deepseek-ai/deepseek-v4-pro-0813` | OK |
| 28 | `cline/deepseek/deepseek-v4-pro` | FAIL 402 credits |
| 29 | `cline/deepseek/deepseek-v4-pro-0813` | FAIL 402 credits |
| 30 | `cline/~deepseek/deepseek-pro-latest` | FAIL 402 credits |
| 31 | `xkiro/deepseek/deepseek-v4-pro` | FAIL 404 |
| 32 | `cfp/deepseek-ai/deepseek-r1-distill-qwen-32b` | FAIL timeout |
| 33 | `cfp/deepseek-ai/deepseek-v4-flash-0731` | FAIL timeout |
| 34 | `cline/deepseek/deepseek-chat` | FAIL 402 credits |
| 35 | `cline/deepseek/deepseek-chat-v3-0324` | FAIL 402 credits |
| 36 | `cline/deepseek/deepseek-r1` | FAIL 400 |
| 37 | `cline/deepseek/deepseek-r1-0528` | FAIL 402 credits |
| 38 | `cline/deepseek/deepseek-v4-flash` | FAIL 402 credits |
| 39 | `cline/deepseek/deepseek-v4-flash-0731` | FAIL 402 credits |
| 40 | `cline/deepseek/deepseek-v4-flash-vision-exp` | FAIL 402 credits |
| 41 | `cline/~deepseek/deepseek-flash-latest` | FAIL 402 credits |
| 42 | `cline/~deepseek/deepseek-v4-flash-latest` | FAIL 402 credits |
| 43 | `xkiro/deepseek/deepseek-v4-flash` | FAIL 404 |
| 44 | `auto/best-coding` | router (live) |

<a id="combogemini-best"></a>
### combo/gemini-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `gemini/gemini-3.7-flash` | FAIL 400 |
| 2 | `agy/gemini-3.8-flash-low` | OK |
| 3 | `cline/google/gemini-3.8-flash` | FAIL 402 credits |
| 4 | `gemini/gemini-3.8-flash` | FAIL 400 |
| 5 | `agy/gemini-3.7-flash-low` | FAIL 400 |
| 6 | `cline/google/gemini-3.7-flash` | FAIL 402 credits |
| 7 | `agy/gemini-3.6-flash-low` | FAIL 400 |
| 8 | `cline/google/gemini-3.6-flash` | FAIL 402 credits |
| 9 | `agy/gemini-3.5-flash-lite` | OK |
| 10 | `antigravity/gemini-3.5-flash-lite` | OK |
| 11 | `cline/google/gemini-3.5-flash` | FAIL 402 credits |
| 12 | `cline/google/gemini-3.5-flash-lite` | FAIL 402 credits |
| 13 | `agy/gemini-3.1-pro-low` | FAIL 400 |
| 14 | `antigravity/gemini-3.1-pro-low` | FAIL 400 |
| 15 | `agy/gemini-3.1-flash-lite` | OK |
| 16 | `antigravity/gemini-3.1-flash-lite` | OK |
| 17 | `cline/google/gemini-3.1-flash-lite` | FAIL 402 credits |
| 18 | `gemini/gemini-3.1-flash-lite` | OK |
| 19 | `agy/gemini-3-flash` | OK |
| 20 | `antigravity/gemini-3-flash` | OK |
| 21 | `gemini/gemini-3-flash-preview` | OK |
| 22 | `cline/google/gemini-2.5-pro` | FAIL 402 credits |
| 23 | `cline/google/gemini-2.5-flash` | FAIL 402 credits |
| 24 | `cline/google/gemini-2.5-flash-lite` | FAIL 402 credits |
| 25 | `gemini/gemini-2.5-flash-lite` | FAIL 404 |
| 26 | `agy/gemini-pro-agent` | FAIL 400 |
| 27 | `antigravity/gemini-pro-agent` | FAIL 400 |
| 28 | `cline/~google/gemini-pro-latest` | FAIL 402 credits |
| 29 | `cline/~google/gemini-flash-latest` | FAIL 402 credits |
| 30 | `auto/best-coding` | router (live) |

<a id="combogemma-best"></a>
### combo/gemma-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `cfp/google/gemma-4-26b-a4b-it` | FAIL timeout |
| 2 | `cline/google/gemma-4-26b-a4b-it` | FAIL 402 credits |
| 3 | `cline/google/gemma-4-26b-a4b-it:free` | FAIL 402 credits |
| 4 | `cline/google/gemma-4-31b-it` | FAIL 402 credits |
| 5 | `cline/google/gemma-4-31b-it:free` | FAIL 402 credits |
| 6 | `nvidia/google/gemma-4-31b-it` | OK |
| 7 | `openrouter/google/gemma-4-26b-a4b-it:free` | OK |
| 8 | `openrouter/google/gemma-4-31b-it:free` | FAIL timeout |
| 9 | `cline/google/gemma-3-12b-it` | FAIL 402 credits |
| 10 | `cline/google/gemma-3-27b-it` | FAIL 402 credits |
| 11 | `cline/google/gemma-3-4b-it` | FAIL 402 credits |
| 12 | `nvidia/google/gemma-3-12b-it` | FAIL 404 |
| 13 | `nvidia/google/gemma-3-4b-it` | FAIL 404 |
| 14 | `cline/google/gemma-2-27b-it` | FAIL 402 credits |
| 15 | `nvidia/google/codegemma-1.1-7b` | FAIL 404 |
| 16 | `cfp/aisingapore/gemma-sea-lion-v4-27b-it` | OK |
| 17 | `ddgw/tinfoil/gemma4-31b` | OK |
| 18 | `nvidia/google/codegemma-7b` | FAIL 404 |
| 19 | `nvidia/google/gemma-2b` | FAIL 404 |
| 20 | `nvidia/google/recurrentgemma-2b` | FAIL 404 |
| 21 | `auto/best-coding` | router (live) |

<a id="comboglm-best"></a>
### combo/glm-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `cfp/zai-org/glm-4.7-flash` | OK |
| 2 | `cfp/zai-org/glm-5.2` | OK |
| 3 | `auto/best-coding` | router (live) |
| 4 | `cline/z-ai/glm-5.3` | FAIL 402 credits |
| 5 | `cline/z-ai/glm-5.3-flash` | FAIL 402 credits |
| 6 | `cline/z-ai/glm-5.3-flash:batch` | FAIL 402 credits |
| 7 | `cline/z-ai/glm-5.3-flashx` | FAIL 402 credits |
| 8 | `cline/z-ai/glm-5.3-prime` | FAIL 402 credits |
| 9 | `cline/z-ai/glm-5.3:batch` | FAIL 402 credits |
| 10 | `cline/z-ai/glm-5.2` | FAIL 402 credits |
| 11 | `cline/z-ai/glm-5.1` | FAIL 402 credits |
| 12 | `cline/z-ai/glm-5-turbo` | FAIL 402 credits |
| 13 | `cline/z-ai/glm-4.7` | FAIL 402 credits |
| 14 | `cline/z-ai/glm-4.7-flash` | FAIL 402 credits |
| 15 | `cline/z-ai/glm-4.6` | FAIL 402 credits |
| 16 | `cline/z-ai/glm-4.6v` | FAIL 402 credits |
| 17 | `cline/z-ai/glm-4.5` | FAIL 402 credits |
| 18 | `cline/z-ai/glm-4.5-air` | FAIL 402 credits |
| 19 | `cline/z-ai/glm-4.5v` | FAIL 402 credits |
| 20 | `cline/z-ai/glm-5` | FAIL 402 credits |
| 21 | `cline/z-ai/glm-5v-turbo` | FAIL 402 credits |
| 22 | `cline/~z-ai/glm-flash-latest` | FAIL 402 credits |
| 23 | `cline/~z-ai/glm-latest` | FAIL 402 credits |
| 24 | `kiro/glm-5` | FAIL 429 quota |
| 25 | `aug/glm-5.2` | FAIL 502 |
| 26 | `zai-web/glm-5.2` | FAIL timeout |
| 27 | `zai-web/glm-5.3-flash-max` | FAIL timeout |
| 28 | `zai-web/glm-5.3-max` | FAIL timeout |
| 29 | `zai-web/glm-5.3-flash-high` | FAIL timeout |
| 30 | `zai-web/glm-5.3-high` | FAIL timeout |
| 31 | `nvidia/z-ai/glm-5.3` | FAIL timeout |
| 32 | `nvidia/z-ai/glm-5.3-flash` | FAIL timeout |
| 33 | `zai-web/glm-5.3` | FAIL timeout |
| 34 | `zai-web/glm-5.3-flash` | FAIL timeout |
| 35 | `zai-web/glm-5.3-flash-low` | FAIL timeout |
| 36 | `zai-web/glm-5.3-low` | FAIL timeout |
| 37 | `zai-web/glm-5.2-max` | FAIL timeout |
| 38 | `zai-web/glm-5.2-high` | FAIL timeout |
| 39 | `openai/glm-5.3` | FAIL 404 |

<a id="combogpt-best"></a>
### combo/gpt-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `codex/gpt-6-luna` | FAIL timeout |
| 2 | `cline/openai/gpt-5.6-sol` | FAIL timeout |
| 3 | `codex/gpt-5.6-luna` | FAIL timeout |
| 4 | `codex/gpt-5.6-terra` | FAIL timeout |
| 5 | `codex/gpt-5.5` | FAIL timeout |
| 6 | `cline/openai/gpt-5.4-mini` | FAIL timeout |
| 7 | `groq/openai/gpt-oss-120b` | OK |
| 8 | `groq/openai/gpt-oss-20b` | FAIL timeout |
| 9 | `cline/openai/gpt-4o-2024-05-13` | FAIL timeout |
| 10 | `cline/openai/gpt-4o-2024-08-06` | FAIL timeout |
| 11 | `cline/openai/gpt-4o-2024-11-20` | FAIL timeout |
| 12 | `cline/openai/gpt-4o-mini-2024-07-18` | FAIL timeout |
| 13 | `cline/openai/gpt-6.1-sol-pro` | FAIL timeout |
| 14 | `cline/openai/gpt-6.1-sol-pro:batch` | FAIL timeout |
| 15 | `cline/openai/gpt-6.1-sol` | FAIL timeout |
| 16 | `cline/openai/gpt-6.1-sol:batch` | FAIL timeout |
| 17 | `codex/gpt-6-astra-max` | FAIL timeout |
| 18 | `codex/gpt-6-astra-ultra` | FAIL timeout |
| 19 | `codex/gpt-6-luna-max` | FAIL timeout |
| 20 | `codex/gpt-6-sol-max` | FAIL 400 |
| 21 | `codex/gpt-6-sol-ultra` | FAIL 400 |
| 22 | `cline/openai/gpt-6-astra-pro` | FAIL 402 credits |
| 23 | `cline/openai/gpt-6-astra-pro:batch` | FAIL 402 credits |
| 24 | `cline/openai/gpt-6-luna-pro` | FAIL 402 credits |
| 25 | `cline/openai/gpt-6-luna-pro:batch` | FAIL 402 credits |
| 26 | `cline/openai/gpt-6-sol-pro` | FAIL timeout |
| 27 | `cline/openai/gpt-6-sol-pro:batch` | FAIL timeout |
| 28 | `codex/gpt-6-astra-high` | FAIL 400 |
| 29 | `codex/gpt-6-astra-xhigh` | FAIL 400 |
| 30 | `codex/gpt-6-luna-high` | FAIL timeout |
| 31 | `codex/gpt-6-luna-xhigh` | FAIL timeout |
| 32 | `codex/gpt-6-sol-high` | FAIL timeout |
| 33 | `codex/gpt-6-sol-xhigh` | FAIL timeout |
| 34 | `cline/openai/gpt-6-astra` | FAIL 402 credits |
| 35 | `cline/openai/gpt-6-astra:batch` | FAIL timeout |
| 36 | `cline/openai/gpt-6-luna` | FAIL timeout |
| 37 | `cline/openai/gpt-6-luna:batch` | FAIL timeout |
| 38 | `cline/openai/gpt-6-sol` | FAIL timeout |
| 39 | `cline/openai/gpt-6-sol:batch` | FAIL 402 credits |
| 40 | `codex/gpt-6-astra` | FAIL 400 |
| 41 | `codex/gpt-6-sol` | FAIL 400 |
| 42 | `codex/gpt-6-astra-medium` | FAIL 400 |
| 43 | `codex/gpt-6-luna-medium` | OK |
| 44 | `codex/gpt-6-sol-medium` | FAIL 400 |
| 45 | `codex/gpt-6-astra-low` | FAIL 400 |
| 46 | `codex/gpt-6-luna-low` | OK |
| 47 | `codex/gpt-6-sol-low` | FAIL 400 |
| 48 | `codex/gpt-5.6-luna-max` | OK |
| 49 | `codex/gpt-5.6-sol-max` | FAIL 400 |
| 50 | `codex/gpt-5.6-sol-ultra` | FAIL timeout |
| 51 | `codex/gpt-5.6-terra-max` | OK |
| 52 | `codex/gpt-5.6-terra-ultra` | OK |
| 53 | `cline/openai/gpt-5.6-luna-pro` | FAIL 402 credits |
| 54 | `cline/openai/gpt-5.6-luna-pro:batch` | FAIL 402 credits |
| 55 | `cline/openai/gpt-5.6-sol-pro` | FAIL 402 credits |
| 56 | `cline/openai/gpt-5.6-sol-pro:batch` | FAIL 402 credits |
| 57 | `cline/openai/gpt-5.6-terra-pro` | FAIL 402 credits |
| 58 | `cline/openai/gpt-5.6-terra-pro:batch` | FAIL 402 credits |
| 59 | `codex/gpt-5.6-luna-high` | OK |
| 60 | `codex/gpt-5.6-luna-xhigh` | OK |
| 61 | `codex/gpt-5.6-sol-high` | FAIL 400 |
| 62 | `codex/gpt-5.6-sol-xhigh` | FAIL 400 |
| 63 | `codex/gpt-5.6-terra-high` | OK |
| 64 | `codex/gpt-5.6-terra-xhigh` | OK |
| 65 | `cline/openai/gpt-5.6-luna` | FAIL 402 credits |
| 66 | `cline/openai/gpt-5.6-luna:batch` | FAIL 402 credits |
| 67 | `cline/openai/gpt-5.6-sol:batch` | FAIL 402 credits |
| 68 | `cline/openai/gpt-5.6-terra` | FAIL 402 credits |
| 69 | `cline/openai/gpt-5.6-terra:batch` | FAIL 402 credits |
| 70 | `codex/gpt-5.6-sol` | FAIL 400 |
| 71 | `ddgw/gpt-5.6-luna` | OK |
| 72 | `kiro/gpt-5.6-luna` | FAIL 400 |
| 73 | `kiro/gpt-5.6-sol` | FAIL 400 |
| 74 | `kiro/gpt-5.6-terra` | FAIL 400 |
| 75 | `codex/gpt-5.6-luna-medium` | OK |
| 76 | `codex/gpt-5.6-sol-medium` | FAIL 400 |
| 77 | `codex/gpt-5.6-terra-medium` | OK |
| 78 | `codex/gpt-5.6-luna-low` | OK |
| 79 | `codex/gpt-5.6-sol-low` | FAIL timeout |
| 80 | `codex/gpt-5.6-terra-low` | FAIL timeout |
| 81 | `cline/openai/gpt-5.5-pro` | FAIL timeout |
| 82 | `cline/openai/gpt-5.5-pro:batch` | FAIL timeout |
| 83 | `codex/gpt-5.5-high` | FAIL 400 |
| 84 | `codex/gpt-5.5-xhigh` | FAIL 400 |
| 85 | `cline/openai/gpt-5.5` | FAIL timeout |
| 86 | `cline/openai/gpt-5.5:batch` | FAIL timeout |
| 87 | `codex/gpt-5.5-medium` | FAIL 400 |
| 88 | `codex/gpt-5.5-low` | FAIL 400 |
| 89 | `cline/openai/gpt-5.4-pro` | FAIL timeout |
| 90 | `cline/openai/gpt-5.4-pro:batch` | FAIL 402 credits |
| 91 | `cline/openai/gpt-5.4` | FAIL 402 credits |
| 92 | `cline/openai/gpt-5.4:batch` | FAIL 402 credits |
| 93 | `cline/openai/gpt-5.4-nano` | FAIL 402 credits |
| 94 | `cline/openai/gpt-5.4-nano:batch` | FAIL 402 credits |
| 95 | `cline/openai/gpt-5.4-mini:batch` | FAIL 402 credits |
| 96 | `ddgw/gpt-5.4-mini` | OK |
| 97 | `cline/openai/gpt-5.3-codex` | FAIL 402 credits |
| 98 | `cline/openai/gpt-5.2-pro` | FAIL 402 credits |
| 99 | `cline/openai/gpt-5.2-pro:batch` | FAIL 402 credits |
| 100 | `cline/openai/gpt-5.2` | FAIL 402 credits |
| 101 | `cline/openai/gpt-5.2-chat` | FAIL 402 credits |
| 102 | `cline/openai/gpt-5.2:batch` | FAIL 402 credits |
| 103 | `cline/openai/gpt-5.1` | FAIL 402 credits |
| 104 | `cline/openai/gpt-5.1:batch` | FAIL 402 credits |
| 105 | `cline/openai/gpt-5-pro` | FAIL 402 credits |
| 106 | `cline/openai/gpt-5-pro:batch` | FAIL 402 credits |
| 107 | `cline/openai/gpt-5-nano` | FAIL 402 credits |
| 108 | `cline/openai/gpt-5-nano:batch` | FAIL 402 credits |
| 109 | `cline/openai/gpt-5-mini` | FAIL 402 credits |
| 110 | `cline/openai/gpt-5-mini:batch` | FAIL 402 credits |
| 111 | `cfp/openai/gpt-oss-120b` | OK |
| 112 | `cfp/openai/gpt-oss-20b` | OK |
| 113 | `cline/openai/gpt-4o` | FAIL 402 credits |
| 114 | `cline/openai/gpt-4o:batch` | FAIL 402 credits |
| 115 | `cline/openai/gpt-5` | FAIL 402 credits |
| 116 | `cline/openai/gpt-5:batch` | FAIL 402 credits |
| 117 | `cline/openai/gpt-oss-120b` | FAIL 402 credits |
| 118 | `cline/openai/gpt-oss-120b:batch` | FAIL 402 credits |
| 119 | `cline/openai/gpt-oss-20b` | FAIL 402 credits |
| 120 | `cline/openai/gpt-oss-20b:batch` | FAIL 402 credits |
| 121 | `ddgw/tinfoil/gpt-oss-120b` | OK |
| 122 | `nvidia/openai/gpt-oss-20b` | FAIL timeout |
| 123 | `agy/gpt-oss-120b-medium` | FAIL timeout |
| 124 | `antigravity/gpt-oss-120b-medium` | FAIL timeout |
| 125 | `cline/openai/gpt-4o-mini` | FAIL 402 credits |
| 126 | `cline/openai/gpt-4o-mini:batch` | FAIL 402 credits |
| 127 | `auto/best-coding` | router (live) |

<a id="combogrok-best"></a>
### combo/grok-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `grok-cli/grok-4.7-high` | OK |
| 2 | `grok-cli/grok-4.7-medium` | OK |
| 3 | `grok-cli/grok-4.7-low` | OK |
| 4 | `cline/x-ai/grok-4.5` | FAIL 402 credits |
| 5 | `grok-web/fast` | OK |
| 6 | `cline/x-ai/grok-4.20` | FAIL 402 credits |
| 7 | `cline/x-ai/grok-4.20-multi-agent` | FAIL 402 credits |
| 8 | `grok-cli/grok-4.7-xhigh` | OK |
| 9 | `cline/x-ai/grok-4.7` | FAIL 402 credits |
| 10 | `grok-cli/grok-4.7` | OK |
| 11 | `cline/x-ai/grok-4.6` | FAIL 402 credits |
| 12 | `cline/x-ai/grok-4.3` | FAIL 402 credits |
| 13 | `cline/x-ai/grok-4.3:batch` | FAIL 402 credits |
| 14 | `cline/x-ai/grok-build-0.1` | FAIL 402 credits |
| 15 | `cline/~x-ai/grok-latest` | FAIL 402 credits |
| 16 | `grok-web/expert` | FAIL 403 |
| 17 | `grok-web/heavy` | FAIL 403 |
| 18 | `auto/best-coding` | router (live) |

<a id="combokeep-trying"></a>
### combo/keep-trying - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | FAIL timeout |
| 2 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | FAIL timeout |
| 3 | `groq/openai/gpt-oss-120b` | OK |
| 4 | `gemini/gemini-3.8-flash` | FAIL 400 |
| 5 | `auto/best-coding` | router (live) |

<a id="combokilocode-best"></a>
### combo/kilocode-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `kilocode/nvidia/nemotron-3.5-lightning:free` | OK |
| 2 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | FAIL timeout |
| 3 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | OK |
| 4 | `kilocode/poolside/laguna-s-2.1:free` | OK |
| 5 | `kilocode/poolside/laguna-xs-2.1:free` | OK |
| 6 | `kilocode/cohere/north-mini-code:free` | OK |
| 7 | `auto/best-coding` | router (live) |

<a id="combokimi-best"></a>
### combo/kimi-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `openai/kimi-k3` | FAIL 404 |
| 2 | `cline/moonshotai/kimi-k3` | FAIL 402 credits |
| 3 | `aug/kimi-k2.7` | FAIL 502 |
| 4 | `cfp/moonshotai/kimi-k2.7-code` | FAIL timeout |
| 5 | `cline/moonshotai/kimi-k2.7-code` | FAIL 402 credits |
| 6 | `aug/kimi-k2.6` | FAIL 502 |
| 7 | `cfp/moonshotai/kimi-k2.6` | FAIL timeout |
| 8 | `cline/moonshotai/kimi-k2.6` | FAIL 402 credits |
| 9 | `nvidia/moonshotai/kimi-k2.6` | FAIL 404 |
| 10 | `ollama-cloud/kimi-k2.6` | FAIL 402 credits |
| 11 | `cline/moonshotai/kimi-k2.5` | FAIL 402 credits |
| 12 | `cline/moonshotai/kimi-k2` | FAIL 402 credits |
| 13 | `cline/moonshotai/kimi-k2-0905` | FAIL 402 credits |
| 14 | `cline/moonshotai/kimi-k2-thinking` | FAIL 402 credits |
| 15 | `cline/moonshotai/kimi-k3:batch` | FAIL 402 credits |
| 16 | `cline/~moonshotai/kimi-latest` | FAIL 402 credits |
| 17 | `nvidia/moonshotai/kimi-k3` | FAIL 400 |
| 18 | `auto/best-coding` | router (live) |

<a id="combokiro-best"></a>
### combo/kiro-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `kiro/glm-5` | FAIL 429 quota |
| 2 | `kiro/qwen3-coder-next` | FAIL 429 quota |
| 3 | `kiro/claude-sonnet-4.5` | FAIL 429 quota |
| 4 | `kiro/claude-haiku-4.5` | FAIL 429 quota |
| 5 | `kiro/deepseek-3.2` | FAIL 429 quota |
| 6 | `kiro/minimax-m2.5` | FAIL 429 quota |
| 7 | `kiro/minimax-m2.1` | FAIL 429 quota |
| 8 | `auto/best-coding` | router (live) |

<a id="comboliterouter-best"></a>
### combo/literouter-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `literouter/glm-5.3-flash:free` | OK |
| 2 | `literouter/llama-3.3-70b-instruct-turbo:free` | OK |
| 3 | `literouter/deepseek-v3.2:free` | OK |
| 4 | `literouter/kimi-k2.7-code-cheap:free` | FAIL 403 |
| 5 | `literouter/glm-5:free` | FAIL 400 |
| 6 | `literouter/gpt-oss-120b:free` | FAIL 403 |
| 7 | `literouter/qwen3-coder-next:free` | FAIL 403 |

<a id="combollama-best"></a>
### combo/llama-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `ollama-cloud/gemma4:31b` | OK |
| 2 | `cfp/meta/llama-4-scout-17b-16e-instruct` | OK |
| 3 | `cline/meta-llama/llama-4-maverick` | FAIL 402 credits |
| 4 | `cline/meta-llama/llama-4-scout` | FAIL 402 credits |
| 5 | `cfp/meta-llama/llama-3.3-70b-instruct-fp8-fast` | OK |
| 6 | `cline/meta-llama/llama-3.3-70b-instruct` | FAIL 402 credits |
| 7 | `cline/meta-llama/llama-3.2-1b-instruct` | FAIL 402 credits |
| 8 | `cline/meta-llama/llama-3.2-3b-instruct` | FAIL 402 credits |
| 9 | `nvidia/meta/llama-3.2-11b-vision-instruct` | OK |
| 10 | `nvidia/meta/llama-3.2-90b-vision-instruct` | FAIL timeout |
| 11 | `cfp/meta/llama-3.1-8b-instruct-fp8` | OK |
| 12 | `cline/aion-labs/aion-rp-llama-3.1-8b` | FAIL 402 credits |
| 13 | `cline/meta-llama/llama-3.1-70b-instruct` | FAIL 402 credits |
| 14 | `cline/meta-llama/llama-3.1-8b-instruct` | FAIL 402 credits |
| 15 | `cline/nousresearch/hermes-3-llama-3.1-405b` | FAIL 402 credits |
| 16 | `cline/nousresearch/hermes-3-llama-3.1-70b` | FAIL 402 credits |
| 17 | `ollama-cloud/minimax-m2.7` | FAIL 402 credits |
| 18 | `nvidia/nvidia/llama3-chatqa-1.5-70b` | FAIL 404 |
| 19 | `nvidia/meta/codellama-70b` | FAIL 404 |
| 20 | `nvidia/meta/llama2-70b` | FAIL 404 |
| 21 | `auto/best-coding` | router (live) |

<a id="combomistral-best"></a>
### combo/mistral-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `codestral/codestral-latest` | OK |
| 2 | `codestral/codestral-2508` | OK |
| 3 | `xkiro/mistralai/mistral-medium-3.5` | OK |
| 4 | `xkiro/mistralai/codestral-2508` | OK |
| 5 | `xkiro/mistralai/mistral-large-2512` | OK |
| 6 | `xkiro/mistralai/mistral-small-2603` | OK |
| 7 | `xkiro/mistralai/devstral-medium` | OK |
| 8 | `cline/mistralai/mistral-large-4-0` | FAIL 402 credits |
| 9 | `cline/mistralai/mistral-small-3.2-24b-instruct` | FAIL 402 credits |
| 10 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | OK |
| 11 | `cline/mistralai/mistral-small-3.1-24b-instruct` | FAIL 402 credits |
| 12 | `cline/mistralai/mistral-medium-3.1` | FAIL 402 credits |
| 13 | `cline/mistralai/mistral-medium-3.1:batch` | FAIL 402 credits |
| 14 | `cline/mistralai/mistral-medium-3-5` | FAIL 402 credits |
| 15 | `cline/mistralai/mistral-medium-3-5:batch` | FAIL 402 credits |
| 16 | `literouter/ministral-3-8b-instruct:free` | OK |
| 17 | `nvidia/mistralai/mistral-large-2-instruct` | FAIL 404 |
| 18 | `nvidia/mistralai/mistral-7b-instruct-v0.3` | FAIL 404 |
| 19 | `nvidia/mistralai/codestral-22b-instruct-v0.1` | FAIL 404 |
| 20 | `nvidia/mistralai/mixtral-8x22b-v0.1` | FAIL 404 |
| 21 | `cline/cognitivecomputations/dolphin-mistral-24b-venice-edition` | FAIL 402 credits |
| 22 | `cline/mistralai/codestral-2508` | FAIL 402 credits |
| 23 | `cline/mistralai/codestral-2508:batch` | FAIL 402 credits |
| 24 | `cline/mistralai/devstral-2512` | FAIL 402 credits |
| 25 | `cline/mistralai/mistral-large` | FAIL 402 credits |
| 26 | `cline/mistralai/mistral-large-2407` | FAIL 402 credits |
| 27 | `cline/mistralai/mistral-large-2512` | FAIL 402 credits |
| 28 | `cline/mistralai/mistral-large-2512:batch` | FAIL 402 credits |
| 29 | `cline/mistralai/mistral-nemo` | FAIL 402 credits |
| 30 | `cline/mistralai/mistral-saba` | FAIL 402 credits |
| 31 | `cline/mistralai/mistral-small-24b-instruct-2501` | FAIL 402 credits |
| 32 | `cline/mistralai/mistral-small-2603` | FAIL 402 credits |
| 33 | `cline/mistralai/mistral-small-2603:batch` | FAIL 402 credits |
| 34 | `cline/mistralai/mixtral-8x22b-instruct` | FAIL 402 credits |
| 35 | `cline/mistralai/voxtral-small-24b-2507` | FAIL 402 credits |
| 36 | `ddgw/mistral-small-2603` | OK |
| 37 | `mistral/codestral-latest` | OK |
| 38 | `nvidia/mistralai/mistral-large` | FAIL 404 |
| 39 | `nvidia/nv-mistralai/mistral-nemo-12b-instruct` | FAIL 404 |
| 40 | `cline/mistralai/mistral-medium-3` | FAIL 402 credits |
| 41 | `cline/mistralai/ministral-14b-2512` | FAIL 402 credits |
| 42 | `cline/mistralai/ministral-3b-2512` | FAIL 402 credits |
| 43 | `cline/mistralai/ministral-8b-2512` | FAIL 402 credits |
| 44 | `cline/mistralai/ministral-8b-2512:batch` | FAIL 402 credits |
| 45 | `literouter/ministral-3b-2512:free` | OK |
| 46 | `nvidia/nvidia/mistral-nemo-minitron-8b-8k-instruct` | FAIL 404 |
| 47 | `xkiro/mistralai/ministral-14b` | OK |
| 48 | `xkiro/mistralai/ministral-3b` | OK |
| 49 | `xkiro/mistralai/ministral-8b` | OK |
| 50 | `auto/best-coding` | router (live) |

<a id="combonara-best"></a>
### combo/nara-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `nara/laguna-s-2.1` | OK |
| 2 | `nara/nemotron-3.5-lightning-free` | FAIL 400 |
| 3 | `auto/best-coding` | router (live) |

<a id="combonvidia-best"></a>
### combo/nvidia-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `cline/nvidia/nemotron-3.5-lightning:free` | FAIL 402 credits |
| 2 | `kilocode/nvidia/nemotron-3.5-content-safety:free` | OK |
| 3 | `kilocode/nvidia/nemotron-3.5-lightning:free` | OK |
| 4 | `openrouter/nvidia/nemotron-3.5-lightning:free` | OK |
| 5 | `cline/nvidia/nemotron-3-ultra-550b-a55b:free` | FAIL 402 credits |
| 6 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | OK |
| 7 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | OK |
| 8 | `ollama-cloud/nemotron-3-super` | OK |
| 9 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | FAIL timeout |
| 10 | `nvidia/nvidia/nemotron-4-340b-instruct` | FAIL 404 |
| 11 | `nvidia/nvidia/nemotron-4-340b-reward` | FAIL 404 |
| 12 | `cline/nvidia/nemotron-3.5-content-safety` | FAIL 402 credits |
| 13 | `cline/nvidia/nemotron-3.5-content-safety:free` | FAIL 402 credits |
| 14 | `cline/nvidia/nemotron-3.5-lightning` | FAIL 402 credits |
| 15 | `nvidia/nvidia/nemotron-3.5-content-safety` | OK |
| 16 | `nvidia/nvidia/nemotron-3.5-lightning-30b-a3b` | OK |
| 17 | `openrouter/nvidia/nemotron-3.5-content-safety:free` | OK |
| 18 | `nvidia/nvidia/llama-3.1-nemotron-ultra-253b-v1` | FAIL 404 |
| 19 | `nvidia/nvidia/llama-3.1-nemotron-51b-instruct` | FAIL 404 |
| 20 | `nvidia/nvidia/llama-3.1-nemotron-70b-instruct` | FAIL 404 |
| 21 | `cline/nvidia/nemotron-3-ultra-550b-a55b` | FAIL 402 credits |
| 22 | `nvidia/nvidia/nemotron-3-ultra-550b-a55b` | OK |
| 23 | `cfp/nvidia/nemotron-3-120b-a12b` | OK |
| 24 | `cline/nvidia/nemotron-3-super-120b-a12b` | FAIL 402 credits |
| 25 | `cline/nvidia/nemotron-3-super-120b-a12b:free` | FAIL 402 credits |
| 26 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | OK |
| 27 | `cline/nvidia/nemotron-3-nano-30b-a3b` | FAIL 402 credits |
| 28 | `cline/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | FAIL 402 credits |
| 29 | `nvidia/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | OK |
| 30 | `nvidia/nvidia/nemotron-nano-3-30b-a3b` | FAIL 404 |
| 31 | `nvidia/nvidia/nemotron-parse-2.0` | OK |
| 32 | `nvidia/nvidia/nemotron-parse` | FAIL 400 |
| 33 | `auto/best-coding` | router (live) |

<a id="comboollama-best"></a>
### combo/ollama-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `ollama-cloud/nemotron-3-super` | OK |
| 2 | `ollama-cloud/gemma4:31b` | OK |
| 3 | `auto/best-coding` | router (live) |

<a id="comboopenrouter-best"></a>
### combo/openrouter-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `openrouter/nvidia/nemotron-3.5-lightning:free` | OK |
| 2 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | OK |
| 3 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | FAIL timeout |
| 4 | `openrouter/poolside/laguna-s-2.1:free` | OK |
| 5 | `openrouter/apodex/apodex-1.1-mini:free` | FAIL 400 |
| 6 | `openrouter/cohere/north-mini-code:free` | OK |
| 7 | `openrouter/google/gemma-4-31b-it:free` | FAIL timeout |
| 8 | `openrouter/liquid/lfm-2.5-2.6b:free` | OK |
| 9 | `openrouter/poolside/laguna-xs-2.1:free` | OK |
| 10 | `auto/best-coding` | router (live) |

<a id="comboqwen-best"></a>
### combo/qwen-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `groq/qwen/qwen3.8-27b` | OK |
| 2 | `cline/qwen/qwen3-coder-next` | FAIL 402 credits |
| 3 | `kiro/qwen3-coder-next` | FAIL 429 quota |
| 4 | `cline/qwen/qwen3.8-max-0902` | FAIL 402 credits |
| 5 | `cline/qwen/qwen3.8-max-prime` | FAIL 402 credits |
| 6 | `cline/qwen/qwen3.8-2.4t-a95b` | FAIL 402 credits |
| 7 | `cline/qwen/qwen3.8-27b` | FAIL 402 credits |
| 8 | `cline/qwen/qwen3.8-flash` | FAIL 402 credits |
| 9 | `cline/qwen/qwen3.8-omni-flash` | FAIL 402 credits |
| 10 | `cline/qwen/qwen3.7-max` | FAIL 402 credits |
| 11 | `cline/qwen/qwen3.7-flash` | FAIL 402 credits |
| 12 | `cline/qwen/qwen3.7-plus` | FAIL 402 credits |
| 13 | `cline/qwen/qwen3.6-27b` | FAIL 402 credits |
| 14 | `cline/qwen/qwen3.6-35b-a3b` | FAIL 402 credits |
| 15 | `cline/qwen/qwen3.6-flash` | FAIL 402 credits |
| 16 | `cline/qwen/qwen3.6-plus` | FAIL 402 credits |
| 17 | `cline/qwen/qwen3.5-122b-a10b` | FAIL 402 credits |
| 18 | `cline/qwen/qwen3.5-27b` | FAIL 402 credits |
| 19 | `cline/qwen/qwen3.5-35b-a3b` | FAIL 402 credits |
| 20 | `cline/qwen/qwen3.5-397b-a17b` | FAIL 402 credits |
| 21 | `cline/qwen/qwen3.5-9b` | FAIL 402 credits |
| 22 | `cline/qwen/qwen3.5-flash-02-23` | FAIL 402 credits |
| 23 | `cline/qwen/qwen3.5-plus-02-15` | FAIL 402 credits |
| 24 | `cline/qwen/qwen3.5-plus-20260420` | FAIL 402 credits |
| 25 | `cfp/qwen/qwen2.5-coder-32b-instruct` | OK |
| 26 | `cline/qwen/qwen-2.5-72b-instruct` | FAIL 402 credits |
| 27 | `cline/qwen/qwen-2.5-7b-instruct` | FAIL 402 credits |
| 28 | `cline/qwen/qwen-2.5-coder-32b-instruct` | FAIL 402 credits |
| 29 | `cfp/qwen/qwen3-30b-a3b-fp8` | OK |
| 30 | `cfp/qwen/qwq-32b` | OK |
| 31 | `cline/qwen/qwen-plus` | FAIL 402 credits |
| 32 | `cline/qwen/qwen3-14b` | FAIL 402 credits |
| 33 | `cline/qwen/qwen3-235b-a22b-2507` | FAIL 402 credits |
| 34 | `cline/qwen/qwen3-235b-a22b-thinking-2507` | FAIL 402 credits |
| 35 | `cline/qwen/qwen3-30b-a3b` | FAIL 402 credits |
| 36 | `cline/qwen/qwen3-30b-a3b-instruct-2507` | FAIL 402 credits |
| 37 | `cline/qwen/qwen3-32b` | FAIL 402 credits |
| 38 | `cline/qwen/qwen3-coder` | FAIL 402 credits |
| 39 | `cline/qwen/qwen3-coder-30b-a3b-instruct` | FAIL 402 credits |
| 40 | `cline/qwen/qwen3-coder-flash` | FAIL 402 credits |
| 41 | `cline/qwen/qwen3-next-80b-a3b-instruct` | FAIL 402 credits |
| 42 | `cline/qwen/qwen3-next-80b-a3b-thinking` | FAIL 402 credits |
| 43 | `auto/best-coding` | router (live) |

<a id="combospark-best"></a>
### combo/spark-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `cline/meta/muse-spark-1.3` | FAIL 402 credits |
| 2 | `cline/meta/muse-spark-1.2` | FAIL 402 credits |
| 3 | `cline/meta/muse-spark-1.1` | FAIL 402 credits |
| 4 | `cline/meta/muse-spark-1.3-contributor` | FAIL 402 credits |
| 5 | `cline/meta/muse-spark-1.2-contributor` | FAIL 402 credits |
| 6 | `auto/best-coding` | router (live) |

<a id="combosteady-coding"></a>
### combo/steady-coding - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `groq/openai/gpt-oss-120b` | OK |
| 2 | `gemini/gemini-3.8-flash` | FAIL 400 |
| 3 | `auto/best-coding` | router (live) |

<a id="combotrae-best"></a>
### combo/trae-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `trae/gpt-5.4` | FAIL 401 auth |
| 2 | `trae/gpt-5.2` | FAIL 401 auth |
| 3 | `auto/best-coding` | router (live) |

<a id="comboxkiro-best"></a>
### combo/xkiro-best - [back to list](#8-combo-catalog-live)


| # | Model | OK? |
|---|-------|-----|
| 1 | `xkiro/qwen/qwen3-coder-plus:free` | OK |
| 2 | `xkiro/mistralai/codestral-2508` | OK |
| 3 | `xkiro/mistralai/devstral-medium` | OK |
| 4 | `xkiro/qwen/qwen3-max:free` | OK |
| 5 | `xkiro/qwen/qwen3.8-max:free` | OK |
| 6 | `xkiro/qwen/qwen3.7-max:free` | OK |
| 7 | `xkiro/qwen/qwen3.6-max-preview:free` | OK |
| 8 | `xkiro/qwen/qwen3.5-plus:free` | OK |
| 9 | `xkiro/qwen/qwen3.7-plus:free` | OK |
| 10 | `xkiro/qwen/qwen3.6-27b:free` | OK |
| 11 | `xkiro/qwen/qwen-plus-2025-07-28:free` | OK |
| 12 | `xkiro/mistralai/mistral-large-2512` | OK |
| 13 | `xkiro/mistralai/mistral-medium-3.5` | OK |
| 14 | `xkiro/mistralai/mistral-small-2603` | OK |
| 15 | `xkiro/mistralai/ministral-14b` | OK |
| 16 | `xkiro/mistralai/ministral-8b` | OK |
| 17 | `xkiro/mistralai/ministral-3b` | OK |
| 18 | `xkiro/sensenova/sensenova-6.8-flash-lite` | OK |

