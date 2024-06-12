
# capacities of the jugs
jug_capacities = [36, 88, 132, 70, 87, 111]
# target volumes for the buckets
bucket_volumes = [225, 237, 243]

def water_jug_problem(jug_capacities, bucket_volumes):
    actions = []
    for i in range(len(bucket_volumes)):
        remaining = bucket_volumes[i]
        while remaining > 0:
            jug_index = -1
            for j in range(len(jug_capacities)):
                if jug_capacities[j] <= remaining and (jug_index == -1 or jug_capacities[j] > jug_capacities[jug_index]):
                    jug_index = j
            if i < len(bucket_volumes) - 1 and bucket_volumes[i+1] < remaining - jug_capacities[jug_index]:
                actions.append(('+', jug_capacities[jug_index], i+1))
                remaining -= jug_capacities[jug_index]
            else:
                actions.append(('+', remaining, i))
                remaining = 0
    return actions

print(water_jug_problem(jug_capacities, bucket_volumes))
