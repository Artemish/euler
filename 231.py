from collections import Counter
from itertools import chain
from utils import prime_factor_field

N = 20000000
K = 5000000
# N = 10
# K = 3

field = prime_factor_field(N)
print("Got the field")

small_factors = chain(*field[1:K+1])
print("Collected the smalls")

C_d1 = Counter(small_factors)
print("First counter")

big_factors = chain(*field[(N-K)+1:N+1])
print("Collected the bigs")

C_n = Counter(big_factors)
print("Second counter")

c = C_n - C_d1

print(sum([c[i] * i for i in c.keys()]))
