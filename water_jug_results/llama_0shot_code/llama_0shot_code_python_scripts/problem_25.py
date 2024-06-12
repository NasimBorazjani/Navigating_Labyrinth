
jugs = [(75, 1), (20, 2), (64, 3), (106, 4), (88, 5), (13, 6), (107, 7), (131, 8)]
buckets = [287, 394, 455]

def solve(jugs, buckets):
    jugs.sort(reverse=True)
    actions = []
    for i, b in enumerate(buckets):
        while b > 0:
            j = next((j for j in jugs if j[0] <= b), None)
            if j:
                if j[0] == b:
                    actions.append(('+', j[1], i+1))
                    b = 0
                else:
                    actions.append(('+', j[1], i+1))
                    b -= j[0]
                    jugs.remove(j)
            else:
                j = jugs.pop()
                actions.append(('+', j[1], i+1))
                b -= j[0]
                jugs.append((b, j[1]))
                jugs.sort(reverse=True)
    return actions

print(solve(jugs, buckets))
