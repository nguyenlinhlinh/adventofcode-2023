f= open("3/input.txt", "r")
total = 0
schematic = {}
symbols = []
numbers = []
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
            isSymbol = char != "." and char != "\n"
            if isSymbol:
                symbols.append((row, col))
            if len(nbr) > 0: 
                numbers.append(int(nbr))
                nbr = ""

for symbol  in symbols:
    (r, c) = symbol
    pos = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r , c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
    for p in pos:
        if p in schematic:
            idx = schematic[p]
            del schematic[p]
            if numbers[idx]:
                total += numbers[idx]
                numbers[idx] = None

print(total)

# Solution 520019