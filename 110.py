from factoring import primes_below, cheese_factor_list
from collections import Counter

small_primes = primes_below(100)

candidates = range(8000001, 8050001, 2)

factors = cheese_factor_list(candidates)

values = []

for c in candidates:
    i = 0
    v = 1
    for (p, k) in sorted(factors[c])[::-1]:
        exp = (p - 1) // 2
        for j in range(k):
            v *= (small_primes[i] ** exp)
            i += 1

    values.append(v)

print(min(values))
