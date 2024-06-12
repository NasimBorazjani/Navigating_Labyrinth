
def water_jug_problem(jugs, buckets):
    # Sort jugs and buckets in ascending order
    jugs.sort()
    buckets.sort()

    actions = []
    for i in range(len(buckets)):
        diff = buckets[i] - sum(buckets[:i])
        found = False
        for j in range(len(jugs)):
            if jugs[j] <= diff:
                actions.append(('+', jugs[j], i+1))
                found = True
                break
        if not found:
            return 'No Solution'

    return actions

jugs = [146, 45, 136, 13, 148, 17, 42, 137, 141, 31]
buckets = [307, 384, 555, 575]

print(water_jug_problem(jugs, buckets))
