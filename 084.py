import numpy as np
from numpy.linalg import matrix_power
from fractions import Fraction

labels = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1',
          'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 
          'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2',
          'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1',
          'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

matrix = np.array([[Fraction(0)] * 40] * 40)

def find_next(spot, prefix):
    ls = list(enumerate(labels))
    labelled = ls[spot+1:] + ls[:spot]
    return filter(lambda x: x[1].startswith(prefix), labelled)[0][0]

def update_prob(start, end, prob):
    if labels[end] == 'G2J':
        matrix[start][labels.index('JAIL')] += prob

    elif labels[end].startswith('CH'):
        matrix[start][find_next(end, 'R')] += prob * Fraction(2,16)
        matrix[start][find_next(end, 'U')] += prob * Fraction(1,16)
        matrix[start][(end - 3) % 40] += prob * Fraction(1,16)

        for l in ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1']:
            matrix[start][labels.index(l)] += prob * Fraction(1,16)

        matrix[start][end] += prob * Fraction(6,16)

    elif labels[end].startswith('CC'):
        matrix[start][labels.index('GO')] += prob * Fraction(1, 16)
        matrix[start][labels.index('JAIL')] += prob * Fraction(1, 16)
        matrix[start][end] += prob * Fraction(14, 16)

    else:
        matrix[start][end] += prob
        
def update_start(start):
    prob = Fraction(1,16)

    for i in range(1,5):
        for j in range(1,5):
            if i == j:
                continue
            update_prob(start, (start + i + j) % 40, prob)

    prob = Fraction(1,4) * Fraction(1,16)

    for i in range(1,5):
        for j in range(1,5):
            if i == j:
                continue

            for x in range(1,5):
                update_prob(start, (start + i + j + 2*x) % 40, prob * Fraction(1,4))

    prob = Fraction(1,16) * Fraction(1,16)

    for i in range(1,5):
        for j in range(1,5):
            if i == j:
                continue
            for x in range(1,5):
                for y in range(1,5):
                    update_prob(start, (start + i + j + 2*x + 2*y) % 40, prob * Fraction(1,16))

    update_prob(start, labels.index('JAIL'), Fraction(1,4) ** 3)

for start in range(40):
    update_start(start)

float_matrix = np.array([map(float, l) for l in matrix])

power1 = np.array(float_matrix)
power2 = np.array(float_matrix)

for n in range(8):
    power2 = np.matmul(power1, power1)
    power1 = power2

state = np.array([0] * 40)
state[0] = 1.0

latest_state = np.matmul(state, power1)

le = sorted(enumerate(list(latest_state)), key=lambda x: x[1])
le = le[-1:-4:-1]
print(reduce(lambda x, y: x+y, map(lambda x: str(x[0]), le), ''))
