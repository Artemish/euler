from utils import is_fermat_pseudoprime

TOP = 10000000

vals = []

def check(n):
    base = n*n
    vs = [base + i for i in [1,3,7,9,13,27]]
    non_vs = [base + i for i in [5,11,15,17,19,21,23,25]]

    for v in vs:
        if not is_fermat_pseudoprime(v):
            return False

    for v in non_vs:
        if is_fermat_pseudoprime(v):
            return False

    return True

vals = filter(check, xrange(1, TOP+1))
