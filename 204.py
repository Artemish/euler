from utils import primes_below
from memoizers import key_memoized

TOP = 1000000000

primes = primes_below(100)

@key_memoized
def count_multiplicities(prime_index, top):
    global primes

    if prime_index >= len(primes):
        return 0

    p = primes[prime_index]

    if p > top:
        return 0

    v1 = count_multiplicities(prime_index + 1, top)
    v2 = count_multiplicities(prime_index, top // p)

    return 1 + v1 + v2

print(count_multiplicities(0, TOP)) + 1
