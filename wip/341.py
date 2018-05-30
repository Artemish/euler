from collections import defaultdict
import sys

sys.setrecursionlimit(100)

TOP = 1000

cache = defaultdict(int)
cache[1] = 1

total = 0

for n in range(1,TOP):
    total += golomb(n*n*n)

print(total)
