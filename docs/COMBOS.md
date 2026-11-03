# Combos - full leg lists

[Back to README](../README.md)

Every OmniRoute combo on this machine, with each leg and its 30-day success rate.
A `priority` combo stops at the **first leg that answers**, so leg order is the ranking.

> **Updated 2026-11-03:** Auto-generated from live OmniRoute catalog.

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

---

| Combo | Legs | Working | Failed | Status |
|---|---:|---:|---:|---|
| `combo/agy-antigravity-best` | 15 | 15 | 0 | [OK] |
| `combo/claude-best` | 5 | 4 | 1 | [WARN] |
| `combo/cloudflare-best` | 15 | 12 | 3 | [WARN] |
| `combo/codex-best` | 4 | 3 | 1 | [WARN] |
| `combo/coding-elite` | 19 | 14 | 5 | [WARN] |
| `combo/free-ai-best` | 7 | 5 | 2 | [WARN] |
| `combo/gemini-best` | 11 | 11 | 0 | [OK] |
| `combo/gemini-web-best` | 3 | 1 | 2 | [WARN] |
| `combo/gpt-best` | 27 | 14 | 13 | [WARN] |
| `combo/grok-best` | 7 | 6 | 1 | [WARN] |
| `combo/groq-best` | 6 | 3 | 3 | [WARN] |
| `combo/inceptionai-best` | 1 | 0 | 1 | [FAIL] |
| `combo/kilocode-best` | 13 | 3 | 10 | [WARN] |
| `combo/mistral-best` | 12 | 12 | 0 | [OK] |
| `combo/morph-best` | 2 | 0 | 2 | [FAIL] |
| `combo/nvidia-best` | 7 | 1 | 6 | [WARN] |
| `combo/ollama-cloud-best` | 4 | 1 | 3 | [WARN] |
| `combo/openrouter-best` | 11 | 4 | 7 | [WARN] |

<a id="comboagy-antigravity-best"></a>
### combo/agy-antigravity-best

AGY + Antigravity Claude and Gemini

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `antigravity/claude-opus-4-6-thinking` | [OK] | 20ms |
| 2 | `agy/claude-opus-4-6-thinking` | [OK] | 64ms |
| 3 | `antigravity/claude-sonnet-4-6` | [OK] | 188ms |
| 4 | `agy/claude-sonnet-4-6` | [OK] | 35ms |
| 5 | `antigravity/gemini-3.8-flash-tiered` | [OK] | 249ms |
| 6 | `agy/gemini-3.8-flash-tiered` | [OK] | 211ms |
| 7 | `agy/gemini-3.8-flash-medium` | [OK] | 15ms |
| 8 | `agy/gemini-3.8-flash-high` | [OK] | 195ms |
| 9 | `agy/gemini-3.8-flash-low` | [OK] | 13ms |
| 10 | `agy/gemini-3.1-flash-lite` | [OK] | 319ms |
| 11 | `agy/gemini-3.5-flash-lite` | [OK] | 212ms |
| 12 | `agy/gemini-3-flash` | [OK] | 257ms |
| 13 | `antigravity/gemini-3.1-flash-lite` | [OK] | 28ms |
| 14 | `antigravity/gemini-3-flash` | [OK] | 121ms |
| 15 | `antigravity/gemini-3.5-flash-lite` | [OK] | 39ms |

<a id="comboclaude-best"></a>
### combo/claude-best

Best Claude models via antigravity and agy

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `antigravity/claude-opus-4-6-thinking` | [OK] | 20ms |
| 2 | `agy/claude-opus-4-6-thinking` | [OK] | 64ms |
| 3 | `antigravity/claude-sonnet-4-6` | [OK] | 188ms |
| 4 | `agy/claude-sonnet-4-6` | [OK] | 35ms |
| 5 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="combocloudflare-best"></a>
### combo/cloudflare-best

