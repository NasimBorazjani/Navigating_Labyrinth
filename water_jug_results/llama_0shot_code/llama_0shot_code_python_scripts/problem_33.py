
jugs = [(146, 'A'), (57, 'B'), (69, 'C'), (52, 'D'), (132, 'E'), (80, 'F'), (145, 'G')]
buckets = [456, 538, 549]

def solve(jugs, buckets):
    actions = []
    jugs.sort(reverse=True)
    bucket_order = sorted(range(len(buckets)), key=lambda i: -buckets[i])
    bucket_index = 0
    while True:
        while buckets[bucket_order[bucket_index]] > 0:
            for i, (capacity, label) in enumerate(jugs):
                if capacity <= buckets[bucket_order[bucket_index]]:
                    actions.append(('+', label, bucket_order[bucket_index] + 1))
                    buckets[bucket_order[bucket_index]] -= capacity
                    jugs[i] = (0, label)
                    break
            else:
                break
            bucket_index += 1
        if bucket_index == len(buckets):
            break
        while buckets[bucket_order[bucket_index]] == 0:
            bucket_index += 1
            if bucket_index == len(buckets):
                break
    return actions

print(solve(jugs, buckets))
