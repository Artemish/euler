import sys

from utils import pyth_triple_gen
from collections import Counter

ways = Counter()

for (a,b,c) in pyth_triple_gen(1000000):
    ways[a] += b/2 - (b - a) + 1
    if ways[a] > 1000000:
        print(a)
        sys.exit()
