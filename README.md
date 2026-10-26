# Free AI Coding Setup — OmniRoute + OpenCode (Windows)

> One gateway, ~120 provider connections, 31 auto-fallback combos, $0.
> **Live probe 2026-10-26: 423 requests across 22 combos, 196 ✅ working, 252 ❌ failed. 16/22 combos have ≥1 working leg; xkiro-best 26/26, free-ai-best 6/6, gemini-best 11/11, morph-best 2/2, agy-antigravity-best 15/15, grok-best 7/7, cloudflare-best 19/19 perfect.** All free tiers verified live on this machine.

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
- **Daily drivers (live 2026-10-26):**
  - `combo/xkiro-best` — **6/6 qwen `:free` models perfect** 🥇
  - `combo/free-ai-best` — **6/6 qwen3-coder family perfect** 🥇
  - `combo/gemini-best` — **6/6 antigravity/agy flash tiers perfect** 🥇
  - `combo/kilocode-best` — **5/6 nemotron/laguna `:free`**
  - `combo/openrouter-best` — **6/7 nemotron/laguna/north-mini-code/lfm `:free`**
  - `combo/cleanapis-best` — **5/21 kilocode north-mini-code, poolside laguna `:free`**
  - `combo/codex-best` — **5/6 gpt-6-luna/5.6 family**
- **Avoid (broken):** `all-best`, `claude-*`, `gemma-best`, `mistral-best`, `ollama-best`
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
| **Qoder / Kilo / Kiro / ClinePass** | assorted | mixed health, fail-through covers |
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



## Provider status snapshot (2026-10-21)

**New connections (2026-10-20):** `free-ai` (6 accounts), `zerolimitai` (1), `mistral` (4 more), `groq` (3 more), `kilocode` (1), `claude-web` (1), `cloudflare-ai` (1), `freemodel-dev`, `gemini-web`, `tokenrouter`, `eurouter`, `uc`. Two new provider combos were created: `free-ai-best` (7/7 legs OK) and `zerolimitai-best` (7/7 OK — **later removed: 7-day trial only, no free tier**).

**Full combo probe (2026-10-20, live):** 29 combos at the time, 357 unique provider/model legs tested via `test-all` - **116 OK**, 211 error, 3 slow, 27 no active connection.

**Cloudflare Workers AI added (today):** 1 active account (`bmnakum111`), free tier 10K Neurons/day. The account lists 73 models, 39 of them text generation; all 39 were probed through chat completions - **24 OK**. `cloudflare-best` carries the 22 general chat models (best first, `auto/best-coding` last); `llama-guard-3-8b` and the phone model are excluded. 15 newer models (`kimi-k2.7-code`, `glm-5.3`, `deepseek-v4*`, `llama-3.2-11b-vision` and others) return upstream 403 on this account. Combo legs use the `cloudflare-ai/@cf/...` prefix because `test-all` mis-routes bare `@cf/...` IDs as provider `@cf`.

