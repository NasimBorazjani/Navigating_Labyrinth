
stacks = [[], ['Green', 'Blue', 'Yellow', 'Green'], ['Yellow', 'Red', 'Red', 'Blue'], [], ['Blue', 'Green', 'Yellow', 'Red'], []]
costs = {0: 4, 1: 3, 2: 2, 3: 4, 4: 2, 5: 5}

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
