
stacks = [['White', 'Green', 'Red', 'Blue', 'Red', 'Yellow'], 
          ['Black', 'Black', 'White', 'Blue', 'Green', 'Green'], 
          ['White', 'Blue', 'White', 'Yellow', 'Black', 'Green'], 
          [], [], [], [], 
          ['Green', 'Yellow', 'Red', 'White', 'Blue', 'Black'], 
          ['Yellow', 'Red', 'Blue', 'Red', 'Black', 'Yellow'], 
          []]

costs = {0: 8, 1: 8, 2: 10, 3: 6, 4: 8, 5: 4, 6: 3, 7: 7, 8: 11, 9: 9}

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
            stacks[min_dest].append(stacks[i].pop(j))
        
print(transfer_pairs)
