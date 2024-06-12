
jugs = [(150, 'A'), (84, 'B'), (29, 'C'), (140, 'D'), (98, 'E'), (83, 'F'), (32, 'G')]
buckets = [243, 250, 446]

def solve(jugs, buckets):
    jugs.sort(reverse=True)
    actions = []
    for i, b in enumerate(buckets):
        while b > 0:
            for j, (capacity, label) in enumerate(jugs):
                if capacity <= b:
                    b -= capacity
                    actions.append(('+', label, i+1))
                    jugs[j] = (capacity, label)
                    break
                else:
                    actions.append(('-', label, i+1))
                    b += capacity - b
                    jugs[j] = (0, label)
    return actions

print(solve(jugs, buckets))
