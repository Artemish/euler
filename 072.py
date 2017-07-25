from collections import defaultdict
from itertools import combinations
import sys

divisors = defaultdict(list)

TOP = int(sys.argv[1])

for i in range(2,TOP):
    # If prime
    if len(divisors[i]) == 0:
        for n in range(2*i,TOP,i):
            divisors[n].append(i)

total = 0

for i in range(2,TOP):
    total_i = (i - 1)

    for x in range(1,len(divisors[i])+1):
        for dl in combinations(divisors[i], x):
            d = 1
            for d_i in dl:
                d *= d_i
            if (x % 2 == 0):
                total_i += (i / d) - 1
            else:
                total_i -= (i / d) - 1

    total += total_i

print(total)
