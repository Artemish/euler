import sys

from utils import pyth_triple_gen
from collections import Counter

ways = Counter()

for (a,b,c) in pyth_triple_gen(5000):
    (a,b) = min(a,b), max(a,b)

    ways[b] += a // 2

    if b > 2*a:
        continue
    else:
        ways[a] += a - (b-1)//2

total = 0

for M in range(2000):
    total += ways[M]
    if total > 1000000:
        print(M)
        break
