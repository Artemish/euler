from itertools import combinations
from utils import primes_below

TOP = 10000000
primes = primes_below(TOP)

def M(p,q,N):
    v = p
    max_v = 0

    while v < N:
        v *= p

    while (v * q) > N:
        v /= p

    v = v * q

    while (v % p) == 0:
        if (v > max_v):
            max_v = v

        while (v * q) > N and (v % p) == 0:
            v /= p

        v *= q
    
    return max_v

total = 0
n_p = len(primes)

for i in range(n_p):
    p = primes[i]
    for j in range(i+1,n_p):
        q = primes[j]
        if (p*q) > TOP:
            break

        total += M(p,q,TOP)

    if (p*p) > TOP:
        break

print(total)
