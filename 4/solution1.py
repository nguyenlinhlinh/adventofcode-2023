f= open("4/input.txt", "r")
total = 0
for line in f:
    match = 0
    [win, nbrs] = line.split(":")[1].split("|")
    winNumbers = set(win.split())
    nbrs = nbrs[:-1].split()
    for nbr in nbrs:
        if nbr in winNumbers:
            match += 1
    if match > 0:
        total += pow(2, match - 1)

print(total)
# Solution 21558