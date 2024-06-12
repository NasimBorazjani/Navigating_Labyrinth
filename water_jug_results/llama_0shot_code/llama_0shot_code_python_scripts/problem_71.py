
def solve_water_jugs(jug_capacities, bucket_amounts):
    actions = []
    while bucket_amounts:
        # Find the jug with the largest capacity that is smaller than the amount of water that needs to be distributed
        # and the smallest capacity of the unfilled buckets
        jug_index = -1
        for i, capacity in enumerate(jug_capacities):
            if capacity <= bucket_amounts[0] < bucket_amounts[1]:
                jug_index = i
                break

        # If no such jug exists, find the smallest jug and the smallest unfilled bucket, and move the water between them
        if jug_index == -1:
            min_jug_index = jug_capacities.index(min(jug_capacities))
            min_bucket_index = bucket_amounts.index(min(bucket_amounts))
            min_amount = min(bucket_amounts[min_bucket_index], jug_capacities[min_jug_index])
            actions.append(('+', min_jug_index + 1, min_bucket_index + 1))
            bucket_amounts[min_bucket_index] -= min_amount
            jug_capacities[min_jug_index] -= min_amount
        else:
            # Otherwise, fill the smallest unfilled bucket with the jug
            actions.append(('+', jug_index + 1, 0))
            bucket_amounts[0] -= jug_capacities[jug_index]
            jug_capacities[jug_index] = 0

        # Remove the bucket that is now full from the list of unfilled buckets
        bucket_amounts.pop(0)

    return actions

jug_capacities = [141, 92, 12, 77, 49, 140]
bucket_amounts = [304, 333, 349, 413]
bucket_amounts.sort()

print(solve_water_jugs(jug_capacities, bucket_amounts))
