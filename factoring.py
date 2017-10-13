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

def primes_below(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
