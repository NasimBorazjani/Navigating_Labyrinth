
stacks = [[], [], ['Blue', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Black'], ['Red', 'Red', 'Blue', 'White', 'Blue', 'Black'], ['White', 'Green', 'Red', 'Black', 'Blue', 'Yellow'], [], ['White', 'Green', 'Green', 'White', 'Green', 'Green'], ['Black', 'Red', 'Red', 'Blue', 'White', 'Black'], [], []]
costs = {0: 7, 1: 7, 2: 8, 3: 5, 4: 8, 5: 10, 6: 5, 7: 5, 8: 4, 9: 8}

transfer_pairs = []
total_cost = 0

for i in range(len(stacks)):
    if stacks[i]:
        block = stacks[i].pop(0)
        min_cost = float('inf')
        min_cost_stack = None
        
        for j in range(len(stacks)):
            if not stacks[j] or stacks[j][0] == block:
                cost = costs[j]
                if cost < min_cost:
                    min_cost = cost
                    min_cost_stack = j
        
        transfer_pairs.append((i, min_cost_stack))
        total_cost += min_cost
        stacks[min_cost_stack].insert(0, block)

print(transfer_pairs)
print("Total cost:", total_cost)
