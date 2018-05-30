from collections import Counter

DIGITS = 100

incmap = {(1, i) : 1 for i in range(1,10)}
for x in range(2,DIGITS+1):
    for d in range(1,10):
        incmap[(x,d)] = 0

    for d in range(1,10):
        val = incmap[(x-1,d)]
        for higher in range(d, 10):
            incmap[(x,higher)] += val

decmap = {(1, i) : 1 for i in range(1,10)}
decmap[(1,0)] = 0

for x in range(2,DIGITS+1):
    for d in range(10):
        decmap[(x,d)] = 0

    for d in range(10):
        val = decmap[(x-1,d)]
        for lower in range(d+1):
            decmap[(x,lower)] += val

allequal = 9 * (DIGITS)

print(sum(incmap.values()) + sum(decmap.values()) - allequal)
