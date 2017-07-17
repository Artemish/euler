TOP_DIGITS = 14

def is_harshad(n):
    n0 = n
    t = 0
    while n0 > 0:
        t += n0 % 10
        n0 /= 10

    return (n % t) == 0

def is_strong_harshad(n):
    if n < 10:
        return False

    n0 = n
    t = 0
    while n0 > 0:
        t += n0 % 10
        n0 /= 10

    if (n % t) != 0:
        return False

    return naive_prime_check(n / t)

def naive_prime_check(n):
    if (n % 2 == 0) and n != 2:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if (n % i) == 0:
            return False

    return True

harshads = [None, range(1,10)]

for d in range(2, TOP_DIGITS):
    d_harshads = harshads[d-1]
    harshads.append([])

    for h in d_harshads:
        for i in range(10):
            if is_harshad(h*10 + i):
                harshads[d].append(h*10 + i)

strong_harshads = [None] + map(lambda l: filter(is_strong_harshad, l), harshads[1:])

total = 0

for d in range(1, TOP_DIGITS):
    for sh in strong_harshads[d]:
        for i in range(10):
            if naive_prime_check(i + sh * 10):
                total += i + sh * 10

print(total)
