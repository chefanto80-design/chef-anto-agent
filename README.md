# Chef Anto AI Agency 🌿

**A working Claude agent team for marketing and cooking, built by Chef Anto (Antoanela Alexander), Miami.**
*I am the heart. AI is the brain.*

The agency runs like a professional kitchen: the **Director** agent is the pass, and each specialist agent is a station. Chef Anto is the head chef and approves everything before it goes out.

- Portfolio: https://chef-antoai.netlify.app
- Brand home: https://chefanto.com
- Mission: save one billion meals from food waste

---

## The team

| Station | Skill file | What it does |
|---|---|---|
| Agency Director | [`skills/chef-anto-agent`](skills/chef-anto-agent/SKILL.md) | Reads the order, splits it into stations, checks the result, serves one package |
| Brand Kit Guardian | [`skills/chef-anto-brand-kit`](skills/chef-anto-brand-kit/SKILL.md) | Voice, taglines, colors, fonts, handles. Every piece is checked against it |
| Recipe Agent | [`skills/chef-anto-recipes`](skills/chef-anto-recipes/SKILL.md) | Fridge photo or ingredient list to 3 zero-waste recipes |
| Social Content Agent | [`skills/chef-anto-social`](skills/chef-anto-social/SKILL.md) | Instagram, TikTok, Facebook, LinkedIn, YouTube posts and reel scripts |
| Email Marketing Agent | [`skills/chef-anto-email`](skills/chef-anto-email/SKILL.md) | MailerLite newsletters, welcome sequences, list growth |
| Pop-up Ops Agent | [`skills/chef-anto-popup-ops`](skills/chef-anto-popup-ops/SKILL.md) | Baba / Dream House menus, prep timelines, shopping lists, costing |
| Website Agent | [`skills/chef-anto-website`](skills/chef-anto-website/SKILL.md) | Cozy, premium static sites ready for Netlify |
| Global Intelligence Agent | [`skills/chef-anto-global-intel`](skills/chef-anto-global-intel/SKILL.md) | Daily brief on food, water, energy, money and hospitality news |

Each folder holds one `SKILL.md`: the agent's full instructions, exactly as installed on Chef Anto's Claude account.

---

## How to use the agent

### Option 1: Claude app (Cowork or claude.ai)
1. Download this repo (green **Code** button → **Download ZIP**).
2. Zip each folder inside `skills/` on its own (for example `chef-anto-recipes.zip` containing the `chef-anto-recipes` folder with its `SKILL.md`).
3. In Claude's **Settings**, open the **Skills** section and upload each zip.
4. Start a chat and ask for the Director, for example:
   > Use the chef-anto-agent. My fridge has cabbage, eggs, dill and feta. Give me 3 recipes and an Instagram post.

The Director sends each part to the right station. If a station isn't installed, the Director does that part itself with its built-in fallback modes.

### Option 2: Claude Code
Copy the skill folders into your skills directory, then ask Claude to use them:
```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

### Good orders to try
- "3 recipes from this fridge photo" (attach a photo)
- "Write a LinkedIn post about building the Chef Anto app in public"
- "Welcome email #1 for the MailerLite 'Website Signups' group"
- "Plan Baba Tuesday for 20 guests: menu, shopping list and costing"
- "Give me today's Chef Anto Daily Brief"

### Rules the agents always follow
- **Drafts only.** They never post, send, book or pay. Chef Anto approves and publishes.
- No hype words, no fake reviews, no invented numbers.
- Every answer ends with the next 1–3 steps.

---

## Real demo: fridge to Instagram

Run on **2026-10-01 02:20 UTC** in Claude (Cowork), model `claude-opus-5-5`, using the `chef-anto-agent` skill.

**Input** ([full input](demo/01-fridge-to-instagram/input.md))
```
My fridge has half a head of green cabbage, 4 eggs, a bunch of dill that's starting to wilt,
1 cup plain Greek yogurt, 2 carrots, 2 cups leftover cooked rice, 1 red bell pepper and a
block of feta. Give me 3 recipes, then one Instagram post (A/B captions) promoting the
Chef Anto app using one of the recipes.
```

**Output** ([full output, verbatim](demo/01-fridge-to-instagram/output.md))
- Fridge sorted into *Use today / Use this week / Pantry*, with a food-safety note on the leftover rice
- 3 recipes: **Sarmale leneșe** (Romanian lazy cabbage rolls), **Dill & feta egg fried rice** (15 min), **Cabbage & feta fritters with dill yogurt** (Greek lahanopita-style)
- "Ingredients rescued: 8 | Meals made: 3 (about 8–9 servings)"
- Instagram post with Caption A (story) and Caption B (practical tip + lead magnet), hashtags, visual idea
- Brand-kit pass check table and next steps

Excerpt (Caption A):
> My grandmother never threw out half a cabbage. 🥬
> Tonight it became golden fritters with feta, carrot and the dill that was about to give up.
> Crispy edges, soft middle, a cool spoon of garlicky yogurt.
> With What We Have, always.

---

## Test results

Only tests that were actually run are reported. Details: [test-results.md](demo/01-fridge-to-instagram/test-results.md)

| # | Test | Result |
|---|---|---|
| 1 | Live run of `chef-anto-agent` on the demo order | ✅ Complete package produced, routed to Recipe, Social and Brand Kit stations |
| 2 | Automated brand-rule check: `python3 tests/check_output.py demo/01-fridge-to-instagram/output.md` | ✅ 15/15 passed |
| 3 | Checker sanity test on a deliberately bad sample | ✅ Caught the errors (3/15 passed, as expected) |

**Not tested yet:** recipes not cooked or taste-tested; post not published (no engagement data); email, pop-up ops, website and global-intel stations not run in this demo.

### Run the checker yourself
```bash
python3 tests/check_output.py demo/01-fridge-to-instagram/output.md
```
Needs only Python 3, no installs.

---

## Repo structure
```
skills/        8 agent instruction files (SKILL.md each)
demo/          real runs: input, verbatim output, test results
tests/         check_output.py, brand-rule checker
```

## Roadmap (agents in the lab)
Client Proposal Agent · Growth & Analytics Agent · Video Producer Agent

---

Built in Creativity Hub Miami's Digital Marketing AI Academy.

Chef Anto 🌿🤓❤️
