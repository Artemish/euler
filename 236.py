from fractions import gcd

A = [5248, 1312, 2624, 5760, 3936]
B = [640, 1888, 3776, 3776, 5664]
A_t = sum(A)
B_t = sum(B)

reduced = []
for i in range(5):
    g = gcd(A[i], B[i])
    reduced.append((A[i]/g, B[i]/g))
