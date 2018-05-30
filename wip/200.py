from itertools import permutations
from utils import primes_below

TOP = 100

primes = primes_below(TOP)
p_set = set(primes)

print("Computed primes")

squbes = []

for p in primes:
    print("Moved to " + str(p))
    for q in primes:
        if p == q:
            continue

        v = p*p*q*q*q

        if '200' in str(v):
            squbes.append(v)
            # print("Found sqube {}".format(v))
