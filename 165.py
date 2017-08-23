from myfractions import Fraction

def bbs():
    s = 290797

    while True:
        s = (s * s) % 50515093
        yield (s % 500)

def process_line(lines, new_line, intersects):
    (new_x1, new_y1, new_x2, new_y2) = new_line

    new_A = new_y2 - new_y1
    new_B = new_x1 - new_x2
    new_C = new_A * new_x1 + new_B * new_y1

    for old_line in lines:
        (old_x1,old_y1,old_x2,old_y2) = old_line

        old_A = old_y2 - old_y1
        old_B = old_x1 - old_x2
        old_C = old_A * old_x1 + old_B * old_y1

        det = old_A * new_B - new_A * old_B

        if (det == 0):
            continue

        int_x = Fraction(new_B * old_C - old_B * new_C, det)
        int_y = Fraction(old_A * new_C - new_A * old_C, det)

        if between(int_x, int_y, new_line) and between(int_x, int_y, old_line):
            intersects.add((int_x.numerator, int_x.denominator, int_y.numerator, int_y.denominator))

    pass

def between(p_x, p_y, (l_x1, l_y1, l_x2, l_y2)):
    (low_x, high_x) = min(l_x1, l_x2), max(l_x1, l_x2)
    (low_y, high_y) = min(l_y1, l_y2), max(l_y1, l_y2)

    if (low_x != high_x) and (low_y != high_y):
        return (p_x > low_x) and (p_x < high_x) and (p_y > low_y) and (p_y < high_y)
    elif low_x == high_x:
        return (p_y > low_y) and (p_y < high_y)
    elif low_y == high_y:
        return (p_x > low_x) and (p_x < high_x)


b = bbs()
lines = []
intersects = set()

for i in xrange(5000):
    x1 = next(b)
    y1 = next(b)
    x2 = next(b)
    y2 = next(b)
    new_line = (x1,y1,x2,y2)

    if (x1 == x2) and (y1 == y2):
        continue

    print(i)

    process_line(lines, (x1,y1,x2,y2), intersects)

    lines.append(new_line)

print(len(intersects))

# l1 = (0,0,1,10)
# l2 = (0,1,2,1)
# 
# lines = [l1]
# intersects = set()
# process_line(lines, l2, intersects)
