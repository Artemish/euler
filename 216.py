from utils import naive_prime_check, is_fermat_pseudoprime
import sys

TOP = 50000000

total = 0
pseudos = 0

for n in xrange(2,TOP+1):
    if (n % 100000) == 0:
        sys.stderr.write("{} - {}\n".format(n, total))

    v = 2*n*n-1

    if is_fermat_pseudoprime(v):
        print(v)
        total += 1
