import sys
f= open("1/input2.txt", "r")
sum = 0
digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
set = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in f:
    print(line)
    firstDigit = ""
    firstStr = ""
    lastDigit = ""
    lastStr = ""
    for i in range(0, len(line)):
        if line[i].isdigit():
            firstDigit = line[i]
            break
        else:
            firstStr += line[i]
            if(len(firstStr) > 2):
                minIdx = sys.maxint
                for s in set:
                    if firstStr.find(s) != -1:
                        firstDigit = str(digits[s])
                        break
        if firstDigit != "":
            break

    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            lastDigit = line[i]
            break
        else:
            lastStr = line[i] + lastStr
            if(len(lastStr) > 2):
                for s in set:
                    if lastStr.find(s) != -1:
                        lastDigit = str(digits[s])
                        break
        if lastDigit != "":
            break
    print(firstDigit + lastDigit)
    sum += int(firstDigit + lastDigit)
print(sum)
        

# Solution 54581