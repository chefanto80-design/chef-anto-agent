"""Brand-rule checks for a Chef Anto agent output file.

Usage: python tests/check_output.py demo/01-fridge-to-instagram/output.md
Checks only things a script can verify. Taste and voice still need Chef Anto.
"""
import re
import sys

path = sys.argv[1]
text = open(path, encoding="utf-8").read()
lower = text.lower()

# Remove the brand-kit table row that lists the banned words, so it isn't counted.
body = "\n".join(l for l in lower.splitlines() if "no hype words" not in l and "fridgechef ai\"/\"larder" not in l)

checks = []

def check(name, ok, detail=""):
    checks.append((name, ok, detail))

for word in ["revolutionary", "game-changer", "hurry", " deal"]:
    check(f"No hype word '{word.strip()}'", word not in body)

legacy = re.findall(r"fridgechef ai|larder", body)
check("No legacy app name (FridgeChef AI / Larder)", not legacy, f"found {len(legacy)}")

signoffs = text.count("Chef Anto 🌿🤓❤️")
check("Sign-off 'Chef Anto 🌿🤓❤️' present", signoffs >= 1, f"{signoffs} found")

recipes = len(re.findall(r"^### Recipe \d", text, re.M))
check("Exactly 3 recipes", recipes == 3, f"{recipes} found")

balkan = any(w in lower for w in ["sarmale", "ciorb", "zacusc", "mămălig", "spanakopita", "lahanopita", "tzatziki"])
check("At least one Balkan dish", balkan)

check("Meals-saved line present", "ingredients rescued:" in lower and "meals made:" in lower)
check("Zero-waste tip in every recipe", lower.count("zero-waste tip") >= recipes)
check("A/B captions present", "caption a" in lower and "caption b" in lower)
check("App CTA present", "chef anto app" in lower)
check("Email lead magnet CTA present", "5 meals from what's already in your fridge" in lower)
check("Food-safety note present", "food-safety" in lower or "food safety" in lower)
check("States it is a draft / not posted", "draft only" in lower)

passed = sum(ok for _, ok, _ in checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))
print(f"\n{passed}/{len(checks)} checks passed")
sys.exit(0 if passed == len(checks) else 1)
