#!/usr/bin/env python3
from utils import primes_below

TOP = 100000000

total = 0

primes = primes_below(TOP*1.6)
prime_set = set(primes)

vals = [True] * (TOP + 1)

for p in primes:
    if 2*p > TOP:
        break

    print(p)
    vals[p] = False
    for i in range(2,(TOP//p)+1):
        if i + p not in prime_set:
            vals[i*p] = False

v = set([i for i in range(1,TOP+1) if vals[i]])
v2 = set(map(lambda x: x-1, prime_set))

print(sum(v & v2))
