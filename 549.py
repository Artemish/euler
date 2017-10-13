from collections import defaultdict
from utils import prime_factor_field, multiplicities_from_prime_divisors

TOP = 10**8

def update_lookup(lookup, prime):
    lookup[prime] = [0]

    a, total = 1, 0

    while (prime**a) <= TOP:
        m = padic_order(prime, a) + 1
        (old, total) = total, total+m
        for i in xrange(old+1, total+1):
            lookup[prime].append(a * prime)

        a += 1

    return

def padic_order(p, a):
    m, ax = 0, a
    while (ax % p) == 0:
        ax /= p
        m += 1

    return m

lookup = {}
maxes = [0] * (TOP+1)

for i in xrange(2, TOP+1):
    if maxes[i] == 0:
        maxes[i] = i
        update_lookup(lookup, i)
        for j in xrange(2, TOP//i+1):
            m = padic_order(i, j) + 1
            maxes[i*j] = max(maxes[i*j], lookup[i][m])

print(sum(maxes))
