#!/usr/bin/python3
"GG"


def canUnlockAll(boxes):
    "GG"

    counter = 0
    dic_box = {}
    for i in range(len(boxes) - 1):
        if len(boxes[i]) > 1:
            counter += 1
        if boxes[i] == []:
            k = '[]'
            if k not in dic_box.keys():
                dic_box[k] = 0
            if k in dic_box.keys():
                dic_box[k] += 1

        for j in range(len(boxes[i])):
            key = str(boxes[i][j])
            if key not in dic_box.keys():
                dic_box[key] = 0
            if key in dic_box.keys():
                if key not in dic_box.keys():
                    dic_box[key] = 1
                elif key in dic_box.keys():
                    dic_box[key] += 1
    if counter == 0:
        return True
    counter = 0
    for key in dic_box.keys():
        if dic_box[key] >= 1 and key != '[]':
            counter += 1
    if counter == len(dic_box):
        return True

    if counter != len(dic_box):
        return False
    