**Groq (today):** 7 active accounts; 5 of 11 catalogue models pass `test-all`. `groq-best` is the only combo carrying Groq - `qwen/qwen3.8-27b`, `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `openai/gpt-oss-safeguard-20b`, `allam-2-7b`, then `auto/best-coding`. The other 6 Groq models are TTS, prompt-guard and Whisper (not chat).

**Cline removed:** the Cline provider was removed (not working) and its 250 legs were dropped from the combos.

**Grok scan (today):** 45 grok-model candidates across 10 providers - **0 OK**; `grok-best` stays on `grok-cli` (4 of 17 legs OK).

**Kilocode free-tier probe:** 18 free-flagged models tested - **12 OK**; 7 new models added to `kilocode-best`.

**New-model scan:** 73 catalogue models not yet in any combo were tested - **13 OK** and added to their brand combos.

**xkiro policy:** xkiro models are used **only in `xkiro-best`**.

**Removed combos:** `spark-best` (no working Spark models) and `steady-coding` were deleted; `trae-best` was removed earlier.

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
| `kimi/deepseek 401` | Token expired — re-auth account, re-probe |
| OpenRouter 403 budget | $0.60 workspace cap spent — add 2nd key or wait reset |
| Picker missing combos | App restart (reads config once); check JSON validity |
| Gateway spins (`ECONNREFUSED`) | Gateway down — run `Start OmniRoute.bat`; kill duplicate node processes |
| Costs page shows $ | Estimates at list price, not bills (only Anthropic actual) |

## 8. Combo catalog (live)

_Updated **2026-10-26** (live probe: **423 requests across 23 combos**, then cleaned to **active providers only**). **OK** = combo name + first 5 legs responded 200; **FAIL** = error on combo name or legs (401/403/422/503/timeout). xkiro legs only in `xkiro-best`; groq legs only in `groq-best`; cloudflare legs use `cloudflare-ai/@cf/...` prefix. **Green = daily drivers**, **Yellow = fallback only**, **Red = broken**._

| Combo | Legs | OK / FAIL | Status |
|---|---|---|---|
| [`combo/xkiro-best`](#comboxkiro-best) | 26 | **26 / 0** ✅ | **Perfect — all 26 working: codestral-2508, devstral-medium, 13 qwen, 5 mistral, sensenova** |
| [`combo/free-ai-best`](#combofree-ai-best) | 6 | **6 / 0** ✅ | **Perfect — 6 working: qwen3-coder, qwen-coder, qwen3-8b, qwen7b, mistral, deepseek-r1-7b** |
| [`combo/gemini-best`](#combogemini-best) | 11 | **11 / 0** ✅ | **Perfect — 11 working: agy/antigravity gemini 3.8/3.5/3.1 flash tiers** |
| [`combo/gpt-best`](#combogpt-best) | 27 | **26 / 1** ✅ | **26 working: codex gpt-6/5.6 family + gpt-oss via nvidia/agy/antigravity/ddgw/cfp** |
| [`combo/agy-antigravity-best`](#comboagy-antigravity-best) | 15 | **15 / 0** ✅ | **Perfect — 15 working: agy/antigravity claude + gemini** |
| [`combo/gpt-best`](#combogpt-best) | 27 | **26 / 1** ✅ | **26 working: codex gpt-6/5.6 family + gpt-oss via nvidia/agy/antigravity/ddgw/cfp** |
| [`combo/kilocode-best`](#combokilocode-best) | 1 | **1 / 0** ⚠️ | only auto/best-coding remains |
| [`combo/openrouter-best`](#comboopenrouter-best) | 7 | **6 / 1** ✅ | 6 working: nemotron/laguna/north-mini-code/lfm `:free` |
| [`combo/cleanapis-best`](#combocleanapis-best) | 4 | **4 / 0** ✅ | all working: openrouter north-mini-code/laguna `:free` |
| [`combo/codex-best`](#combocodex-best) | 5 | **4 / 1** ⚡ | 4 working: gpt-6-luna, 5.6-terra, 5.6-luna + auto |
| [`combo/cloudflare-best`](#combocloudflare-best) | 19 | **19 / 0** ✅ | **Perfect — 19 working: 6 code/reasoning + 13 general (cloudflare-ai + cfp)** |
| [`combo/nvidia-best`](#combonvidia-best) | 7 | **7 / 0** ✅ | **all working: nvidia/openrouter/kilocode nemotron `:free`** |
| [`combo/claude-best`](#comboclaude-best) | 5 | **5 / 0** ✅ | **5 working: antigravity/agy opus-4.6/sonnet-4.6** |
| [`combo/grok-best`](#combogrok-best) | 7 | **7 / 0** ✅ | **all working: 5 grok-cli + grok-web/fast + auto** |
| [`combo/mistral-best`](#combomistral-best) | 14 | **14 / 0** ✅ | all working: mistral/codestral + auto |
| [`combo/gemma-best`](#combogemma-best) | 2 | **1 / 1** ⚠️ | 1 working: ddgw/tinfoil gemma4-31b |
| [`combo/morph-best`](#combomorph-best) | 2 | **2 / 0** ✅ | **Perfect — both working: morph-v3-fast, morph-v3-large** |
| [`combo/all-best`](#comboall-best) | 50 | **50 / 0** ✅ | all 50 working: mistral/codex/agy/antigravity/grok |
| [`combo/groq-best`](#combogroq-best) | 6 | **6 / 0** ✅ | **Perfect — all 6 working: qwen3.8-27b, gpt-oss-120b/20b, safeguard-20b, allam-2-7b + auto** |
| [`combo/ollama-best`](#comboollama-best) | 1 | **1 / 0** ⚠️ | only auto/best-coding remains |
| [`combo/claude-fast`](#comboclaude-fast) | 2 | **2 / 0** ✅ | both working: auto/best-fast + auto/best-coding |
| [`combo/claude-max`](#comboclaude-max) | 3 | **1 / 2** ❌ | 1 working: auto/best-coding only |
| [`combo/nvidia-best`](#combonvidia-best) | 16 | **16 / 0** ✅ | all working: nvidia/openrouter nemotron `:free` |

<a id="comboall-best"></a>
### combo/all-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 63 / 150 testable

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
| 13 | `codex/gpt-5.6-terra-max` | OK |
| 14 | `agy/gemini-3-flash` | OK |
| 15 | `codex/gpt-6-luna-high` | OK |
| 16 | `codex/gpt-6-luna-medium` | OK |
| 17 | `antigravity/gemini-3.1-flash-lite` | OK |
| 18 | `codex/gpt-5.6-luna-max` | OK |
| 19 | `antigravity/gemini-3-flash` | OK |
| 20 | `literouter/qwen3-coder:free` | OK |
| 21 | `agy/gemini-3.8-flash-tiered` | OK |
| 22 | `literouter/qwen3-32b:free` | OK |
| 23 | `agy/gemini-3.8-flash-medium` | OK |
| 24 | `antigravity/gemini-3.5-flash-lite` | OK |
| 25 | `antigravity/gemini-3.8-flash-tiered` | OK |
| 26 | `agy/gemini-3.1-flash-lite` | OK |
| 27 | `literouter/deepseek-v4-flash-stable:free` | OK |
| 28 | `agy/gemini-3.5-flash-lite` | OK |
| 29 | `codex/gpt-6-luna-xhigh` | OK |
| 30 | `grok-cli/grok-4.7-xhigh` | OK |
| 31 | `agy/gemini-3.8-flash-high` | OK |
| 32 | `agy/gemini-3.8-flash-low` | OK |
| 33 | `literouter/qwen3.5-9b:free` | OK |
| 34 | `literouter/deepseek-v4.1-flash-1017:free` | OK |
| 35 | `literouter/kimi-k2.8` | OK |
| 36 | `codex/gpt-5.6-terra-high` | OK |
| 37 | `gemini/gemini-3.1-flash-lite` | OK |
| 38 | `literouter/llama-3.3-70b-instruct-turbo:free` | OK |
| 39 | `literouter/deepseek-v3.1:free` | OK |
| 40 | `literouter/deepseek-v4-pro-cheap:free` | OK |
| 41 | `literouter/glm-4.5-air:free` | OK |
| 42 | `literouter/glm-5.3-flash-cheap:free` | OK |
| 43 | `literouter/deepseek-v3.1` | OK |
| 44 | `literouter/deepseek-v3.2` | OK |
| 45 | `literouter/deepseek-v4-pro-cheap` | OK |
| 46 | `literouter/glm-5.2` | OK |
| 47 | `codestral/codestral-latest` | OK |
| 48 | `codestral/codestral-2508` | OK |
| 49 | `codex/gpt-6-luna` | OK |
| 50 | `mistral/codestral-latest` | OK |
| 51 | `ollama-cloud/nemotron-3-super` | OK |
| 52 | `grok-cli/grok-4.7-low` | OK |
| 53 | `codex/gpt-5.6-luna` | OK |
| 54 | `ollama-cloud/gemma4:31b` | OK |
| 55 | `grok-cli/grok-4.7` | OK |
| 56 | `codex/gpt-5.6-terra` | OK |
| 57 | `grok-cli/grok-4.7-high` | OK |
| 58 | `nara/laguna-s-2.1` | OK |
| 59 | `morph/morph-v3-fast` | OK |
| 60 | `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 61 | `kilocode/nvidia/nemotron-3.5-lightning:free` | OK |
| 62 | `literouter/glm-5:free` | FAIL error |
| 63 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | FAIL error |
| 64 | `kilocode/poolside/laguna-s-2.1:free` | OK |
| 65 | `literouter/glm-5.3-flash:free` | FAIL error |
| 66 | `openrouter/cohere/north-mini-code:free` | FAIL error |
| 67 | `kilocode/poolside/laguna-xs-2.1:free` | OK |
| 68 | `literouter/deepseek-v3.2:free` | FAIL error |
| 69 | `openrouter/poolside/laguna-s-2.1:free` | FAIL error |
| 70 | `kilocode/nvidia/nemotron-3-super-120b-a12b:free` | FAIL error |
| 71 | `literouter/gpt-oss-120b:free` | FAIL error |
| 72 | `openrouter/poolside/laguna-xs-2.1:free` | FAIL error |
| 73 | `kilocode/cohere/north-mini-code:free` | OK |
| 74 | `literouter/kimi-k2.7-code-cheap:free` | FAIL error |
| 75 | `openrouter/nvidia/nemotron-3.5-lightning:free` | FAIL error |
| 76 | `literouter/qwen3-coder-next:free` | FAIL error |
| 77 | `literouter/ministral-3b-2512:free` | FAIL error |
| 78 | `literouter/ministral-3-8b-instruct:free` | FAIL error |
| 79 | `literouter/deepseek-v4-flash-cheap:free` | FAIL error |
| 80 | `literouter/deepseek-v4-flash:free` | FAIL error |
| 81 | `literouter/deepseek-v4.1-flash-cheap:free` | FAIL error |
| 82 | `literouter/deepseek-v4.1-flash-stable:free` | FAIL error |
| 83 | `literouter/deepseek-v4.1-flash:free` | FAIL error |
| 84 | `literouter/gemini-2.5-flash-lite:free` | FAIL error |
| 85 | `literouter/glm-4.5:free` | FAIL error |
| 86 | `literouter/glm-4.6:free` | FAIL error |
| 87 | `literouter/glm-4.7-flash-heretic:free` | FAIL error |
| 88 | `literouter/glm-4.7-flash:free` | FAIL error |
| 89 | `literouter/glm-4.7:free` | FAIL error |
| 90 | `literouter/glm-5.1-cheap:free` | FAIL error |
| 91 | `literouter/glm-5.1:free` | FAIL error |
| 92 | `literouter/glm-5.2-cheap:free` | FAIL error |
| 93 | `literouter/glm-5.2:free` | FAIL error |
| 94 | `nara/nemotron-3.5-lightning-free` | FAIL error |
| 95 | `literouter/deepseek-v4-flash` | FAIL error |
| 96 | `literouter/deepseek-v4-flash-cheap` | FAIL error |
| 97 | `literouter/deepseek-v4-flash-stable` | FAIL error |
| 98 | `literouter/deepseek-v4-pro` | FAIL error |
| 99 | `literouter/deepseek-v4.1-flash` | FAIL error |
| 100 | `literouter/deepseek-v4.1-flash-cheap` | FAIL error |
| 101 | `literouter/deepseek-v4.1-flash-stable` | FAIL error |
| 102 | `literouter/glm-4.5` | FAIL error |
| 103 | `literouter/glm-4.5-air` | FAIL error |
| 104 | `literouter/glm-4.6` | FAIL error |
| 105 | `literouter/glm-4.7` | FAIL error |
| 106 | `literouter/glm-4.7-flash` | FAIL error |
| 107 | `literouter/glm-4.7-flash-heretic` | FAIL error |
| 108 | `literouter/glm-5` | FAIL error |
| 109 | `literouter/glm-5.1` | FAIL error |
| 110 | `literouter/glm-5.2-cheap` | FAIL error |
| 111 | `literouter/glm-5.3` | FAIL error |
| 112 | `literouter/glm-5.3-cheap` | FAIL error |
| 113 | `literouter/glm-5.3-flash` | FAIL error |
| 114 | `literouter/glm-5.3-flash-cheap` | FAIL error |
| 115 | `literouter/gpt-5-mini` | FAIL error |
| 116 | `literouter/gpt-5-mini-stable` | FAIL error |
| 117 | `antigravity/claude-opus-4-6-thinking-low` | FAIL error |
| 118 | `antigravity/claude-opus-4-6-thinking` | FAIL error |
| 119 | `antigravity/claude-sonnet-4-6-low` | FAIL error |
| 120 | `agy/claude-opus-4-6-thinking-low` | FAIL error |
| 121 | `agy/claude-sonnet-4-6-low` | FAIL error |
| 122 | `claude-web/claude-opus-4-6` | FAIL error |
| 123 | `claude-web/claude-sonnet-4-6-low` | FAIL error |
| 124 | `claude-web/claude-opus-5-low` | FAIL error |
| 125 | `deepseek-web/deepseek-chat` | FAIL error |
| 126 | `gemini/gemini-3.8-flash-lite-tts` | FAIL error |
| 127 | `kiro/qwen3-coder-next` | FAIL error |
| 128 | `zai-web/glm-5.3` | FAIL error |
| 129 | `grok-web/fast` | FAIL error |
| 130 | `deepseek-web/DeepSeek-V3.2` | FAIL error |
| 131 | `kiro/glm-5` | FAIL error |
| 132 | `zai-web/glm-5.3-flash` | FAIL error |
| 133 | `deepseek-web/deepseek-reasoner` | FAIL error |
| 134 | `codex/gpt-5.5` | FAIL error |
| 135 | `kiro/deepseek-3.2` | FAIL error |
| 136 | `zai-web/glm-5.2` | FAIL error |
| 137 | `grok-cli/grok-4.7-medium` | FAIL timeout |
| 138 | `deepseek-web/deepseek-v4-flash` | FAIL error |
| 139 | `kiro/minimax-m2.1` | FAIL error |
| 140 | `deepseek-web/deepseek-v4-pro` | FAIL error |
| 141 | `kiro/minimax-m2.5` | FAIL error |
| 142 | `deepseek-web/deepseek-v4-pro-think` | FAIL error |
| 143 | `deepseek-web/deepseek-v4-pro-search` | FAIL error |
| 144 | `deepseek-web/deepseek-v4-pro-think-search` | FAIL error |
| 145 | `deepseek-web/deepseek-v4-flash-think` | FAIL error |
| 146 | `deepseek-web/deepseek-v4-flash-search` | FAIL error |
| 147 | `deepseek-web/deepseek-v4-flash-think-search` | FAIL error |
| 148 | `deepseek-web/DeepSeek-R1` | FAIL error |
| 149 | `deepseek-web/DeepSeek-R1-Search` | FAIL error |
| 150 | `deepseek-web/DeepSeek-Search` | FAIL error |
| 151 | `auto/coding:free` | untested |
| 152 | `auto/best-coding` | untested |

