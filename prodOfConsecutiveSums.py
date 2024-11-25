bound = 2024
prod = 1

def sum_from(lbound):
    t = 0
    els = 0
    for i in range(lbound, bound + 1):
        t += i
        els += 1
        if t == bound:
            return True, els
    return False, els

for j in range(bound + 1):
    c = sum_from(j)
    if c[0]:
        prod *= c[1]

print(prod)
