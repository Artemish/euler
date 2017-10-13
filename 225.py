def tribonacci():
    a,b,c = 1,1,1

    yield a
    yield b
    yield c

    while True:
        a,b,c = b,c,a+b+c
        yield c

def process(i, base, found):
    for b in base:
        if (i % b) == 0:
            found.append(i)
            return

    t = tribonacci()
    a, b, c = next(t), next(t), next(t)
    states = set([(a,b,c)])

    while True:
        v = next(t) % i

        if v == 0:
            break

        a, b, c = b, c, v

        if (a,b,c) in states:
            base.append(i)
            found.append(i)
            break
        else:
            states.add((a,b,c))

    i += 2

def main():
    i = 27
    base = []
    found = []

    while True:
        process(i, base, found)

        if len(found) == 124:
            print(found[-1])
            return
        
        i += 2

if  __name__ == "__main__":
    main()
