f= open("1/input.txt", "r")
sum = 0
for line in f:
    print(line)
    firstDigit = ""
    lastDigit = ""
    for i in range(0, len(line)):
        if line[i].isdigit():
            firstDigit = line[i]
            break
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            lastDigit = line[i]
            break
    print(firstDigit + lastDigit)
    sum += int(firstDigit + lastDigit)
print(sum)

# Solution 54927