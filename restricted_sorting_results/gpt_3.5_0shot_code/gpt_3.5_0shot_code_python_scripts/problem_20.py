
initial_state = [[], ['Green', 'Red', 'Yellow', 'Blue'], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Red', 'Yellow', 'Blue', 'Green'], []]
costs = {0: 4, 1: 2, 2: 5, 3: 2, 4: 4, 5: 1}

transfer_pairs = []

for i in range(len(initial_state)):
    for j in range(len(initial_state[i])):
        block = initial_state[i][j]
        min_cost = float('inf')
        min_dest = -1
        
        for k in range(len(initial_state)):
            if k != i and (len(initial_state[k]) == 0 or initial_state[k][-1] == block):
                cost = costs[k]
                if cost < min_cost:
                    min_cost = cost
                    min_dest = k
        
        if min_dest != -1:
            transfer_pairs.append((i, min_dest))
            initial_state[min_dest].append(initial_state[i].pop())
            
print(transfer_pairs)
