# Troubleshooting

[Back to README](../README.md)

## Quick fixes

| Symptom | Cause -> fix |
|---|---|
| Combo 403/401 terminal, stops early | Dead leg first — probe legs, drop 401/402s, interleave providers |
| "Maximum combo attempts exceeded" | Budget hit — bump `maxGlobalAttempts` (cap 200) |
| `kimi/deepseek 401` | Token expired — re-auth account, re-probe |
| OpenRouter 403 budget | $0.60 workspace cap spent — add 2nd key or wait reset |
| Picker missing combos | App restart (reads config once); check JSON validity |
| Gateway spins (`ECONNREFUSED`) | Gateway down — run `Start OmniRoute.bat`; kill duplicate node processes |
| Costs page shows $ | Estimates at list price, not bills (only Anthropic actual) |
| `dva/*` 500 "DEVIN_AGENTIC_HOME must be an absolute path" | Set the env var to an absolute dir inside the bridge sandbox |
| `zc/*` 502 "spawn zcode ENOENT" | Install the `zcode` CLI |
| `aug/*` 502 "Auggie CLI not found" | Install `auggie` + `auggie login`, or set `AUGGIE_BIN` |
| `cxa/*` 503 "Codex app-server transport is not configured" | Fill in the app-server url/token |
| `free-ai/*` hangs ~100 s | Provider dead (6 conns) - drop it |
| `gw/expert`, `gw/heavy` 403 "SSO cookie may be expired" | Re-paste the Grok `sso` cookie |

## Blocked models and the exact fix

These would rank at or near the top - they are blocked by configuration, not by ability.

| Would-be rank | Model | Coding signal | Error today | Fix |
|---|---|---|---|---|
| 1 | `openrouter/anthropic/claude-opus-5.5-max` | coding Elo **1814** - top of the gateway leaderboard | 403 `Workspace lifetime budget of $0.60 exceeded ... does not reset` | new OpenRouter key/workspace (paid only) |
| 2 | `cxa/gpt-6-astra-max` | Elo **1788** | 503 `Codex app-server transport is not configured (missing url or token)` | configure the codex app-server transport |
| 3 | `dva/claude-sonnet-5-xhigh` | Elo **1773** | 500 `DEVIN_AGENTIC_HOME must be an absolute path inside the bridge sandbox` | set `DEVIN_AGENTIC_HOME` |
| 4 | `cxa/gpt-6.1-sol-max` | Elo **1757** | same as #2 | same as #2 |
| 5 | `dva/claude-fable-5-1-max` | Elo **1745** | same as #3 | same as #3 |
| 6 | `openrouter/anthropic/claude-sonnet-5.5-high` | Elo 1716 | 403 budget | OpenRouter budget |
| 7 | `dva/claude-opus-5-max` | Elo 1692 | devin bridge | `DEVIN_AGENTIC_HOME` |
| 8 | `cxa/gpt-6-sol-max` | Elo 1687 | codex app-server | transport config |
| 9 | `agy/gemini-4-argon-disabled` | Elo **1678** | id is literally `-disabled` on these accounts | needs Gemini account with Argon access |
| 11 | `free-ai/*` (501 synced ids, incl. `kimi-k3`) | Elo **1655** for Kimi K3 | every call hangs >100 s | provider dead - remove |
| 12 | `zc/glm-5.3` / `zc/glm-5.3-max` | GLM 5.3: DeepSWE 66.9 | 502 `spawn zcode ENOENT` | install the `zcode` CLI |
| 13 | `nvidia/z-ai/glm-5.3` / `glm-5.3-flash` | same weights | timeout >50 s | retry later |
| 14 | `aug/opus4.8`, `aug/gpt5.6-sol`, `aug/sonnet5-high`, `aug/fable-5` | Opus 4.8 / GPT-5.6 Sol | 502 `Auggie CLI not found: auggie` | install + `auggie login` |
| 15 | `dva/swe-1-7`, `dva/kimi-k3-max`, `dva/nemotron-3-ultra-high`, `dva/inkling-max` | SWE-1.7, Kimi K3, Nemotron Ultra, Inkling | devin bridge | `DEVIN_AGENTIC_HOME` |
| 16 | `openrouter/thinkingmachines/inkling:free` | TB2.1 63.8 | 403 `only available on agentic harnesses` | harness-only endpoint |
| 17 | `mistral/mistral-medium-3.5`, `mistral-vibe-cli-*`, `magistral-medium` | Mistral medium/vibe | timeout >50 s (only codestral line answers) | retry / drop |
| 18 | `gw/expert`, `gw/heavy` | Grok 4.20 expert/heavy | 403 `Grok auth failed - SSO cookie may be expired` | re-paste the `sso` cookie |
| 19 | `antigravity/claude-sonnet-4-6-high`, `-thinking` | Sonnet 4.6 | 400 `not available in the active live catalog` | catalog drift - use the plain id |
| 20 | `openrouter/google/gemma-4-*:free` | small | 429 all credentials cooling down | rate limited, retry |
| 21 | `larprouter/*` | - | 400 `not priced or available in this pool` | pool config |
| 22 | `unc/turboderp/Qwen3.8-27B-exl3` | local exl3 endpoint | 401 `public beta is closed` | needs API key |
| 23 | `nvidia/poolside/laguna-xs-2.1`, `nvidia/openai/gpt-oss-20b` | - | timeout >50 s | retry later |
| 24 | `openrouter/meta/muse-spark-1.3-max` | Elo 1656 | 403 budget (old `opencode` pool inactive) | OpenRouter budget / re-auth |

## Re-probe anything before trusting it

```powershell
$k = $env:OMNIROUTE_API_KEY
$b = @{ model = "codex/gpt-6-luna-high"; messages = @(@{ role = "user"; content = "Reply with exactly: OK" }); max_tokens = 16 } | ConvertTo-Json -Depth 5
(Invoke-WebRequest "http://localhost:20128/v1/chat/completions" -Method POST -Headers @{ Authorization = "Bearer $k" } -ContentType "application/json" -Body $b -UseBasicParsing).Content
```

Swap the `model` value for any id from the ranking table. A model that cannot answer this
line does not belong in a combo.
