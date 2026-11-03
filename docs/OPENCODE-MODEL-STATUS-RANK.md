# OpenCode Free Models — Status & Agentic Rank

> The 9 free models in the OpenCode picker, ranked for **agentic coding** (long-horizon tool use,
> terminal work, multi-file edits) — not chat quality. **Verified 2026-10-27.**
> Free tier only — no paid routes, pricing or subscriptions in this file.
> Complements [README section 4](https://github.com/papercodeIN/OmniRoute#4-coding-model-ranking---best-first-2026-10-27),
> which ranks models across *all* providers; this file is scraped down to the free OpenCode tier.

---

## 1. Ranking — best agentic coder first

| # | Model | ID | DeepSWE | TB 2.1 | SWE-V | Ctx | Verdict |
|---|---|---|---|---|---|---|---|
| **1** | **DeepSeek V4.1 Flash Free** | `deepseek-v4.1-flash-free` | **74.2** | **90.6** | — | 200K | Best long-horizon agent; highest real-world adoption (19T tok/day). **Default pick.** |
| **2** | **GLM-5.3-Flash Free** | `glm-5.3-flash-free` | 63.4 | 84.3 | 79.1 | 200K | Best all-round balance; beats #1 on SWE-V. **Best fallback.** |
| **3** | **Beam Free** | `beam-free` | 43.3 | 80.1 | **81.6** | **1M** | Highest SWE-V, but weakest plan adherence of the top group. Single-shot patches + huge ctx only. |
| **4** | **MiMo-V2.6-Flash Free** | `mimo-v2.6-flash-free` | 67.9 | — | — | 200K | Strong agentic scores, coding rank #22/152. Underrated mid-tier pick. |
| **5** | **Big Pickle** | `big-pickle` | — | — | — | 200K | Unrankable — stealth model that rotates. Fast/pleasant, no reliability guarantee. |
| **6** | **Flint 40B Free** | `flint-40b-free` | — | 54.9 | 74.2\* | 262K | Decent patch quality, weak terminal loop. Chat-tier agent. |
| **7** | **Nemotron 3.5 Super VL Free** | `nemotron-3.5-super-vl-free` | 24.65 | 60.67 | 71.1 | **1M** | Vision-capable, but agentic loop collapses on multi-step work. |
| **8** | **Nemotron 3 Ultra Free** | `nemotron-3-ultra-free` | 3.0 | — | 73.9 | **1M** | Big context, near-zero autonomous agent score. Never use as an agent. |
| **9** | **Nemotron 3.5 Lightning Free** | `nemotron-3.5-lightning-free` | — | 23.5 | 52.8 | 262K | Fastest of the group, worst at everything this ranking measures. |

`*` self-reported by the vendor.

**Weighting:** DeepSWE (long-horizon agentic) > Terminal-Bench 2.1 (terminal/tool use) > SWE-bench Verified (single-issue patch).

**Reading the table**

- Ranks **1–4** are genuinely usable as agents.
- Ranks **5–6** are situational.
- Ranks **7–9** are chat models wearing agent clothing — fine for "explain this file", bad for "refactor this module".

---

## 2. Benchmark caveats (read before quoting numbers)

| Caveat | Detail |
|---|---|
| Not apples-to-apples | Vendor self-reports, different scaffolds, different reasoning-effort settings |
| Noise floor | Treat gaps under ~5 points as a tie |
| Missing cells | A dash = no comparable published number, not a zero |
| Stealth models | Big Pickle rotates; any number would be stale within weeks |
| Context ≠ quality | The 1M-context models (Beam, Nemotron Ultra/Super VL) rank low *because* of agentic scores, not ctx |

---

## 3. Free-tier limits (OpenCode Zen)

**No numeric limit is published.** Docs say only "free for a limited time" at $0 pricing. What is actually enforced on the free tier:

| Limit | Value |
|---|---|
| Price | $0 in / $0 out / $0 cached |
| Context — DeepSeek V4.1 Flash Free | **200K** |
| Max output — DeepSeek V4.1 Flash Free | **32K** |
| Where it runs | **OpenCode app only** |
| Raw API access | `403 FreeTierError` |
| Rate limit | Global, undocumented, **shared across all free models** |
| End date | none published — can be pulled any day |

### The real constraint: one shared free bucket

There is **no per-model quota**. Every free model on this list draws from a single global pool, so
switching from DeepSeek to GLM does *not* restore quota if the throttle is global.

| Symptom | Meaning |
|---|---|
| `Error: Rate limit exceeded. Please try again later.` | bucket drained |
| HTTP `429 FreeUsageLimitError` | same, API-level |
| `403 FreeTierError` | calling from outside the OpenCode app |
| Multi-day 429s | provider-side incident, not your account (see upstream issues) |

Community estimate for bucket size: **~$1/day of equivalent usage** — a few hundred agent turns,
or one or two long refactors. It refills over time (people report a usable chunk again a few days
later); it is **not** a per-hour request count.

Also expect **cold starts and slow responses at peak** — free traffic is deprioritized.

---

## 4. Free-model context windows

| Model | Context | Note |
|---|---|---|
| Beam Free | **1M** | largest free ctx with usable patch quality |
| Nemotron 3 Ultra Free | **1M** | ctx-rich, agent-poor |
| Nemotron 3.5 Super VL Free | **1M** | ctx-rich, vision, agent-poor |
| Flint 40B Free | 262K | |
| Nemotron 3.5 Lightning Free | 262K | |
| DeepSeek V4.1 Flash Free | 200K | free-tier ceiling |
| GLM-5.3-Flash Free | 200K | |
| MiMo-V2.6-Flash Free | 200K | |
| Big Pickle | 200K | rotates |

---

## 5. Verdict — what to actually use

| Situation | Pick |
|---|---|
| Default agent work | **DeepSeek V4.1 Flash Free** (`deepseek-v4.1-flash-free`) |
| Rate-limited / throttled | **GLM-5.3-Flash Free** (`glm-5.3-flash-free`) |
| Need 1M ctx with decent patches | **Beam Free** (`beam-free`) |
| Want something different / faster | **MiMo-V2.6-Flash Free** (`mimo-v2.6-flash-free`) |
| Novelty / exploration only | Big Pickle |
| Screenshot / image input | Nemotron 3.5 Super VL Free (vision only — don't let it drive an agent loop) |
| Anything autonomous or multi-file | **never** ranks 7–9 |

---

## 6. Stretching the free bucket

1. **Fresh session per task** — compaction burns the budget twice.
2. **Plan mode first** (Tab), then switch to Build — cheap iteration before expensive edits.
3. **`/compact` deliberately** rather than letting it fire mid-file.
4. **`@` specific files** instead of loading the whole repo.
5. **No parallel subagents** — they multiply the drain on one shared bucket.
6. On 200K models, treat "it got dumb / looped" as **mid-session compaction**, not model regression.

---

## 7. When the free models throttle

| Free fallback | What it gives you |
|---|---|
| `combo/coding-elite` (this repo) | routes around dead/throttled legs automatically — see README §3 |
| `glm-5.3-flash-free` | second-best free agent; only helps if the throttle is model-specific, not global |
| `mimo-v2.6-flash-free` | third distinct free pool, still agent-capable |
| `larprouter/deepseek-v4.1-flash` | free pool, #1 leg of `coding-elite`; 402 = pool credit exhausted, combo falls through |
| `openrouter/poolside/laguna-s-2.1:free` | free, single-file work only |
| `openrouter/recursive/flint-v1.0:free` | free patch-quality specialist |

---

## 8. Notes

- Free `deepseek-v4.1-flash-free` is the **pre-1017 build**. A separate `deepseek-v4.1-flash-1017`
  entry scores higher (~AA index 45) but is a different free model with its own usage accounting.
- Because the bucket is shared, free legs degrade together — `coding-elite`'s ordering exists so a
  request fails *through* the free tier instead of stalling in it.
- Source pages: [opencode.ai/docs/zen](https://opencode.ai/docs/zen/) ·
  [opencode.ai/data](https://opencode.ai/data/) · vendor cards for DeepSeek, GLM, Beam, MiMo, Flint, Nemotron.
