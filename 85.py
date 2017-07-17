n = 1

total = 0
while True:
    total += n*n*n
    if total > 2000000:
        break
    n += 1

print(n)
