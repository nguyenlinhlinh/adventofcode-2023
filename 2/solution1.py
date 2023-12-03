f= open("2/input.txt", "r")
cubes = {"red": 12, "green": 13, "blue": 14}
total = 0
for line in f:
    line = line.split(" ")
    gameId = int(line[1].removesuffix(":"))
    colors = line[2:] 
    impossible = False 
    for i in range(0, len(colors), 2):
        nbr = int(colors[i])
        color = colors[i + 1][:-1]
        if nbr > cubes[color]:
            impossible = True
            break
    if not impossible:
        total += gameId
print(total)

# Solution 2617