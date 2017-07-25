from utils import isqrt, square_root_convergents

TOP = 1000000000

total = 0

for (c,d) in square_root_convergents(3):
    if (c * c - 3 * d * d == 1):
        if (c % 3) == 1:
            k = (c + 2) // 3
        elif (c % 3) == 2:
            k = (c - 2) // 3
        else:
            continue

        print("+/- {} {}".format(6*k+2, 6*k-2))

        if (6 * k - 2) > TOP:
            break

        inner = 3*k*k - 4*k + 1
        if isqrt(inner) ** 2 == inner:
            total += (6*k-2)

        inner = 3*k*k + 4*k + 1
        if isqrt(inner) ** 2 == inner:
            total += (6*k+2)

print(total)
