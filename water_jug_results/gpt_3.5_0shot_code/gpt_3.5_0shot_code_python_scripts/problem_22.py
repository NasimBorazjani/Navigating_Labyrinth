
from itertools import permutations

def pour_water(jugs, buckets):
    def fill(bucket, jug):
        if buckets[bucket] + jugs[jug] <= capacities[bucket]:
            return buckets[:bucket] + (buckets[bucket] + jugs[jug],) + buckets[bucket+1:]
        return None

    def empty(bucket):
        return buckets[:bucket] + (0,) + buckets[bucket+1:]

    def pour(bucket1, bucket2):
        space = capacities[bucket2] - buckets[bucket2]
        if buckets[bucket1] <= space:
            return (0,) * bucket1 + (buckets[bucket1] + buckets[bucket2],) + (0,) * (bucket2 - bucket1 - 1) + (0,) + buckets[bucket2+1:]
        return (0,) * bucket1 + (buckets[bucket1] - space,) + (capacities[bucket2],) + (0,) * (bucket2 - bucket1 - 1) + (0,) + buckets[bucket2+1:]

    capacities = [263, 341, 360]
    actions = []

    for perm in permutations(range(7), 3):
        buckets_copy = buckets
        temp_actions = []
        for i in perm:
            buckets_copy = fill(0, i)
            if buckets_copy is not None:
                temp_actions.append(('+', jugs[i], 1))
            buckets_copy = fill(1, i)
            if buckets_copy is not None:
                temp_actions.append(('+', jugs[i], 2))
            buckets_copy = fill(2, i)
            if buckets_copy is not None:
                temp_actions.append(('+', jugs[i], 3))
        if buckets_copy == tuple(capacities):
            actions = temp_actions
            break

    return actions

jugs = [16, 124, 57, 40, 99, 45, 72, 98]
buckets = (0, 0, 0)

result = pour_water(jugs, buckets)
print(result)
