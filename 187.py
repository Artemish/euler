from bisect import bisect_left
from utils import primes_below
from itertools import combinations

TOP = 100000000
comp = 0

primes = primes_below(TOP)

for i_p in range(len(primes) - 1):
    p = primes[i_p]

    if (p * p) > TOP:
        break

    comp += 1

    index = bisect_left(primes, (TOP // p), lo=i_p+1)

    if p * primes[index] > TOP:
        comp += index - 1 - i_p
    else:
        comp += index - i_p

print(comp)
