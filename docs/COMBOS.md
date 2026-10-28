# Combos - full leg lists

[Back to README](../README.md)

Every OmniRoute combo on this machine, with each leg and its 30-day success rate.
A `priority` combo stops at the **first leg that answers**, so leg order is the ranking.

## Combo index

- [`combo/coding-elite`](#combocoding-elite)
- [`combo/claude-best`](#comboclaude-best)
- [`combo/cloudflare-best`](#combocloudflare-best)
- [`combo/codex-best`](#combocodex-best)
- [`combo/gemini-best`](#combogemini-best)
- [`combo/morph-best`](#combomorph-best)
- [`combo/gpt-best`](#combogpt-best)
- [`combo/grok-best`](#combogrok-best)
- [`combo/groq-best`](#combogroq-best)
- [`combo/agy-antigravity-best`](#comboagy-antigravity-best)
- [`combo/kilocode-best`](#combokilocode-best)
- [`combo/mistral-best`](#combomistral-best)
- [`combo/nvidia-best`](#combonvidia-best)
- [`combo/openrouter-best`](#comboopenrouter-best)
- [`combo/free-ai-best`](#combofree-ai-best)

---

| Combo | Legs | OK / FAIL | Status |
|---|---|---|---|
| [`combo/coding-elite`](#combocoding-elite) | 22 | **22 / 0** ✅ | **Best today — ranked legs: deepseek-v4.1-flash (larprouter) → gpt-6-luna-high/max → grok-4.7-xhigh → opus-4.6-thinking → free frontier (laguna, flint, north-mini-code, kimi-k2.7-code, deepseek-v4-pro, glm-5.2) → codestral** |
| [`combo/free-ai-best`](#combofree-ai-best) | 6 | **6 / 0** ✅ | **Perfect — 6 working: qwen3-coder, qwen-coder, qwen3-8b, qwen7b, mistral, deepseek-r1-7b** |
| [`combo/gemini-best`](#combogemini-best) | 11 | **11 / 0** ✅ | **Perfect — 11 working: agy/antigravity gemini 3.8/3.5/3.1 flash tiers** |
| [`combo/gpt-best`](#combogpt-best) | 27 | **26 / 1** ✅ | **26 working: codex gpt-6/5.6 family + gpt-oss via nvidia/agy/antigravity/ddgw/cfp** |
| [`combo/agy-antigravity-best`](#comboagy-antigravity-best) | 15 | **15 / 0** ✅ | **Perfect — 15 working: agy/antigravity claude + gemini** |
| [`combo/kilocode-best`](#combokilocode-best) | 13 | **13 / 0** ✅ | 12 working free legs ranked by coding + auto fallback: poolside/laguna-s → nemotron-3-ultra → cohere/north-mini-code → poolside/laguna-xs → nemotron-3.5-lightning → content-safety → super-vl → kilo-auto/small → openrouter/free → lfm-2.5 → dots-3-note → reflection/beam-free → auto/best-coding |
| [`combo/openrouter-best`](#comboopenrouter-best) | 7 | **6 / 1** ✅ | 6 working: nemotron/laguna/north-mini-code/lfm `:free` |
| [`combo/codex-best`](#combocodex-best) | 5 | **4 / 1** ⚡ | 4 working: gpt-6-luna, 5.6-terra, 5.6-luna + auto |
| [`combo/cloudflare-best`](#combocloudflare-best) | 19 | **19 / 0** ✅ | **Perfect — 19 working: 6 code/reasoning + 13 general (cloudflare-ai + cfp)** |
| [`combo/nvidia-best`](#combonvidia-best) | 7 | **7 / 0** ✅ | **all working: nvidia/openrouter/kilocode nemotron `:free`** |
| [`combo/claude-best`](#comboclaude-best) | 5 | **5 / 0** ✅ | **5 working: antigravity/agy opus-4.6/sonnet-4.6** |
| [`combo/grok-best`](#combogrok-best) | 7 | **7 / 0** ✅ | **all working: 5 grok-cli + grok-web/fast + auto** |
| [`combo/mistral-best`](#combomistral-best) | 14 | **14 / 0** ✅ | all working: mistral/codestral + auto |
| [`combo/morph-best`](#combomorph-best) | 2 | **2 / 0** ✅ | **Perfect — both working: morph-v3-fast, morph-v3-large** |

<a id="combocoding-elite"></a>
### combo/coding-elite

**Strategy** `priority` · **maxGlobalAttempts** 200 · 29 live legs · created 2026-10-27.
`priority` = it stops at the first leg that answers, so the order *is* the ranking: subscription agentic models first, free frontier second, small/fast last.

| # | Model | 30-day success |
|---|-------|----------------|
| 1 | `larprouter/deepseek-v4.1-flash` | 6/6 today |
| 2 | `codex/gpt-6-luna-high` | 98.6% |
| 3 | `codex/gpt-6-luna-max` | 88.9% |
| 4 | `gc/grok-4.7-xhigh` | 85.9% |
| 5 | `antigravity/claude-opus-4-6-thinking` | 63.2% |
| 6 | `agy/claude-opus-4-6-thinking` | - |
| 7 | `larprouter/glm-5.3-flash` | 5/5 today |
| 8 | `cx/gpt-6-luna` | 98.6% |
| 9 | `codex/gpt-6-luna` | 98.6% |
| 10 | `grok-cli/grok-4.7` | 85.9% |
| 11 | `openrouter/poolside/laguna-s-2.1:free` | 85.7% |
| 12 | `openrouter/recursive/flint-v1.0:free` | 66.7% |
| 13 | `openrouter/cohere/north-mini-code:free` | 96.0% |
| 14 | `cfp/moonshotai/kimi-k2.7-code` | 36.8% |
| 15 | `cfp/deepseek-ai/deepseek-v4-pro-0813` | - |
| 16 | `cfp/zai-org/glm-5.2` | - |
| 17 | `openrouter/nvidia/nemotron-3.5-lightning:free` | 97.4% |
| 18 | `nvidia/nvidia/nemotron-3-ultra-550b-a55b` | 60.9% |
| 19 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | 72.0% |
| 20 | `mistral/codestral-latest` | 81.8% |
| 21 | `groq/qwen/qwen3.8-27b` | 22.3% |
| 22 | `auto/best-coding` | - |

Registered in `opencode.jsonc` as `combo/coding-elite` and bare `coding-elite` (200k ctx / 32k out). Verified 2026-10-27: resolves to `codex/gpt-6-luna`, returns `tool_calls` correctly.

<a id="comboclaude-best"></a>
### combo/claude-best

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

<a id="combocloudflare-best"></a>
### combo/cloudflare-best

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
### combo/codex-best

| # | Model | Status |
|---|-------|--------|
| 1 | `codex/gpt-6-luna` | ✅ |
| 2 | `codex/gpt-5.6-luna` | ✅ |
| 3 | `codex/gpt-5.6-terra` | ✅ |
| 4 | `codex/gpt-5.5` | ❌ |
| 5 | `auto/best-coding` | ✅ |

<a id="combogemini-best"></a>
### combo/gemini-best

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

<a id="combomorph-best"></a>
### combo/morph-best

| # | Model | Status |
|---|-------|--------|
| 1 | `morph/morph-v3-fast` | ✅ |
| 2 | `morph/morph-v3-large` | ✅ |

<a id="combogpt-best"></a>
### combo/gpt-best

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
### combo/grok-best

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
### combo/agy-antigravity-best

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

<a id="combokilocode-best"></a>
### combo/kilocode-best

**Strategy** `priority` · **maxGlobalAttempts** 200 · 13 live legs · created 2026-10-28.
Sorted by coding quality: poolside laguna code models first, then the large nemotron reasoners, then small/free fallbacks, ending with `auto/best-coding`.

| # | Model | Provider | Status |
|---|-------|----------|--------|
| 1 | `kilocode/poolside/laguna-s-2.1:free` | kilocode | ✅ 🏆 |
| 2 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | kilocode | ✅ |
| 3 | `kilocode/cohere/north-mini-code:free` | kilocode | ✅ |
| 4 | `kilocode/poolside/laguna-xs-2.1:free` | kilocode | ✅ |
| 5 | `kilocode/nvidia/nemotron-3.5-lightning:free` | kilocode | ✅ |
| 6 | `kilocode/nvidia/nemotron-3.5-content-safety:free` | kilocode | ✅ |
| 7 | `kilocode/nvidia/nemotron-3.5-super-vl:free` | kilocode | ✅ |
| 8 | `kilocode/kilo-auto/small` | kilocode | ✅ |
| 9 | `kilocode/openrouter/free` | kilocode | ✅ |
| 10 | `kilocode/liquid/lfm-2.5-2.6b:free` | kilocode | ✅ |
| 11 | `kilocode/dots-studio/dots-3-note-preview:free` | kilocode | ✅ |
| 12 | `kilocode/reflection/beam-free` | kilocode | ✅ |
| 13 | `auto/best-coding` | auto | ✅ fallback |

Registered in `opencode.jsonc` as `combo/kilocode-best` (available in the OpenCode picker). Verified 2026-10-28: resolves to `kilocode/poolside/laguna-s-2.1:free`, returns text correctly.

<a id="combomistral-best"></a>
### combo/mistral-best

**Strategy** `priority` · **maxGlobalAttempts** 200 · 12 live legs · created 2026-10-27.
Sorted by coding quality: codestral first (larger/agent-friendly), then mistral-code, then ministral by size.

| # | Model | Provider | Status |
|---|-------|----------|--------|
| 1 | `codestral/codestral-latest` | codestral | ✅ |
| 2 | `codestral/codestral-2508` | codestral | ✅ |
| 3 | `mistral/codestral-latest` | mistral | ✅ |
| 4 | `mistral/codestral-2508` | mistral | ✅ |
| 5 | `mistral/mistral-code-latest` | mistral | ✅ |
| 6 | `mistral/mistral-code-fim-latest` | mistral | ✅ |
| 7 | `mistral/ministral-14b-latest` | mistral | ✅ |
| 8 | `mistral/ministral-8b-latest` | mistral | ✅ |
| 9 | `mistral/ministral-3b-latest` | mistral | ✅ |
| 10 | `mistral/ministral-3b-2512` | mistral | ✅ |
| 11 | `mistral/ministral-8b-2512` | mistral | ✅ |
| 12 | `mistral/ministral-14b-2512` | mistral | ✅ |

<a id="combonvidia-best"></a>
### combo/nvidia-best

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

<a id="comboopenrouter-best"></a>
### combo/openrouter-best

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

<a id="combogroq-best"></a>
### combo/groq-best

**Strategy** `priority` · 6 live legs · sorted by coding quality.

| # | Model | Status |
|---|-------|--------|
| 1 | `groq/openai/gpt-oss-120b` | ✅ |
| 2 | `groq/qwen/qwen3.8-27b` | ✅ |
| 3 | `groq/openai/gpt-oss-20b` | ✅ |
| 4 | `groq/openai/gpt-oss-safeguard-20b` | ✅ |
| 5 | `groq/allam-2-7b` | ✅ |
| 6 | `auto/best-coding` | ✅ |

<a id="combofree-ai-best"></a>
### combo/free-ai-best

| # | Model | Category | Status |
|---|-------|----------|--------|
| 1 | `free-ai/qwen3-coder` | Code-specialized | ✅ **Best for coding** |
| 2 | `free-ai/qwen-coder` | Code-specialized | ✅ |
| 3 | `free-ai/qwen3-8b` | Qwen 8B | ✅ |
| 4 | `free-ai/qwen7b` | Qwen 7B | ✅ |
| 5 | `free-ai/mistral` | Mistral | ✅ |
| 6 | `free-ai/deepseek-r1-7b` | DeepSeek R1 7B | ✅ |

> **⚠️ zerolimitai removed** — Provider offers only a **7-day trial**, no permanent free tier. Combo deleted to avoid wasted attempts.

