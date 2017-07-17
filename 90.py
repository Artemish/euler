from itertools import product, combinations

possibilities = product(combinations(range(10), 6), combinations(range(10), 6))

def covers((d1, d2)):
    if d2 > d1:
        return 0

    # Non sixes
    for a,b in [(0,1), (0,4), (2,5), (8,1)]:
        if not ((a in d1 and b in d2) or (a in d2 and b in d1)):
            print(a,b)
            return 0

    if not (((6 in d1 or 9 in d1) and 4 in d2) or ((6 in d2 or 9 in d2) and 4 in d1)):
        print("No 49")
        return 0

    for a in [0,1,3,4]:
        if not (((6 in d1 or 9 in d1) and a in d2) or ((6 in d2 or 9 in d2) and a in d1)):
            print(a)
            return 0

    return 1

d1, d2 = [0,5,9,7,8,9], [1,2,3,4,8,9]

print("Total: " + str(sum(map(covers, possibilities))))
