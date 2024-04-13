from collections import Counter
from functools import cmp_to_key
f= open("9/input-simple.txt", "r")
total = 0
for line in f:
    nbrs = [int(i) for i in line.strip().split()]
    nbrs.reverse()
    differences = [nbrs]
    print(differences)
    allZeros = False
    while not allZeros:
        allZeros = True
        diff = []
        lastRow = differences[-1]
        for i in range(len(lastRow) -1):
            a = lastRow[i]
            b = lastRow[i+1]
            diff.append(a - b)
            allZeros = allZeros and (a - b == 0) 
        if(allZeros):
            diff.append(0)
        differences.append(diff)
    for r in range(len(differences) -1 , -1 , -1):
        a = differences[r][-1]
        b = differences[r -1][-1]
        c = b - a
        differences[r -1].append(c)
    total += differences[0][-1]

print(total)

# Solution 1208