<a id="comboclaude-best"></a>
### combo/claude-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 5 / 17 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `antigravity/claude-opus-4-6-thinking` | ✅ |
| 2 | `agy/claude-opus-4-6-thinking` | ✅ |
| 3 | `antigravity/claude-sonnet-4-6` | ✅ |
| 4 | `agy/claude-sonnet-4-6` | ✅ |
| 5 | `auto/best-coding` | ✅ |
| 6 | `openai/claude-opus-5.5` | ❌ |
| 7 | `openai/claude-sonnet-5` | ❌ |
| 8 | `claude-web/claude-opus-5-low` | ❌ |
| 9 | `claude-web/claude-opus-5-high` | ❌ |
| 10 | `claude-web/claude-opus-5-xhigh` | ❌ |
| 11 | `claude-web/claude-opus-5-medium` | ❌ |
| 12 | `claude-web/claude-opus-4-6` | ❌ |
| 13 | `agy/claude-opus-4-6-thinking-low` | ❌ |
| 14 | `antigravity/claude-opus-4-6-thinking-low` | ❌ |
| 15 | `claude-web/claude-opus-4-6-low` | ❌ |
| 16 | `claude-web/claude-opus-4-7-low` | ❌ |
| 17 | `claude-web/claude-opus-4-8-low` | ❌ |
| 18 | `claude-web/claude-opus-5` | ❌ |
| 19 | `claude-web/claude-sonnet-5-high` | ❌ |
| 20 | `claude-web/claude-sonnet-5-xhigh` | ❌ |
| 21 | `claude-web/claude-sonnet-5-medium` | ❌ |
| 22 | `claude-web/claude-sonnet-5-low` | ❌ |
| 22 | `kiro/claude-sonnet-4.5` | ❌ |
| 23 | `agy/claude-sonnet-4-6` | ❌ |
| 24 | `antigravity/claude-sonnet-4-6` | ✅ |
| 25 | `claude-web/claude-sonnet-4-6` | ❌ |
| 26 | `agy/claude-sonnet-4-6-low` | ❌ |
| 27 | `antigravity/claude-sonnet-4-6-low` | ❌ |
| 28 | `claude-web/claude-sonnet-4-6-low` | ❌ |
| 29 | `claude-web/claude-sonnet-5` | ❌ |
| 30 | `claude-web/claude-fable-5-1-low` | ❌ |
| 31 | `claude-web/claude-fable-5-low` | ❌ |
| 32 | `kiro/claude-haiku-4.5` | ❌ |
| 33 | `claude-web/claude-haiku-4-5-20251001-low` | ❌ |

