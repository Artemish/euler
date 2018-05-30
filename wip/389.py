from random import randint
from collections import Counter

def trial():
    t = randint(1,4)
    c = sum([randint(1,6) for i in range(t)])
    # o = sum([randint(1,8) for i in range(c)])
    # d = sum([randint(1,12) for i in range(o)])
    # i = sum([randint(1,20) for i in range(d)])

    return c

data = [trial() for i in xrange(500000)]

mean = sum(data) / (1.0*len(data))
vs = map(lambda x: (x-mean)**2, data)

print(sum(vs) / (1.0 * len(vs)))
