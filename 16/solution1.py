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


memo = [[set() for j in range(len(contraption[i]))] for i in range(len(contraption))]
energizedTiles = 0

def isOutOfRange(r,c):
    return r < 0 or r >= len(contraption) or c < 0 or c >= len(contraption[0])

beams = [(0,0, Right)]
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
        
print(energizedTiles)
# Solution 7543