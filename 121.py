from itertools import combinations
from fractions import Fraction

TOP = 15

def probability(wins):
    odds = Fraction(1,1)
    for i in range(1, TOP + 1):
        if i in wins:
            odds *= Fraction(1, (i + 1))
        else:
            odds *= Fraction(i, (i + 1))

    return odds

odds = Fraction(0,1)

for i in range(TOP/2+1, TOP+1):
    odds += sum(map(probability, combinations(range(1,TOP+1), i)))

print(odds.denominator // odds.numerator)