Cloudflare Workers AI + CFP models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `cloudflare-ai/@cf/qwen/qwen2.5-coder-32b-instruct` | [OK] | 31ms |
| 2 | `cloudflare-ai/@cf/qwen/qwq-32b` | [OK] | 35ms |
| 3 | ~~`cloudflare-ai/@cf/deepseek-ai/deepseek-r1-distill-qwen-32b`~~ | [FAIL] - Empty response | 63ms |
| 4 | `cfp/qwen/qwq-32b` | [OK] | 16ms |
| 5 | `cfp/qwen/qwen3-30b-a3b-fp8` | [OK] | 27ms |
| 6 | ~~`cfp/deepseek-ai/deepseek-r1-distill-qwen-32b`~~ | [FAIL] - Empty response | 109ms |
| 7 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | [OK] | 32ms |
| 8 | `cloudflare-ai/@cf/mistral/mistral-7b-instruct-v0.2-lora` | [OK] | 1061ms |
| 9 | `cloudflare-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast` | [OK] | 34ms |
| 10 | ~~`cloudflare-ai/@cf/google/gemma-4-26b-a4b-it`~~ | [FAIL] - Empty response | 1786ms |
| 11 | `cfp/google/gemma-4-26b-a4b-it` | [OK] | 41ms |
| 12 | `cfp/aisingapore/gemma-sea-lion-v4-27b-it` | [OK] | 103ms |
| 13 | `cfp/mistralai/mistral-small-3.1-24b-instruct` | [OK] | 32ms |
| 14 | `cloudflare-ai/@cf/meta/llama-3.2-3b-instruct` | [OK] | 82ms |
| 15 | `cloudflare-ai/@cf/mistral/mistral-7b-instruct-v0.2-lora` | [OK] | 1061ms |

<a id="combocodex-best"></a>
### combo/codex-best

Codex GPT models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `codex/gpt-6-luna` | [OK] | 2081ms |
| 2 | `codex/gpt-5.6-luna` | [OK] | 34ms |
| 3 | `codex/gpt-5.6-terra` | [OK] | 2109ms |
| 4 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="combocoding-elite"></a>
### combo/coding-elite

Daily driver - best coding models ranked by quality

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `codex/gpt-6-luna-max` | [OK] | 3508ms |
| 2 | `codex/gpt-6-luna-high` | [OK] | 2290ms |
| 3 | `gc/grok-4.7-xhigh` | [OK] | 9108ms |
| 4 | `antigravity/claude-opus-4-6-thinking` | [OK] | 20ms |
| 5 | `agy/claude-opus-4-6-thinking` | [OK] | 64ms |
| 6 | ~~`inceptionai/mercury-3`~~ | [FAIL] - Empty response | 1330ms |
| 7 | `cx/gpt-6-luna` | [OK] | 2173ms |
| 8 | `codex/gpt-6-luna` | [OK] | 2081ms |
| 9 | `grok-cli/grok-4.7` | [OK] | 15279ms |
| 10 | ~~`openrouter/cohere/north-mini-code:free`~~ | [FAIL] - Empty response | 1375ms |
| 11 | `cfp/moonshotai/kimi-k2.7-code` | [OK] | 30ms |
| 12 | `cfp/deepseek-ai/deepseek-v4-pro-0813` | [OK] | 31ms |
| 13 | `cfp/zai-org/glm-5.2` | [OK] | 156ms |
| 14 | ~~`openrouter/nvidia/nemotron-3.5-lightning:free`~~ | [FAIL] - Empty response | 1416ms |
| 15 | ~~`nvidia/nvidia/nemotron-3-ultra-550b-a55b`~~ | [FAIL] - Empty response | 1533ms |
| 16 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | [OK] | 185ms |
| 17 | `mistral/codestral-latest` | [OK] | 211ms |
| 18 | `groq/qwen/qwen3.8-27b` | [OK] | 34ms |
| 19 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="combofree-ai-best"></a>
### combo/free-ai-best

Verified working FreeAI models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `free-ai/qwen3-coder` | [OK] | 65ms |
| 2 | `free-ai/qwen-coder` | [OK] | 42ms |
| 3 | ~~`free-ai/deepseek-r1`~~ | [FAIL] - Empty response | 2345ms |
| 4 | `free-ai/mistral` | [OK] | 52ms |
| 5 | `free-ai/qwen3-8b` | [OK] | 21ms |
| 6 | `free-ai/qwen7b` | [OK] | 124ms |
| 7 | ~~`free-ai/deepseek-r1-7b`~~ | [FAIL] - Empty response | 2196ms |

<a id="combogemini-best"></a>
### combo/gemini-best

AGY + Antigravity Gemini flash tiers

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `agy/gemini-3.8-flash-tiered` | [OK] | 211ms |
| 2 | `agy/gemini-3.8-flash-medium` | [OK] | 15ms |
| 3 | `antigravity/gemini-3.8-flash-tiered` | [OK] | 249ms |
| 4 | `agy/gemini-3.8-flash-high` | [OK] | 195ms |
| 5 | `agy/gemini-3.8-flash-low` | [OK] | 13ms |
| 6 | `agy/gemini-3.5-flash-lite` | [OK] | 212ms |
| 7 | `antigravity/gemini-3.5-flash-lite` | [OK] | 39ms |
| 8 | `agy/gemini-3.1-flash-lite` | [OK] | 319ms |
| 9 | `antigravity/gemini-3.1-flash-lite` | [OK] | 28ms |
| 10 | `agy/gemini-3-flash` | [OK] | 257ms |
| 11 | `antigravity/gemini-3-flash` | [OK] | 121ms |

