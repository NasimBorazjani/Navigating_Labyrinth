
def solve_water_jugs(jugs, buckets):
    # Sort jugs and buckets in ascending order
    jugs.sort()
    buckets.sort()

    actions = []
    for i in range(len(buckets)):
        difference = buckets[i] - sum(buckets[:i])
        while difference > 0:
            for j in range(len(jugs)):
                if jugs[j] <= difference:
                    actions.append(('+', jugs[j], i+1))
                    difference -= jugs[j]
                else:
                    actions.append(('+', difference, i+1))
                    difference = 0
                    break

    # Empty remaining jugs to the next bucket
    for i in range(len(jugs)):
        if jugs[i] > 0:
            actions.append(('-', jugs[i], buckets.index(min(buckets[i:]))+1))

    return actions

jugs = [73, 129, 120, 38, 72, 138]
buckets = [278, 295, 323, 383]

print(solve_water_jugs(jugs, buckets))
