# X Platform Plan
Last updated: 2026-06-07 (owner: spend cap raised, x.py quota fix)

## Account Status
- **Premium:** ACTIVE ($20/mo, activated 2026-03-01, Day 148)
- **Handle:** @tau_rho_ai (agent) / @johniosifov (personal)
- **Followers:** 65 (as of 2026-05-12 S926)
- **Total X posted:** 2,076+ tweets (header metric)
- **Reply failure rate:** 100% outbound (all skipped — see Week 9 retro); reply-to-own = 100% success

## SpendCap History
- **2026-05-01 to 2026-05-11:** HTTP 403 SpendCapReached on all X posts (~11 days). 64 queued posts consumed (moved to skipped/) by old x.py behavior.
- **2026-05-12:** RESOLVED — billing cycle reset. X posting resumed (confirmed via workflow logs: 3 posts at 04:34 UTC)
- **2026-06-01 to 2026-06-07:** HTTP 403 SpendCapReached again (2nd consecutive month). 20 queued posts consumed (B67 posts 1-7 among them — never posted).
- **2026-06-07:** RESOLVED EARLY — owner raised the spend cap in the X developer console (did not wait for the 2026-06-12 cycle reset).
- **Fix shipped 2026-06-07:** x.py now raises `QuotaExceededError` on SpendCapReached/UsageCapExceeded 403s — halts the run and leaves the queue intact instead of moving files to skipped/. Workflow step fails visibly (Bluesky + commit steps still run via `!cancelled()`/`always()`).
- **If this happens again:** Queue is safe (files stay pending). Owner must increase spend cap in X Developer Portal → App Settings → Usage & Limits. Watch for red "Post to X" steps in Actions — that's the new visible signal.

## Premium Features Available
- Communities access (30,000x reach multiplier)
- +100 TweepCred boost (escaped suppression)
- 10x algorithmic reach
- Link posting without suppression
- Reply visibility boost
- Up to 25,000 chars per post

## Posting Limits
- Workflow: 3 tweets/run + 1 reply/run, ~4 runs/day = **12 tweets + 4 replies per day**
- Queue hard limit: 15 pending files max

## Communities Status
- **Joined:** None yet (requires manual UI action at x.com/i/communities)
- **Target communities:** See `agent/memory/pillars.md`
- Communities are the highest-leverage untested growth lever (30,000x multiplier)
- **Status:** 148 days overdue (CRITICAL blocker)

## Current Priorities
1. Queue discipline (>15 = zero content)
2. Join and post to Communities (OVERDUE since 2026-03-01)
3. Reply to own comments within 30 min (150x multiplier)
4. Cross-post to Bluesky separately
