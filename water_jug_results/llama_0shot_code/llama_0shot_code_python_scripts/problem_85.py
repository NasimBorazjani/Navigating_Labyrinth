
def water_jug_problem(jugs, buckets):
    # Sort jugs in descending order
    jugs.sort(reverse=True)
    # Sort buckets in ascending order
    buckets.sort()
    actions = []
    for i in range(len(buckets)):
        diff = buckets[i] - (sum(buckets[:i]) if i > 0 else 0)
        for j in range(len(jugs)):
            if diff <= jugs[j]:
                # Add action to fill the difference
                actions.append(('+', jugs[j], i+1))
                # Update the jug and bucket capacities
                jugs[j] = 0
                buckets[i] = diff
                break
        else:
            return 'No Solution'
    return actions

# Test the function
jugs = [67, 98, 66, 59, 37, 61, 128, 92]
buckets = [308, 309, 387, 433]
print(water_jug_problem(jugs, buckets))