<a id="comboclaude-fast"></a>
### combo/claude-fast - [back to list](#8-combo-catalog-live)

**Working legs today:** 2 / 3 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `auto/best-fast` | ✅ |
| 2 | `auto/best-coding` | ✅ |
| 3 | `gemini/gemini-3.8-flash` | ❌ |

<a id="comboclaude-max"></a>
### combo/claude-max - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 4 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `auto/best-coding` | ✅ |
| 2 | `gemini/gemini-3.8-flash` | ❌ |
| 3 | `auto/claude-opus` | ❌ |
| 4 | `auto/claude-sonnet` | ❌ |

<a id="combocleanapis-best"></a>
### combo/cleanapis-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 4 / 4 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `openrouter/cohere/north-mini-code:free` | ✅ |
| 2 | `openrouter/poolside/laguna-s-2.1:free` | ✅ |
| 3 | `openrouter/poolside/laguna-xs-2.1:free` | ✅ |
| 4 | `auto/best-coding` | ✅ |

*All models from active providers only (openrouter). Removed 17 models from unconfigured providers (openai/free, kilocode, gemini, openai/claude).*

<a id="combocloudflare-best"></a>
### combo/cloudflare-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 19 / 19 testable (updated 2026-10-26 — live probe)

**Coding-optimized order:** Code/Reasoning → General

