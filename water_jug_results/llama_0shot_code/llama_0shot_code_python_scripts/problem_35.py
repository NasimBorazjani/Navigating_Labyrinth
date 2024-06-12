
# capacities of the jugs
jug_capacities = [120, 95, 49, 150, 83, 97, 44, 43]
# target volumes for the buckets
bucket_volumes = [225, 334, 381]

def solve_water_jug_problem(jug_capacities, bucket_volumes):
    actions = []
    # iterate over each bucket
    for i, volume in enumerate(bucket_volumes):
        remaining = volume
        while remaining > 0:
            # find the jug that can fill the remaining volume 
            # in the least number of steps
            jug_index = min(range(len(jug_capacities)), 
                            key=lambda x: (remaining % jug_capacities[x] != 0,
                                           -remaining // jug_capacities[x],
                                           jug_capacities[x]))
            jug_capacity = jug_capacities[jug_index]
            steps = remaining // jug_capacity
            # add the action to fill the bucket
            actions.append(('+', jug_capacity, i+1))
            remaining -= steps * jug_capacity
            # empty the jug
            if steps > 0:
                actions.append(('-', jug_capacity, i+1))
                jug_capacities[jug_index] = 0
        # remove the filled bucket
        bucket_volumes[i] = 0
    return actions

print(solve_water_jug_problem(jug_capacities, bucket_volumes))
