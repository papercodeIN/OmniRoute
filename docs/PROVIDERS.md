# Providers - what works, what is dead, and where to get keys

[Back to README](../README.md)

## Rules that keep the gateway usable

Per-provider health, exact model ids and the errors blocking the rest live in
[section 8](#8-coding-model-ranking---all-providers-best-first-probed-2026-10-27) (8.1 = reachable now, 8.2 = blocked with the fix).

Policies that do not change day to day:

- **One provider per brand combo** (`cloudflare-best`, `groq-best`, `mistral-best`, ...) so one dead provider cannot poison the others. `all-best` and `coding-elite` interleave on purpose.
- **Cloudflare legs must use the `cloudflare-ai/@cf/...` prefix** - bare `@cf/...` ids get mis-routed as provider `@cf`.
- **Removed for good:** `spark-best` (no working Spark models), `steady-coding`, `trae-best`, `zerolimitai-best` (7-day trial only), Cline (250 dead legs).
- **Durable failures (401/402/404) are auto-disabled; transient ones (429/5xx/timeout) recover on retry.**

- **larprouter** (`anthropic-compatible-larprouter`, base `https://larprouter.com/v1`) is a
  free pool: `deepseek-v4.1-flash` and `glm-5.3-flash` answer in 1-9 s, everything else on that
  provider is either 400 "not priced or available in this pool" (claude, kimi, qwen) or 402
  "insufficient credit" (glm-5.3, minimax). It does not need a key of its own - the gateway holds it.

## Kilocode (new provider, 2 OAuth accounts active)
- 2 accounts (urviahmnakum, mantra.u.nakum@gmail.com), both active, no errors.
- 17 ids on /v1/models; 10 answer and score 100 on coding quiz (glyph-cluster, beam-free, dots-preview, nemotron-ultra, lfm, kilo-auto + cohere/north-mini etc). 6 new good legs added to coding-elite at #16-21. 7 others are router/pass-through (openrouter/free) or non-coding (content-safety, super-vl, beam-501b block).
- All new legs verified with real test cases; tool_calls work on glyph-cluster / beam-free / dots-preview / nemotron-ultra.
\n## Where the free keys come from

| Provider | Free models | Sign up |
|---|---|---|
| **Groq** | gpt-oss-120b / 20b, qwen3.8-27b (rate limited) | https://console.groq.com/keys |
| **OpenRouter** | every `:free` id (laguna s/xs, flint, north-mini-code, nemotron, gemma) | https://openrouter.ai/keys |
| **NVIDIA NIM** | nemotron ultra / lightning, minimax, glm | https://build.nvidia.com |
| **Mistral / Codestral** | codestral-latest, codestral-2508, code-fim | https://console.mistral.ai |
| **Cloudflare** | `@cf/qwen/*`, qwq-32b, glm-4.7-flash, r1-distill | https://dash.cloudflare.com |
| **Morph** | morph-v3-fast / large (edit engine, not chat) | https://morphllm.com |
| **Gemini AI Studio** | gemini-3.8-flash (currently inactive here) | https://aistudio.google.com/api-keys |
| **DeepSeek** | *no free API tier* - pay-as-you-go, ~$0.15/1M in, $0.60/1M out | https://platform.deepseek.com |

Everything else in this setup is an **account bridge**: you log in once, the gateway reuses
that session. No key needed.

## Notes

- Attempt budget is 200 per request, so 150-leg combos are safe.
- OpenRouter's paid routes are blocked by a **workspace lifetime** budget of $0.60 that does
  not reset - only `:free` ids work there.
- Cloudflare legs must use the `cloudflare-ai/@cf/...` prefix; bare `@cf/...` ids get
  mis-routed as provider `@cf`.
