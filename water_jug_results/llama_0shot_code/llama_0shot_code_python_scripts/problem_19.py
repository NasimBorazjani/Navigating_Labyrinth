
# capacities of the jugs
jug_capacities = [21, 62, 98, 143, 61, 110, 140, 40]
# target volumes for the buckets
bucket_volumes = [280, 338, 353]

# sort the jugs by capacity in ascending order
jug_capacities.sort()

# initialize the solution
solution = []

# for each bucket
for i in range(len(bucket_volumes)):
    # find the jug that can fill the current bucket to the maximum possible extent
    jug_index = next(x for x in range(len(jug_capacities)) if jug_capacities[x] >= bucket_volumes[i] - (sum(bucket_volumes[:i]) if i > 0 else 0))
    # if we have already filled some previous buckets, we need to remove the excess water from the current bucket
    if i > 0:
        solution.append(('-', jug_capacities[jug_index], i+1))
    # fill the current bucket with the selected jug
    solution.append(('+', jug_capacities[jug_index], i+1))

print(solution)
