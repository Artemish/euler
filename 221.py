from utils import cheese_factor_list, divisor_gen

MAX_P = 100000

factored = cheese_factor_list([p*p+1 for p in range(1, MAX_P)])

found = []

for p in range(1,MAX_P):
    for k in divisor_gen(p*p+1, factored[p*p+1]):
        q = -1* (k+p)
        r = -1 * (((p*p+1)/k) + p)
        found.append(p*q*r)

uniques = sorted(list(set(found)))
print(uniques[149999])
