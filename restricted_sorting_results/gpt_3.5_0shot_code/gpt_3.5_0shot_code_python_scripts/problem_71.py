
stacks = [[], [], ['White', 'Yellow', 'Yellow', 'Green', 'Blue', 'Green'], ['Red', 'Yellow', 'White', 'Blue', 'Black', 'Black'], ['Black', 'Red', 'Blue', 'Black', 'Green', 'Green'], ['Green', 'Black', 'Yellow', 'Red', 'White', 'Red'], ['White', 'Blue', 'Red', 'Blue', 'White', 'Yellow'], [], [], []]
costs = {0: 4, 1: 1, 2: 1, 3: 9, 4: 2, 5: 9, 6: 1, 7: 9, 8: 6, 9: 4}

transfer_pairs = []
total_cost = 0

for i in range(len(stacks)):
    if stacks[i]:
        block = stacks[i][-1]
        min_cost = float('inf')
        min_cost_stack = None
        
        for j in range(len(stacks)):
            if not stacks[j] or stacks[j][-1] == block:
                if costs[j] < min_cost:
                    min_cost = costs[j]
                    min_cost_stack = j
        
        if min_cost_stack is not None:
            transfer_pairs.append((i, min_cost_stack))
            stacks[min_cost_stack].append(stacks[i].pop())
            total_cost += min_cost

print(transfer_pairs)
print("Total cost:", total_cost)
