
jugs = [(80, 1), (76, 2), (132, 3), (60, 4), (83, 5), (28, 6), (75, 7)]
buckets = [337, 378, 398]

def solve(jugs, buckets):
    actions = []
    for i, b in enumerate(buckets):
        while b > 0:
            j = next((j for j in sorted(jugs, key=lambda x: x[0]-x[1]) if j[0] <= b), None)
            if j:
                if j[0] == b:
                    actions.append(('+', j[1], i+1))
                    b = 0
                else:
                    actions.append(('+', j[1], i+1))
                    b -= j[0]
                    jugs.remove(j)
            else:
                break
    return actions

print(solve(jugs, buckets))
