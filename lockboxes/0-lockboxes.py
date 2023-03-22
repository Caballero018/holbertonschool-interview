#!/usr/bin/python3
"GG"


def canUnlockAll(boxes):
    "GG"
    unlocked = [0]
    for box_iterator, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_iterator:
                unlocked.append(key)
    if len(boxes) == len(unlocked):
        return True
    return False