sequence = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
steps = map(lambda c: {'D': 0, 'U': 1, 'd': 2}[c], sequence)

def collatz(n):
  while n != 1:
    if (n % 3) == 0:
      n /= 3
      yield 'D'
    elif (n % 3) == 1:
      n = (4*n + 2) // 3
      yield 'U'
    else:
      n = (2*n - 1) // 3
      yield 'd'

def cz(n):
    print(''.join(list(collatz(n))))