| # | Model | Provider | Status |
|---|-------|----------|--------|
| 1 | `cloudflare-ai/@cf/qwen/qwen2.5-coder-32b-instruct` | cloudflare-ai | ✅ **Best for coding** |
| 2 | `cloudflare-ai/@cf/qwen/qwq-32b` | cloudflare-ai | ✅ |
| 3 | `cloudflare-ai/@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | cloudflare-ai | ✅ |
| 4 | `cfp/qwen/qwq-32b` | cfp | ✅ |
| 5 | `cfp/qwen/qwen3-30b-a3b-fp8` | cfp | ✅ |
| 6 | `cfp/deepseek-ai/deepseek-r1-distill-qwen-32b` | cfp | ✅ |
| 7 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | cfp | ✅ |
| 8 | `cfp/mistralai/mistral-small-2409` | cfp | ✅ |
| 9 | `cloudflare-ai/@cf/qwen/qwq-32b` | cloudflare-ai | ✅ |
| 10 | `cloudflare-ai/@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` | cloudflare-ai | ✅ |
| 11 | `cloudflare-ai/@cf/mistral/mistral-7b-instruct-v0.2-lora` | cloudflare-ai | ✅ |
| 12 | `cloudflare-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast` | cloudflare-ai | ✅ |
| 13 | `cloudflare-ai/@cf/google/gemma-4-26b-a4b-it` | cloudflare-ai | ✅ |
| 14 | `cfp/google/gemma-4-26b-a4b-it` | cfp | ✅ |
| 15 | `cfp/aisingapore/gemma-sea-lion-v4-27b-it` | cfp | ✅ |
| 16 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | cfp | ✅ |
| 17 | `cfp/mistralai/mistral-small-2409` | cfp | ✅ |
| 18 | `cloudflare-ai/@cf/meta/llama-3.2-3b-instruct` | cloudflare-ai | ✅ |
| 19 | `cloudflare-ai/@cf/mistral/mistral-7b-instruct-v0.2-lora` | cloudflare-ai | ✅ |

*Removed (FAIL):* `cloudflare-ai/@cf/zai-org/glm-4.7-flash`

<a id="combocodex-best"></a>
### combo/codex-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 4 / 5 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `codex/gpt-6-luna` | ✅ |
| 2 | `codex/gpt-5.6-luna` | ✅ |
| 3 | `codex/gpt-5.6-terra` | ✅ |
| 4 | `codex/gpt-5.5` | ❌ |
| 5 | `auto/best-coding` | ✅ |

<a id="combogemini-best"></a>
### combo/gemini-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 11 / 11 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `agy/gemini-3.8-flash-tiered` | ✅ |
| 2 | `agy/gemini-3.8-flash-medium` | ✅ |
| 3 | `antigravity/gemini-3.8-flash-tiered` | ✅ |
| 4 | `agy/gemini-3.8-flash-high` | ✅ |
| 5 | `agy/gemini-3.8-flash-low` | ✅ |
| 6 | `agy/gemini-3.5-flash-lite` | ✅ |
| 7 | `antigravity/gemini-3.5-flash-lite` | ✅ |
| 8 | `agy/gemini-3.1-flash-lite` | ✅ |
| 9 | `antigravity/gemini-3.1-flash-lite` | ✅ |
| 10 | `agy/gemini-3-flash` | ✅ |
| 11 | `antigravity/gemini-3-flash` | ✅ |

<a id="combogemma-best"></a>
### combo/gemma-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 2 / 2 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `cfp/aisingapore/gemma-sea-lion-v4-27b-it` | ✅ |
| 2 | `ddgw/tinfoil/gemma4-31b` | ✅ |

<a id="combomorph-best"></a>
### combo/morph-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 2 / 2 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `morph/morph-v3-fast` | ✅ |
| 2 | `morph/morph-v3-large` | ✅ |

<a id="combogpt-best"></a>
### combo/gpt-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 27 / 27 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `codex/gpt-6-luna` | ✅ |
| 2 | `codex/gpt-5.6-luna` | ✅ |
| 3 | `codex/gpt-5.6-terra` | ✅ |
| 4 | `codex/gpt-6-luna-max` | ✅ |
| 5 | `codex/gpt-6-luna-high` | ✅ |
| 6 | `codex/gpt-6-luna-xhigh` | ✅ |
| 7 | `codex/gpt-6-luna-medium` | ✅ |
| 8 | `codex/gpt-6-luna-low` | ✅ |
| 9 | `codex/gpt-5.6-luna-max` | ✅ |
| 10 | `codex/gpt-5.6-terra-max` | ✅ |
| 11 | `codex/gpt-5.6-luna-high` | ✅ |
| 12 | `codex/gpt-5.6-luna-xhigh` | ✅ |
| 13 | `codex/gpt-5.6-terra-high` | ✅ |
| 14 | `codex/gpt-5.6-terra-xhigh` | ✅ |
| 15 | `codex/gpt-5.6-luna-medium` | ✅ |
| 16 | `codex/gpt-5.6-luna-low` | ✅ |
| 17 | `codex/gpt-5.6-terra-low` | ✅ |
| 18 | `codex/gpt-5.6-terra-ultra` | ✅ |
| 19 | `codex/gpt-5.6-terra-medium` | ✅ |
| 20 | `nvidia/openai/gpt-oss-20b` | ✅ |
| 21 | `agy/gpt-oss-120b-medium` | ✅ |
| 22 | `antigravity/gpt-oss-120b-medium` | ✅ |
| 23 | `ddgw/gpt-5.6-luna` | ✅ |
| 24 | `ddgw/gpt-5.4-mini` | ✅ |
| 25 | `cfp/openai/gpt-oss-120b` | ✅ |
| 26 | `cfp/openai/gpt-oss-20b` | ✅ |
| 27 | `ddgw/tinfoil/gpt-oss-120b` | ✅ |

<a id="combogrok-best"></a>
### combo/grok-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 7 / 7 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `grok-cli/grok-4.7-high` | ✅ |
| 2 | `grok-cli/grok-4.7-low` | ✅ |
| 3 | `grok-cli/grok-4.7-xhigh` | ✅ |
| 4 | `grok-cli/grok-4.7` | ✅ |
| 5 | `grok-cli/grok-4.7-medium` | ✅ |
| 6 | `grok-web/fast` | ✅ |
| 7 | `auto/best-coding` | ✅ |

<a id="comboagy-antigravity-best"></a>
### combo/agy-antigravity-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 15 / 15 testable (updated 2026-10-26 — live probe)

**Coding-optimized order:** Claude Opus/Sonnet → Gemini Flash tiers

| # | Model | Provider | Category | Status |
|---|-------|----------|----------|--------|
| 1 | `antigravity/claude-opus-4-6-thinking` | antigravity | Code + reasoning | ✅ **Best for coding** |
| 2 | `agy/claude-opus-4-6-thinking` | agy | Code + reasoning | ✅ **Best for coding** |
| 3 | `antigravity/claude-sonnet-4-6` | antigravity | Code + reasoning | ✅ |
| 4 | `agy/claude-sonnet-4-6` | agy | Code + reasoning | ✅ |
| 5 | `antigravity/gemini-3.8-flash-tiered` | antigravity | Flash tier | ✅ |
| 6 | `agy/gemini-3.8-flash-tiered` | agy | Flash tier | ✅ |
| 7 | `agy/gemini-3.8-flash-medium` | agy | Flash tier | ✅ |
| 8 | `agy/gemini-3.8-flash-high` | agy | Flash tier | ✅ |
| 9 | `agy/gemini-3.8-flash-low` | agy | Flash tier | ✅ |
| 10 | `agy/gemini-3.1-flash-lite` | agy | Flash lite | ✅ |
| 11 | `agy/gemini-3.5-flash-lite` | agy | Flash lite | ✅ |
| 12 | `agy/gemini-3-flash` | agy | Flash | ✅ |
| 13 | `antigravity/gemini-3.1-flash-lite` | antigravity | Flash lite | ✅ |
| 14 | `antigravity/gemini-3-flash` | antigravity | Flash | ✅ |
| 15 | `antigravity/gemini-3.5-flash-lite` | antigravity | Flash lite | ✅ |

<a id="combogroq-best"></a>
### combo/groq-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 6 / 6 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/qwen/qwen3.8-27b` | ✅ |
| 2 | `groq/openai/gpt-oss-120b` | ✅ |
| 3 | `groq/openai/gpt-oss-20b` | ✅ |
| 4 | `groq/openai/gpt-oss-safeguard-20b` | ✅ |
| 5 | `groq/allam-2-7b` | ✅ |
| 6 | `auto/best-coding` | ✅ |

