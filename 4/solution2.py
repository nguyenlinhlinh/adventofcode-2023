f= open("4/input.txt", "r")
total = 0
instances = {}
cardNbr = 1
for line in f:
    [win, nbrs] = line.split(":")[1].split("|")
    winNumbers = set(win.split())
    nbrs = nbrs[:-1].split()
    matchingNbrs = 0
    for nbr in nbrs:
        if nbr in winNumbers:
            matchingNbrs += 1
    for i in range(cardNbr+1, cardNbr+1 + matchingNbrs):
        instances[i] =  instances.get(i, 1) + instances.get(cardNbr, 1)
    total += instances.get(cardNbr, 1)
    instances.pop(cardNbr, None)
    cardNbr += 1

print(total)

# Solution 10425665