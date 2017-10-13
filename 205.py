from itertools import combinations_with_replacement, permutations
from collections import Counter
from fractions import Fraction
from operator import mul

pyramid_wins = 0

def fact(n):
    return reduce(mul, range(1,n+1), 1)

for pyramid_rolls in combinations_with_replacement(range(1,5), 9):
    for hex_rolls in combinations_with_replacement(range(1,7), 6):
        if sum(pyramid_rolls) > sum(hex_rolls):
            m = fact(9) * fact(6)

            c_p, c_h = Counter(pyramid_rolls), Counter(hex_rolls)

            x = 1

            for i in range(1,5):
                x *= fact(c_p[i])

            for i in range(1,7):
                x *= fact(c_h[i])
              
            pyramid_wins += (m // x)

print(pyramid_wins)

print(pyramid_wins / (1.0 * ((4 ** 9) * (6 ** 6))))
