
def water_jug_problem():
    # Bucket capacities and target amounts
    buckets = [357, 384, 522]
    # Jug capacities
    jugs = [52, 131, 82, 132, 117, 65]
    # Actions list
    actions = []

    # Fill the buckets
    for i in range(len(buckets)):
        while buckets[i] > 0:
            for j in range(len(jugs)):
                if jugs[j] <= buckets[i]:
                    actions.append(('+', jugs[j], i+1))
                    buckets[i] -= jugs[j]
                else:
                    if buckets[i] < jugs[j]:
                        actions.append(('+', buckets[i], i+1))
                        jugs[j] -= buckets[i]
                        buckets[i] = 0
                    else:
                        actions.append(('+', jugs[j], i+1))
                        buckets[i] -= jugs[j]

    return actions

print(water_jug_problem())
