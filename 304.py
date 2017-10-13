from utils import is_fermat_pseudoprime, nth_fibonacci
from decimal import getcontext, Decimal

START = 10 ** 14
STOP = 10 ** 14 + 3500000
M = 1234567891011

# candidates = filter(is_fermat_pseudoprime, range(START, STOP+1))
# 
# with open("candidates.txt", 'w') as f:
#     for c in candidates:
#         f.write("{}\n".format(c))

# large_primes = filter(lambda x: x > 1, map(lambda n: len(cheese_factor(n)), candidates))

with open("realprimes") as f:
    large_primes = map(int, f.read().split())[:100000]

print(sum(map(lambda x: nth_fibonacci(x, mod=M), large_primes)) % M)
