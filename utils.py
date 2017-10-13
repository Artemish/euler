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

def distinct_permutations(l):
    c = Counter(l)
    vs = c.values()
    permutations = math.factorial(sum(vs))
    return reduce(lambda perms, v: perms // math.factorial(v), vs, permutations)
    

def naive_prime_check(n):
    if (n % 2 == 0) and n != 2:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if (n % i) == 0:
            return False

    return True

def prime_factor_field(n):
    prime_factors = [[] for i in xrange(n+1)]
    prime_factors[1] = [1]
    for i in xrange(2,n):
        if len(prime_factors[i]) == 0:
            v = i
            l = [i]
            while v < n:
                for x in xrange(1, (n // v) + 1):
                    if (x % i == 0):
                        continue
                    prime_factors[x*v].extend(l)

                v *= i
                l += [i]

    return prime_factors

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

def multiplicities_from_prime_divisors(n, prime_factors):
    multiples = []
    for pf in prime_factors:
        n0 = n
        m = 0

        while (n0 % pf) == 0:
            n0 /= pf
            m += 1

        multiples.append((pf, m))

    return multiples

def divisor_gen(n, factors):
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def split_set_generator(s):
    l = len(s)

    if (l % 2) == 0:
        for i in range(1, l / 2):
            for first_tuple in combinations(s, i):
                first_set = set(first_tuple)
                second_set = s - first_set
                yield first_set, second_set

        for first_tuple in combinations(s, l / 2):
            first_set = set(first_tuple)
            second_set = s - first_set
            if first_tuple > tuple(second_set):
                return

            yield first_set, second_set

    else:
        for i in range(1, l / 2 + 1):
            for first_tuple in combinations(s, i):
                first_set = set(first_tuple)
                second_set = s - first_set
                yield first_set, second_set

def square_root_cf(n):
    root = n ** 0.5
    m = int(root)

    if m * m == n:
        return None

    first = m
    rest = []

    y0, y1, y2 = 1, m, n - m*m
    seen = set()

    while True:
        val = (y0 * root + y1) / y2
        m = int(val)
        y0, y1, y2 = y2*y0, y2*(m*y2-y1), y0*y0*n - (m*y2 - y1) * (m*y2 - y1)
        g = gcd(y0, gcd(y1, y2))
        y0, y1, y2 = y0/g, y1/g, y2/g

        if (y0, y1, y2) in seen:
            return first, rest
        else:
            rest.append(m)
            seen.add((y0,y1,y2))

def square_root_representation(n):
    root = n ** 0.5
    m = int(root)

    if m * m == n:
        return None

    first = m
    rest = []

    y0, y1, y2 = 1, m, n - m*m
    seen = set()

    while True:
        val = (y0 * root + y1) / y2
        m = int(val)
        y0, y1, y2 = y2*y0, y2*(m*y2-y1), y0*y0*n - (m*y2 - y1) * (m*y2 - y1)
        g = gcd(y0, gcd(y1, y2))
        y0, y1, y2 = y0/g, y1/g, y2/g

        if (y0, y1, y2) in seen:
            return first, rest
        else:
            rest.append(m)
            seen.add((y0,y1,y2))

def square_root_convergents(n):
    h, hnm1 = 1, 0
    k, knm1 = 0, 1

    first, repeating = square_root_representation(n)
    h, hnm1 = first * h + hnm1, h
    k, knm1 = first * k + knm1, k

    yield (h, k)

    repeating = cycle(repeating)
    
    i = 0
    for a in repeating:
        h, hnm1 = a * h + hnm1, h
        k, knm1 = a * k + knm1, k
        yield (h,k)

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

def primes_below(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

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

def cheese_factor_list(lst):
    factors = {}

    for i in range(0, len(lst), 10000):
        print("Batching with {}".format(i))

        output = factor(*lst[i:i+10000]).stdout
        for line in output.split('\n')[:-1]:
            n = int(line.split(":")[0])
            n_factors = map(int, line.split(' ')[1:])

            c = Counter(n_factors)
            factors[n] = [(p, c[p]) for p in c]

    return factors
 
def cheese_factor(n):
    output = factor(n).stdout
    factors = output[output.find(':')+1:].split()
    return map(int, factors)

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

def list_powerset(lst):
    result = [[]]
    for x in lst:
        result.extend([subset + [x] for subset in result])
    return result

def powerset(s):
    return frozenset(map(frozenset, list_powerset(list(s))))
