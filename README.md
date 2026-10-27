# Free AI Coding Setup - OmniRoute + OpenCode (Windows)

> One local gateway at `127.0.0.1:20128`. 111 provider connections, 22 combos, $0 for everything
> used here. **Last verified 2026-10-27**: 2005 callable model ids, 64 probed one-shot
> (43 answered), 55 models sat the same coding quiz.
>
> **Best coding combo: `combo/coding-elite`** - 22 legs, ranked by the table in section 4.

---

## Contents

- [1. Install OmniRoute](#1-install-omniroute)
- [2. Connect OpenCode to OmniRoute](#2-connect-opencode-to-omniroute)
- [3. How to use (daily)](#3-how-to-use-daily)
- [4. Coding model ranking](#4-coding-model-ranking---best-first-2026-10-27)
- [5. Providers - what works](#5-providers---what-works)
- [6. Automation and files](#6-automation-and-files)
- [7. Troubleshooting](#7-troubleshooting)

**Separate files:** [full combo lists](docs/COMBOS.md) ·
[provider details + signup links](docs/PROVIDERS.md) ·
[all errors and fixes](docs/TROUBLESHOOTING.md) ·
[OpenCode free models — status, rank, limits](docs/OPENCODE-MODEL-STATUS-RANK.md)

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

- OpenCode model picker → provider **OmniRoute** → pick a `combo/*` (they sort to the top)
- **Start here for coding:** `combo/coding-elite` - 22 legs, ranked best-first (section 4). `priority` stops at the first leg that answers, so the order *is* the ranking.
- **Widest net:** `combo/all-best` - fails through everything that is still alive.
- **Clean brand combos today:** `gpt-best`, `codex-best`, `gemini-best`, `agy-antigravity-best`, `claude-best`, `grok-best`, `nvidia-best`, `mistral-best`, `cloudflare-best`, `groq-best`, `openrouter-best`, `morph-best`.
- **Free only:** `openrouter-best` / `cleanapis-best` (`:free` legs), or name one directly (`openrouter/poolside/laguna-s-2.1:free`, expires 2026-10-31).
- **Broken right now (kept for reference):** `xkiro-best` (all accounts suspended), `free-ai-best` (provider dead), `kilocode-best` / `ollama-best` (only `auto` leg left).
- **All 22 combos, leg by leg:** [docs/COMBOS.md](docs/COMBOS.md)
- Single models: `auto/*` routes fan out across all healthy providers.

Rules learned the hard way:
- **401/402/403-terminal kills a chain** — never put dead/paid legs early; interleave providers
- Attempt budget is 200/request (max) — big combos are safe
- Quotas fluctuate hourly — combos route around; single models may 429
- A `priority` combo stops at the first leg that answers — keep order equal to quality, never alphabetical

---

## 4. Coding model ranking - best first (2026-10-27)

Two numbers matter, and they measure different things:

- **Coding quiz** - the *same 4 tasks* went to every model on this list, one after another today:
  one tricky "what does this print", then `merge(intervals)`, `longest_inc(nums)` and the classic
  trapping-rain-water `trap(height)`, each written from scratch and graded by running it against
  real test cases. Score = average pass rate across the 4 tasks.
  **Read it as a gate, not a ranking:** 100 means "no excuses, it can code"; anything below ~90
  means it stumbled on a basic task.
- **30-day success** - how often that exact model actually answered on this box over the last
  30 days. A great model that times out is not a great model.

A model needs both. Sorted by coding quality first, then reliability.

| # | Model | Coding quiz | Why it ranks here | 30-day success |
|---|---|---|---|---|
| 1 | `larprouter/deepseek-v4.1-flash` | **100** | DeepSWE 74.2 / TB2.1 90.6 - strongest coding brain reachable; reasoning model, 1-5 s | 6/6 today |
| 2 | `codex/gpt-6-luna-high` | **100** | DeepSWE 66.6, best *reliable* agentic coder you own - 6.5k real requests of history | **98.6%** (6463) |
| 3 | `codex/gpt-6-luna-max` | **100** | same weights at max reasoning effort - deeper plans, same subscription | 88.9% (max) |
| 4 | `gc/grok-4.7-xhigh` | **100** | coding Elo 1638 = highest scored model that actually answers; 500k ctx | 85.9% (575) |
| 5 | `antigravity/claude-opus-4-6-thinking` | **100** | best Claude generation reachable; strongest on multi-file refactors + review | 63.2% (838) |
| 6 | `agy/claude-opus-4-6-thinking` | **100** | same model, second account pool - free redundancy | - |
| 7 | `larprouter/glm-5.3-flash` | **100** | GLM 5.3 flash on the free pool - DeepSWE 66.9 family, fast and stable | 5/5 today |
| 8 | `codex/gpt-5.6-luna-high` | **100** | previous-gen Luna, high effort - still a solid agent | - |
| 9 | `codex/gpt-5.6-terra-high` | **100** | Terra = code-heavy variant of 5.6 | - |
| 10 | `codex/gpt-reserve-high` | **100** | reserve capacity - keeps working when the main pool is throttled | - |
| 11 | `cx/gpt-6-luna` | **100** | medium effort, fastest Luna path | 98.6% |
| 12 | `codex/gpt-6-luna` | **100** | default effort | 98.6% |
| 13 | `grok-cli/grok-4.7` | **100** | independent transport of #3 | 85.9% |
| 14 | `gc/grok-4.7-high` | **100** | mid effort - cheaper on quota than xhigh | - |
| 15 | `openrouter/poolside/laguna-s-2.1:free` | **75** | TB2.1 70.2 / DeepSWE 40.4 - best free coding model for single-file work | 85.7% (21) |
| 16 | `openrouter/recursive/flint-v1.0:free` | **100** | SWE-bench Pro v2 89.7 / SWE-V 74.2 / TB2.1 54.9 - patch-quality specialist | 66.7% |
| 17 | `cfp/moonshotai/kimi-k2.7-code` | **75** | Kimi K2.7 **code** - 256k ctx on free CF quota | 36.8% (19) |
| 18 | `cfp/deepseek-ai/deepseek-v4-pro-0813` | **100** | DeepSeek V4 Pro weights, free CF quota | - |
| 19 | `cfp/zai-org/glm-5.2` | **100** | GLM 5.2 - strong tool use, free | - |
| 20 | `cfp/deepseek-ai/deepseek-v4-flash-0731` | **100** | V4 Flash - fast, free, good for small edits | - |
| 21 | `cfp/moonshotai/kimi-k2.6` | **75** | previous Kimi, still useful as a 2nd opinion | - |
| 22 | `openrouter/cohere/north-mini-code:free` | **100** | code-specialised, small, very consistent | 96.0% (25) |
| 23 | `openrouter/nvidia/nemotron-3.5-lightning:free` | 25 | fastest *reliable* free leg; grunt work | 97.4% (117) |
| 24 | `nvidia/nvidia/nemotron-3-ultra-550b-a55b` | **100** | TB2.1 ~51-56, huge context, no quota pressure | 60.9% (23) |
| 25 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | **100** | same weights, free quota | 72.0% (25) |
| 26 | `cfp/nvidia/nemotron-3-120b-a12b` | **100** | mid-size Nemotron, free | - |
| 27 | `antigravity/gemini-3.8-flash-high` | **100** | long-context Gemini for reading big repos; weaker at pure codegen | 88.0% (flash-low) |
| 28 | `codestral/codestral-latest` | **75** | Devstral/Codestral line - FIM + agent, 10 keys pooled | 89.1% (46) |
| 29 | `mistral/codestral-latest` | **75** | same model, second key pool | 81.8% (22) |
| 30 | `mistral/codestral-2508` / `codestral/codestral-2508` | **75** | pinned build, stable behaviour | 66.7-100% |
| 31 | `mistral/mistral-code-latest` / `mistral-code-fim-latest` | **75** | code-tuned + fill-in-the-middle | - |
| 32 | `nvidia/minimaxai/minimax-m3.1-flash` | **75** | long-context agent model, snappy | - |
| 33 | `cloudflare-ai/@cf/qwen/qwen2.5-coder-32b-instruct` | **75** | small coder, rock solid on CF | 100% (14) |
| 34 | `cfp/qwen/qwen2.5-coder-32b-instruct` | **92** | same model via playground | - |
| 35 | `cfp/qwen/qwq-32b` / `cloudflare-ai/@cf/qwen/qwq-32b` | 0 | reasoning model, free | - |
| 36 | `cfp/qwen/qwen3-30b-a3b-fp8` | 0 | MoE 30B, cheap bulk edits | - |
| 37 | `groq/qwen/qwen3.8-27b` | **100** | TB2.1 73.0 / SWE-Pro 61.7 / LCB 90.3 - great brain, throttled pipe | 22.3% (157) |
| 38 | `ddgw/gpt-5.6-luna` | **100** | free GPT-5.6 Luna via web bridge | - |
| 39 | `ddgw/gpt-5.4-mini` / `ddgw/claude-haiku-4-5` | **100** | cheap free legs, 429-prone | - |
| 40 | `openrouter/xingchen-agi/xing4.0-29b-a4b:free` | **100** | newest free MoE, 30B-class | - |
| 41 | `openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 50 | tiny reasoning model, free | - |
| 42 | `openrouter/poolside/laguna-xs-2.1:free` | 0 | small Laguna - fill-in work only | 47.8% (23) |

A dash means the model could not be quizzed today (rate limit, timeout, or paid route blocked).

**Also live, narrow use only:** `nvidia/nvidia/nemotron-3.5-lightning-30b-a3b` (3.4 s), `cfp/openai/gpt-oss-120b` (9.9 s), `cfp/meta/llama-4-scout-17b-16e-instruct` (8.2 s), `cfp/meta-llama/llama-3.3-70b-instruct-fp8-fast` (10.3 s), `cfp/mistralai/mistral-small-3.1-24b-instruct` (8.2 s), `cloudflare-ai/@cf/zai-org/glm-4.7-flash` (2.9 s), `cloudflare-ai/@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` (3.1 s), `cloudflare-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast` (2.6 s), `cloudflare-ai/@cf/google/gemma-4-26b-a4b-it` (3.1 s), `openrouter/liquid/lfm-2.5-2.6b:free` (2.8 s), `ddgw/mistral-small-2603` (2.7 s), `gw/fast` (Grok 4.20 web, 3.5 s), `nvidia/stepfun-ai/step-5-preview` (ok but 81 s), `morph/morph-v3-fast` + `morph-v3-large` (edit/apply model, not a chat brain).

### What to actually use

- **Agent coding default:** `combo/coding-elite` - 22 legs, same order as this list.
- **Watch the #1 leg:** `larprouter/deepseek-v4.1-flash` rides a free pool with limited credit - if it starts returning 402, the combo silently falls through to `codex/gpt-6-luna-high`.
- **Free only:** `openrouter/poolside/laguna-s-2.1:free` until **2026-10-31**, then
  `openrouter/recursive/flint-v1.0:free` + `cfp/moonshotai/kimi-k2.7-code`.
- **Blocked but worth unlocking** (GLM 5.3, Opus 5, Kimi K3, Grok 4.20 expert): see
  [Blocked models and the exact fix](docs/TROUBLESHOOTING.md#blocked-models-and-the-exact-fix).

## 5. Providers - what works

| Provider | Verified working models | State |
|---|---|---|
| **Codex (ChatGPT)** | `gpt-6-luna` (high/max), `gpt-5.6-luna`, `gpt-5.6-terra`, `gpt-reserve` | 98.6% success, 6.5k requests |
| **Grok CLI** | `grok-4.7` (high/xhigh) | 85.9% |
| **Antigravity + AGY** | `claude-opus-4-6-thinking`, `gemini-3.8-flash` | bills Anthropic (~$5.8 est.) |
| **OpenRouter** | every `:free` id - laguna, flint, north-mini-code, nemotron, gemma | paid routes blocked ($0.60 cap) |
| **Cloudflare (cfp + ai)** | kimi-k2.7-code, deepseek-v4-pro, glm-5.2, qwen-coder, qwq | free quota, 3-25 s |
| **Mistral / Codestral** | codestral-latest, codestral-2508, code-fim | 89% (codestral) |
| **NVIDIA NIM** | nemotron-3-ultra, minimax-m3.1-flash, lightning-30b | free, no quota pressure |
| **Groq** | qwen3.8-27b, gpt-oss-120b | fast, but 22% (rate limits) |
| **duckduckgo-web** | gpt-5.6-luna, gpt-5.4-mini, claude-haiku-4-5 | 429-prone |
| **larprouter** | `deepseek-v4.1-flash`, `glm-5.3-flash` | 6/6 stable, 1-9 s (other ids 400/402) |
| **Morph** | morph-v3-fast / large | edit engine, not a chat brain |
| **xKiro, free-ai, Devin, z.ai code, Augment** | - | dead or unconfigured today |

Full detail, signup links, costs and dead-provider reasons:
**[docs/PROVIDERS.md](docs/PROVIDERS.md)**

## 6. Automation and files (all in `%USERPROFILE%\.config\opencode\`)

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

### Files map

- Gateway data: `C:\Users\<you>\.omniroute\` (storage.sqlite, .env — **contains encryption key**)
- OpenCode: `%USERPROFILE%\.config\opencode\opencode.jsonc`, `%USERPROFILE%\.local\share\opencode\auth.json`
- This folder: guide PDFs, `BEST_50_MODELS.txt`, `FREE_CODING_MODELS.txt`, `setup-omniroute-windows.bat`, `omniroute-migration\` (full export + restore guide), `omniroute-providers.xlsx` (**contains plaintext keys — move to USB, delete here**)

---

## 7. Troubleshooting

| Symptom | Fix |
|---|---|
| Combo stops early with 403/401 | A dead leg sits early - probe legs, drop them, interleave providers |
| "Maximum combo attempts exceeded" | Bump `maxGlobalAttempts` (cap 200) |
| Picker missing combos | Restart the app; it reads config once. Check the JSON parses |
| Gateway spins / `ECONNREFUSED` | Start `Start OmniRoute.bat`; kill duplicate node processes |
| Costs page shows $ | Estimates at list price, not bills (only Anthropic is actual) |

Everything else - provider-specific errors, the 24 blocked models with their exact fix, and a
copy-paste probe snippet: **[docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)**

