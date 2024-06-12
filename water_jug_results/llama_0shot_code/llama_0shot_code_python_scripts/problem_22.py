
# capacities of the jugs
jugs = [16, 124, 57, 40, 99, 45, 72, 98]
# target volumes for the buckets
buckets = [263, 341, 360]

def solve_water_jug_problem(jugs, buckets):
    actions = []
    for i, b in enumerate(buckets):
        remaining = b
        while remaining > 0:
            # find the jug that gives us the maximum remaining capacity after filling a bucket
            jug_index = max(range(len(jugs)), key=lambda j: min(remaining, jugs[j]) if remaining <= jugs[j] else 0)
            amount = min(remaining, jugs[jug_index])
            if amount > 0:
                actions.append(('+', jugs[jug_index], i+1))
                remaining -= amount
                if remaining > 0:
                    # empty the jug since it cannot be used for the next bucket
                    actions.append(('-', jugs[jug_index], i+1))
    return actions

print(solve_water_jug_problem(jugs, buckets))
