#!/usr/bin/python3

def canUnlockAll(boxes):
    counter = 0
    for i in range(len(boxes) - 1):
        if len(boxes[i]) > 1:
            counter += 1
            


    if counter == 0:
        return True
