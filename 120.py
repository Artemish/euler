from itertools import product
from fractions import gcd

total = 0

for a in xrange(3, 1001):
    rmax = 2
    v1, v2 = 1, 1

    seen_1 = [v1]
    seen_2 = [v2]

    while True:
        v1 = (v1 * (a - 1)) % (a*a)
        if v1 in seen_1:
            break
        else:
            seen_1.append(v1)

    while True:
        v2 = (v2 * (a + 1)) % (a*a)
        if v2 in seen_2:
            break
        else:
            seen_2.append(v2)

    all_combos = product(enumerate(seen_1), enumerate(seen_2))

    g = gcd(len(seen_1), len(seen_2))

    if g != 1:
        valid_combos =[(v1, v2) for ((i1, v1), (i2, v2)) in all_combos if (i1 % g) == (i2 % g)]
    else:
        valid_combos = all_combos

    rmax = max(map(lambda (v1, v2): (v1 + v2) % (a * a), valid_combos))

    print(a, rmax)
    total += rmax

print(total)
