
stacks = [[], ['Blue', 'Black', 'Black', 'Yellow', 'White', 'Green'], ['Green', 'Black', 'Red', 'Green', 'Yellow', 'Blue'], [], ['Green', 'Red', 'Blue', 'Yellow', 'Green', 'Blue'], ['Black', 'White', 'White', 'Red', 'White', 'Black'], [], ['White', 'Red', 'Blue', 'Yellow', 'Yellow', 'Red'], [], []]
costs = {0: 5, 1: 4, 2: 7, 3: 7, 4: 11, 5: 11, 6: 8, 7: 3, 8: 7, 9: 9}

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
        if min_dest != -1:
            transfer_pairs.append((i, min_dest))
            stacks[min_dest].append(stacks[i].pop())

print(transfer_pairs)
