
jugs = [(15, 1), (138, 2), (24, 3), (10, 4), (30, 5), (82, 6), (11, 7)]
buckets = [239, 275, 286]

def solve(jugs, buckets):
    actions = []
    for i in range(len(buckets)):
        remaining = buckets[i]
        while remaining > 0:
            for jug in sorted(jugs, key=lambda x: x[0], reverse=True):
                if jug[0] <= remaining:
                    actions.append(('+', jug[1], i+1))
                    remaining -= jug[0]
                    break
                else:
                    amount = min(remaining, jug[0])
                    actions.append(('+', jug[1], i+1))
                    remaining -= amount
            if remaining > 0:
                actions.append(('-', buckets[i-1], i))
    return actions

print(solve(jugs, buckets))
