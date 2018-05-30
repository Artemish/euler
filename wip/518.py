from utils import primes_below
from fractions import gcd

TOP = 100
primes = primes_below(TOP)

candidates = map(lambda x: x+1, primes)
candidate_set = set(candidates)

values = []

TESTS = [(2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17),
         (7, 23, 71), (11, 23, 47), (17, 23, 31), (17, 41, 97), (31, 47, 71),
         (71, 83, 97)]

for (i, a) in enumerate(candidates):
    print(a)
    for b in candidates[(i+1):]:
        if ((b*b) % a) != 0:
            continue

        candidate = (b*b) // a
        if candidate >= TOP:
            break

        if candidate in candidate_set:
            values.append((a-1,b-1,candidate-1))

print(sum(map(sum, values)))
