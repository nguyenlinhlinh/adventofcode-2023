f= open("17/input.txt", "r")

steps = [ s for s in f.readline().strip().split(",")]
total = 0
for s in steps:
    currentValue = 0
    for char in s:
        value = ord(char)
        currentValue += value
        currentValue *= 17
        currentValue %= 256
    total += currentValue
print(total)
# Solution 498538