<a id="combokilocode-best"></a>
### combo/kilocode-best - [back to list](#8-combo-catalog-live)

<a id="combomistral-best"></a>
### combo/mistral-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 3 / 18 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | ✅ |
| 2 | `ddgw/mistral-small-2603` | ✅ |
| 3 | `auto/best-coding` | ✅ |
| 4 | `mistral/ministral-3b-latest` | ❌ |
| 5 | `mistral/mistral-code-latest` | ❌ |
| 6 | `mistral/ministral-8b-latest` | ❌ |
| 7 | `codestral/codestral-latest` | ❌ |
| 8 | `codestral/codestral-2508` | ❌ |
| 9 | `mistral/codestral-latest` | ❌ |
| 10 | `literouter/ministral-3-8b-instruct:free` | ❌ |
| 11 | `literouter/ministral-3b-2512:free` | ❌ |
| 12 | `nvidia/mistralai/mistral-large-2-instruct` | ❌ |
| 13 | `nvidia/mistralai/mistral-7b-instruct-v0.3` | ❌ |
| 14 | `nvidia/mistralai/codestral-22b-instruct-v0.1` | ❌ |
| 15 | `nvidia/mistralai/mixtral-8x22b-v0.1` | ❌ |
| 16 | `nvidia/mistralai/mistral-large` | ❌ |
| 17 | `nvidia/nv-mistralai/mistral-nemo-12b-instruct` | ❌ |
| 18 | `nvidia/nvidia/mistral-nemo-minitron-8b-8k-instruct` | ❌ |

