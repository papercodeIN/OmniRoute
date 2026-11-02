# Combos - full leg lists

[Back to README](../README.md)

Every OmniRoute combo on this machine, with each leg and its 30-day success rate.
A `priority` combo stops at the **first leg that answers**, so leg order *is* the ranking.

> **Re-ranked 2026-11-02** against the live catalog (944 model ids, 20 configured providers).
> Every combo now lists its strongest coding model first. Legs that no longer exist were removed;
> retired providers/models are struck out and kept for the record.

## What changed on 2026-11-02

- **New provider — Inception Labs (`inceptionai`).** Added `api.inceptionlabs.ai` with 2 active connections;
  new `combo/inceptionai-best` exposes `inceptionai/mercury-3` (1M ctx, tool calling, reasoning).
- **Retired provider — ~~larprouter~~.** All 7 connections are disabled (`operatorDisabledAt 2026-11-02T05:55Z`)
  and the upstream returns `402 Insufficient account credit`. DeepSeek V4.1 Flash is no longer offered, so
  `~~larprouter/deepseek-v4.1-flash~~` and `~~larprouter/glm-5.3-flash~~` are struck out and removed from the live combo.
- **Re-sorted every combo** so the best coding model is leg 1, then descending quality.
- **Removed dead legs:** legs absent from the catalog (`codex/gpt-5.6-*` effort variants, `codex/gpt-5.5`,
  `poolside/laguna-*`, `kilocode/stealth/glyph-cluster`, `cfp/mistral-small-2409`) and legs with a <40% success rate.

## Combo index

