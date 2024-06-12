
stacks = [[], [], ['Blue', 'Blue', 'Blue', 'Green', 'Black', 'Red'], [], ['Red', 'Black', 'Blue', 'White', 'Blue', 'Yellow'], ['Yellow', 'White', 'Green', 'Black', 'Yellow', 'Red'], [], [], ['White', 'Black', 'White', 'White', 'Black', 'Red'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow', 'Green']]
costs = {0: 3, 1: 10, 2: 9, 3: 8, 4: 8, 5: 7, 6: 6, 7: 9, 8: 2, 9: 8}

transfer_pairs = []

for i in range(len(stacks)):
    for j in range(len(stacks[i])):
        min_cost = float('inf')
        min_dest = -1
        for k in range(len(stacks)):
            if k == i:
                continue
            if len(stacks[k]) == 0 or stacks[k][-1] == stacks[i][j]:
                cost = costs[k]
                if cost < min_cost:
                    min_cost = cost
                    min_dest = k
        transfer_pairs.append((i, min_dest))
        stacks[min_dest].append(stacks[i][j])
        stacks[i].pop()

print(transfer_pairs)
