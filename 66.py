from utils import square_root_convergents 

(maxD, maxN) = (-1, 0)

for D in range(2,1001):
    r = int(D ** 0.5)

    if r * r == D:
        continue

    for (n, d) in square_root_convergents(D):
        if n*n - D * d * d == 1:
            break

    if (n > maxN):
        (maxD, maxN) = D, n

    # h / k is the first convergent of c_fract(sqrt(D))

    print("D: {}, N: {}, d: {}".format(D, n, d))

print maxD, maxN
