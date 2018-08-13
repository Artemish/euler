from utils import ncr

# lol chromatic polynomial
def coeffs(c):
    alpha = (c-4)*(c-5)*(c-2) + \
            (c-4)*(c-1) + \
            (c-4)*(c-2)*2 + \
            2*(c-2)*(c-4) + \
            2*(c-2)*2

    beta = (c-3)*(c-2)*(c-4) + \
           (c-3)*(c-1) + \
           (c-3)*(c-2) + \
           (c-2)*(c-3) + \
           c-2

    delta = (c-2)*(c-2)*(c-3) + \
            (c-2)*(c-1)

    sigma = (c-3)*(c-2)*(c-4) + \
            (c-3)*(c-1) + \
            (c-2)*(c-3) + \
            (c-3)*(c-2)*2 + \
            (c-2)*2

    return alpha, beta, delta, sigma

def calculate(a, b, c):
    alpha, beta, delta, sigma = coeffs(c)

    first = c * (c-1)

    alpha_multip = (c-2)*(c-3)
    beta_multip = c-2
    delta_multip = 1
    sigma_multip = c-2

    structure_closed = alpha_multip * alpha + \
            beta_multip * beta * 2 + \
            delta_multip * delta

    structure_open = structure_closed + sigma_multip * sigma

    M = int(1e8)

    return (first * \
            ncr(a+b, a) * \
            pow(structure_closed, a, M) * \
            pow(structure_open, b, M)) % M

print(calculate(25,75,1984))