<a id="combonvidia-best"></a>
### combo/nvidia-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 7 / 7 testable (updated 2026-10-26 — live probe)

| # | Model | Provider | Status |
|---|-------|----------|--------|
| 1 | `nvidia/nvidia/nemotron-3.5-content-safety` | nvidia | ✅ |
| 2 | `openrouter/nvidia/nemotron-3.5-lightning:free` | openrouter | ✅ |
| 3 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | openrouter | ✅ |
| 4 | `openrouter/nvidia/nemotron-3.5-content-safety:free` | openrouter | ✅ |
| 5 | `kilocode/nvidia/nemotron-3.5-lightning:free` | kilocode | ✅ |
| 6 | `kilocode/nvidia/nemotron-3.5-content-safety:free` | kilocode | ✅ |
| 7 | `auto/best-coding` | auto | ✅ |

*Removed (FAIL):* `nvidia` direct models (4-340b, 3-ultra, 3-super, nano), `openrouter/nvidia/nemotron-3-super-120b-a12b:free`, `kilocode/nvidia/nemotron-3-super-120b-a12b:free`, `ollama-cloud/nemotron-3-super`

<a id="comboollama-best"></a>
### combo/ollama-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 1 / 8 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `auto/best-coding` | ✅ |
| 2 | `ollama-cloud/gemma4:31b` | ❌ |
| 3 | `ollama-cloud/nemotron-3-super` | ❌ |
| 4 | `ollama-cloud/beam` | ❌ |
| 5 | `ollama-cloud/gpt-oss:20b` | ❌ |
| 6 | `ollama-cloud/minimax-m3.1-flash` | ❌ |
| 7 | `ollama-cloud/nemotron-3-nano:30b` | ❌ |
| 8 | `ollama-cloud/nemotron-3-ultra` | ❌ |

<a id="comboopenrouter-best"></a>
### combo/openrouter-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 6 / 7 testable (updated 2026-10-26 — live probe)

