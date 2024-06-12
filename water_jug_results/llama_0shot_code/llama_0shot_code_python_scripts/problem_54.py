
jugs = [(45, 1), (67, 2), (134, 3), (133, 4), (86, 5), (66, 6), (107, 7), (94, 8), (124, 9), (122, 10)]
buckets = [229, 303, 307]

def solve(jugs, buckets):
    jugs.sort(reverse=True)
    actions = []
    bucket_index = 0

    for jug in jugs:
        while buckets[bucket_index] <= jug[0]:
            actions.append(('+', jug[1], bucket_index+1))
            buckets[bucket_index] -= jug[0]

            if bucket_index < len(buckets) - 1:
                bucket_index += 1
            else:
                break

    return actions

print(solve(jugs, buckets))
