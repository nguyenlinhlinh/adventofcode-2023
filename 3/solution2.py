f= open("3/input-simple.txt", "r")
total = 0
schematic = {}
symbols = []
numbers = {}
row = -1
for line in f:
    row += 1
    nbr = ""
    for col in range(0, len(line)):
        char = line[col]
        if char.isdigit():
            schematic[(row, col)] = len(numbers)
            nbr += char
        else:
            if char == "*":
                symbols.append((row, col))
            if len(nbr) > 0: 
                numbers[len(numbers)] = int(nbr)
            nbr = ""

for symbol  in symbols:
    (r, c) = symbol
    pos = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r , c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
    gears = set()
    for p in pos:
        if p in schematic:
            idx = schematic[p]
            del schematic[p]
            if idx in numbers:
                gears.add(idx)
                
    if len(gears) == 2:
        idx1 = gears.pop()
        idx2 = gears.pop()
        total+= numbers.pop(idx1)* numbers.pop(idx2) 

print(numbers)
print(total)

# Solution 75519888