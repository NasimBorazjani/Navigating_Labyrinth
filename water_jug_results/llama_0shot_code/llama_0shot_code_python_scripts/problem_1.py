
jugs = [(41, 1), (26, 2), (44, 3), (75, 4), (40, 5), (136, 6)]  # capacities and labels
buckets = [274, 297, 343]  # target volumes

# sort jugs and buckets by volume
jugs.sort(key=lambda x: x[0])
buckets.sort()

solution = []

for i, b in enumerate(buckets):
    remaining = b
    while remaining > 0:
        # find the largest jug that fits in the remaining space
        for j, (capacity, label) in enumerate(jugs):
            if capacity <= remaining:
                jugs.pop(j)  # remove the used jug
                solution.append(('+', label, i+1))
                remaining -= capacity
                break
        else:
            # if no jug fits in the remaining space, move the water to the next bucket
            solution.append(('-', labels[i], i+2))
            remaining = b

print(solution)
