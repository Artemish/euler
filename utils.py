from collections import defaultdict, Counter
from itertools import combinations, cycle
from fractions import gcd
import operator as op
import math
import sys

from sh import factor

import numpy as np

phi = (1 + 5**0.5) / 2
psi = (1 - 5**0.5) / 2

def n_choose_k(n, k):
    num, den = 1, 1
    for i in range(1,k+1):
        num *= (n + 1 - i)
        den *= i

    return num // den

def phi_from_prime_factors(n, factors):
    numerator, denominator = n, 1
    for pf in factors:
        numerator *= (pf - 1)
        denominator *= pf

    return numerator / denominator

def phi_field_direct(n):
    phi = [0] * (n + 1)
    phi[1] = 1
    for i in range(2,n):
        if phi[i] == 0:
            phi[i] = i - 1
            for j in range(2, n / i + 1):
                if phi[j] == 0:
                    continue

                q = j
                f = i - 1

                while (q % i) == 0:
                    f *= i
                    q /= i

                phi[i*j] = f * phi[q]

    return phi

# sqrt(2) convergents:
# 1/1, 3/2, 7/5, 17/12, 41/29

def pyth_triple_gen(max_c, primitive=False):
    m = 1
    while True:
        m += 1
        if m*m > max_c:
            return

        for n in range(1, m):
            if gcd(m,n) == 1 and (m % 2) != (n % 2):
                a0 = a = m*m - n*n
                b0 = b = 2 * m*n
                c0 = c = m*m + n*n

                if c0 > max_c:
                    continue

                if primitive:
                    yield (a,b,c)
                    continue

                while c <= max_c:
                    yield (a,b,c)
                    a, b, c = a+a0, b+b0, c+c0

def ncr(n, r):
    r = min(r, n-r)

    if r == 0:
        return 1

    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))

    return numer//denom

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def palindromes_of_length(n):
    pals = range(1,10)
    
    prefix_digits = n // 2

    for prefix in range(1,10**prefix_digits):
        string = str(prefix)
        pals.append(int(string + string[::-1]))

        if 2* len(string) < n:
            for i in range(10):
                pals.append(int(string + str(i) + string[::-1]))

    return sorted(pals)

def is_fermat_pseudoprime(n):
    if n in [2,3,4,5,7,11,13,17,19]:
        return True

    if any([(n % i) == 0 for i in [2,3,5,7]]):
        return False

    for a in [2,3,5,7,11,13,17,19]:
        if pow(a, n-1, n) != 1:
            return False

    return True

def my_powmod(a,e,n):
        m = 1 << (int(math.log(e,2)) + 3)

        x = 1
        while m != 0:
                x = (x*x)%n
                if (e&m) != 0: x = (a*x)%n
                m >>= 1

        return x
 
 
# This function assumes that a,b > 0.
def my_gcd(a,b):
        r = a%b
        while r != 0:
                a,b = b,r
                r = a%b
 
        return b

def phi_sieve(n):
    field = [0] * (n + 1)
    field[1] = 1;

    for i in range(2, n):
        if (field[i] == 0) :
            field[i] = i-1
            for j in range(i<<1, n+1, i):
                if (field[j] == 0):
                    field[j] = j;
                field[j] = field[j]/i*(i-1);

    return field

def matrix_pow(m, n, mod, dtype=object):
    v = 1 << (int(math.log(n,2)) + 2)

    x = np.identity(m.shape[0], dtype=dtype)
    while v != 0:
        print("v == 2^{}".format(int(math.log(v, 2))))
        x = x*x % mod

        if (n & v):
            x = (m*x) % mod

        v >>= 1

    return x

def nth_fibonacci(n, mod=None):
    m = np.matrix([[1,1],[1,0]], dtype=object)
    
    Q = matrix_pow(m, n, mod)

    return Q[(0,1)]
