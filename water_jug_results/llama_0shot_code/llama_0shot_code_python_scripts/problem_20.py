
jugs = [(76, 'A'), (48, 'B'), (35, 'C'), (94, 'D'), (93, 'E'), (115, 'F'), (16, 'G')]
buckets = [247, 261, 273]

def solve(jugs, buckets):
    jugs.sort(reverse=True)
    actions = []
    bucket_order = []
    for b in range(len(buckets)):
        bucket_order.append(b+1)
    bucket_order.sort()
    for b in bucket_order:
        while buckets[b-1] > 0:
            for j in jugs:
                if j[1] not in [i[2] for i in actions]:
                    if buckets[b-1] >= j[0]:
                        actions.append(('+', j[0], b))
                        buckets[b-1] -= j[0]
                    else:
                        actions.append(('+', buckets[b-1], b))
                        buckets[b-1] = 0
    return actions

print(solve(jugs, buckets))
