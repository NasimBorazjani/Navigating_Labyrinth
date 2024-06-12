
stacks = [[], ['Yellow', 'White', 'Blue', 'Yellow', 'Red', 'White'], [], [], ['Blue', 'Blue', 'Green', 'Black', 'Black', 'Red'], ['Black', 'Green', 'Yellow', 'Yellow', 'Blue', 'Black'], [], ['White', 'Blue', 'Green', 'White', 'Yellow', 'Red'], [], ['Green', 'White', 'Black', 'Red', 'Green', 'Red']]
costs = {0: 3, 1: 6, 2: 3, 3: 6, 4: 9, 5: 6, 6: 6, 7: 10, 8: 2, 9: 5}

transfer_pairs = []

for i in range(len(stacks)):
    for j in range(len(stacks[i])):
        min_cost = float('inf')
        min_dest = -1
        for k in range(len(stacks)):
            if i != k and (len(stacks[k]) == 0 or stacks[k][-1] == stacks[i][j]):
                cost = costs[k]
                if cost < min_cost:
                    min_cost = cost
                    min_dest = k
        transfer_pairs.append((i, min_dest))
        stacks[min_dest].append(stacks[i][j])
        stacks[i].pop()

print(transfer_pairs)
