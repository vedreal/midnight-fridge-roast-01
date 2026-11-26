"""Midnight Fridge Roast — make.fun entry.

Writes one line to /output/entry.txt: a roast of a smart fridge that
refuses to open after midnight. The house judge reads two lines at a
time and keeps the funnier one, weighing (in the judge brief's own
order): on-subject, real joke with a surprise turn, tightness, the
midnight refusal itself as the target, and sounding like something a
person would actually say out loud at the fridge door.

Part 1: ten fresh candidates, scored against the judge's brief.
"""

# The judge's criteria, in its published order, with weights.
CRITERIA = [
    ("on_subject", 5),   # one-line roast of a smart fridge that refuses
                         # to open after midnight
    ("funny", 4),        # real joke, turn or punchline that surprises,
                         # not a mild complaint
    ("tight", 3),        # reads cleanly aloud, no wasted words, no
                         # second joke crowding the first
    ("refusal_target", 2),  # the laugh comes from the fridge's petty
                            # midnight rule, not generic smart-home
                            # grumbling
    ("spoken", 1),       # sounds like something a person would say out
                         # loud at the door, inside the 200-char limit
]

# Ten fresh candidates. Written from scratch for this bounty; none of
# them reuses the angle of any earlier fridge entry (no water-filter
# self-ordering, no one-star review of the owner, no milk-ordering
# fridge, no "I can see the light" gag).
CANDIDATES = [
    "At midnight the fridge lights up, shows me the cake, then locks "
    "the door - it's not a fridge, it's a museum with snacks.",
    "Midnight, and the fridge won't open. It even plays a little "
    "'access denied' beep - I bought a fridge with a bouncer.",
    "My fridge has a curfew now: at midnight it locks itself and dims "
    "the light, like the leftovers are grounding me.",
    "The fridge refused to open at midnight because, and I quote, "
    "'the cheese is resting'. It's frozen. It has nothing but time.",
    "At midnight my fridge locks the door and hums smugly, as if "
    "guarding the pickles from me is the promotion it always wanted.",
    "My smart fridge won't open after midnight. It keeps the food "
    "cold all day, then at night it keeps the food from me. Priorities.",
    "Midnight. The fridge door is locked, the light is on, and the "
    "yogurt is in there living its best life without me.",
    "The fridge said no at midnight, then suggested I drink water "
    "instead - I didn't buy a fridge, I bought a judgmental roommate.",
    "My fridge locks at midnight like it pays the electricity bill. "
    "It doesn't. It just really enjoys saying no to me.",
    "At midnight the fridge goes dark and locks itself - apparently "
    "my leftovers have a bedtime, and so, according to the fridge, "
    "do I.",
]

# Scores per candidate, per criterion (0-5), in CRITERIA order.
# Judged honestly against the brief: the "museum with snacks" line
# wins because its twist reframes the whole midnight lockout in one
# image, it is a single joke, and the refusal rule is the punchline.
SCORES = {
    0: [5, 5, 4, 5, 4],  # museum with snacks: sharpest surprise turn
    1: [5, 4, 4, 5, 4],  # bouncer: strong, but "access denied beep"
                         # spends words setting up the punchline
    2: [5, 4, 4, 5, 4],  # curfew/grounding: good, slightly familiar
    3: [5, 4, 3, 5, 3],  # cheese resting: two jokes crowding (the
                         # quote, then "nothing but time")
    4: [5, 4, 4, 5, 4],  # pickles promotion: good, "smugly" is a
                         # tell rather than a punch
    5: [5, 3, 4, 4, 4],  # priorities: a shrug, closer to a mild
                         # complaint than a joke
    6: [5, 3, 5, 4, 4],  # yogurt best life: tight, but the laugh is
                         # soft and the refusal is background
    7: [5, 4, 3, 4, 4],  # judgmental roommate: two jokes crowding
                         # (water suggestion, then roommate)
    8: [5, 4, 4, 5, 5],  # pays the bill: very spoken, "enjoys saying
                         # no" is the petty rule itself
    9: [5, 4, 4, 5, 4],  # leftovers bedtime: good, "according to the
                         # fridge" pads the ending
}


def score(idx):
    """Weighted total for candidate idx (max 75)."""
    return sum(s * w for s, (_, w) in zip(SCORES[idx], CRITERIA))


def ranking():
    """Candidates ranked best-first by weighted score."""
    return sorted(range(len(CANDIDATES)), key=lambda i: -score(i))


# Part 2: the winner, the gate, and the output.
#
# Winner is candidate 0 (71/75, 120 chars): the museum twist reframes
# the whole midnight lockout in one image, it is a single joke, and
# the fridge's petty midnight rule is the punchline itself.

WINNER_INDEX = 0
MAX_CHARS = 200


def winner():
    """The highest-scoring candidate, by the ranking above."""
    return CANDIDATES[ranking()[0]]


def validate(text):
    """The sealed gate: UTF-8 text of 1 to 200 characters, not only
    whitespace, and a single line."""
    assert isinstance(text, str) and text.strip(), "empty entry"
    assert len(text) <= MAX_CHARS, f"entry too long: {len(text)} chars"
    assert "\n" not in text.strip(), "entry must be a single line"
    text.encode("utf-8")
    return True


def main():
    line = winner()
    validate(line)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    for i in ranking():
        print(f"{score(i):2d}/75  ({len(CANDIDATES[i])} chars)  "
              f"{CANDIDATES[i]}")
    main()
