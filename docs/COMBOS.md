# Combos - full leg lists

[Back to README](../README.md)

Every OmniRoute combo on this machine, with each leg and its 30-day success rate.
A `priority` combo stops at the **first leg that answers**, so leg order is the ranking.

> **Updated 2026-11-05:** Auto-generated from live OmniRoute catalog.

## Combo index

- [`combo/agy-antigravity-best`](#comboagy-antigravity-best)
- [`combo/claude-best`](#comboclaude-best)
- [`combo/cloudflare-best`](#combocloudflare-best)
- [`combo/codex-best`](#combocodex-best)
- [`combo/coding-elite`](#combocoding-elite)
- [`combo/free-ai-best`](#combofree-ai-best)
- [`combo/gemini-best`](#combogemini-best)
- [`combo/gemini-web-best`](#combogemini-web-best)
- [`combo/gpt-best`](#combogpt-best)
- [`combo/grok-best`](#combogrok-best)
- [`combo/groq-best`](#combogroq-best)
- [`combo/inceptionai-best`](#comboinceptionai-best)
- [`combo/kilocode-best`](#combokilocode-best)
- [`combo/mistral-best`](#combomistral-best)
- [`combo/morph-best`](#combomorph-best)
- [`combo/nvidia-best`](#combonvidia-best)
- [`combo/ollama-cloud-best`](#comboollama-cloud-best)
- [`combo/openrouter-best`](#comboopenrouter-best)
- [`combo/orcarouter-best`](#comboorcarouter-best)

---

| Combo | Legs | Working | Failed | Status |
|---|---:|---:|---:|---|
| `combo/agy-antigravity-best` | 15 | 15 | 0 | [OK] |
| `combo/claude-best` | 5 | 4 | 1 | [WARN] |
| `combo/cloudflare-best` | 15 | 12 | 3 | [WARN] |
| `combo/codex-best` | 30 | 15 | 15 | [WARN] |
| `combo/coding-elite` | 56 | 45 | 11 | [WARN] |
| `combo/free-ai-best` | 7 | 5 | 2 | [WARN] |
| `combo/gemini-best` | 11 | 11 | 0 | [OK] |
| `combo/gemini-web-best` | 3 | 0 | 3 | [FAIL] |
| `combo/gpt-best` | 27 | 12 | 15 | [WARN] |
| `combo/grok-best` | 7 | 6 | 1 | [WARN] |
| `combo/groq-best` | 6 | 2 | 4 | [WARN] |
| `combo/inceptionai-best` | 1 | 0 | 1 | [FAIL] |
| `combo/kilocode-best` | 11 | 2 | 9 | [WARN] |
| `combo/mistral-best` | 12 | 12 | 0 | [OK] |
| `combo/morph-best` | 2 | 0 | 2 | [FAIL] |
| `combo/nvidia-best` | 7 | 1 | 6 | [WARN] |
| `combo/ollama-cloud-best` | 4 | 1 | 3 | [WARN] |
| `combo/openrouter-best` | 11 | 3 | 8 | [WARN] |
| `combo/orcarouter-best` | 4 | 0 | 4 | [FAIL] |

<a id="comboagy-antigravity-best"></a>
### combo/agy-antigravity-best

AGY + Antigravity Claude and Gemini

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `antigravity/claude-opus-4-6-thinking` | [OK] | 3687ms |
| 2 | `agy/claude-opus-4-6-thinking` | [OK] | 74ms |
| 3 | `antigravity/claude-sonnet-4-6` | [OK] | 43ms |
| 4 | `agy/claude-sonnet-4-6` | [OK] | 2437ms |
| 5 | `antigravity/gemini-3.8-flash-tiered` | [OK] | 3480ms |
| 6 | `agy/gemini-3.8-flash-tiered` | [OK] | 106ms |
| 7 | `agy/gemini-3.8-flash-medium` | [OK] | 2721ms |
| 8 | `agy/gemini-3.8-flash-high` | [OK] | 22ms |
| 9 | `agy/gemini-3.8-flash-low` | [OK] | 2776ms |
| 10 | `agy/gemini-3.1-flash-lite` | [OK] | 34ms |
| 11 | `agy/gemini-3.5-flash-lite` | [OK] | 3531ms |
| 12 | `agy/gemini-3-flash` | [OK] | 1298ms |
| 13 | `antigravity/gemini-3.1-flash-lite` | [OK] | 1582ms |
| 14 | `antigravity/gemini-3-flash` | [OK] | 2266ms |
| 15 | `antigravity/gemini-3.5-flash-lite` | [OK] | 81ms |

<a id="comboclaude-best"></a>
### combo/claude-best

Best Claude models via antigravity and agy

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `antigravity/claude-opus-4-6-thinking` | [OK] | 3687ms |
| 2 | `agy/claude-opus-4-6-thinking` | [OK] | 74ms |
| 3 | `antigravity/claude-sonnet-4-6` | [OK] | 43ms |
| 4 | `agy/claude-sonnet-4-6` | [OK] | 2437ms |
| 5 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="combocloudflare-best"></a>
### combo/cloudflare-best

Cloudflare Workers AI + CFP models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `cloudflare-ai/@cf/qwen/qwen2.5-coder-32b-instruct` | [OK] | 482ms |
| 2 | `cloudflare-ai/@cf/qwen/qwq-32b` | [OK] | 841ms |
| 3 | ~~`cloudflare-ai/@cf/deepseek-ai/deepseek-r1-distill-qwen-32b`~~ | [FAIL] - Empty response | 1091ms |
| 4 | `cfp/qwen/qwq-32b` | [OK] | 14643ms |
| 5 | `cfp/qwen/qwen3-30b-a3b-fp8` | [OK] | 14912ms |
| 6 | ~~`cfp/deepseek-ai/deepseek-r1-distill-qwen-32b`~~ | [FAIL] - Empty response | 16230ms |
| 7 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | [OK] | 18881ms |
| 8 | `cloudflare-ai/@cf/mistral/mistral-7b-instruct-v0.2-lora` | [OK] | 1219ms |
| 9 | `cloudflare-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast` | [OK] | 970ms |
| 10 | ~~`cloudflare-ai/@cf/google/gemma-4-26b-a4b-it`~~ | [FAIL] - Empty response | 3101ms |
| 11 | `cfp/google/gemma-4-26b-a4b-it` | [OK] | 12315ms |
| 12 | `cfp/aisingapore/gemma-sea-lion-v4-27b-it` | [OK] | 9145ms |
| 13 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | [OK] | 18881ms |
| 14 | `cloudflare-ai/@cf/meta/llama-3.2-3b-instruct` | [OK] | 1280ms |
| 15 | `cloudflare-ai/@cf/mistral/mistral-7b-instruct-v0.2-lora` | [OK] | 1219ms |

<a id="combocodex-best"></a>
### combo/codex-best

Codex GPT models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `codex/gpt-6-luna-max` | [OK] | 1795ms |
| 2 | `codex/gpt-6-luna-xhigh` | [OK] | 3340ms |
| 3 | `codex/gpt-6-luna-high` | [OK] | 4323ms |
| 4 | `codex/gpt-6-luna` | [OK] | 1620ms |
| 5 | `codex/gpt-6-luna-medium` | [OK] | 1388ms |
| 6 | `codex/gpt-6-luna-low` | [OK] | 3239ms |
| 7 | ~~`codex/gpt-5.6-terra-max`~~ | [FAIL] | - |
| 8 | ~~`codex/gpt-5.6-terra-xhigh`~~ | [FAIL] | - |
| 9 | ~~`codex/gpt-5.6-terra-high`~~ | [FAIL] | - |
| 10 | `codex/gpt-5.6-terra` | [OK] | 1287ms |
| 11 | ~~`codex/gpt-5.6-terra-medium`~~ | [FAIL] | - |
| 12 | ~~`codex/gpt-5.6-terra-low`~~ | [FAIL] | - |
| 13 | ~~`codex/gpt-5.6-luna-max`~~ | [FAIL] | - |
| 14 | ~~`codex/gpt-5.6-luna-xhigh`~~ | [FAIL] | - |
| 15 | ~~`codex/gpt-5.6-luna-high`~~ | [FAIL] | - |
| 16 | `codex/gpt-5.6-luna` | [OK] | 39ms |
| 17 | ~~`codex/gpt-5.6-luna-medium`~~ | [FAIL] | - |
| 18 | ~~`codex/gpt-5.6-luna-low`~~ | [FAIL] | - |
| 19 | `codex/gpt-reserve-max` | [OK] | 2370ms |
| 20 | `codex/gpt-reserve-xhigh` | [OK] | 1254ms |
| 21 | `codex/gpt-reserve-high` | [OK] | 1410ms |
| 22 | `codex/gpt-reserve` | [OK] | 1631ms |
| 23 | `codex/gpt-reserve-medium` | [OK] | 1200ms |
| 24 | `codex/gpt-reserve-low` | [OK] | 1482ms |
| 25 | ~~`codex/codex-auto-review-max`~~ | [FAIL] | - |
| 26 | ~~`codex/codex-auto-review-xhigh`~~ | [FAIL] | - |
| 27 | ~~`codex/codex-auto-review-high`~~ | [FAIL] | - |
| 28 | `codex/codex-auto-review` | [OK] | 1298ms |
| 29 | ~~`codex/codex-auto-review-medium`~~ | [FAIL] | - |
| 30 | ~~`codex/codex-auto-review-low`~~ | [FAIL] | - |

<a id="combocoding-elite"></a>
### combo/coding-elite

Daily driver - best coding models ranked by quality

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `codestral/codestral-latest` | [OK] | 19ms |
| 2 | `mistral/mistral-code-fim-latest` | [OK] | 720ms |
| 3 | `codestral/codestral-2508` | [OK] | 820ms |
| 4 | `mistral/codestral-2508` | [OK] | 17ms |
| 5 | `mistral/codestral-latest` | [OK] | 443ms |
| 6 | `cloudflare-ai/@cf/qwen/qwen2.5-coder-32b-instruct` | [OK] | 482ms |
| 7 | `mistral/mistral-code-latest` | [OK] | 1457ms |
| 8 | `free-ai/qwen3-coder` | [OK] | 1267ms |
| 9 | `free-ai/qwen-coder` | [OK] | 1959ms |
| 10 | `codex/gpt-6-luna` | [OK] | 1620ms |
| 11 | `antigravity/claude-opus-4-6-thinking` | [OK] | 3687ms |
| 12 | `agy/claude-opus-4-6-thinking` | [OK] | 74ms |
| 13 | `antigravity/claude-sonnet-4-6` | [OK] | 43ms |
| 14 | `agy/claude-sonnet-4-6` | [OK] | 2437ms |
| 15 | `codex/gpt-reserve` | [OK] | 1631ms |
| 16 | `codex/gpt-5.6-terra` | [OK] | 1287ms |
| 17 | `codex/gpt-5.6-luna` | [OK] | 39ms |
| 18 | `openadapter/GPT-6-Luna` | [OK] | 8189ms |
| 19 | `grok-cli/grok-4.7-xhigh` | [OK] | 5726ms |
| 20 | ~~`openadapter/0G-DeepSeek-v4-Flash`~~ | [FAIL] - Empty response | 8094ms |
| 21 | ~~`openadapter/DeepSeek-V4.1-Flash`~~ | [FAIL] - Empty response | 9094ms |
| 22 | ~~`openadapter/DeepSeek-V4-Flash`~~ | [FAIL] - Empty response | 2374ms |
| 23 | ~~`openadapter/0G-DeepSeek-V3`~~ | [FAIL] - HTTP 503: {"error":{"message":"[openadapter/0G-DeepSeek-V3]  | 25192ms |
| 24 | `openadapter/Qwen3.8-27B` | [OK] | 7844ms |
| 25 | ~~`openadapter/Kimi-K2-Think`~~ | [FAIL] | - |
| 26 | ~~`openadapter/GLM-5.3-Flash`~~ | [FAIL] - Empty response | 2878ms |
| 27 | ~~`openadapter/GLM-4.7-Flash`~~ | [FAIL] - HTTP 503: {"error":{"message":"[openadapter/GLM-4.7-Flash] [ | 24395ms |
| 28 | ~~`openadapter/MiMo-V2.6-Pro`~~ | [FAIL] - Empty response | 6011ms |
| 29 | `openadapter/MiMo-V2.6-Flash` | [OK] | 7560ms |
| 30 | `openadapter/gpt-oss-120b` | [OK] | 1677ms |
| 31 | `openadapter/Llama-3.1-405B` | [OK] | 2234ms |
| 32 | `antigravity/gemini-3.8-flash-tiered` | [OK] | 3480ms |
| 33 | `antigravity/gemini-3.8-flash-medium` | [OK] | 22ms |
| 34 | `antigravity/gemini-3.8-flash-high` | [OK] | 4611ms |
| 35 | `agy/gemini-3.8-flash-tiered` | [OK] | 106ms |
| 36 | `agy/gemini-3.8-flash-medium` | [OK] | 2721ms |
| 37 | `agy/gemini-3.8-flash-high` | [OK] | 22ms |
| 38 | `antigravity/gemini-3.5-flash-lite` | [OK] | 81ms |
| 39 | `agy/gemini-3.5-flash-lite` | [OK] | 3531ms |
| 40 | `antigravity/gemini-3.1-flash-lite` | [OK] | 1582ms |
| 41 | `agy/gemini-3.1-flash-lite` | [OK] | 34ms |
| 42 | `codex/codex-auto-review` | [OK] | 1298ms |
| 43 | `nvidia/poolside/laguna-xs-2.1` | [OK] | 611ms |
| 44 | `mistral/ministral-14b-latest` | [OK] | 524ms |
| 45 | `openadapter/MiMo-V2.5-Pro` | [OK] | 4411ms |
| 46 | ~~`mistral/mistral-large-4`~~ | [FAIL] - HTTP 400: {"object":"error","message":"top_p must be 1 when  | 1565ms |
| 47 | `cloudflare-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast` | [OK] | 970ms |
| 48 | `cloudflare-ai/@cf/qwen/qwq-32b` | [OK] | 841ms |
| 49 | `antigravity/gemini-3-flash` | [OK] | 2266ms |
| 50 | `ollama-cloud/gemma4:31b` | [OK] | 725ms |
| 51 | `openadapter/Gemma-4-31B-TEE` | [OK] | 3609ms |
| 52 | `openadapter/Hermes-4-14B` | [OK] | 1544ms |
| 53 | ~~`openadapter/gemma-4-31b-it`~~ | [FAIL] - HTTP 503: {"error":{"message":"[openadapter/gemma-4-31b-it]  | 22880ms |
| 54 | `mistral/ministral-8b-latest` | [OK] | 863ms |
| 55 | ~~`openadapter/Gemma-3-27B`~~ | [FAIL] - HTTP 503: {"error":{"message":"[openadapter/Gemma-3-27B] [50 | 20906ms |
| 56 | `free-ai/mistral` | [OK] | 1052ms |

<a id="combofree-ai-best"></a>
### combo/free-ai-best

Completely free models across multiple providers

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `free-ai/qwen3-coder` | [OK] | 1267ms |
| 2 | `free-ai/qwen-coder` | [OK] | 1959ms |
| 3 | ~~`free-ai/deepseek-r1`~~ | [FAIL] - Empty response | 1117ms |
| 4 | `free-ai/mistral` | [OK] | 1052ms |
| 5 | `free-ai/qwen3-8b` | [OK] | 1137ms |
| 6 | `free-ai/qwen7b` | [OK] | 901ms |
| 7 | ~~`free-ai/deepseek-r1-7b`~~ | [FAIL] - Empty response | 2265ms |

<a id="combogemini-best"></a>
### combo/gemini-best

Best Gemini models via antigravity and agy

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `agy/gemini-3.8-flash-tiered` | [OK] | 106ms |
| 2 | `agy/gemini-3.8-flash-medium` | [OK] | 2721ms |
| 3 | `antigravity/gemini-3.8-flash-tiered` | [OK] | 3480ms |
| 4 | `agy/gemini-3.8-flash-high` | [OK] | 22ms |
| 5 | `agy/gemini-3.8-flash-low` | [OK] | 2776ms |
| 6 | `agy/gemini-3.5-flash-lite` | [OK] | 3531ms |
| 7 | `antigravity/gemini-3.5-flash-lite` | [OK] | 81ms |
| 8 | `agy/gemini-3.1-flash-lite` | [OK] | 34ms |
| 9 | `antigravity/gemini-3.1-flash-lite` | [OK] | 1582ms |
| 10 | `agy/gemini-3-flash` | [OK] | 1298ms |
| 11 | `antigravity/gemini-3-flash` | [OK] | 2266ms |

<a id="combogemini-web-best"></a>
### combo/gemini-web-best

Gemini Web free models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`gemini-web/gemini-3.7-flash`~~ | [FAIL] | - |
| 2 | ~~`gemini-web/gemini-3.1-pro`~~ | [FAIL] | - |
| 3 | ~~`gemini-web/gemini-3.1-flash-lite`~~ | [FAIL] | - |

<a id="combogpt-best"></a>
### combo/gpt-best

GPT models via CX + Codex

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `codex/gpt-6-luna` | [OK] | 1620ms |
| 2 | `codex/gpt-5.6-luna` | [OK] | 39ms |
| 3 | `codex/gpt-5.6-terra` | [OK] | 1287ms |
| 4 | `codex/gpt-6-luna-max` | [OK] | 1795ms |
| 5 | `codex/gpt-6-luna-high` | [OK] | 4323ms |
| 6 | `codex/gpt-6-luna-xhigh` | [OK] | 3340ms |
| 7 | `codex/gpt-6-luna-medium` | [OK] | 1388ms |
| 8 | `codex/gpt-6-luna-low` | [OK] | 3239ms |
| 9 | ~~`codex/gpt-5.6-luna-max`~~ | [FAIL] | - |
| 10 | ~~`codex/gpt-5.6-terra-max`~~ | [FAIL] | - |
| 11 | ~~`codex/gpt-5.6-luna-high`~~ | [FAIL] | - |
| 12 | ~~`codex/gpt-5.6-luna-xhigh`~~ | [FAIL] | - |
| 13 | ~~`codex/gpt-5.6-terra-high`~~ | [FAIL] | - |
| 14 | ~~`codex/gpt-5.6-terra-xhigh`~~ | [FAIL] | - |
| 15 | ~~`codex/gpt-5.6-luna-medium`~~ | [FAIL] | - |
| 16 | ~~`codex/gpt-5.6-luna-low`~~ | [FAIL] | - |
| 17 | ~~`codex/gpt-5.6-terra-low`~~ | [FAIL] | - |
| 18 | ~~`codex/gpt-5.6-terra-ultra`~~ | [FAIL] | - |
| 19 | ~~`codex/gpt-5.6-terra-medium`~~ | [FAIL] | - |
| 20 | ~~`nvidia/openai/gpt-oss-20b`~~ | [FAIL] | - |
| 21 | ~~`agy/gpt-oss-120b-medium`~~ | [FAIL] - Empty response | 1189ms |
| 22 | ~~`antigravity/gpt-oss-120b-medium`~~ | [FAIL] - Empty response | 6182ms |
| 23 | `ddgw/gpt-5.6-luna` | [OK] | 983ms |
| 24 | `ddgw/gpt-5.4-mini` | [OK] | 1769ms |
| 25 | `cfp/openai/gpt-oss-120b` | [OK] | 13869ms |
| 26 | ~~`cfp/openai/gpt-oss-20b`~~ | [FAIL] - Timeout | 30000ms |
| 27 | `ddgw/tinfoil/gpt-oss-120b` | [OK] | 1426ms |

<a id="combogrok-best"></a>
### combo/grok-best

Grok CLI + Web models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `grok-cli/grok-4.7-high` | [OK] | 12795ms |
| 2 | `grok-cli/grok-4.7-low` | [OK] | 12939ms |
| 3 | `grok-cli/grok-4.7-xhigh` | [OK] | 5726ms |
| 4 | `grok-cli/grok-4.7` | [OK] | 13086ms |
| 5 | `grok-cli/grok-4.7-medium` | [OK] | 12861ms |
| 6 | `grok-web/fast` | [OK] | 1842ms |
| 7 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="combogroq-best"></a>
### combo/groq-best

Groq fast inference models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`groq/openai/gpt-oss-120b`~~ | [FAIL] - Empty response | 1353ms |
| 2 | `groq/qwen/qwen3.8-27b` | [OK] | 368ms |
| 3 | ~~`groq/openai/gpt-oss-20b`~~ | [FAIL] - Empty response | 715ms |
| 4 | ~~`groq/openai/gpt-oss-safeguard-20b`~~ | [FAIL] - Empty response | 295ms |
| 5 | `groq/allam-2-7b` | [OK] | 246ms |
| 6 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="comboinceptionai-best"></a>
### combo/inceptionai-best

Inception Labs Mercury-3

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`inceptionai/mercury-3`~~ | [FAIL] - Empty response | 1707ms |

<a id="combokilocode-best"></a>
### combo/kilocode-best

KiloCode free models ranked by coding quality

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | [OK] | 45ms |
| 2 | ~~`kilocode/stealth/glyph-cluster`~~ | [FAIL] - Empty response | 1788ms |
| 3 | ~~`kilocode/reflection/beam-free`~~ | [FAIL] - Empty response | 1209ms |
| 4 | ~~`kilocode/cohere/north-mini-code:free`~~ | [FAIL] - Empty response | 855ms |
| 5 | ~~`kilocode/nvidia/nemotron-3.5-super-vl:free`~~ | [FAIL] - Empty response | 7235ms |
| 6 | ~~`kilocode/nvidia/nemotron-3.5-lightning:free`~~ | [FAIL] - Empty response | 792ms |
| 7 | ~~`kilocode/dots-studio/dots-3-note-preview:free`~~ | [FAIL] - Empty response | 3237ms |
| 8 | ~~`kilocode/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`~~ | [FAIL] - Empty response | 802ms |
| 9 | `kilocode/kilo-auto/small` | [OK] | 1313ms |
| 10 | ~~`kilocode/kilo-auto/free`~~ | [FAIL] - Empty response | 1685ms |
| 11 | ~~`kilocode/openrouter/free`~~ | [FAIL] - Empty response | 1761ms |

<a id="combomistral-best"></a>
### combo/mistral-best

Mistral AI models via mistral and codestral

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `codestral/codestral-latest` | [OK] | 19ms |
| 2 | `codestral/codestral-2508` | [OK] | 820ms |
| 3 | `mistral/codestral-latest` | [OK] | 443ms |
| 4 | `mistral/codestral-2508` | [OK] | 17ms |
| 5 | `mistral/mistral-code-latest` | [OK] | 1457ms |
| 6 | `mistral/mistral-code-fim-latest` | [OK] | 720ms |
| 7 | `mistral/ministral-14b-latest` | [OK] | 524ms |
| 8 | `mistral/ministral-8b-latest` | [OK] | 863ms |
| 9 | `mistral/ministral-3b-latest` | [OK] | 594ms |
| 10 | `mistral/ministral-3b-2512` | [OK] | 756ms |
| 11 | `mistral/ministral-8b-2512` | [OK] | 663ms |
| 12 | `mistral/ministral-14b-2512` | [OK] | 680ms |

<a id="combomorph-best"></a>
### combo/morph-best

Morph fast reasoning and coding

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`morph/morph-v3-fast`~~ | [FAIL] - HTTP 402: {"error":{"message":"[402]: upstream error","type" | 710ms |
| 2 | ~~`morph/morph-v3-large`~~ | [FAIL] - HTTP 402: {"error":{"message":"[morph] All 1 connection(s) c | 20ms |

<a id="combonvidia-best"></a>
### combo/nvidia-best

NVIDIA NIM models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`nvidia/nvidia/nemotron-3.5-content-safety`~~ | [FAIL] | - |
| 2 | ~~`openrouter/nvidia/nemotron-3.5-lightning:free`~~ | [FAIL] - Empty response | 785ms |
| 3 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | [OK] | 48ms |
| 4 | ~~`openrouter/nvidia/nemotron-3.5-content-safety:free`~~ | [FAIL] | - |
| 5 | ~~`kilocode/nvidia/nemotron-3.5-lightning:free`~~ | [FAIL] - Empty response | 792ms |
| 6 | ~~`kilocode/nvidia/nemotron-3.5-content-safety:free`~~ | [FAIL] | - |
| 7 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="comboollama-cloud-best"></a>
### combo/ollama-cloud-best

Ollama Cloud Nemotron + Gemma

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`ollama-cloud/nemotron-3-ultra`~~ | [FAIL] - HTTP 400: {"error":{"message":"Model 'nemotron-3-ultra' is n | 36ms |
| 2 | ~~`ollama-cloud/nemotron-3-super`~~ | [FAIL] - Empty response | 1708ms |
| 3 | ~~`ollama-cloud/beam`~~ | [FAIL] - HTTP 400: {"error":{"message":"Model 'beam' is not available | 17ms |
| 4 | `ollama-cloud/gemma4:31b` | [OK] | 725ms |

<a id="comboopenrouter-best"></a>
### combo/openrouter-best

OpenRouter free coding/reasoning models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`openrouter/cohere/north-mini-code:free`~~ | [FAIL] - Empty response | 900ms |
| 2 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | [OK] | 48ms |
| 3 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free-high` | [OK] | 40ms |
| 4 | ~~`openrouter/nvidia/nemotron-3-ultra-550b-a55b:free-medium`~~ | [FAIL] - Empty response | 3446ms |
| 5 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free-none` | [OK] | 2391ms |
| 6 | ~~`openrouter/nvidia/nemotron-3.5-lightning:free`~~ | [FAIL] - Empty response | 785ms |
| 7 | ~~`openrouter/nvidia/nemotron-3.5-super-vl:free`~~ | [FAIL] - Empty response | 1107ms |
| 8 | ~~`openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`~~ | [FAIL] - Empty response | 1268ms |
| 9 | ~~`openrouter/dots-studio/dots-3-note-preview:free`~~ | [FAIL] - Empty response | 1693ms |
| 10 | ~~`openrouter/liquid/lfm-2.5-2.6b:free`~~ | [FAIL] - Empty response | 1931ms |
| 11 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="comboorcarouter-best"></a>
### combo/orcarouter-best

OrcaRouter models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`orcarouter/orcarouter/free`~~ | [FAIL] - HTTP 429: {"error":{"message":"All credentials for model orc | 996ms |
| 2 | ~~`orcarouter/deepseek/deepseek-v4.1-flash-free`~~ | [FAIL] - Timeout | 30000ms |
| 3 | ~~`orcarouter/deepseek/deepseek-v4-flash-free`~~ | [FAIL] - Timeout | 30000ms |
| 4 | ~~`orcarouter/z-ai/glm-5.3-flash-free`~~ | [FAIL] - Timeout | 30000ms |
