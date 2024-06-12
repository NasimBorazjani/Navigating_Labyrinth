
def solve_water_jugs(jug_capacities, bucket_capacities, target_volumes):
    actions = []
    jugs = sorted([(capacity, 'jug'+str(i+1)) for i, capacity in enumerate(jug_capacities)], reverse=True)
    buckets = sorted([(volume, 'bucket'+str(i+1)) for i, volume in enumerate(bucket_capacities)], reverse=True)

    while True:
        for i, (capacity, jug) in enumerate(jugs):
            for j, (volume, bucket) in enumerate(buckets):
                if volume < target_volumes[j]:
                    to_fill = min(capacity, target_volumes[j] - volume)
                    actions.append(('+', jug, bucket, to_fill))
                    volume += to_fill
                    if volume > bucket_capacities[j]:
                        actions.append(('-', bucket, bucket_capacities[j] - (volume - bucket_capacities[j])))
                        volume = bucket_capacities[j]
                    buckets[j] = (volume, bucket)
        if all(volume == target for volume, target in zip(bucket_capacities, target_volumes)):
            break

    return actions

jug_capacities = [140, 58, 129, 130, 125]
bucket_capacities = [391, 401, 431]
target_volumes = [391, 401, 431]

print(solve_water_jugs(jug_capacities, bucket_capacities, target_volumes))
