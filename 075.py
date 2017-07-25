from collections import Counter
from utils import pyth_triple_gen

TOP = 1500000

ways = Counter()

for (a,b,c) in pyth_triple_gen(TOP):
    if a+b+c <= TOP:
        ways[a+b+c] += 1
