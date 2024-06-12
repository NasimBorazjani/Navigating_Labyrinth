
jugs = [(71, 1), (124, 2), (95, 3), (42, 4), (56, 5), (41, 6)]  # list of jugs with their capacities
buckets = [291, 292, 326]  # list of target capacities for the buckets

def solve_puzzle(jugs, buckets):
    actions = []
    for i in range(len(buckets)):
        remaining = buckets[i]
        if i < len(buckets) - 1:
            remaining -= buckets[i + 1]
        while remaining > 0:
            jug = max(filter(lambda x: x[0] <= remaining, jugs), key=lambda x: x[0])
            if jug[0] <= remaining:
                actions.append(('+', jug[1], i + 1))
                remaining -= jug[0]
            else:
                break
    return actions

print(solve_puzzle(jugs, buckets))
