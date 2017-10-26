from fractions import gcd
import operator as op
import math
import sys

import numpy as np

def n_choose_k(n, k):
    num, den = 1, 1
    for i in range(1,k+1):
        num *= (n + 1 - i)
        den *= i

    return num // den


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

def my_powmod(a,e,n):
        m = 1 << (int(math.log(e,2)) + 3)

        x = 1
        while m != 0:
                x = (x*x)%n
                if (e&m) != 0: x = (a*x)%n
                m >>= 1

        return x
 
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
