import sys
from collections import Counter
from itertools import takewhile

def gen_pentagonals():
    n = 1
    while True:
        yield (3*n*n - n) / 2
        yield (3*n*n + n) / 2
        n += 1

partitions = Counter()
partitions[0] = 1
partitions[1] = 1

n = 2
while True:
    terms = takewhile(lambda x: x <= n, gen_pentagonals())
    p = sum([(-1)**(index//2) * partitions[n-term] for index, term in enumerate(terms)])

    if (p % 1000000) == 0:
        print(n)
        sys.exit(1)

    partitions[n] = p

    n += 1
