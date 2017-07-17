TOP = 6

def recurrence(l, r):
    if l == 1:
        return 1
    if r == 0:
        return 1

    return sum([recurrence(i+1, r-1) for i in range(l)])

inc = recurrence(10, TOP)
dec = recurrence(10, TOP)

print(inc + dec)
