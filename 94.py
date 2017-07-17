from utils import pyth_triple_gen

TOP = 1000000

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

total = 0

for x in range(2, TOP/6+2):
    if (x % 100000) == 0:
        print(x)

    n = x * (3 * x + 2)
    s = isqrt(n)
    if s*s == n:
        print(x, 6*x + 4)
        total += 6*x + 4

print(total)
