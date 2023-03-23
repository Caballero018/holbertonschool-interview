#!/usr/bin/python3
"Module that have a method that determines if all the boxes can be opened."


def canUnlockAll(boxes):
    "Method that determines if all the boxes can be opened."
    unlocked = []
    for box_iterator, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked:
                if key != box_iterator:
                    unlocked.append(key)
    if len(boxes) == len(unlocked):
        return True
    elif len(boxes) == len(unlocked) + 1:
        return True
    return False
