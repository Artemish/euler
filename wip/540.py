from utils import pyth_triple_gen

MAX = 3141592653589793

g = pyth_triple_gen(MAX, primitive=True)

count = 1

try:
    while True:
        next(g)
        count += 1
except:
    print(count)
