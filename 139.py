from utils import pyth_triple_gen

total = 0

for a, b, c in pyth_triple_gen(50000000):
    if a+b+c >= 100000000:
        continue

    if c % (b - a) == 0:
        total += 1

print(total)
