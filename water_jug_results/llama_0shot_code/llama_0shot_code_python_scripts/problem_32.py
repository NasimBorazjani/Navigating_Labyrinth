
jugs = [(137, 'A'), (29, 'B'), (70, 'C'), (138, 'D'), (47, 'E'), (64, 'F'), (87, 'G')]
buckets = [295, 327, 442]

def solve(jugs, buckets):
    actions = []
    for i, b in enumerate(buckets):
        while b > 0:
            for c, j in sorted(jugs, key=lambda x: -x[0]):
                if c <= b:
                    actions.append(('+', j, i+1))
                    b -= c
                    break
                else:
                    actions.append(('+', j, i+1))
                    b -= c
            if b > 0:
                actions.append(('-', 'bucket', i+1))
    return actions

print(solve(jugs, buckets))