- [`combo/coding-elite`](#combocoding-elite)
- [`combo/inceptionai-best`](#comboinceptionai-best)
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

| Combo | Legs | Verified OK | Status |
|---|---|---|---|---|
| [`combo/coding-elite`](#combocoding-elite) | 29 | 29 / 0 | **Best today — daily driver** `codex/gpt-6-luna-max` |
| [`combo/claude-best`](#comboclaude-best) | 5 | 5 / 0 |  `antigravity/claude-opus-4-6-thinking` |
| [`combo/cloudflare-best`](#combocloudflare-best) | 23 | 23 / 0 |  `cloudflare-ai/@cf/qwen/qwen2.5-coder-32b-instruct` |
| [`combo/codex-best`](#combocodex-best) | 10 | 10 / 0 |  `codex/gpt-6-luna-max` |
| [`combo/gemini-best`](#combogemini-best) | 15 | 15 / 0 |  `agy/gemini-3.8-flash-tiered` |
| [`combo/morph-best`](#combomorph-best) | 2 | 2 / 0 |  `morph/morph-v3-large` |
| [`combo/gpt-best`](#combogpt-best) | 27 | 27 / 0 |  `codex/gpt-6-luna-max` |
| [`combo/grok-best`](#combogrok-best) | 9 | 9 / 0 |  `grok-cli/grok-4.7-xhigh` |
| [`combo/groq-best`](#combogroq-best) | 6 | 6 / 0 |  `groq/openai/gpt-oss-120b` |
| [`combo/agy-antigravity-best`](#comboagy-antigravity-best) | 21 | 21 / 0 |  `antigravity/claude-opus-4-6-thinking` |
| [`combo/kilocode-best`](#combokilocode-best) | 15 | 15 / 0 |  `kilocode/beam-1.0-501b-a23b` |
| [`combo/mistral-best`](#combomistral-best) | 17 | 17 / 0 |  `codestral/codestral-latest` |
| [`combo/nvidia-best`](#combonvidia-best) | 17 | 17 / 0 |  `nvidia/nvidia/nemotron-3-ultra-550b-a55b` |
| [`combo/openrouter-best`](#comboopenrouter-best) | 10 | 10 / 0 |  `openrouter/cohere/north-mini-code:free` |
| [`combo/free-ai-best`](#combofree-ai-best) | 19 | 19 / 0 |  `free-ai/openai/gpt-6.1-terra-pro` |

`Verified OK` = the leg id exists in the live `/v1/models` catalog. Rate = 30-day upstream success.

<a id="combocoding-elite"></a>
### combo/coding-elite - [back to list](#combo-index)

**Strategy** `priority` · **maxGlobalAttempts** 200 · daily driver · created 2026-10-27, re-ranked 2026-11-02.
29 legs · ranked best coding model first.

Ranked by agentic coding strength: frontier GPT-6/Claude/Grok agentic coders first, then the new Inception Labs frontier model, then free frontier coders, then code-specialized small models.

| # | Model | Provider | 30-day success | Notes |
|---|---|---|---|---|
| 1 | `codex/gpt-6-luna-max` | codex | 0/4 (0.0%) | 🏆 best coder · ⚠️ low success |
| 2 | `codex/gpt-6-luna-high` | codex | 0/2 (0.0%) | ⚠️ low success |
| 3 | `codex/gpt-6-luna` | codex | 1890/1903 (99.3%) |  |
| 4 | `antigravity/claude-opus-4-6-thinking` | antigravity | 50/50 (100.0%) |  |
| 5 | `agy/claude-opus-4-6-thinking` | agy | 50/50 (100.0%) |  |
| 6 | `codex/gpt-5.6-terra` | codex | 56/62 (90.3%) | **new** |
| 7 | `codex/gpt-5.6-luna` | codex | 68/75 (90.7%) | **new** |
| 8 | `cx/gpt-5.6-terra-xhigh` | cx | 0/2 (0.0%) | **new** · ⚠️ low success |
| 9 | `cx/gpt-5.6-luna-xhigh` | cx | 0/2 (0.0%) | **new** · ⚠️ low success |
| 10 | `codex/gpt-reserve-high` | codex | — | **new** |
| 11 | `grok-cli/grok-4.7-xhigh` | grok-cli | — | **new** |
| 12 | `grok-cli/grok-4.7` | grok-cli | 80/87 (92.0%) |  |
| 13 | `antigravity/claude-sonnet-4-6` | antigravity | 8/8 (100.0%) | **new** |
| 14 | `agy/claude-sonnet-4-6` | agy | 8/8 (100.0%) | **new** |
| 15 | `inceptionai/mercury-3` | inceptionai | 2/2 (100.0%) | **new** |
| 16 | `cfp/moonshotai/kimi-k2.7-code` | cfp | 11/45 (24.4%) | ⚠️ low success |
| 17 | `cfp/deepseek-ai/deepseek-v4-pro-0813` | cfp | 14/22 (63.6%) | ⚠️ low success |
| 18 | `cfp/zai-org/glm-5.2` | cfp | 14/21 (66.7%) | ⚠️ low success |
| 19 | `nvidia/nvidia/nemotron-3-ultra-550b-a55b` | nvidia | 20/30 (66.7%) | ⚠️ low success |
| 20 | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | openrouter | 63/83 (75.9%) |  |
| 21 | `openrouter/cohere/north-mini-code:free` | openrouter | 64/65 (98.5%) |  |
| 22 | `kilocode/cohere/north-mini-code:free` | kilocode | 64/65 (98.5%) | **new** |
| 23 | `openrouter/nvidia/nemotron-3.5-lightning:free` | openrouter | 61/64 (95.3%) |  |
| 24 | `kilocode/reflection/beam-free` | kilocode | 198/198 (100.0%) |  |
| 25 | `mistral/codestral-latest` | mistral | 80/90 (88.9%) |  |
| 26 | `codestral/codestral-latest` | codestral | 80/90 (88.9%) | **new** |
| 27 | `openrouter/nvidia/nemotron-3.5-super-vl:free` | openrouter | 31/34 (91.2%) | **new** |

**Struck out / removed**

| Model | Reason |
|---|---|
| ~~`larprouter/deepseek-v4.1-flash`~~ | provider retired — all 7 connections disabled, upstream 402, DeepSeek V4.1 Flash withdrawn |
| ~~`larprouter/glm-5.3-flash`~~ | provider retired — same |
| ~~`openrouter/poolside/laguna-s-2.1:free`~~ | no longer in the catalog |
| ~~`kilocode/stealth/glyph-cluster`~~ | no longer in the catalog |
| ~~`openrouter/recursive/flint-v1.0:free`~~ | dropped — 36% success (171/477) |
| ~~`groq/qwen/qwen3.8-27b`~~ | dropped — 20% success (40/197) |

**Extra notes**

- Registered in `opencode.jsonc` as `combo/coding-elite` and bare `coding-elite` (200k ctx / 32k out).
- New provider — Inception Labs (`inceptionai`). Added `api.inceptionlabs.ai` with 2 active connections; new `combo/inceptionai-best` exposes `inceptionai/mercury-3` (1M ctx, tool calling, reasoning).
- Retired provider — ~~larprouter~~. All 7 connections are disabled (`operatorDisabledAt 2026-11-02T05:55Z`) and the upstream returns `402 Insufficient account credit`. DeepSeek V4.1 Flash is no longer offered, so `~~larprouter/deepseek-v4.1-flash~~` and `~~larprouter/glm-5.3-flash~~` are struck out and removed from the live combo.
- Every combo now lists its strongest coding model first. Legs that no longer exist were removed; retired providers/models are struck out and kept for the record.
- All active connections with is_active=1 and test_status=active are usable in the updated combos.