<a id="combogemini-web-best"></a>
### combo/gemini-web-best

Gemini Web models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`gemini-web/gemini-3.7-flash`~~ | [FAIL] - HTTP 400: {"error":{"message":"Model provider \"gemini-web\" | 12467ms |
| 2 | ~~`gemini-web/gemini-3.1-pro`~~ | [FAIL] - Timeout | 30000ms |
| 3 | `gemini-web/gemini-3.1-flash-lite` | [OK] | 43ms |

<a id="combogpt-best"></a>
### combo/gpt-best

All GPT variants across providers

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `codex/gpt-6-luna` | [OK] | 2081ms |
| 2 | `codex/gpt-5.6-luna` | [OK] | 34ms |
| 3 | `codex/gpt-5.6-terra` | [OK] | 2109ms |
| 4 | `codex/gpt-6-luna-max` | [OK] | 3508ms |
| 5 | `codex/gpt-6-luna-high` | [OK] | 2290ms |
| 6 | `codex/gpt-6-luna-xhigh` | [OK] | 4607ms |
| 7 | `codex/gpt-6-luna-medium` | [OK] | 2173ms |
| 8 | `codex/gpt-6-luna-low` | [OK] | 1577ms |
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
| 20 | `nvidia/openai/gpt-oss-20b` | [OK] | 253ms |
| 21 | ~~`agy/gpt-oss-120b-medium`~~ | [FAIL] - Empty response | 2948ms |
| 22 | ~~`antigravity/gpt-oss-120b-medium`~~ | [FAIL] - Timeout | 30000ms |
| 23 | `ddgw/gpt-5.6-luna` | [OK] | 163ms |
| 24 | `ddgw/gpt-5.4-mini` | [OK] | 31ms |
| 25 | `cfp/openai/gpt-oss-120b` | [OK] | 38ms |
| 26 | `cfp/openai/gpt-oss-20b` | [OK] | 16ms |
| 27 | `ddgw/tinfoil/gpt-oss-120b` | [OK] | 37ms |

<a id="combogrok-best"></a>
### combo/grok-best

Grok CLI + Web models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `grok-cli/grok-4.7-high` | [OK] | 15548ms |
| 2 | `grok-cli/grok-4.7-low` | [OK] | 11585ms |
| 3 | `grok-cli/grok-4.7-xhigh` | [OK] | 10003ms |
| 4 | `grok-cli/grok-4.7` | [OK] | 15279ms |
| 5 | `grok-cli/grok-4.7-medium` | [OK] | 9557ms |
| 6 | `grok-web/fast` | [OK] | 58ms |
| 7 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="combogroq-best"></a>
### combo/groq-best

Groq hosted models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `groq/openai/gpt-oss-120b` | [OK] | 20ms |
| 2 | `groq/qwen/qwen3.8-27b` | [OK] | 34ms |
| 3 | `groq/openai/gpt-oss-20b` | [OK] | 35ms |
| 4 | ~~`groq/openai/gpt-oss-safeguard-20b`~~ | [FAIL] - Empty response | 467ms |
| 5 | ~~`groq/allam-2-7b`~~ | [FAIL] - HTTP 400: {"error":{"message":"Model 'allam-2-7b' is not ava | 153ms |
| 6 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="comboinceptionai-best"></a>
### combo/inceptionai-best

Inception Labs Mercury-3 (1M context, reasoning, tool calling)

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`inceptionai/mercury-3`~~ | [FAIL] - Empty response | 1330ms |

<a id="combokilocode-best"></a>
### combo/kilocode-best

KiloCode free models ranked by coding quality

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`kilocode/poolside/laguna-s-2.1:free`~~ | [FAIL] | - |
| 2 | `kilocode/nvidia/nemotron-3-ultra-550b-a55b:free` | [OK] | 26ms |
| 3 | ~~`kilocode/cohere/north-mini-code:free`~~ | [FAIL] - Empty response | 7770ms |
| 4 | ~~`kilocode/poolside/laguna-xs-2.1:free`~~ | [FAIL] | - |
| 5 | ~~`kilocode/nvidia/nemotron-3.5-lightning:free`~~ | [FAIL] - Empty response | 2472ms |
| 6 | ~~`kilocode/nvidia/nemotron-3.5-content-safety:free`~~ | [FAIL] | - |
| 7 | ~~`kilocode/nvidia/nemotron-3.5-super-vl:free`~~ | [FAIL] - Timeout | 30000ms |
| 8 | `kilocode/kilo-auto/small` | [OK] | 40ms |
| 9 | `kilocode/openrouter/free` | [OK] | 9552ms |
| 10 | ~~`kilocode/liquid/lfm-2.5-2.6b:free`~~ | [FAIL] - Timeout | 30000ms |
| 11 | ~~`kilocode/dots-studio/dots-3-note-preview:free`~~ | [FAIL] - Empty response | 8035ms |
| 12 | ~~`kilocode/reflection/beam-free`~~ | [FAIL] - Empty response | 2508ms |
| 13 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="combomistral-best"></a>
### combo/mistral-best

Mistral + Codestral models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | `codestral/codestral-latest` | [OK] | 61ms |
| 2 | `codestral/codestral-2508` | [OK] | 15ms |
| 3 | `mistral/codestral-latest` | [OK] | 211ms |
| 4 | `mistral/codestral-2508` | [OK] | 16ms |
| 5 | `mistral/mistral-code-latest` | [OK] | 112ms |
| 6 | `mistral/mistral-code-fim-latest` | [OK] | 33ms |
| 7 | `mistral/ministral-14b-latest` | [OK] | 288ms |
| 8 | `mistral/ministral-8b-latest` | [OK] | 33ms |
| 9 | `mistral/ministral-3b-latest` | [OK] | 1515ms |
| 10 | `mistral/ministral-3b-2512` | [OK] | 1364ms |
| 11 | `mistral/ministral-8b-2512` | [OK] | 88ms |
| 12 | `mistral/ministral-14b-2512` | [OK] | 72ms |

<a id="combomorph-best"></a>
### combo/morph-best

Morph v3 models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`morph/morph-v3-fast`~~ | [FAIL] - HTTP 402: {"error":{"message":"[morph] All 1 connection(s) c | 15ms |
| 2 | ~~`morph/morph-v3-large`~~ | [FAIL] - HTTP 402: {"error":{"message":"[morph] All 1 connection(s) c | 28ms |

<a id="combonvidia-best"></a>
### combo/nvidia-best

Nemotron models across providers

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`nvidia/nvidia/nemotron-3.5-content-safety`~~ | [FAIL] - HTTP 429: {"error":{"message":"All credentials for model nvi | 160ms |
| 2 | ~~`openrouter/nvidia/nemotron-3.5-lightning:free`~~ | [FAIL] - Empty response | 1416ms |
| 3 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | [OK] | 185ms |
| 4 | ~~`openrouter/nvidia/nemotron-3.5-content-safety:free`~~ | [FAIL] | - |
| 5 | ~~`kilocode/nvidia/nemotron-3.5-lightning:free`~~ | [FAIL] - Empty response | 2472ms |
| 6 | ~~`kilocode/nvidia/nemotron-3.5-content-safety:free`~~ | [FAIL] | - |
| 7 | ~~`auto/best-coding`~~ | [FAIL] | - |

<a id="comboollama-cloud-best"></a>
### combo/ollama-cloud-best

Ollama Cloud Nemotron + Gemma

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`ollama-cloud/nemotron-3-ultra`~~ | [FAIL] - HTTP 400: {"error":{"message":"Model 'nemotron-3-ultra' is n | 13ms |
| 2 | ~~`ollama-cloud/nemotron-3-super`~~ | [FAIL] - Empty response | 1210ms |
| 3 | ~~`ollama-cloud/beam`~~ | [FAIL] - HTTP 400: {"error":{"message":"Model 'beam' is not available | 24ms |
| 4 | `ollama-cloud/gemma4:31b` | [OK] | 56ms |

<a id="comboopenrouter-best"></a>
### combo/openrouter-best

OpenRouter free coding/reasoning models

| # | Model | Status | Latency |
|---|-------|--------|---------|
| 1 | ~~`openrouter/cohere/north-mini-code:free`~~ | [FAIL] - Empty response | 1375ms |
| 2 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | [OK] | 185ms |
| 3 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free-high` | [OK] | 84ms |
| 4 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free-medium` | [OK] | 88ms |
| 5 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free-none` | [OK] | 39ms |
| 6 | ~~`openrouter/nvidia/nemotron-3.5-lightning:free`~~ | [FAIL] - Empty response | 1416ms |
| 7 | ~~`openrouter/nvidia/nemotron-3.5-super-vl:free`~~ | [FAIL] - Timeout | 30000ms |
| 8 | ~~`openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`~~ | [FAIL] - Empty response | 2006ms |
| 9 | ~~`openrouter/dots-studio/dots-3-note-preview:free`~~ | [FAIL] - Empty response | 6945ms |
| 10 | ~~`openrouter/liquid/lfm-2.5-2.6b:free`~~ | [FAIL] - Empty response | 3575ms |
| 11 | ~~`auto/best-coding`~~ | [FAIL] | - |
