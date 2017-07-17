from fractions import gcd
from utils import prime_factor_field

TOP = 120000

factors = prime_factor_field(TOP+1)

total = 0

for c in range(3, TOP+1):
    for b in range(c // 2 + 1, c):
        a = c - b

        if gcd(a,b) == 1 and gcd(a,c)== 1 and gcd(b,c) == 1:
            abc = reduce(lambda x, y: x*y, factors[a] + factors[b] + factors[c], 1)
            if abc < c:
                total += c

print("Total for c up to {} is {}".format(TOP, total))
