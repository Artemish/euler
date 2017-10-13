def square_root_cf(n):
    root = n ** 0.5
    m = int(root)

    if m * m == n:
        return None

    first = m
    rest = []

    y0, y1, y2 = 1, m, n - m*m
    seen = set()

    while True:
        val = (y0 * root + y1) / y2
        m = int(val)
        y0, y1, y2 = y2*y0, y2*(m*y2-y1), y0*y0*n - (m*y2 - y1) * (m*y2 - y1)
        g = gcd(y0, gcd(y1, y2))
        y0, y1, y2 = y0/g, y1/g, y2/g

        if (y0, y1, y2) in seen:
            return first, rest
        else:
            rest.append(m)
            seen.add((y0,y1,y2))

def square_root_representation(n):
    root = n ** 0.5
    m = int(root)

    if m * m == n:
        return None

    first = m
    rest = []

    y0, y1, y2 = 1, m, n - m*m
    seen = set()

    while True:
        val = (y0 * root + y1) / y2
        m = int(val)
        y0, y1, y2 = y2*y0, y2*(m*y2-y1), y0*y0*n - (m*y2 - y1) * (m*y2 - y1)
        g = gcd(y0, gcd(y1, y2))
        y0, y1, y2 = y0/g, y1/g, y2/g

        if (y0, y1, y2) in seen:
            return first, rest
        else:
            rest.append(m)
            seen.add((y0,y1,y2))

def square_root_convergents(n):
    h, hnm1 = 1, 0
    k, knm1 = 0, 1

    first, repeating = square_root_representation(n)
    h, hnm1 = first * h + hnm1, h
    k, knm1 = first * k + knm1, k

    yield (h, k)

    repeating = cycle(repeating)
    
    i = 0
    for a in repeating:
        h, hnm1 = a * h + hnm1, h
        k, knm1 = a * k + knm1, k
        yield (h,k)
