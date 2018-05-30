import operator as op

phi = (1 + 5**0.5) / 2
psi = (1 - 5**0.5) / 2

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
