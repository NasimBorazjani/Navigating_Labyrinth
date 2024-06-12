
# capacities of the jugs
jug_capacities = [56, 92, 66, 85, 65, 136]
# target volumes for the buckets
bucket_volumes = [209, 293, 326, 379]
# initialize the buckets with 0 volume
buckets = [0]*len(bucket_volumes)
# sort the jug capacities in descending order
jug_capacities.sort(reverse=True)
# list to store the actions
actions = []

for i in range(len(bucket_volumes)):
    remaining = bucket_volumes[i]
    while remaining > 0:
        for j in range(len(jug_capacities)):
            if remaining >= jug_capacities[j] and buckets[i] + jug_capacities[j] <= bucket_volumes[i+1] if i < len(bucket_volumes)-1 else True:
                actions.append(('+', jug_capacities[j], i+1))
                buckets[i] += jug_capacities[j]
                remaining -= jug_capacities[j]
                break
            elif buckets[i] >= jug_capacities[j] and buckets[i] - jug_capacities[j] >= bucket_volumes[i] if i > 0 else 0:
                actions.append(('-', jug_capacities[j], i+1))
                buckets[i] -= jug_capacities[j]
                break

print(actions)
