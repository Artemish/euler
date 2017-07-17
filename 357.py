#!/usr/bin/env python3
import utils

TOP = 100000000
divisor_field = utils.fast_divisor_field(TOP+1)

total = 0

def is_prime(n):
    return len(divisor_field[n]) == 0

def is_prime_generating(n, factors, acc):
    if len(factors) == 0:
        return True

    head, tail = factors[0], factors[1:]

    fac = head * acc

    n_fac = n / fac

    return is_prime(fac + n_fac) and is_prime_generating(n, tail, fac) and is_prime_generating(n, tail, acc)

for i in range(2, TOP+1):
    if (i % 2) == 1:
        continue

    multiples = utils.multiplicities_from_prime_divisors(i, divisor_field[i])

    if is_prime_generating(i, multiples, 1):
        print(str(i) + " is prime generating")
        total += i
