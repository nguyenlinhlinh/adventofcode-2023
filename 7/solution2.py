from collections import Counter
from functools import cmp_to_key

f= open("7/input.txt", "r")
CARDS = {"A": 13, "K": 12 ,"Q": 11, "T": 10, "9":9,"8":8,"7":7,"6":6, "5":5, "4":4, "3":3, "2": 2, "J": 1 }
grouped = [[] for i in range(7)]
Five = 6
Four = 5
Full = 4
Three = 3
Two = 2
One = 1
High = 0

def compare(a, b):
    hand1 = a[0]
    hand2 = b[0]

    for i in range(len(hand1)):
        if hand1[i] != hand2[i]:
            return CARDS[hand1[i]] - CARDS[hand2[i]]
    return 0

def getMaxDuplicateCards(count):
    maxValue = 0
    key = ""
    for k,v in count.items():
        if k != "J" and v > maxValue:
            maxValue = v
            key = k
    return (key, maxValue)

for hand in f:
    (hand, bid) = hand.strip().split()
    bid = int(bid)
    count = Counter(hand)
    (card, maxDup) = getMaxDuplicateCards(count) 
    maxDup += count.get("J", 0)
    count[card] = maxDup
    groupIdx = 0
    if maxDup == 5:
        groupIdx = Five
    elif maxDup == 4:
        groupIdx = Four
    elif maxDup == 3:
        maxV = 0
        for k, v in count.items():
            if v != 3 and k != "J":
                maxV = max(maxV, v)
        groupIdx = Full if maxV == 2 else Three
    elif maxDup == 2:
        pairs = 0
        for k, v in count.items():
            if v == 2:
                pairs += 1
        groupIdx = Two if pairs == 2 else One
    grouped[groupIdx].append((hand, bid))

finished = []
for i in range(len(grouped)):
    s = sorted(grouped[i], key=cmp_to_key(compare) )
    finished += s

total = 0
for i in range(len(finished)):
    total += finished[i][1] * (i+1)
             
print(total)
# Solution 252127335
