#!/usr/bin/python3
"Box"


def canUnlockAll(boxes):
    "Box"
    counter = 0
    for i in range(len(boxes) - 1):
        if len(boxes[i]) > 1:
            counter += 1



    if counter == 0:
        return True
