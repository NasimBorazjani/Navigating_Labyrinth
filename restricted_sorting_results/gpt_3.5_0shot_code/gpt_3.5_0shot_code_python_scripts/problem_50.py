
stacks = [[], [], ['Blue', 'Green', 'Black', 'Blue', 'Red'], ['Green', 'Red', 'Blue', 'Black', 'Blue'], [], ['Red', 'Green', 'Yellow', 'Yellow', 'Black'], ['Green', 'Black', 'Red', 'Yellow', 'Yellow'], []]
costs = {0: 1, 1: 3, 2: 3, 3: 8, 4: 7, 5: 9, 6: 8, 7: 8}

transfer_pairs = []

for i in range(len(stacks)):
    if stacks[i]:
        block = stacks[i][-1]
        min_cost = float('inf')
        min_cost_index = -1
        
        for j in range(len(stacks)):
            if i != j and (not stacks[j] or stacks[j][-1] == block):
                if costs[j] < min_cost:
                    min_cost = costs[j]
                    min_cost_index = j
        
        if min_cost_index != -1:
            transfer_pairs.append((i, min_cost_index))
            stacks[min_cost_index].append(stacks[i].pop())

print(transfer_pairs)
