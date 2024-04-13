f= open("9/input.txt", "r")
total = 0
for line in f:
    nbrs = [int(i) for i in line.strip().split()]
    nbrs.reverse()
    allZeros = False
    lastRow = nbrs
    lastNbrs = [nbrs[-1]] 
    while not allZeros:
        allZeros = True
        diff = []
        for i in range(len(lastRow) -1):
            a = lastRow[i]
            b = lastRow[i+1]
            diff.append(a - b)
            allZeros = allZeros and (a - b == 0) 
        lastNbrs.append(diff[-1]) 
        lastRow = diff

    lastValue = 0
    for r in range(len(lastNbrs) -1 , -1 , -1):
        a = lastNbrs[r]
        lastValue = a -lastValue
        
    total += lastValue

print(total)

# Solution 1208