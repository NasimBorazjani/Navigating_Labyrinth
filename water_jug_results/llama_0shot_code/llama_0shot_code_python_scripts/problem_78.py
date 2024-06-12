
def solve_water_jug_problem(jug_capacities, target_volumes):
    jug_capacities.sort(reverse=True)
    target_volumes.sort()
    actions = []
    i = 0
    for target in target_volumes:
        while i < len(jug_capacities) and jug_capacities[i] > target:
            i += 1
        if i == len(jug_capacities):
            i -= 1
            actions.append(('-', jug_capacities[i-1], len(target_volumes)))
            target += jug_capacities[i-1]
        actions.append(('+', jug_capacities[i], len(target_volumes)))
        target_volumes[len(target_volumes)-1] = 0
    return actions

jug_capacities = [58, 18, 19, 47, 86, 75, 119, 34]
target_volumes = [234, 331, 343, 379]

print(solve_water_jug_problem(jug_capacities, target_volumes))
