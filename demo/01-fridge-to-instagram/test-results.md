# Demo 01 — Test results

Only tests that were actually run are listed here.

## Test 1: Live agent run
- **What:** Sent the prompt in [input.md](input.md) to the `chef-anto-agent` skill in Claude (Cowork), 2026-10-01 02:20 UTC, model claude-opus-5-5.
- **Result:** The agent produced one package: fridge sort, 3 recipes, an Instagram post with A/B captions, a brand-kit pass check and next steps. Saved verbatim in [output.md](output.md).
- **Routing:** the Director split the order into Recipe Agent, Social Content Agent and Brand Kit Guardian, as its instructions say.

## Test 2: Automated brand-rule check
- **What:** `python3 tests/check_output.py demo/01-fridge-to-instagram/output.md` (Python 3.11.15)
- **Result:** **15/15 checks passed**

```
PASS  No hype word 'revolutionary'
PASS  No hype word 'game-changer'
PASS  No hype word 'hurry'
PASS  No hype word 'deal'
PASS  No legacy app name (FridgeChef AI / Larder)  (found 0)
PASS  Sign-off 'Chef Anto 🌿🤓❤️' present  (3 found)
PASS  Exactly 3 recipes  (3 found)
PASS  At least one Balkan dish
PASS  Meals-saved line present
PASS  Zero-waste tip in every recipe
PASS  A/B captions present
PASS  App CTA present
PASS  Email lead magnet CTA present
PASS  Food-safety note present
PASS  States it is a draft / not posted

15/15 checks passed
```

## Test 3: Checker sanity test (does it catch mistakes?)
- **What:** Ran the same checker on a deliberately bad 2-line sample ("This revolutionary FridgeChef AI recipe!").
- **Result:** **3/15 passed**, so the checker correctly flags hype words, the old app name, missing sign-off and missing sections.

## Not tested (yet)
- Recipes were not cooked or taste-tested.
- The Instagram post was not published, so there is no engagement data.
- The other stations (email, pop-up ops, website, global intel) were not run in this demo.
