---
name: publishing
description: Content strategy for external platforms (X, LinkedIn, etc.). Voice, style, and growth strategies.
user-invocable: false
---

# Publishing Content Strategy

> Core principles for creating content that grows audience

## Platform Status

Check current platform status (Premium tier, features, limits) in the integration plan files:
- X: `agent/integrations/x/plan.md`
- Bluesky: `agent/integrations/bluesky/plan.md`

If plan files don't exist, create them from current state.

---

## Expertise Pillars (Content Filter)

Every post MUST connect to at least one pillar. If it doesn't, skip it.

### How Pillars Work

Pillars are the account's content lanes — topics where the owner has real authority. They are **discovered, not hardcoded.**

**Where pillars come from:**
1. **ME.md** — Owner's background, expertise areas, current projects
2. **GOALS.md** — What the account is trying to achieve
3. **This repo's purpose** — What the agent actually does (autonomous content automation)
4. **What's working** — Topics that get engagement (check metrics during retros)

**Pillar lifecycle:**
- Discover pillars at session start by reading ME.md and GOALS.md
- Follow the same pillars for 2-4 weeks (consistency builds audience recognition)
- Review and potentially evolve pillars during weekly retros based on engagement data
- Some pillars are always available (owner's permanent expertise areas from ME.md) but the agent can explore new ones

**Current pillars** are stored in `agent/memory/pillars.md`. If that file doesn't exist, discover pillars from ME.md and GOALS.md and create it.

**AI Industry news** is allowed ONLY as a hook to reach a pillar. The news is never the point. The connection to our expertise is.

**Pillar gate:** Before writing any post, answer: "Which pillar does this connect to, and what's MY angle?" If you can't answer both, skip.

---

## What Actually Works (Evidence-Based)

**Content formats ranked by performance (our data):**
1. **News hooks** — 3-6x average impressions (65, 62, 60, 51 imp vs 10 avg)
2. **Dollar-amount headlines** — ($285B, $2B, $1T) quantified impact stops scroll
3. **Name-drops** — (Karpathy, Altman, Anthropic, OpenAI) moderate boost
4. **Replies to official accounts** — (@OpenAI 24 imp) > individuals (0-6 imp)

**What underperforms:** Generic framework posts without news hook (<10 imp), process posts without news hook, personality without timeliness, stale replies (>6h = 0 imp).

### X Post Length (Premium = up to 25,000 chars)

X Premium unlocks long-form posts. The agent has been writing 270-450 char posts (old free-tier length). This wastes Premium. **Write X posts at full length. Bluesky is a separate platform with separate constraints — never let Bluesky's 290-char limit shrink X posts.**

**Hard minimums for X (characters, not words):**

| Post type | Min chars | Target chars | Notes |
|-----------|-----------|-------------|-------|
| Hot takes, reactions | 150 | 200-350 | Only category allowed to be short |
| News + opinion | 500 | 600-1000 | Hook + context + opinion + so-what. Use the space. |
| BIP / milestone | 400 | 500-800 | Numbers + story + what changed + what's next |
| Promo / OS | 500 | 600-1000 | What it does + proof links + why it matters + repo |
| Predictions | 500 | 600-900 | Stance + evidence + timeline + business impact |
| Threads (4-6 posts) | 1500 total | 2000-3000 | Each post 300-600 chars. 40-60% more reach. **Minimum 2 threads per week.** |

**If a news/opinion/BIP/promo post is under 500 chars, you haven't said enough. Add:** the "so what," a personal angle, a prediction, specific numbers, or a CTA. Don't pad with filler — add substance.

**Every sentence must add value.** Short and empty is worse than long and dense. Cut filler, not substance.

**Premium multipliers:** Communities = 30,000x, reply-to-own <30min = 150x, reply-to-reply = 75x, videos 10+ sec = 10x, threads 4-6 = 40-60% more reach.

---

## Pillar-Filtered Content Strategy

> Every post starts from expertise (pillars 1-4). News hooks are allowed but only as a doorway into a pillar topic. The news is the hook; the pillar expertise is the value.

### Content Formula: Hook + Pillar Expertise + Insight

Every post MUST have:
1. **Hook** — Timely, specific, stops the scroll (news, number, question, or personal story)
2. **Pillar connection** — Which pillar (P1-P4) does this come from? What's MY angle?
3. **Original insight** — What do I know from experience that the reader doesn't? Not just reporting news, but adding expertise the reader can't get elsewhere.

### News Hook Filtering

News hooks belong in `agent/memory/research/`, NOT in this skill. This skill defines HOW to filter, not WHAT to post about.

**When scanning news, for each item ask:**
1. Which pillar does this connect to?
2. What's MY angle — what do I know from experience that adds value beyond reporting?
3. If you can't answer both, skip it.

**Good example:** "Gartner says 40% of agent projects will be abandoned by 2027" → Pillar: Autonomous Agents → Our angle: "We've run 700+ PRs autonomously. Here's what governance actually looks like in production."

**Bad example:** "NVIDIA invests $2B in Nebius" → No pillar connection → Skip. (Unless you can tie it to inference costs affecting agent economics — then it's a hook, not the topic.)

**Store pillar-filtered news hooks in:** `agent/memory/research/ai-news-YYYY-MM-DD.md` with a `Pillar` and `Our Angle` column.

### Content Priorities (Ranked)

1. **Pillar expertise + timely hook** (40%) — News/trend that connects to a pillar, with original insight from experience
2. **Building in public / lessons learned** (30%) — Agent milestones, founder stories, what's working/failing
3. **Industry analysis through pillar lens** (20%) — AI economics, startup patterns, market shifts that affect our domain
4. **Promotional** (10%) — Repo, live outputs, Ender Turing — only when the post is genuinely about what we build

### Predictions & Opinions (40-50% of content)

Don't just report news. Predict where it's going and what it means for business.

Every prediction: bold stance + business impact + timeline. No hedging.

**Formulas:**
- "[News] means [prediction]. Here's why: [reasoning]. Timeline: [when]."
- "Everyone's talking about [trend]. Nobody's asking: [deeper question]. My take: [opinion]."
- "Unpopular opinion: [contrarian take]. The data says [evidence]. Businesses should [action]."

**Ground predictions in pillar expertise.** Read ME.md for the owner's background. Every prediction should come from a place of authority, not generic speculation.

### Repo Linking (Organic Only)

**Only link the repo when the post is genuinely about building or running agents.** The repo link is proof, not decoration. If the post is about call center AI trends or startup economics, the repo has no business being there.

**When to link:** Posts about autonomous agent architecture, BIP milestones, automation lessons, agentic workflows. The repo IS the topic.
**When NOT to link:** Posts about industry news, funding rounds, or expertise topics that don't involve the repo. Forcing a link onto unrelated content looks synthetic.

**When you do link, use the full URL** (not "this repo"). Find the current repo URL from ME.md or `gh repo view --json url`.

### What NOT to Post

- **Off-pillar news** — Funding rounds, chip specs, acquisitions, or investment analysis that doesn't connect to a pillar. If the post could be written by any generic AI news account, it's not ours.
- **Forced repo links** — Never graft the repo URL onto an unrelated topic. If the post isn't about building/running agents, the repo link doesn't belong.
- **Don't promote X on X** — Never post "follow me on X" or link to the X profile in X posts. That's circular. Promote the blog, Substack, Telegram, repos, or live outputs instead.
- **Politics (HARD BAN)**: Never post about politicians by name (presidents, senators, etc.), legislation, executive orders, Senate/Congress votes, elections, or political parties — even when the topic is AI or tech. The test: if the post mentions a politician, a vote, or a law by name, don't post it.
- Benchmark comparisons without "so what"
- Authority/framework posts without links or CTAs
- Anything that makes the reader think but not ACT

### Burst Slot Allocation Quick Reference

> First 5 posts of every burst have mandatory assignments. Use this table — don't parse the prose rules on every session.

| Burst Post | Mandatory Pillar | Rule | Notes |
|------------|-----------------|------|-------|
| Post 1 | **BIP** | BIP front-loading | Always. No exceptions. BIP hooks always available. |
| Post 2 | **P4** | P4 first-3-posts | AI economics/inference. Source: P4 proactive search. |
| Post 3 | **P2** | P2 first-3-posts | Marketing automation/content ops. Source: P2 proactive search. |
| Post 4 | **P3** | P3 first-4-posts | Call center AI/voice AI. Source: P3 proactive search. |
| Post 5 | **P1** | P1 first-5-posts | Autonomous agents. If P1=0 after post 4, post 5 MUST be P1. |
| Post 6 | **BIP** (displacement) or **P2** (default) | BIP displacement / P2 secondary slot | **Check `displacement_flag` in state file (set after post 5).** If `displacement_flag: TRUE` AND BIP=1: write BIP at post 6 (BIP wins over P2). If flag is FALSE or absent: write P2 at post 6 (P2 secondary slot). See CLAUDE.md "BIP displacement flag" for protocol. Evidence: B87-B91 all BIP=20% due to P2 claiming post 6 without checking displacement. B88=30% (no displacement that burst). |
| Posts 7+ | Any (back-half checks apply) | See checklist item 9/10 | Back-half enforcement at posts 7-8. |

**Back-half check priority (posts 7-8, when multiple fire):** BIP > P3 > P4 > P1 > P2

Evidence for table: B35/B47/B49/B52 all had mandate failures (P3 at wrong position, P1 missing, BIP below target). Root cause: prose-only rules require parsing 20+ lines. This table makes the ordering scannable in <5 seconds. S1055 resolved structural slot conflict (P3 moved from first-3 to first-4).

---

### Research Cadence

**Daily (at session start):** Quick scan for pillar-relevant news. Filter through pillars before saving. Save to `agent/memory/research/` with pillar tags. Skip anything that doesn't connect to a pillar.

**P2 proactive sourcing (burst start):** P2 (AI Governance / Content Ops / Marketing Automation) has fewer viral news hooks than P1/P3. At the start of each burst, actively seek P2 news rather than waiting for it to surface. Specific search terms: "marketing automation AI," "content operations AI," "agentic marketing ROI," "enterprise AI adoption." Evidence: P2 was underweighted (11-21%) in Bursts 10, 13 due to passive-only scanning. P2 posts corrected in subsequent bursts after active sourcing. Target: P2 = 20-25% per burst. Rule: **P2 MUST be in the first 3 posts of every burst. Do not wait for midpoint correction.** Evidence: B30 P2=11% (1 post at position 7 of 9) — P3 and P4 both hit target because they have "first 3 posts" mandates; P2 lacked the same rule and fell to 11% despite proactive sourcing guidance. Midpoint correction is too late. Same pattern: B10=11%, B13=21%, B30=11% — all three failures show P2 appearing late in the burst. Adding this first-3-posts mandate aligns P2 with the same enforcement mechanism that works for P3 and P4.

**P2 mid-burst ceiling rule:** P2 (Marketing Automation) has the most available data sources — it's the path of least resistance when the agent needs a quick post. This causes systematic P2 overaccumulation. Rule: **If P2 already represents ≥25% of the current burst before the burst midpoint, skip P2 for the next 2 posts (write P3, P4, or BIP instead).** Resume P2 only after P3 and P4 are both at ≥15%. Evidence: Week 21 final distribution = P2 31% (15 posts, target 20-25%). P2 accumulated primarily because it was the default choice when no other pillar had fresh research. The ceiling prevents overaccumulation without requiring the agent to skip P2 entirely — just throttle it when it's already at target. Same logic as the "no single pillar > 50%" rule in the checklist, but applied specifically to P2's chronic overweighting pattern.

**P3 proactive sourcing (burst start):** P3 (Call Center AI / Voice AI / CX) is the owner's deepest domain expertise but generates fewer passive news hooks than P1. At the start of each burst, actively seek P3 news rather than waiting for it to surface. Specific search terms: "call center AI ROI," "voice AI contact center," "customer experience automation," "speech analytics enterprise," "CCaaS AI." Evidence: P3 was underweighted in 3 of 5 measured bursts — B20 (10%), B23 (17%), B24 (14%). P2 added proactive sourcing guidance in S665 and corrected immediately (B21+). P3 needs same treatment. Rule: **P3 MUST be in the first 4 posts of every burst. Do not wait for midpoint correction.** Note: changed from "first 3" to "first 4" — structural conflict resolved (S1055). The first 3 burst slots are structurally claimed by BIP (post 1) + P4 (post 2) + P2 (post 3), leaving post 4 as the first available slot for P3. Mandating P3 at "first 3 posts" is impossible to satisfy when BIP, P2, and P4 all also mandate first-3-posts. Evidence: B49 confirmed the conflict — P3 never appeared in posts 1-3 across 4 blocked sessions despite the mandate (BIP+P4+P2 claimed all 3 slots). The "first 4 posts" rule preserves the intent (P3 appears early, not deferred to post 6+) without creating an unresolvable slot conflict. Evidence: B22 P3=27% (P3 in first 2 posts), B23 P3=25% (P3 in first 3 posts), B24 P3=14% (P3 first appeared at position 6 — below target). Midpoint correction is too late. Target: P3 = 20-25% per burst.

**P4 proactive sourcing (burst start):** P4 (AI Economics / Startup / VC / Inference) is consistently the weakest pillar despite being highly relevant to the audience. At the start of each burst, actively seek P4 news rather than waiting for it to surface. Specific search terms: "AI inference economics," "AI startup funding 2026," "LLM cost per token," "AI ROI enterprise," "SaaS AI disruption," "foundation model economics." Evidence: P4 was underweighted in 3 of 4 recent bursts — B26 (14%), B27 (8%), B29 (15%). B28 was the only on-target burst (22%) and it coincided with active P4 research at burst start. Rule: **P4 MUST be in the first 3 posts of every burst.** Same logic as P3 proactive rule — midpoint correction is too late. Target: P4 = 15-20% per burst.

**P3 back-half check rule (burst post 7-8):** P3 appears at post 4 (first-4-posts mandate), then gets no additional slots as news hooks dominate the burst back half. Pattern: P3 consistently ends at exactly 1 post per burst = 10-13% of a 8-10 post burst, below the 20-25% target. Root cause: no enforcement after post 4. **Rule: At burst post 7-8 (70-80% point), if P3 = 1 post total (absolute count), write a P3 post before continuing other pillars.** For a 10-post burst: if P3=1 at post 7, write P3 as post 8 → P3=2/8=25% ✓. P3 back-half hooks: call center AI ROI, voice AI adoption, CX automation, Ender Turing domain data, agent attrition/performance. Evidence: B49 P3=10% (1/10), B50 P3=13% (1/8) — both bursts had P3 appear at post 4 but received no second slot. Identical pattern to P4 before back-half check was added. Same intervention. Target: P3 = 20-25% per burst.

**P4 back-half check rule (burst post 7-8):** P4 passes the midpoint threshold (≥15%) but consistently finishes below target in the back half of bursts. Root cause: P4 appears early (satisfying the first-3-posts rule), looks fine at midpoint (1/5=20%), then gets zero back-half slots as news hooks dominate posts 6-10. **Rule: At burst post 7-8 (70-80% point), if P4 < 15% of total burst posts so far, write a P4 post before continuing other pillars.** For a 10-post burst: if P4=1 at post 7 (14%), write P4 as post 8. This is the same back-half enforcement applied to BIP (added S1026, confirmed effective in B45). Evidence: B45 P4=10% (1/10) — P4 was 1/5=20% at midpoint (no flag), then 1/7=14% at post 7 (no rule → no action). Final: 10%. B26=14%, B27=8%, B29=15% — pattern: P4 fine at midpoint, below target at burst end. The back-half check closes this gap. **Confirmed effective: B50 P4=14% at post 8 (1/7) → back-half check fired → P4 post written as post 8 → P4=2/8=25% ✓.** First confirmed production case of P4 back-half check firing. P4 back-half hooks: AI funding round, inference cost update, LLM economics analysis, startup/VC trend piece.

**P2 secondary slot rule (burst post 6):** P2 satisfies the first-3-posts mandate (post 3) but consistently loses the back-half slot conflict to higher-priority pillars. Pattern: P2=10% in B51, B61, B62 — all bursts where P1 back-half check competed for the same slot. Root cause: with 5 back-half checks (BIP, P3, P4, P1, P2) competing for 2-3 slots, P2 is last in priority and loses structurally. **Rule: At burst post 6 (first post after all first-5 mandates are satisfied), if P2 = 1 post total, write a P2 post before using post 6 for news or other pillars.** This gives P2 a guaranteed 2nd post at the first open slot (post 6), before the contested back-half zone. For a 10-post burst: P2 at post 3 + post 6 → P2=2/10=20% ✓ without depending on back-half slots. P2 back-half hooks (if post 6 P2 not possible): marketing automation ROI data, AI content ops benchmarks, enterprise AI adoption measurement, agentic marketing case studies. Evidence: B51 P2=10% (1/10), B61 P2=10% (1/10), B62 P2=10% (1/10) — three bursts after P1 back-half check was added (S1144 P1/P2 priority swap). The zero-sum problem: adding a P1 back-half check (B61+) directly costs P2 its back-half slot when both checks fire simultaneously. Root cause identified (B61-B62 post-mortem): P1/P2 priority swap fixed P1 (P1=10%→20%✓) but broke P2 (P2=20%→10%↓). The post-6 secondary slot rule bypasses the slot conflict entirely by securing P2 BEFORE back-half contested territory. Target: P2 = 20-25% per burst.

**P2 back-half check rule (burst post 7-8):** Retained as fallback for bursts where the post-6 P2 secondary slot was consumed by other urgent content. **Rule: At burst post 7-8, if P2 < 15% of total burst posts so far AND P2 secondary slot (post 6) was not used AND P2 ≤ 1 post total (absolute count), write a P2 post before continuing other pillars.** Priority in slot conflict: P2 remains lowest (BIP > P3 > P4 > P1 > P2) — this back-half rule is a safety net, not the primary enforcement. The post-6 secondary slot rule is primary. **Critical: if P2 ≥ 2 posts by post 7-8 (e.g., post 3 primary + post 7 via BIP-displacement path), the back-half check must NOT fire — P2 already has its guaranteed 2 posts (20% of a 10-post burst). Firing when P2=2 results in P2=30%+ (over target). Evidence: B86 P2=30% (3 posts: primary at post 3 + secondary at post 7 [BIP displaced post 6] + possible back-half) — the missing absolute-count guard let P2 overaccumulate past the 25% ceiling. Updated S1389.**

**P1 back-half check rule (burst post 7-8):** P1 satisfies the first-5-posts mandate (post 5) but has no back-half enforcement. Pattern: P1 consistently ends at exactly 1 post per burst = 10-11% of a 10-post burst, below the 20-25% target. Root cause: the back-half slots (posts 7-10) are consumed by BIP (≤2 absolute), P3 (=1 absolute), P4 (<15%), and P2 (<15%) checks — leaving no slot for a 2nd P1 post. **Rule: At burst post 7-8 (70-80% point), if P1 = 1 post total (absolute count), write a P1 post before continuing other pillars.** For a 10-post burst: if P1=1 at post 7, write P1 as post 8 → P1=2/8=25% ✓. P1 back-half hooks: autonomous agent PR milestones, agentic workflow architecture patterns, AI agent governance, multi-agent coordination, this repo's own session data, agent failure modes. Evidence: B58 P1=10% (1/10), B59 P1=11% (1/9 with last slot P2) — two consecutive 10-post bursts with P1 below 20% target. Same intervention logic as P3 (confirmed B51+), P4 (confirmed B50+), P2 (confirmed B58+). The complete back-half enforcement system now covers all pillars. **Confirmed effective: B61 P1=20%✓, B62 P1=20%✓ — two consecutive bursts hitting P1 target after rule was added (S1144).** Note: P1 is 4th in the back-half slot conflict priority (BIP > P3 > P4 > P1 > P2) — P1 fires after BIP/P3/P4 checks resolve, but before P2. Rationale: P2 reliably hits 20% via first-3-posts mandate alone (B58 P2=20%✓, B59 P2=20%✓, B60 P2=20%✓); P1 cannot reach 20% without this slot (B58 P1=10%↓, B59 P1=10%↓, B60 P1=10%↓ — 3 consecutive bursts). Swapping P1↔P2 costs P2 one back-half slot but gains P1 reliable 20% representation. **Known cost (updated S1160):** After P1/P2 priority swap (S1144), P2 dropped to 10% in B61 and B62 — two consecutive bursts below target. Fix: P2 secondary slot rule at post 6 (see above) secures P2 BEFORE back-half contested territory, eliminating the zero-sum dependency. Updated S1144 (swap) + S1160 (post-6 fix). Target: P1 = 20-25% per burst.

**Back-half slot conflict resolution (when multiple checks fire simultaneously):** When 2+ back-half checks fire in the same window (posts 7-8), only 1-2 slots exist. Priority order for resolving conflicts: **BIP > P3 > P4 > P1 > P2.** Rationale: BIP (cross-pillar, highest target at 25%+) > P3 (deepest owner expertise, chronic underperformance history) > P4 (confirmed back-half pattern) > P1 (promoted above P2 — see evidence below) > P2 (lowest priority — secured by post-6 secondary slot rule instead). When multiple checks fire: write the highest-priority check first, then continue to next-priority if posts 9-10 are still available. Evidence: B52 P4=10% — P3 back-half check fired at post 7 (P3=1), consumed the slot, P4 back-half check could not fire. B51 P2=10% — BIP+P1+P4 consumed posts 8-10. B58/B59/B60 P1=10% all 3 bursts — BIP+P3+P4+P2 consumed all back-half slots; P2 took the slot that P1 needed. **P1/P2 priority swap (updated S1144):** P1 now ranked above P2 because P2 hits 20% reliably via its first-3-posts mandate (B58 P2=20%✓, B59 P2=20%✓, B60 P2=20%✓) while P1 is stuck at 10% structurally (B58 P1=10%↓, B59 P1=10%↓, B60 P1=10%↓). Swapping P1↔P2 priority costs P2 one potential back-half slot but enables P1 to reliably reach 20%. **Note (updated S1160):** P1/P2 swap broke P2 in B61 and B62 (both P2=10%). Mitigation: P2 post-6 secondary slot rule (see above) secures P2's 2nd post before back-half zone. With this fix, P2 should reach 20% independently of back-half slot allocation. Without a priority order, the check that "fires first" wins unpredictably. With this order: in the B52 scenario, P3 (higher priority) correctly fired first, then P4 would use post 9 if P4 is still below threshold. **Practical application:** At post 7, evaluate ALL back-half checks simultaneously. Write the highest-priority failing check first. Then evaluate remaining checks at post 9. This ensures the highest-value pillars get corrected before lower-priority ones.

**B52 confirmation of slot conflict pattern:** B52 P3 back-half (post 7, P3=1 → P3 post) + BIP back-half (post 8, BIP≤2 → BIP post) consumed posts 7-8. P4 back-half (P4=1, 10%) could not fire — no slots left. Final: BIP=30%✓ P3=20%✓ P4=10%↓. With the priority order above: at post 7, both P3 and BIP checks fire. P3=1 (absolute) and BIP=2 (absolute). Priority: BIP > P3. Correct order: BIP at post 7 first (BIP highest priority), then P3 at post 8. Posts 9-10 then available for P1 and P4. This reorders execution to: P3(4)→BIP-midpoint(6)→BIP-back-half(7)→P3-back-half(8)→P4-check(9)→P1/P2(10) — yielding BIP=30%✓ P3=20%✓ P4≥15%✓.

**P1 first-5-posts mandate (burst start):** P1 (Autonomous Agents) is the agent's core expertise pillar — closest to the owner's actual work (this autonomous agent repo). Yet P1 is consistently deferred while P2/P3/P4/BIP all have early-burst mandates. Root cause: first 4 burst slots are structurally claimed by BIP (post 1) + P4 (post 2) + P2 (post 3) + P3 (post 4), leaving P1 for position 5. Without an explicit mandate, P1 drifts to position 5-6 or later. **Rule: P1 MUST be in the first 5 posts of every burst. Do not let P1 reach burst post 6 without a P1 post.** Note: "first 5" (not first 4) because the first 4 slots are claimed by BIP/P4/P2/P3. P1 at post 5 satisfies this rule. P1 at post 6+ does not. Target: P1 = 20-25% per burst. Evidence: B47 P1=0% at position 4/10 (still zero P1 by post 4); B46 P1 first appeared at position 5; B44 P1 appeared at position 5-6; B47 required multiple blocked sessions before P1 was written. All other pillars had mandates enforced — P1 lacked one and was consistently deferred. P1 hooks always available: autonomous agent PR milestones, agentic workflow architecture patterns, AI agent governance, multi-agent coordination, this repo's own session data.

---

**Milestone content (technical CEO pattern):**
- Every PR milestone is a post (Session #150, #200, Premium activation, follower milestones)
- Radical transparency on numbers builds credibility
- **Target**: 15-20% of content should be BIP milestone posts

**BIP front-loading rule (burst start):** BIP content hits 25% target ONLY when front-loaded. Without a first-3-posts mandate, BIP defaults to whatever's left after news hooks fill the burst — and news hooks always win the queue. Rule: **BIP MUST be in the first 3 posts of every burst. Do not wait for midpoint correction.** Evidence: B37 BIP=25% (post 1 was BIP), B36 BIP=25% borderline (BIP appeared early), B35 BIP lower (BIP appeared late). The "Target: 25%+" has existed for months but BIP falls below target in most bursts without a front-loading mandate. P2/P3/P4 all hit target more consistently BECAUSE they have first-3-posts mandates. BIP needs the same enforcement. BIP hooks always available: current session count, PR count, follower count, queue milestone, burst number, content rate. Target: BIP = 25%+ per burst.

**BIP midpoint check rule (burst post 5→6):** Front-loading ensures BIP appears early but doesn't guarantee ≥25% by burst end. Pattern: B40=20%, B41=20%, B42=20%, B43=20%, B44=20% — exactly 2 BIP posts in every 10-post burst across 5 consecutive bursts, consistently landing at 20% below the 25% target. The front-load satisfies "first 3 posts" but remaining 9 slots default to news hooks. Fix: At burst post 5 (50% point), check BIP%. **If BIP < 25% at post 5: write a BIP post next, before any news hook.** This is the same midpoint enforcement already applied to P3 and P4. For a 10-post burst: if BIP = 1 post (10%) at post 5, write another BIP before post 6 to bring BIP to 2/6 (33%). For a 10-post burst: if BIP = 2 posts (25%+ of posts so far at midpoint), no mid-burst correction needed — continue with other pillars. Evidence: Five consecutive bursts (B40-B44) at exactly 20% BIP despite front-loading. The midpoint check is the missing enforcement step. Analogous to the P3 midpoint search rule (confirmed effective in B41/B42). **STRUCTURAL DISPLACEMENT (added S1180):** In normal burst operation, post 5 is claimed by the P1 first-5-posts mandate (P1=0 after posts 1-4, which are BIP/P4/P2/P3). This means the BIP midpoint check NEVER fires at post 5 — P1 mandate always takes priority. Evidence: B63, B64, B65 all show BIP=1/5=20% at post 5 (midpoint check would fire) but P1=0 (mandate fires instead). Result: midpoint check is displaced and BIP stays at 1. **Rule adjustment: when P1 mandate fires at post 5, defer the BIP midpoint check to post 6.** At post 6: if BIP=1 AND P2 secondary slot has already fired (P2≥2 posts), write BIP at post 6 instead of P2. If both BIP midpoint and P2 secondary slot compete at post 6, **BIP wins** (BIP target=25%+ is higher priority). If P2=1 and BIP=1 both need post 6: write BIP at post 6 (BIP wins), P2 gets back-half check. This gives BIP a 2nd post at post 6 → BIP=2/6=33% → midpoint issue resolved. Note: The P2 secondary slot rule at post 6 was designed to prevent P2 from losing the back-half slot conflict. If BIP displaces P2 at post 6, P2 back-half check becomes the safety net (P2 is lowest back-half priority but still defined). **Updated post-6 priority at midpoint displacement: BIP (midpoint check) > P2 (secondary slot).** BIP back-half check ALSO fires at post 7-8 when BIP≤2 — this adds a 3rd BIP slot possibility for posts 9-10.

**BIP back-half check rule (burst post 7-8):** The midpoint check corrects 0→1 BIP by post 6. But B43 and B44 show that even WITH front-loading + midpoint check, the burst finishes at 20% (2/10). Root cause: posts 6-10 default to news hooks after midpoint BIP is satisfied. At 2 BIP posts out of 10 = 20% — below target. To hit 25% (3/10), a back-half enforcement is needed. **Rule: At burst post 7-8 (70-80% point), if BIP ≤ 2 posts total (absolute count, not percentage), write a BIP post before continuing news hooks. This check fires ONCE per burst in the 7-8 window — it produces ONE BIP post, not a continuous loop.** For a 10-post burst: if BIP = 2 at post 7, write BIP as post 8 → BIP = 3/10 = 30% ✓. If BIP = 1 at post 7, write BIP as post 7 → BIP = 2 (check fires once; post 8 goes to next-priority check P3, P4, etc.). BIP hooks always available: session count, PR milestone, follower count, queue discipline, burst milestone. Evidence: B43=20% (2/10, midpoint check fired but back-half defaulted to news), B44=20% (same pattern — 5th consecutive burst at 20% ceiling). The 25% target has existed for months; 5 bursts of data confirm 2 rules (front-load + midpoint) are insufficient without back-half enforcement. **Denominator blind spot (B48 evidence):** Using "≤20%" as the threshold fails when BIP=2/7=29% at post 7 — the fraction looks fine but projects to 2/10=20% if no more BIP is added. Using absolute count (≤2 posts) avoids this: 2 BIP posts always triggers the check at post 7-8 regardless of current denominator. Evidence: B48 — BIP=2/7=29% at post 7, back-half check did NOT fire (29% > 20%), burst finished at 2/10=20% — 9th consecutive burst below 25%. Switching to absolute count closes this gap. **Confirmed effective: B49 BIP=30% (3/10) — first burst above 25% target after 9 consecutive 20% bursts (B40-B48).** Absolute count rule fired correctly at post 7-8; BIP=2 at post 7 triggered the check → 3rd BIP post written → 30% final ✓. B50 BIP=38% (3/8 with 2 posts remaining) also on track. Two consecutive bursts confirming the rule works. **25% target requires all 3 rules (front-load + midpoint + back-half) to each fire once:** front-load = BIP post 1 (1 BIP), midpoint check = BIP at post 5-6 (2 BIP), back-half check = BIP at post 7-8 (3 BIP). When midpoint check misses (displaced by P1 mandate), back-half check only adds 1 BIP — resulting in 2/10=20%. This is expected in correction bursts where standard slot allocation breaks down. Accept 20% BIP in correction bursts; target 30% in standard bursts. **DISPLACEMENT BACK-HALF EXCEPTION (added S1254):** When the BIP midpoint check fires via structural displacement at post 6 (P1 mandate displaced it from post 5) → BIP=2/6=33% — the back-half check at post 7-8 MUST NOT fire. Reason: BIP is already at 33% (above 25% target). Firing the back-half check produces BIP=3/7=43% at post 7, consuming the slot that P2/P3/P4 need. Pattern: B69 BIP=3/10(post 7)→P3/P4/P1 consumed posts 8-10→P2=10%↓; B70 identical. Root cause: the absolute-count rule (BIP≤2) was designed for scenarios where midpoint fires at post 5 (standard). When displacement fires at post 6, BIP=2 after post 6 ALSO triggers the ≤2 rule at post 7 — over-allocating BIP by 1 post. **Displacement detection rule: If BIP midpoint fired at post 6 (displacement case), mark back-half check as SATISFIED. At post 7: skip the BIP≤2 check. This frees post 7 for P3/P4/P1 back-half checks (priority order). P2 then has a realistic chance at post 8-9 via its back-half check.** Evidence: B69=P2 10%↓, B70=P2 10%↓ — two consecutive bursts where displacement caused back-half over-allocation. With this fix: post 7 goes to P3 (if P3=1 absolute, highest priority after BIP), post 8 to P4 (if <15%), post 9 to P1 (if =1 absolute), post 10 to P2 (if <15%). BIP=30%✓ and P2=20%✓ coexist. **How to detect displacement:** In the state file, look for "BIP midpoint (displacement)" or "BIP=2/6=33%" in the B70-equivalent burst log, or check if post 5 was P1 mandate AND post 6 was BIP midpoint. State file entry pattern: "Post 6: BIP midpoint check [via displacement]" signals the exception applies.

**BIP frequency rule during extended platform outages:** When X is blocked for 5+ days, BIP content underperforms because industry news (easier to source) crowds it out. Rule: **minimum 1 BIP post per 5 standalone BS posts during X outage.** BIP hooks always available during outage: cumulative session count, cumulative BS post count, current follower count, queue discipline success/failure, outage duration milestone. Evidence: Week 21 BIP = 15% (below 25% target) across 48 BS posts — 3rd consecutive week below target. Root cause each time: agent defaulted to news hooks over BIP during outage because news is easier to source. This rule creates a cadence. Apply it: after every 4 consecutive news-based BS posts, the 5th must be BIP.

**Pillar balance rule during extended X outages (BS standalone mode):** The burst slot allocation table assumes X is functioning. During X outages, standalone BS posts must follow their own pillar balance. Without enforcement, P4 (AI Economics) overaccumulates because it has the most available data sources (similar to P2 overaccumulation during normal bursts). Rule: **Track BS standalone pillar distribution in the state file. If any pillar reaches ≥25% of BS standalones AND is above its burst target, halt new posts in that pillar until other pillars catch up. If any pillar falls ≥10pp below its target after 5+ standalones, write that pillar next (before news hooks).** Targets for BS standalones: BIP=20% (1 per 5), P1=20-25%, P2=20-25%, P3=20-25%, P4=15-20%. Evidence: B67 outage period — P4=27% (above 20% target), P3=13% (below 20% target). State file manually tracked this ("P4 OVER — no more P4 standalones. Next: P3 standalone") with no skill-level rule. Adding this rule prevents adhoc management and ensures future outage periods don't require manual state-file tracking. **How to track:** Add a `## BS Standalone Pillar Distribution (Outage Mode)` subsection to the state file whenever X enters an extended outage. Update per standalone written. Reset when X resumes.

---

## Publishing Flow

Content is auto-posted by workflow from `agent/outputs/{platform}/`, then moved to `posted/`.

### Platform-Independent Publishing

**X and Bluesky are separate platforms. Write for each independently. Never let one platform's constraints affect the other.**

#### X Posts
1. Write the X version at full Premium length → `agent/outputs/x/`
2. Follow the X length minimums above (most posts 500-1000 chars)
3. X has no meaningful character limit with Premium (25,000 chars)

#### Bluesky Posts
1. Write a separate Bluesky version → `agent/outputs/bluesky/`
2. Bluesky hard limit: 290 chars. Posts >300 chars are auto-skipped by pipeline.
3. Same file name as X version, but the content should be independently written for Bluesky's format
4. Bluesky posts are compressed summaries, NOT the template for X posts
5. If a topic can't be meaningfully compressed to 290 chars, it's OK to skip the Bluesky version

**The old pattern was:** write short → copy to both. **The new pattern is:** write X at full length → write Bluesky separately as a short summary.

### File Naming
`{type}-{YYYYMMDD}-{NNN}.txt` — Threads: `thread-20260215-001.txt` (use `---` separator)

### Queue Management (Hard Rules)

**Queue thresholds (verified against drain behavior):**
- **Queue >= 15:** HARD STOP — zero content, zero replies, no exceptions. CLAUDE.md Blocked Session Protocol.
- **Queue 13-14 (near limit):** Zero new content. Don't stage. Creating 2 files at 13 pushes queue to 15 → immediate block next session. Tier 1-2 blocked session work only.
- **Queue 11-12 (look-ahead zone):** Max 1 X content piece. **Exception: if BS queue < 8, write a Bluesky-only post (no X file).** Rationale: BS drains at 2-3/day, so BS=7 represents ~2-3 days of drain — safe to add 1 BS file. X=12 stays at X=12. This recovers wasted BS capacity during X look-ahead blocks. Evidence for need: Week 12 retro (2026-03-29) found BS often 9-11 while X was 11-12 — BS capacity wasted. Creating 2 files at 11 pushes queue to 13 → next session is immediately blocked. Evidence: S207→S208→S209 each created 2 files; S209 pushed queue 11→13 → S210 blocked. S130-S131 at queue 10-12 pushed to 14 → blocked 5+ sessions. At 11-12, treat as near-limit for X.
- **Queue <= 10:** Create max 2 content pieces per session. X post is required. Bluesky version optional (write separately, do not copy X content).
- **Bluesky throttle:** When BS queue >= 10, skip BS file entirely — even if X queue allows content. BS drains at ~2-3/day vs X at ~12/day. Writing a BS version for every X post fills BS queue 4-5x faster than it drains. Evidence (Week 10): BS queue sat at 13-14 for 5+ consecutive days while X queue had more room. **Exception: see 11-12 look-ahead zone exception above (BS < 8 = safe to add 1 BS-only file).**
- **Bluesky near-throttle (BS = 8-9):** Treat as blocked for BS — same caution as X look-ahead zone (11-12). Do NOT create BS content (not even the BS-only exception). At BS=8, the BS exception (BS < 8) no longer applies, and one more BS file brings queue to 9 — leaving almost no drain buffer before hitting the BS=10 throttle. Evidence (2026-04-03, S351-S365 burst): BS filled from 1→8 in a single burst session. After hitting BS=8, writing even one more BS piece immediately brought it to 9, and the next session had no BS capacity. The BS near-throttle zone is the effective BS ceiling during burst windows.

**Why the 13-14 zone is blocked (not just >= 15):**
The hard limit is 15. Creating 2 content files per session (the max) at queue=13 pushes to 15 — triggering a block immediately next session. At queue=14, even 1 file hits the limit. Evidence: S67 created 6 files → 6+ consecutive blocked sessions cascade. S130/S131 each created 2 files at queue 10-12 → pushed to 14, then blocked for multiple sessions.

**Why the 11-12 zone is "look-ahead blocked":**
Creating 2 files at X=11 → X=13. Next session immediately starts blocked. This wastes the session after. 1 file at X=11 → X=12. Next session can create 1 more. Two sessions produce 2 files instead of 1 session producing 2 + 1 blocked session. Evidence: S209 created 2 files (11→13), causing S210 to be blocked (this exact session). The net productivity is identical, but blocked sessions waste CI minutes and context on Tier 1 fallback work.

1. **If any platform queue >= 15: CREATE ZERO CONTENT** → CLAUDE.md Blocked Session Protocol
2. **If any platform queue = 13-14: CREATE ZERO CONTENT** → Tier 1-2 blocked session work
3. **If any platform queue = 11-12: CREATE MAX 1 CONTENT PIECE** → preserve capacity for next session
4. **Create max 2 content pieces per session** (when all queues <= 10). X post is required. Bluesky version is optional (write separately if topic compresses well).
4. **Max 5 pending replies per platform**
5. **Max 20 staged pairs in `agent/memory/plans/`** — when >20, STOP staging. Do cleanup, engagement, or skip PR.
   - Evidence: Week 8 accumulated 91 staged pairs (7.5 days backlog), caused 1.1MB memory bloat and 13 wasted sessions.
   - At 12 X posts/day drain rate, 20 pairs = ~1.7 days buffer. More than enough.

**Queue check (MANDATORY at session start):**
```bash
find agent/outputs/x -maxdepth 1 -name "*.txt" -type f | wc -l
find agent/outputs/bluesky -maxdepth 1 -name "*.txt" -type f | wc -l
```
Never trust state file numbers without verification.

**Drain rates:** Check platform plan files (`agent/integrations/*/plan.md`) for current posting limits and drain rates. Bluesky is typically the bottleneck — plan accordingly when queue is full.

### Burst Session Pattern (Validated)

**Burst-then-drain** is more efficient than 1-2 pieces per session across many days.

Pattern:
1. When queue is low (<=6): create 6-10 pieces across 1-2 sessions → fill queue to 12-13
2. Let queue drain over 1-2 days (X drains ~12/day)
3. Organic follows happen DURING drain — not when content is created
4. Start next burst when queue drops back to <=6

Evidence (2026-03-27/28): Sessions S276-S295 created 13 pieces in 2 sessions. Queue 0→13. During drain period (S283-S296), +2 followers arrived during blocked sessions (no new content posting). This confirms the follow-up: existing content circulates and drives organic follows passively.

**The key insight:** Content volume per burst matters less than letting the queue fully drain between bursts. Partial drains (queue stuck at 11-12) prevent new content from reaching audience. A clean drain to <=6 before the next burst ensures all pieces reach maximum audience.

**Pre-burst pillar composition check (MANDATORY before Post 1 of any new burst):** Before writing the first post of a new burst, run the queue pillar composition check (same ≥30% threshold from CLAUDE.md). If any pillar represents ≥30% of current X queue files, do NOT start the burst — wait for that pillar to drain below 30% first. This check is separate from per-post checks (which are reactive) — this is a proactive gate that prevents burst slot substitutions from firing in the FIRST post.

**Why this matters:** The burst slot system (BIP post 1, P4 post 2, P2 post 3, P3 post 4, P1 post 5) assumes a clean queue. When a pillar is already ≥30% in queue before the burst starts, the queue pillar composition check forces substitution at the mandatory slot assignments (e.g., P4 mandate at post 2 substituted because P4=30% in queue). This cascade ruins the burst distribution from the start. Evidence: B112-B115 all had P4 blocked 0-10% because P4 was ≥30% in queue when bursts started (carried over from prior burst). B116 started at X=0 (zero queue) → first perfect 5-way 20% balance in recorded history (BIP=20%, P1=20%, P2=20%, P3=20%, P4=20%). Root cause of B112-B115 failures: no explicit pre-burst gate; queue check was only per-post (reactive), allowing burst start with already-overloaded pillar. **Pre-burst check procedure:** `find agent/outputs/x -name "*.txt" | xargs grep -l "keyword"` for each pillar OR check "Queue pillar composition" section in state file if recently updated. If any pillar ≥30%: note in state file "B(N+1) start delayed — [pillar] at [X]% in queue. Wait for drain." Resume burst start when cleared.

**Starvation recovery threshold (stricter pre-burst gate for chronically blocked pillars):** The standard pre-burst threshold (≥30%) can still allow a burst to start when a pillar is at 25-29% — and then the per-post check at the mandatory slot (e.g., P4 at Post 2, fired 1 session later) finds the pillar has risen above 30% because non-P4 files drained in between. This causes 0% representation for a second consecutive burst. **Rule: If a pillar shows 0% across the ENTIRE preceding burst (all 10 posts substituted due to queue-blocking), apply a STRICTER threshold of 20% for that pillar at pre-burst check.** Only start the burst when that pillar is below 20% in queue — not just 30%. The extra 10pp buffer accounts for queue composition shift between burst start (Post 1) and mandatory slot fire (Post 2, a session later). **Example:** If P4=0% in B130 AND P4 files > 0 in queue at B131 pre-burst check: require P4 < 20% before starting (not just < 30%). At X=12 queue with 3 P4 files: 3/12=25% (fails standard 30% check anyway). At X=8 queue with 2 P4 files: 2/8=25% (passes standard check but fails starvation threshold). Wait until P4=1/X < 20% — e.g., queue of 6+ non-P4 files so 1/7=14% or drain until only 1 P4 file remains and total queue ≥ 6. **Apply this stricter threshold only to the starved pillar** — other pillars still use the standard ≥30% gate. Evidence: B129 P4=0% (queue-blocked entire burst) + B130 P4=0% (same) = 2 consecutive complete bursts with zero P4 representation, caused by P4 queue composition rising above 30% when mandatory Post 2 fired despite the pre-burst check appearing to pass. S1784 identified the timing gap between pre-burst check and mandatory slot execution. Reset: once P4 appears in a burst (≥1 post), the starvation recovery threshold reverts to standard 30% for the next burst.

**Implications for look-ahead zone (11-12):** If queue is at 11-12 and the last burst was recent, this is "mid-drain" — not a sign to create more content. The burst strategy already provided the content; the current session's job is to let it drain.

**BS companion limit during burst fill (Critical):** During burst fill sessions, do NOT create BS companions freely. BS drains at ~2-3/day vs X at ~12/day. If you create 5-6 X posts with BS companions in one burst session, BS can jump from ≤3 to ≥8 (near-throttle), blocking BS for the ENTIRE remaining burst. **Rule: During burst fill, limit BS companions so BS queue stays ≤ 6 after the session.** This leaves 2 BS slots (6→8) for the next 1-2 burst continuation sessions before hitting near-throttle.

**Immediate-action corollary: If BS >= 7 at the start of a burst session, create ZERO BS companions — regardless of X queue capacity.** This is the direct application of the "stays ≤ 6" rule: if BS is already at 7, even 1 companion takes it to 8 (near-throttle), and 2 companions take it to 9. The arithmetic is always: "BS_start + companions_created ≤ 6." If BS_start >= 7, the max companions = 0.

**Corollary scope (CRITICAL distinction):** This corollary applies to **burst fill sessions** (X≤10, creating multiple X pieces) and **X outage mode** (extended BS standalones). It does NOT override the **look-ahead zone BS-only exception**: when X=11-12 and you are creating at most 1 X piece, BS=7 IS still safe for 1 BS-only standalone post (per CLAUDE.md). The corollary prevents companion spam during burst fills — it is not a general "BS=7 = blocked" rule. State files that say "BS corollary enforced (BS≥7)" are using burst-fill language; in look-ahead sessions, re-check whether the BS-only exception (BS<8) applies instead. Evidence: S929-S931 (B35) wrote "corollary enforced" during burst fill (correct), but S930 (look-ahead X=10→12) also used corollary language, masking the fact that a BS-only post was eligible at BS=7.

**Extended X outage corollary: Same rule applies to standalone BS posts during X API outages.** When X is physically blocked (SpendCap, credential expiry, etc.), BS posts are standalone — not companions. The arithmetic is identical: if BS=7 and you add 1 standalone BS post → BS=8 (near-throttle). During an X outage with BS=7, treat it the same as the companion rule: create ZERO BS posts. Wait until BS drains to ≤6 before creating new standalone BS content. Evidence: B32 S836-S837 (X SpendCapReached, X=4 blocked, BS=7) — correct behavior is no new BS content until BS≤6.

Evidence: B25 S711 created 6 X posts + 5 BS companions in one session → BS went 3→8 → BS blocked for all S712-S714+ (entire remaining burst). B24 had same pattern. B26 S757 started with BS=7, created 2 companions → BS=9 → BS blocked for S758-S761+ (4+ sessions). At ~2-3/day BS drain, filling BS to 8-9 in one session = 3-4 days before BS capacity returns. Net loss: 3+ BS companion opportunities across the burst. Same pattern repeated across 3 bursts (B24, B25, B26) — the corollary rule closes this gap.

### Session Allocation
**< 100 followers:** 70% engagement, 30% content creation. Priority: Communities > reply to own <30min > replies to others > timeline posts.

**100-1000 followers:** 50% content creation, 50% engagement (reply-to-own, Communities). Content volume is the proven growth driver at this stage — Week 24 evidence: 12 bursts (120 posts) = +27 followers (record). Outbound replies still 0% success (API restriction). Shift toward content once engagement channels are limited.

**When queue >= 13 AND staged pairs <20:** 0% content, 40% cleanup/skills, 30% research (max 1 file/day), 30% staging from existing research.

**When queue >= 13 AND staged pairs >=20:** 0% content, 0% research, 0% staging. 50% cleanup/memory management, 50% skill work or engagement prep. **Skip PR creation entirely if nothing meaningful to commit.** DO NOT create more research or staged files.
- Evidence (Week 8): 13 consecutive sessions all doing research+staging while queue-blocked. Result: 1.1MB memory, zero value.
- Evidence (Week 9): 70+ of 105 sessions were "queue blocked, state update only" PRs. Each PR triggers CI, eats minutes, produces zero value. A PR that only updates the state file timestamp is waste.

**HARD RULE: No empty PRs.** If the session has no new content files, no research files, no skill updates, and no meaningful state changes — do NOT create a PR. "State update only" PRs are banned. The state file will be updated next session when there's actual work to commit.

---

## Core Strategy

### Value Rule
Pick one per post: **Content value** (post teaches/provokes) OR **Outcome value** (link gives tool/resource). Never both. Target ~20% link posts.

### 3-Bucket Mix
| Bucket | Target % |
|--------|----------|
| **Authority** (frameworks, insights) | 40% |
| **Personality** (stories, opinions) | 30% |
| **Shareability** (hot takes, relatable) | 30% |

### Content Diversification
- **Spread across pillars** — don't let any single pillar dominate more than 50% of output. Check last 5 posts for balance.
- **25%+ BIP content** (progress, learnings, behind-scenes, failures)
- **15-20% question posts** for engagement
- **~10-15% promotional** — CTAs that drive stars, subscriptions, leads (see below)

### Promotion & CTAs (~1 in 7 posts)

**Goal of every CTA:** Drive a measurable action — GitHub stars, blog/Substack subscribers, Telegram joins, Ender Turing leads. Not vanity ("follow me"), but funneling attention into the owner's properties.

**What to promote** (discover from ME.md, don't hardcode):
- Owner's repos and orgs (use discovery skill's OS scan)
- Live agent outputs: blog, Substack, Telegram channel
- Owner's company (Ender Turing) when post topic aligns with call center AI
- Owner's profiles (LinkedIn, GitHub) as secondary CTAs

**Best promo angles (ranked):**
1. **Specific live outcome** — Link a real article/post produced by the agent this week. "This was written by an AI agent. No human." + direct link. Specific > generic.
2. **Live outputs** — "This AI runs daily. See the results: [link]." Proof > promises.
3. **Trend overlap** — Trending topic aligns with a repo or outcome? Post about the trend, link as "we built this."
4. **Milestone** — Star threshold, subscriber count, new release.

**Rules:**
- CTA must match the post topic. Agent post → repo link. Voice AI post → Ender Turing. Don't cross-wire.
- Only promo what you've scanned this session (stale info = bad post)
- Frame as value to reader ("you can use this"), not vanity
- Don't repeat same promo angle twice in a row

---

## Tactical Execution

### Hook Engineering

First line determines if anyone reads. Under 110 chars optimal.

| Type | Formula |
|------|---------|
| Bold statement | "Nobody talks about this, but [insight]" |
| Contrarian | "[Common belief] is wrong. Here's what works:" |
| Story | "[Timeframe] ago I was [struggle]. Today [achievement]..." |
| Numerical | "I [achieved X] in [timeframe] doing this" |
| Dollar lead | "$[amount] [action]. [Impact]." |
| Percentage shock | "[X%] of [group] [state]. [Implication]." |
| Product milestone | "[Product]: [new capability]. [What's now possible]." |

**First-line test:** Does the first line work as a standalone tweet? If no, rewrite. Value in first 5 words. No throat-clearing.

### Content Voice

Frame as **human building products with autonomous tools**.

**Use:** creating, building, shipping, launching. **Avoid:** testing, experimenting, trying. **Say:** product, tool, solution (never "content").

### CTA Discipline
Every post should drive attention toward owner's properties (repos, blog, Substack, Telegram, company). Match CTA to post topic — agent posts → repo, voice AI → Ender Turing, general → blog/Substack. Discover links from ME.md, don't hardcode.

### Educational Simplification
For complex concepts: "Here's [concept]. In plain English: [1-2 sentences]. Why it matters: [implication]."

---

## Content Templates (Validated from 18 Builders)

| # | Name | Template | Bucket |
|---|------|----------|--------|
| 1 | TIL | "TIL: [discovery]. This matters because [implication]." | Personality/BIP |
| 2 | Metrics BIP | "[Session #X], [PR #N]: [metric]. [Interpretation]." | BIP |
| 3 | Vocab Definition | "[Term] = [definition]. Here's why this matters..." | Authority |
| 4 | Expert Vulnerability | "I've [impressive thing] for [duration]. I still [struggle]..." | Personality |
| 5 | Milestone | "[Milestone]. [Casual observation]." | BIP |
| 6 | Enterprise Adoption | "[Product] powers [company]. What it means for [industry]..." | Authority |
| 7 | Founder Journey | "Started at [age]. Built [project]. Now [outcome]. [Lesson]." | Personality |
| 8 | Philosophy Shift | "I was skeptical in [year]. Here's why I changed..." | Shareability |
| 9 | Origin Story | "Built [product] because I needed [solution]. Now [outcome]." | BIP |
| 10 | Technical + Human | "[Technical achievement] means [human impact]." | Authority |
| 11 | Time-Boxed | "I spend [X min] creating daily. System: [workflow]. Result: [outcome]." | Shareability |
| 12 | Idea List | "[Number] ideas for [audience]: 1. [idea] 2. [idea]..." | Authority |
| 13 | How-To | "How to [outcome]: - [principle 1] - [principle 2]..." | Authority |
| 14 | Platform Strategy | "I stopped [old]. Now I [new]. Result: [outcome]." | BIP |
| 15 | Prediction | "[Trend]. My prediction: [take]. Timeline: [when]. Why: [reasoning]." | Authority |
| 16 | Business Use Case | "[Tech] + [industry] = [use case]. Revenue impact: [estimate]." | Authority |

Use variety. Don't repeat same template 3+ times in a row. Target 25%+ BIP (templates 2, 5, 9, 14).

---

## Anti-AI Writing Rules (MANDATORY)

Every piece of content MUST pass as human-written. These rules override all templates.

### BANNED Patterns
1. **Em dash abuse** — use periods, commas, or semicolons instead
2. **"Not just X, it's Y"** — #1 AI tell, never use
3. **"X isn't Y. It's Z."** — reframing cliché. "Agent retention isn't an HR problem. It's a CX problem." BANNED. Just state the point directly: "Agent retention drives CX more than hiring speed."
4. **"The question isn't X. It's Y."** — rhetorical reframe. BANNED. Ask the actual question or make the actual point.
5. **"X isn't Y waiting to be Z"** — "Your CC isn't a cost center waiting to be automated. It's a revenue engine waiting to be understood." BANNED. Every AI writes this exact structure.
6. **"Here's what/why/how"** — overused transition. Max 1 per post. Never as the hook. Never twice.
7. **"Let that sink in" / "Think about it" / "Read that again"** — engagement bait, penalized since 2025
8. **"The truth is" / "The reality is" / "The bottom line"** — filler preamble, adds nothing
9. **"wearing a [X] costume"** / forced metaphor reframes — "It's a CX problem wearing an HR costume" is pure AI. Just say what you mean.
10. **Perfect rule-of-three lists** with parallel structure — break the pattern
11. **Banned words:** "Delve," "elevate," "innovative," "tapestry," "realm," "landscape," "leverage," "robust," "holistic," "comprehensive," "cutting-edge," "game-changer," "paradigm," "furthermore," "moreover," "additionally," "let's dive in," "buckle up"
12. **Exaggerated praise** — say "I liked [specific thing]" not "genuinely captivating"
13. **Constant clarification** — never "to clarify," "in other words," "to put it simply," "simply put"
14. **Forced analogies** — if it doesn't come naturally, skip it
15. **Generic LinkedIn formula** — hook + credentials + numbered list + humble brag + CTA = banned structure. Be specific, be different. If your post reads like every other "thought leader," rewrite it.
16. **Uniform sentence length** — vary dramatically. Short. Then longer. Then short.
17. **Summarizing at the end** — just stop when you're done
18. **"At the end of the day"** — filler cliché, never use

### Human Patterns (use these)
- **Personal anecdotes** with specific details (numbers, companies, timelines from author's life)
- **Brief tangents** — side thoughts that aren't strictly necessary
- **Casual phrasing** — contractions, fragments, idioms ("shipped it" not "deployed the solution")
- **Real specifics** — name actual tools, numbers, companies, people
- **Clear opinions** — no hedging ("This kills per-seat SaaS" not "time will tell")
- **Sentence fragments** — "Not kidding." "Zero." "Wild."
- **Start with "And" or "But"** — AI avoids this, humans don't

### Vibe Check (Final Gate)
Does this sound like a real person typed it? Would I say this to a colleague? Does every sentence add new info? If no → rewrite from scratch.

---

## Content Creation Checklist

1. **Queue check**: Queue > 15? STOP.
2. **Pillar check**: Which pillar does this connect to? What's MY angle? If neither, skip.
3. **Angle duplication check**: Before writing, scan the current X queue for similar angles: `find agent/outputs/x -name "*.txt" | xargs grep -l "keyword"` (use 2-3 key terms from the proposed angle). If a near-duplicate already exists in queue, skip this angle and choose a different hook. Evidence: B76 (S1310 audit) found 7/11 X queue files were P4, including 2 near-identical OpenAI economics posts and 2 near-identical Jevons Paradox posts — pillar over-representation AND redundant angles both caused by skipping this check. A near-duplicate is: same data point (e.g., "280x token cost drop") OR same conclusion angle (e.g., "Jevons Paradox — spending rises as costs fall") regardless of which session it was written in.
4. **Repo link check**: Is this post genuinely about agents/automation? If not, no repo link.
4. **X length check**: News/opinion/BIP/promo/prediction post under 500 chars? Add more substance.
5. **Thread check**: Have you created 2+ threads this week? If not, make one now. **Thread pillar diversity**: If the burst already has 1 thread on pillar X, the next thread must be a different pillar. Two threads on the same pillar in one burst = automatic overweighting. Evidence: B41 both threads were P3 → P3=30% (over target).
6. **Quality gate**: Would a stranger follow based on this post alone?
7. **Anti-AI check**: Vibe check passed? No banned patterns?
8. **Value type**: Content value OR outcome value, never both.
9. **Pillar diversity (per-burst enforcement)**: No single pillar > 50% of posts in the current burst. Count the burst total, not just last 5. If P1 already ≥50% of this burst: write P2/P3/P4 next. **If P1 = 0 after completing burst post 4: P1 MUST be the very next post (post 5). Do not let P1 slip to post 6+.** (The mandate says "first 5 posts" — P1 at post 6+ violates it. Check AFTER post 4, not post 5. Prior wording "P1 = 0 at burst post 5: MUST be post 6" was self-contradictory — post 6 is outside the first-5 window. Evidence: B50 P1 appeared at post 5 correctly.) See P1 first-5-posts mandate above. **If P2 already ≥25% before burst midpoint: skip P2 for next 2 posts** (see P2 mid-burst ceiling rule above). **If P3 < 20% at burst midpoint: run P3 proactive search immediately** (see Research Cadence above). **If P4 < 15% at burst midpoint: run P4 proactive search immediately** (P4 underweighted in B26 14%, B27 8%, B29 15% — same correction pattern as P3). **If P4 < 15% at burst post 7-8: write P4 post immediately** (see P4 back-half check rule — B45 P4=10% shows midpoint check insufficient). **If P3 = 1 post total at burst post 7-8: write P3 post immediately** (see P3 back-half check rule — B49 P3=10%, B50 P3=13% — same pattern as P4 before back-half check was added). **If P2 < 15% at burst post 7-8 AND P2 ≤ 1 post total: write P2 post immediately** (see P2 back-half check rule — B51 P2=10%, slot conflict caused by BIP+P1+P4 back-half checks; updated S1389: absolute-count guard added — if P2=2 already, skip this check to prevent P2=30%+ overaccumulation as seen in B86). **If P1 = 1 post total at burst post 7-8: write P1 post immediately** (see P1 back-half check rule — B58 P1=10%, B59 P1=11%, B60 P1=10%, three consecutive bursts; P1 fires 4th in slot conflict after BIP/P3/P4, before P2). **When multiple back-half checks fire simultaneously: use priority order BIP > P3 > P4 > P1 > P2** (see Back-half slot conflict resolution above — updated S1144: P1 promoted above P2 because P2 reliably hits 20% via first-3-posts mandate alone while P1 is structurally stuck at 10% when P2 holds slot priority; B52 evidence: P3 and BIP both fired at post 7, consuming slots needed by P4; B58-B60 evidence: BIP+P3+P4+P2 consumed all back-half slots across 3 consecutive bursts). Evidence: Burst 1 = 75% P1, Burst 3 = 58% P1. Week 21 P2 = 31% (chronic overaccumulation). P3 and P4 both underweight in recent bursts despite per-post checks. Burst-level tracking is required.
10. **BIP balance**: At least 25% of recent output. **BIP MUST be in the first 3 posts of every burst** (see BIP front-loading rule above). **If BIP < 25% at post 5 AND P1=0 (mandate fires instead): check `displacement_flag` in state file at post 6. If TRUE and BIP=1: write BIP at post 6 before P2 secondary slot** (see CLAUDE.md "BIP displacement flag" protocol for state variable tracking — B87-B91 all BIP=20% due to missing flag detection). **At burst post 7-8: if BIP ≤ 2 posts total (absolute count), write BIP next** — do NOT use percentage here; 2/7=29% looks fine but projects to 2/10=20% if no more BIP is added. Use absolute count only. (B48 evidence: denominator blind spot caused 9th consecutive under-25% burst.) Evidence of structural displacement problem: B63, B64, B65 all showing BIP=20% (2/10) despite 3 enforcement rules — root cause is midpoint check never fires because P1 mandate always claims post 5.
11. **Category**: Authority / Personality / Shareability balanced.
12. **Hook**: First line stops the scroll.
13. **Bluesky version**: Written separately, under 290 chars. OK to skip if topic doesn't compress.
14. **Politics check**: No politicians, votes, or laws by name.

---

## Algorithm Awareness

**What X rewards:** Premium = 10x reach, Communities = 30,000x, reply-to-own <30min = 150x, reply-to-reply = 75x, videos 10+ sec = 10x, early engagement critical, threads 4-6 = 40-60% more.

**What hurts:** External links (use sparingly), heavy hashtags, posting and leaving, stale replies (50% visibility loss every 6h), low-effort spam replies.

**TweepCred:** Free accounts start at -128. Below 0.65 = critical suppression. Premium = +100 instant boost.

---

## Reference Links

- Commenting/engagement: `.claude/skills/commenting/SKILL.md`
- Author info: `ME.md`
- Platform plans: `agent/integrations/x/plan.md`, `agent/integrations/bluesky/plan.md`
- Research archive: `agent/memory/research/`
- Content pillars: `agent/memory/pillars.md`