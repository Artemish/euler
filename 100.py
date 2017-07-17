x = 20
total = 100

while True:
    x_candidate = x ** 2
    rho = (1 + 2 * total * total - 2 * total)

    if x_candidate == rho:
        print("Got x = " + str(x_candidate))
        break
    elif x_candidate < rho:
        x += 1
    else:
        total += 1
