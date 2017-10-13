from utils import phi_sieve

TOP = 40000000
# TOP = 100

phis = phi_sieve(TOP)

print("Computed phis")

primes = map(lambda (i,v): i, filter(lambda (i,v): v == (i - 1), enumerate(phis)))

print("Found the primes")

chain_lengths = [0] * TOP
chain_lengths[1] = 1

for i in range(2, TOP):
    chain_lengths[i] = 1 + chain_lengths[phis[i]]

print("Computed the chains")

print(sum(filter(lambda p: chain_lengths[p] == 25, primes)))
