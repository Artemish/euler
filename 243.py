from fractions import Fraction
from itertools import combinations_with_replacement
from utils import primes_below

TOP = 30

target = Fraction(15499, 94744)

def main(primes, p_i, n, resilience, depth=1):
    if depth > 10:
        return []

    global target 

    p = primes[p_i]

    prime_loss = Fraction((p-1)*(n-1), n*p - 1)
    two_loss = Fraction(2*n-2, 2*n-1)

    prime_branch_resilience = resilience * prime_loss
    prime_n = n * p

    two_branch_resilience = resilience * two_loss
    two_n = 2 * n

    ret = []

    if prime_branch_resilience < target:
        ret = [prime_n]
    if two_branch_resilience < target:
        ret.append(two_n)

    if len(ret) != 0:
        return ret

    print("Taking prime branch with {}, {}".format(n, primes[p_i]))
    prime_branch_found = main(primes, p_i + 1, prime_n, prime_branch_resilience, depth+1)
    print("Taking twos branch with {}".format(n))
    two_branch_found = main(primes, p_i, two_n, two_branch_resilience, depth+1)
    return prime_branch_found + two_branch_found

primes = primes_below(TOP)
candidates = main(primes, 1, 2, Fraction(1))
print(min(candidates))
