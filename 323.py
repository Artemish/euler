from fractions import Fraction
from num_utils import ncr

vs = [0, 2, Fraction(8,3)]

for n in range(3,33):
    v = 2
    for i in range(1, n):
        v += ncr(n, i) * (vs[n - i] + 1)

    vs.append(v / (2**n - 1))

print(float(vs[32]))
