
# capacities of the jugs
jug_capacities = [143, 117, 116, 103, 84, 87]
# target volumes for the buckets
bucket_volumes = [398, 440, 440]
# actions will be stored here
actions = []

# sort the jugs and buckets in descending order
jug_capacities.sort(reverse=True)
bucket_volumes.sort(reverse=True)

# for each bucket
for i in range(len(bucket_volumes)):
    remaining_volume = bucket_volumes[i]
    # for each jug
    for j in range(len(jug_capacities)):
        while remaining_volume > 0:
            # calculate the amount of water to add
            add_volume = min(remaining_volume, jug_capacities[j])
            # add the water
            actions.append(('+', jug_capacities[j], i+1))
            remaining_volume -= add_volume
    # if the bucket is not full, remove the excess water
    if remaining_volume < 0:
        actions.append(('-', remaining_volume, i+1))

print(actions)
