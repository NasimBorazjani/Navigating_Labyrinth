
# capacities of the jugs
jug_capacities = [76, 135, 134, 19, 10, 30]
# target volumes for the buckets
target_volumes = [390, 420, 439]

# sort the capacities in descending order
jug_capacities.sort(reverse=True)

# initialize the buckets and actions
buckets = [0, 0, 0]
actions = []

# for each bucket
for i in range(3):
    # while there is still space in this bucket
    while buckets[i] < target_volumes[i]:
        # find the first jug that can fill the remaining space in this bucket
        for j in jug_capacities:
            if j <= target_volumes[i] - buckets[i]:
                # if this jug can fill the entire bucket
                if j == target_volumes[i] - buckets[i]:
                    actions.append(('+', j, i+1))
                    buckets[i] = target_volumes[i]
                # if this jug can partially fill the bucket
                else:
                    actions.append(('+', j, i+1))
                    buckets[i] += j
                break

print(actions)
