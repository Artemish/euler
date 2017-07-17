N,S,E,W = range(4)

def axes_crossed((x1,y1),(x2,y2)):
    [(x1,y1), (x2,y2)] = sorted([(x1,y1), (x2,y2)])

    axes = set()

    if x2 >= 0 and x1 <= 0 and x1 != x2:
        s = 1.0 * (y2 - y1) / (x2 - x1)
        intercept = y1 + s * (-1 * x1)
        if intercept > 0:
            axes.add(N)
        elif intercept < 0:
            axes.add(S)

    (x1, y1), (x2, y2) = (y1, x1), (y2, x2)

    [(x1,y1), (x2,y2)] = sorted([(x1,y1), (x2,y2)])

    if x2 >= 0 and x1 <= 0 and x1 != x2:
        s = 1.0 * (y2 - y1) / (x2 - x1)
        intercept = y1 + s * (-1 * x1)
        if intercept > 0:
            axes.add(E)
        elif intercept < 0:
            axes.add(W)

    return axes

test_cases = [((-1, -2), (-1, -1), set()), \
              ((-1, -1), (1, 1), set()),\
              ((-1, -1), (0, 1), set([W,N])),\
              ((-1, -1), (-1, 1), set([W])),\
              ((-1, 2), (1, -1), set([N,E])),\
              ((-1, -1), (1,-1), set([S]))]

for p1, p2, s in test_cases:
    c1 = axes_crossed(p1, p2)
    c2 = axes_crossed(p2, p1)
    if c1 != s or c1 != c2:
        print("Bad test case: p1: {}, p2: {}, expected {}, got {}".format(p1, p2, s, c1))

points = []

with open("p102_triangles.txt") as f:
    for line in f:
        x1,y1,x2,y2,x3,y3 = map(int, line.split(','))
        points.append(((x1,y1), (x2,y2), (x3,y3)))

total = 0

for (p1, p2, p3) in points:
    axes = set()
    axes.update(axes_crossed(p1, p2))
    axes.update(axes_crossed(p1, p3))
    axes.update(axes_crossed(p2, p3))

    if len(axes) == 4:
        total += 1

print(total)
