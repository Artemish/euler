from fractions import Fraction

coeffs = [1,-1,1,-1,1,-1,1,-1,1,-1,1]

values = map(lambda n: sum([n ** power * sign for power, sign in enumerate(coeffs)]), range(0,15))

total = 1

def poly_eval(points, x):
    v = 0
    for index, (p_x, p_y) in enumerate(points):
        f = Fraction(p_y,1)
        other_points = points[:index] + points[index+1:]
        for o_x, _ in other_points:
            f *= Fraction(x - o_x, p_x - o_x)
        v += f

    return v

for degree in range(2, 11):
    points = list(enumerate(values))[1:degree+1]
    x = 2
    while poly_eval(points, x) == values[x]:
        x += 1

    total += poly_eval(points, x)

print(int(total))
