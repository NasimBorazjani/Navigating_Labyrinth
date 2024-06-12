
jugs = [(149, 1), (128, 2), (67, 3), (43, 4), (55, 5), (38, 6), (129, 7)]
buckets = [385, 387, 491]

def solve(jugs, buckets):
    actions = []
    for i, b in enumerate(buckets):
        while b > 0:
            j = max(jugs, key=lambda x: min(x[0], b))
            if j[0] <= b:
                actions.append(('+', j[1], i+1))
                b -= j[0]
                jugs.remove(j)
            else:
                amount = b
                for k in sorted(jugs, key=lambda x: -x[0]):
                    if k[0] <= amount:
                        actions.append(('+', k[1], i+1))
                        amount -= k[0]
                        jugs.remove(k)
                        if amount == 0:
                            break
                b = 0
    return actions

print(solve(jugs, buckets))