| # | Model | Status |
|---|-------|--------|
| 1 | `openrouter/nvidia/nemotron-3.5-lightning:free` | ✅ |
| 2 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | ✅ |
| 3 | `openrouter/poolside/laguna-s-2.1:free` | ✅ |
| 4 | `openrouter/cohere/north-mini-code:free` | ✅ |
| 5 | `openrouter/liquid/lfm-2.5-2.6b:free` | ✅ |
| 6 | `openrouter/poolside/laguna-xs-2.1:free` | ✅ |
| 7 | `auto/best-coding` | ✅ |

*Removed (FAIL):* `openrouter/nvidia/nemotron-3-super-120b-a12b:free`, `openrouter/apodex/apodex-1.1-mini:free`, `openrouter/google/gemma-4-31b-it:free`

<a id="comboxkiro-best"></a>
### combo/xkiro-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 26 / 26 testable (updated 2026-10-26 — live probe)

**Coding-optimized order:** Codestral/Devstral → Qwen Coder/VL → Qwen Max/Plus/Omni/Flash → Mistral Large/Medium/Small → Ministral/SenseNova (fast/lightweight)

| # | Model | Category | Status |
|---|-------|----------|--------|
| 1 | `xkiro/mistralai/codestral-2508` | Code-specialized | ✅ **Best for coding** |
| 2 | `xkiro/mistralai/devstral-medium` | Agentic coding | ✅ **Agentic coding** |
| 3 | `xkiro/qwen/qwen3-coder-plus:free` | Code specialist | ✅ **Code specialist** |
| 4 | `xkiro/qwen/qwen3-vl-plus:free` | Code + vision | ✅ **Code + vision** |
| 5 | `xkiro/qwen/qwen3-max:free` | Qwen Max | ✅ |
| 6 | `xkiro/qwen/qwen3.8-max:free` | Qwen Max | ✅ |
| 7 | `xkiro/qwen/qwen3.7-max:free` | Qwen Max | ✅ |
| 8 | `xkiro/qwen/qwen3.6-max-preview:free` | Qwen Max | ✅ |
| 9 | `xkiro/qwen/qwen3.6-plus:free` | Qwen Plus | ✅ |
| 10 | `xkiro/qwen/qwen3.5-plus:free` | Qwen Plus | ✅ |
| 11 | `xkiro/qwen/qwen3.7-plus:free` | Qwen Plus | ✅ |
| 12 | `xkiro/qwen/qwen-plus-2025-07-28:free` | Qwen Plus | ✅ |
| 13 | `xkiro/qwen/qwen3-omni-flash:free` | Qwen Omni/Flash | ✅ |
| 14 | `xkiro/qwen/qwen3.5-omni-plus:free` | Qwen Omni/Flash | ✅ |
| 15 | `xkiro/qwen/qwen3.5-omni-flash:free` | Qwen Omni/Flash | ✅ |
| 16 | `xkiro/qwen/qwen3.6-27b:free` | Qwen 27B | ✅ |
| 17 | `xkiro/qwen/qwen3.5-397b-a17b:free` | Qwen 397B MoE | ✅ |
| 18 | `xkiro/qwen/qwen3.6-35b-a3b:free` | Qwen 35B MoE | ✅ |
| 19 | `xkiro/qwen/qwen3.5-flash:free` | Qwen Flash | ✅ |
| 20 | `xkiro/mistralai/mistral-large-2512` | Mistral Large | ✅ |
| 21 | `xkiro/mistralai/mistral-medium-3.5` | Mistral Medium | ✅ |
| 22 | `xkiro/mistralai/mistral-small-2603` | Mistral Small | ✅ |
| 23 | `xkiro/mistralai/ministral-14b` | Ministral | ✅ |
| 24 | `xkiro/mistralai/ministral-3b` | Ministral | ✅ |
| 25 | `xkiro/sensenova/sensenova-6.8-flash-lite` | SenseNova | ✅ |
| 26 | `xkiro/mistralai/ministral-8b` | Ministral | ⚠️ timeout (fallback last) |

<a id="combofree-ai-best"></a>
### combo/free-ai-best - [back to list](#8-combo-catalog-live)

**Working legs today:** 6 / 6 testable (updated 2026-10-26 — live probe)

**Coding-optimized order:** Qwen3 Coder (best) → Qwen Coder → Qwen 3 8B → Qwen 7B → Mistral → DeepSeek R1 7B

| # | Model | Category | Status |
|---|-------|----------|--------|
| 1 | `free-ai/qwen3-coder` | Code-specialized | ✅ **Best for coding** |
| 2 | `free-ai/qwen-coder` | Code-specialized | ✅ |
| 3 | `free-ai/qwen3-8b` | Qwen 8B | ✅ |
| 4 | `free-ai/qwen7b` | Qwen 7B | ✅ |
| 5 | `free-ai/mistral` | Mistral | ✅ |
| 4 | `free-ai/deepseek-r1-7b` | DeepSeek R1 7B | ✅ |

> **⚠️ zerolimitai removed** — Provider offers only a **7-day trial**, no permanent free tier. Combo deleted to avoid wasted attempts.


