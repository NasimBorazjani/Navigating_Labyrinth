
stacks = [[], [], ['Green', 'Yellow', 'Black', 'Red', 'Black'], ['Black', 'Red', 'Yellow', 'Blue', 'Yellow'], ['Green', 'Blue', 'Blue', 'Red', 'Black'], [], [], ['Red', 'Green', 'Blue', 'Green', 'Yellow']]
costs = {0: 5, 1: 5, 2: 1, 3: 7, 4: 7, 5: 9, 6: 1, 7: 6}

transfer_pairs = []

for i in range(len(stacks)):
    for j in range(len(stacks[i])):
        block = stacks[i][j]
        min_cost = float('inf')
        min_dest = -1
        
        for k in range(len(stacks)):
            if i != k and (len(stacks[k]) == 0 or stacks[k][-1] == block):
                cost = costs[k]
                if cost < min_cost:
                    min_cost = cost
                    min_dest = k
        
        if min_dest != -1:
            transfer_pairs.append((i, min_dest))
            stacks[min_dest].append(stacks[i].pop())
            
print(transfer_pairs)
