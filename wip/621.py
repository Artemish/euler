import itertools
import sys

TOP = 1000

if len(sys.argv) > 1:
    TOP = int(sys.argv[1])

def triangles():
    n = 0
    while True:
        yield (n*n+n) // 2
        n += 1

numbers = set(itertools.takewhile(lambda x: x < TOP, triangles()))
tuples = set()

for a in numbers:
    for b in numbers:
        if b > a:
            continue

        c = TOP - a - b
        if c in numbers:
            tuples.add(tuple(sorted((a,b,c))))

total = 0

for (a,b,c) in tuples:
    if a == b and b == c:
        total += 1
    elif a == b or b == c or a == c:
        total += 3
    else:
        total += 6

print(total)
