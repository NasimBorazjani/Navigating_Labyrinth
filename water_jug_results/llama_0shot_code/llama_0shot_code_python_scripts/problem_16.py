
def solve_water_jug_problem(jug_capacities, bucket_capacities, water_amounts):
    actions = []
    while water_amounts:
        # Find the jug with the largest capacity smaller than the remaining water amount
        # and the bucket with the smallest capacity that needs more water
        jug_index = -1
        bucket_index = -1
        for i, jug_capacity in enumerate(jug_capacities):
            if jug_capacity <= water_amounts[0]:
                for j, (bucket_capacity, amount_needed) in enumerate(zip(bucket_capacities, water_amounts)):
                    if amount_needed > 0 and bucket_capacity - amount_needed >= jug_capacity:
                        jug_index = i
                        bucket_index = j
                        break
                if bucket_index >= 0:
                    break

        # If no such jug and bucket exist, the task is impossible
        if jug_index == -1 or bucket_index == -1:
            return []

        # Add water to the bucket from the jug
        amount_added = min(water_amounts[0], jug_capacities[jug_index])
        actions.append(('+', jug_capacities[jug_index], bucket_index + 1))
        water_amounts[0] -= amount_added

        # If the jug is now empty, remove it from the list of capacities
        if water_amounts[0] == 0:
            del water_amounts[0]
            del jug_capacities[jug_index]

    return actions

jug_capacities = [102, 130, 82, 131, 133, 116]
bucket_capacities = [265, 368, 378]
water_amounts = [265, 368, 378]

actions = solve_water_jug_problem(jug_capacities, bucket_capacities, water_amounts)
print(actions)
