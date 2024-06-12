
jug_capacities = [141, 116, 66, 83, 142]
bucket_capacities = [397, 401, 419, 425]

jug_capacities.sort()
bucket_capacities.sort()

actions = []

for i in range(len(bucket_capacities)):
    difference = bucket_capacities[i] - jug_capacities[i]
    if difference > 0:
        actions.append(('+', jug_capacities[i], i+1))
    elif difference < 0:
        actions.append(('-', jug_capacities[i], i+1))

remaining_water = sum(jug_capacities) - sum(bucket_capacities)
if remaining_water > 0:
    for i in range(len(jug_capacities)):
        if jug_capacities[i] <= remaining_water:
            actions.append(('-', jug_capacities[i], i+1))
            remaining_water -= jug_capacities[i]
        else:
            actions.append(('-', remaining_water, i+1))
            remaining_water = 0
            break

print(actions)
