
def water_jug_problem(jugs, buckets):
    # Sort the jugs and buckets by their capacities
    jugs.sort(reverse=True)
    buckets.sort()

    # Initialize the actions and the remaining capacities of the buckets
    actions = []
    remaining_capacities = [b for b in buckets]

    # While there are still buckets to fill
    while max(remaining_capacities) > 0:
        # Find the jug with the largest capacity that is less than or equal to the remaining capacity of the current bucket
        jug = next((j for j in jugs if j <= remaining_capacities[0]), None)

        # If no such jug exists, return 'No Solution'
        if jug is None:
            return 'No Solution'

        # Add the action to fill the current bucket with the water from the jug
        actions.append(('+', jug, 0))

        # Update the remaining capacity of the current bucket
        remaining_capacities[0] -= jug

        # Remove the jug from the list of jugs
        jugs.remove(jug)

        # Sort the remaining jugs and buckets by their capacities
        jugs.sort(reverse=True)
        remaining_capacities.sort()

    # Return the list of actions
    return actions

# Test the function
jugs = [127, 96, 108, 126, 132, 139, 146, 14]
buckets = [273, 349, 435, 503]
print(water_jug_problem(jugs, buckets))
