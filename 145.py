def is_reversable(n):
    if n % 10 == 0:
        return False

    r, n0 = 0, n

    while n > 0:
        r = (r * 10) + n % 10
        n /= 10

    n2 = r + n0

    while n2 > 0:
        if (n2 % 10) % 2 == 0:
            return False
        n2 /= 10

    return True
