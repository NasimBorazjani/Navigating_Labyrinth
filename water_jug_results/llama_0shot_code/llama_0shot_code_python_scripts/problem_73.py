
def solve_water_jugs(jugs, buckets):
    # Sort the jugs and buckets in ascending order
    jugs.sort()
    buckets.sort()

    # Initialize the actions list
    actions = []

    # While there are still unlabeled buckets that need filling
    while buckets:
        # Get the current bucket and its target amount
        target = buckets.pop(0)

        # Find the jug with the largest capacity that is less than or equal to the remaining amount of water needed
        jug = next((j for j in jugs if j <= target), None)

        # If no such jug exists, find the jug with the smallest capacity that is larger than the remaining amount of water needed
        if jug is None:
            jug = next((j for j in jugs if j > target), None)

        # If no such jug exists, the problem is unsolvable
        if jug is None:
            return None

        # Add the appropriate action to the list of actions
        if jug <= target:
            actions.append(('+', jug, len(buckets) + 1))
        else:
            actions.append(('-', jug, len(buckets) + 1))

        # Update the remaining amount of water needed
        target -= jug

        # If there is still water needed, put the bucket back in the list
        if target > 0:
            buckets.insert(0, target)

    # Return the list of actions
    return actions

# Test the function
jugs = [56, 81, 132, 41, 86, 128, 57, 138]
buckets = [232, 401, 444, 451]
print(solve_water_jugs(jugs, buckets))
