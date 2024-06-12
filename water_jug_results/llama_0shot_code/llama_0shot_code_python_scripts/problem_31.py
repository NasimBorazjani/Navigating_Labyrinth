
jugs = [(14, 1), (46, 2), (13, 3), (110, 4), (38, 5), (21, 6), (45, 7)]
buckets = [215, 219, 262]

def solve(jugs, buckets):
    actions = []
    for i, b in enumerate(buckets):
        while b > 0:
            for c, j in sorted(jugs, reverse=True):
                if c <= b:
                    actions.append(('+', j, i+1))
                    b -= c
                    break
                else:
                    if i+1 < len(buckets) and buckets[i+1] >= c:
                        actions.append(('+', j, i+2))
                        buckets[i+1] -= c
                    else:
                        actions.append(('-', j, i+1))
                        b += c - min(c, b)
            jugs = sorted([(c, j) for c, j in jugs if c > 0], reverse=True)
    return actions

print(solve(jugs, buckets))
