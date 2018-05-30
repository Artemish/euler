from factoring import prime_factor_field
from collection_utils import list_powerset

TOP = 1000000

factors = prime_factor_field(TOP)
primes = [p for p in range(2,TOP) if len(factors[p]) == 1]
bestfac = [0] * (TOP + 1)

def drs(n):
    while n >= 10:
        n = sum(map(int, str(n)))
    return n

for p in primes:
    bestfac[p] = drs(p)

for i in range(4,TOP):
    if i in primes:
        continue

    print(i)

    biggest = drs(i)

    for fs in list_powerset(factors[i])[1:]:
        v1 = reduce(lambda x, y: x*y, fs)
        v2 = i // v1

        v = bestfac[v1] + bestfac[v2]
        if v > biggest:
            biggest = v

    bestfac[i] = biggest
