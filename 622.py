from collection_utils import powerset
from factoring import divisor_gen, cheese_factor, multiplicities_from_prime_divisors
from operator import mul
from sys import argv

EXP = int(argv[1])
N = 2**EXP - 1

def suitable(n):
    for exponent in range(1, EXP):
        if (2**exponent % n) == 1:
            return False
    return True

total = 0

factors = multiplicities_from_prime_divisors(N, list(set(cheese_factor(N))))

seen = set()
dups = 0

for g in divisor_gen(N, factors):
    if (N % g) != 0:
        print("wtf " + str(g))
        break

    if suitable(g) and g > 1:
        if g in seen:
            dups += 1
            continue
        else:
            seen.add(g)

        total += g + 1

print(dups)
print(total)
