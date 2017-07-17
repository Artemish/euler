from collections import defaultdict
from itertools import combinations, cycle
from fractions import gcd
import operator as op

def naive_prime_check(n):
    if (n % 2 == 0) and n != 2:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if (n % i) == 0:
            return False

    return True

def prime_factor_field(n):
    prime_factors = defaultdict(list)
    for i in range(2,n):
        if len(prime_factors[i]) == 0:
            prime_factors[i] = [i]
            for j in range(2*i, n, i):
                prime_factors[j].append(i)

    return prime_factors

def prime_factor_field(n):
    prime_factors = defaultdict(list)
    for i in range(2,n):
        if len(prime_factors[i]) == 0:
            prime_factors[i] = [i]
            for j in range(2*i, n, i):
                prime_factors[j].append(i)

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

def phi_field(n):
    prime_factors = prime_factor_field(n)
    phis = defaultdict(int)
    for x in range(2, n):
        phis[x] = phi_from_prime_factors(x, prime_factors[x])

    return phis

def multiplicities_from_prime_divisors(n, prime_factors):
    multiples = []
    for pf in prime_factors:
        n0 = n
        while (n0 % pf) == 0:
            n0 /= pf
            multiples.append(pf)

    return multiples

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
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

g = list(pyth_triple_gen(100))
