from fractions import Fraction
import sys

TOP = 12

total = 0

def die(b,c):
    print("B: {}, C: {}".format(b,c))
    sys.exit(1)

for b in range(1,TOP):
    for c in range(b, TOP):
        if (2*b + 2*b + 2) >= (TOP + 1):
            X = TOP - 2*c - 2*c + 1
            if (X > 2):
                pass
