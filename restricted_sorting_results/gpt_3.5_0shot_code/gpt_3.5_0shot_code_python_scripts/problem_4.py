
stacks = [['Red', 'Green', 'Yellow', 'Blue'], [], ['Yellow', 'Green', 'Blue', 'Red'], [], ['Green', 'Red', 'Blue', 'Yellow'], []]
costs = {0: 2, 1: 6, 2: 5, 3: 2, 4: 5, 5: 7}

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
