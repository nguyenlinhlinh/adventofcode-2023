import re
from collections import defaultdict
f= open("15/input.txt", "r")

steps = [ s for s in f.readline().strip().split(",")]

boxes = defaultdict(list)

def hash( s ):
    currentValue = 0
    for char in s:
        value = ord(char)
        currentValue += value
        currentValue *= 17
        currentValue %= 256
    return currentValue

def getLensIndex(label, lens):
    for i in range(len(lens)):
        if label == lens[i][0]:
            return i
    return -1

for s in steps:
    (label, focal) = re.split("=|-", s)
    operator = s[len(label)]
    boxIndex = hash(label)
    lens = boxes[boxIndex]
    lensIndex = getLensIndex(label, lens)
    if operator == "-":
        if lensIndex > -1:
            lens.pop(lensIndex)
    if operator == "=":
        if lensIndex > -1:
            lens[lensIndex] = (label, int(focal))
        else:
            lens.append((label, int(focal)))
total = 0
for boxIdx, lens in boxes.items():
    for lenSlot in range(len(lens)):
        print(lens[lenSlot])
        total += (boxIdx + 1) * (lenSlot + 1) * lens[lenSlot][1]




print(total)
# Solution 286278
