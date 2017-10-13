from utils import matrix_pow
import numpy as np

# (answer % 1000) == 479

def lagged_fib_matrix(n):
    m = np.matrix([[0] * n for i in xrange(n)], dtype=np.int64)
    m[(0,n-1)] = 1
    m[(0,n-2)] = 1

    for i in xrange(1,n):
        m[(i, i-1)] = 1

    return m

# def lagged_fib_generator():
#     state = [1] * 2000
#     for i in xrange(2000):
#         yield 1
# 
#     while True:
#         v = state[0] + state[1]
#         state.append(v)
#         del state[0]
#         yield v
# 
# g = lagged_fib_generator()

m = lagged_fib_matrix(2000)
M = 20092010
Q = matrix_pow(m, 10**18, M, dtype=np.int64)
v = np.matrix([[1] for i in xrange(2000)], dtype=np.int64)
print((Q*v)[(1999,0)] % M)
