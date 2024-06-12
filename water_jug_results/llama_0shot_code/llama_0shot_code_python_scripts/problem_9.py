
jugs = [(129, 'A'), (57, 'B'), (45, 'C'), (105, 'D'), (128, 'E'), (78, 'F')]
buckets = [344, 376, 386]

def solve(jugs, buckets):
    actions = []
    for i in range(len(buckets)):
        while buckets[i] > 0:
            jug = max(jugs, key=lambda x: min(x[0], buckets[i]))
            amount = min(jug[0], buckets[i])
            if amount == jug[0]:
                actions.append(('+', jug[1], i+1))
            else:
                actions.append(('-', jug[1], i+1))
            buckets[i] -= amount
    return actions

print(solve(jugs, buckets))
