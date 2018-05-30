def sequence():
    n = '1'
    while True:
        yield n
        i = 0
        n2 = ''

        while i < len(n):
            c = n[i]
            count = 0

            while i < len(n) and n[i] == c:
                count += 1
                i += 1

            n2 += str(count) + str(c)

        n = n2

