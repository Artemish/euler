from fractions import Fraction
from utils import primes_below
# index: (position, jumps_remaining) => probability of completing the sequence

FIELD = 500
STEPS = 15

primes = set(primes_below(FIELD + 1))

sequence = 'PPPPNNPPPNPPNPN'

def to_letter(n):
    return 'P' if n in primes else 'N'

probability_matrix = [[0 for x in range(FIELD + 1)] for y in range(STEPS)]
probability_matrix[0] = [Fraction(1,FIELD)] * (FIELD + 1)
probability_matrix[0][0] = 0

for jump in range(1,STEPS):
    probability_matrix[jump][2] = probability_matrix[jump-1][1]
    probability_matrix[jump][FIELD-1] = probability_matrix[jump-1][FIELD]
    for j in range(2,500):
        probability_matrix[jump][j-1] += Fraction(1,2) * (probability_matrix[jump-1][j])
        probability_matrix[jump][j+1] += Fraction(1,2) * (probability_matrix[jump-1][j])

hit_all_ps = 1

for step in range(STEPS):
    prob = 0
    for j in range(1, FIELD + 1):
        if to_letter(j) == sequence[step]:
            prob += Fraction(2,3) * probability_matrix[step][j]
        else:
            prob += Fraction(1,3) * probability_matrix[step][j]

    print("{}: {}".format(step, prob))
    
    hit_all_ps *= prob

print(hit_all_ps)
