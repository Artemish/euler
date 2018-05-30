from factoring import cheese_primes_below

INFINITY=10000000

def digital_root(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n

def superlist(l1, l2):
    l1 = [i for i in l1]
    l2 = [i for i in l2]
    output = []

    while len(l1) > 0 and len(l2) > 0:
        # print(l1)
        # print(l2)

        try:
            one_to_two = l2.index(l1[0])
        except:
            one_to_two = INFINITY

        try:
            two_to_one = l1.index(l2[0])
        except:
            two_to_one = INFINITY

        if one_to_two < two_to_one:
            # print("A Taking " + str(l2[:one_to_two+1]))
            output.extend(l2[:one_to_two+1])
            l2 = l2[one_to_two+1:]
            del l1[0]
        elif one_to_two > two_to_one:
            # print("B Taking " + str(l1[:two_to_one+1]))
            output.extend(l1[:two_to_one+1])
            l1 = l1[two_to_one+1:]
            del l2[0]
        else:
            if l1[0] < l2[0]:
                # print("C Taking " + str(l1[0]))
                output.append(l1[0])
                del l1[0]
            else:
                # print("D Taking " + str(l2[0]))
                output.append(l2[0])
                del l2[0]

    return output + l2 + l1

TOP=10

primes = sorted(cheese_primes_below(120000))[:TOP]
composites = [i for i in range(1,2*TOP) if i not in primes][1:TOP+1]

p_digits = map(digital_root, primes)
c_digits = map(digital_root, composites)

#                                           1000000007
superint = reduce(lambda x, y: (x*10 + y), superlist(p_digits, c_digits))
