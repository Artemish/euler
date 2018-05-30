from collections import defaultdict

THRESHOLD = 990000 

def lagged_fibonacci():
    record = [(100003 - 200003*k + 300007*k*k*k) % 1000000 for k in range(1,56)]
    for v in record:
        yield v

    while True:
        v = (record[-24] + record[0]) % 1000000
        del record[0]
        record.append(v)

        yield v

PM = 524287
components = [set([PM])]
n_to_c = [-1] * 1000000
n_to_c[PM] = 0

gen = lagged_fibonacci()
calls = 0

while True:
    if (calls % 10000) == 0:
        print("Made {} calls".format(calls))

    caller = next(gen)
    called = next(gen)

    if caller == called:
        continue

    calls += 1

    caller_c = n_to_c[caller]
    called_c = n_to_c[called]

    if (caller_c == -1) and (called_c == -1):
        components.append(set([caller, called]))
        n_to_c[caller] = len(components) - 1
        n_to_c[called] = len(components) - 1
        continue
    elif caller_c == called_c:
        continue

    if (caller_c != -1) and (called_c == -1):

        caller_component = n_to_c[caller]
        components[caller_component].add(called)
        n_to_c[called] = caller_component

        new_size = len(components[caller_component])
        new_component = caller_component

    elif (caller_c == -1) and (called_c != -1):
        called_component = n_to_c[called]
        components[called_component].add(caller)
        n_to_c[caller] = called_component

        new_size = len(components[called_component])
        new_component = called_component

    else:
        combined = components[n_to_c[caller]] | components[n_to_c[called]]
        components[n_to_c[caller]] = combined
        components[n_to_c[called]] = combined

        new_size = len(combined)
        new_component = combined
        print("Combining {} and {} - size {}".format(caller, called, new_size))

    if new_size > THRESHOLD and 524287 in new_component:
        break

print(calls)
