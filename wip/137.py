from utils import square_root_convergents

g = square_root_convergents(5)

def Af(x, terms=100):
    a = b = 1
    v = x + x*x
    f = x*x
    for i in range(terms-2):
        a, b = b, (a+b)
        f = f * x
        v += b * f

    return v
