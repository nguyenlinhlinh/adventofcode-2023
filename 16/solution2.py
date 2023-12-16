f= open("16/input.txt", "r")
contraption = [ list(line.strip()) for line in f]

Right = (0, 1)
Left = (0, -1)
Up = (-1, 0)
Down = (1, 0)
things = {
    ".": {Right: [Right], Left: [Left], Up: [Up], Down: [Down]},
    "/": {Right: [Up], Left: [Down], Down: [Left], Up: [Right]},
    "\\": {Right: [Down], Left: [Up], Down: [Right], Up: [Left]},
    "|": {Right: [Up, Down], Left: [Up, Down], Up: [Up], Down: [Down]},
    "-": {Right: [Right], Left: [Left], Up: [Left, Right], Down: [Left, Right]}
}

def isOutOfRange(r,c):
    return r < 0 or r >= len(contraption) or c < 0 or c >= len(contraption[0])

def getNbrOfEnergizedTiles(startTile):
    memo = [[set() for j in range(len(contraption[i]))] for i in range(len(contraption))]
    energizedTiles = 0
    beams = [startTile]
    while len(beams):
        (r, c, dir) = beams.pop(0)
        if isOutOfRange(r, c) or dir in memo[r][c]: 
            continue
        else:
            if (len(memo[r][c])) == 0:
                energizedTiles += 1
            memo[r][c].add(dir)
            thing = contraption[r][c]

            for d in things[thing][dir]:
                beams.insert(0, (r + d[0], c + d[1], d))
    return energizedTiles

def findMaxEnergizedTiles():
    maxEnergizedTiles = 0
    edges = [(0, 0, [Right, Down]), (0, len(contraption[0]) - 1, [Left, Down]), (len(contraption) - 1, 0, [Right, Up]), (len(contraption) - 1, len(contraption[0]) - 1, [Left, Up])]
    for edge in edges:
        (r, c, dirs) = edge
        for d in dirs:
            maxEnergizedTiles = max(getNbrOfEnergizedTiles((r, c, d)), maxEnergizedTiles)

    for i in range(1, len(contraption[0]) - 1):
        # Top row
        maxEnergizedTiles = max(getNbrOfEnergizedTiles((0, i, Down)), maxEnergizedTiles)
        # Bottom row
        maxEnergizedTiles = max(getNbrOfEnergizedTiles((len(contraption) - 1, i, Up)), maxEnergizedTiles)
        # Leftmost column
        maxEnergizedTiles = max(getNbrOfEnergizedTiles((i, 0, Right)), maxEnergizedTiles)
        # Rightmost column
        maxEnergizedTiles = max(getNbrOfEnergizedTiles((i, len(contraption[0]) - 1, Left)), maxEnergizedTiles)
    return maxEnergizedTiles
        
print(findMaxEnergizedTiles())

# Solution 8231