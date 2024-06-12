
def solve_water_jugs(jug_capacities, bucket_capacities, target_volumes):
    actions = []
    while target_volumes:
        jug_index = -1
        for i, (jug_capacity, target_volume) in enumerate(zip(jug_capacities, target_volumes)):
            if target_volume > 0:
                jug_index = i
                break
        if jug_index == -1:
            return None
        jug_capacity, target_volume = jug_capacities[jug_index], target_volumes[jug_index]
        for i, (bucket_capacity, bucket_target) in enumerate(zip(bucket_capacities, target_volumes)):
            if bucket_target < target_volume and bucket_capacity - bucket_target >= target_volume - bucket_target:
                actions.append(('+', jug_capacity, i + 1))
                target_volumes[jug_index] -= target_volume - bucket_target
                target_volumes[i] = bucket_target
                break
            elif bucket_target == target_volume and bucket_capacity >= target_volume:
                actions.append(('+', jug_capacity, i + 1))
                target_volumes[jug_index] = 0
                break
        else:
            return None
    return actions

jug_capacities = [46, 99, 145, 131, 78, 100]
bucket_capacities = [247, 340, 368]
target_volumes = [247, 340, 368]

actions = solve_water_jugs(jug_capacities, bucket_capacities, target_volumes)
print(actions)
