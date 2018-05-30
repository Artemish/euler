from factoring import cheese_factor_list, cheese_primes_below
from itertools import product

MAX_DIGITS = 11

candidates = map(lambda l: reduce(lambda x, y: x*10+y, l), product(range(3), repeat=MAX_DIGITS))

lst = sorted(candidates)[2:]
factors = cheese_factor_list(lst)
primes = cheese_primes_below(10000)

# For a given number, find the duonumber that spans its prime factors
prime_map = [set() for i in range(10001)]

for n in factors:
    for (p, _) in factors[n]:
        if (p > 10000):
            continue
        prime_map[p].add(n)

factors_low = cheese_factor_list(range(2,10001))

total = 2

specials = []

for n in range(3,10001):
    if (n % 1000) == 0:
        print("Got to {}".format(n))

    facs = factors_low[n]
    s = set(prime_map[facs[0][0]])
    for (p, _) in facs[1:]:
        s &= prime_map[p]

    found = False

    for candidate in sorted(list(s)):
        if (candidate % n) == 0:
            total += (candidate // n)
            found = True
            break

    if (not found):
        specials.append(n)

print("Dealing with " + str(specials))

def bruteforce(n):
    extra_digits = 0
    while True:
        total_digits = MAX_DIGITS + extra_digits
        for prefix in range(1,3):
            for l in product(range(3), repeat=total_digits):
                latter = reduce(lambda x, y: x*10+y, l)
                base = prefix * (10 ** (total_digits))
                v = latter + base
                if (v % n) == 0:
                    print("Found {} for {}".format(v, n))
                    return (v // n)
        extra_digits += 1

total += sum(map(bruteforce, specials))

print(total)
