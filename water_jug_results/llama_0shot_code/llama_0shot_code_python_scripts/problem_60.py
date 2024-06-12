
def solve_water_jugs(jug_capacities, bucket_capacities, water_amounts):
    # Sort capacities and amounts in ascending order
    jug_capacities.sort()
    bucket_capacities.sort()
    water_amounts.sort()

    # Initialize list of actions
    actions = []

    # For each pair of capacities and amounts of water
    for i in range(len(bucket_capacities)):
        # If amount of water is 0
        if water_amounts[i] == 0:
            # Empty the bucket
            actions.append(('-', min(jug_capacities), i+1))
        # If amount of water is less than capacity of the bucket
        elif water_amounts[i] < bucket_capacities[i]:
            # Fill the bucket
            actions.append(('+', min(jug_capacities), i+1))
        # If amount of water is more than capacity of the bucket
        elif water_amounts[i] > bucket_capacities[i]:
            # Fill the bucket to the top
            actions.append(('+', bucket_capacities[i], i+1))
            # Update the amount of water for the previous bucket
            water_amounts[i-1] -= (bucket_capacities[i] - water_amounts[i-1])
            i -= 1

    return actions

# Test the function
jug_capacities = [78, 68, 49, 82, 77, 88]
bucket_capacities = [78, 68, 49, 82]
water_amounts = [176, 189, 251, 285]
print(solve_water_jugs(jug_capacities, bucket_capacities, water_amounts))
