
f= open("2/input.txt", "r")
total = 0
for line in f:
    line = line.split(" ")
    gameId = int(line[1][:-1])
    colors = line[2:] 
    minColors = {"red": 1, "green": 1, "blue": 1} 
    for i in range(0, len(colors), 2):
        nbr = int(colors[i])
        color = colors[i + 1][:-1]
        minColors[color] = max(minColors[color], nbr)
    total += minColors["red"] * minColors["blue"] * minColors["green"]
print(total)

# Solution 59795