def isA003592(n):
    while (n % 2) == 0:
        n /= 2
    while (n % 5) == 0:
        n /= 5
    return n == 1

def A051626(n):
    if isA003592(n):
        return 0
    else:
        lpow=1
        while True:
            for mpow in range(lpow-1, -1, -1):
                if (10**lpow-10**mpow) % n == 0:
                    return lpow-mpow
            lpow += 1
