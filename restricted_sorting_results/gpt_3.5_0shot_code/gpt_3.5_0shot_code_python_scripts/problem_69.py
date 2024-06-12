
stacks = [[], ['Blue', 'Black', 'Black', 'Yellow', 'White', 'Green'], ['Green', 'Black', 'Red', 'Green', 'Yellow', 'Blue'], [], ['Green', 'Red', 'Blue', 'Yellow', 'Green', 'Blue'], ['Black', 'White', 'White', 'Red', 'White', 'Black'], [], ['White', 'Red', 'Blue', 'Yellow', 'Yellow', 'Red'], [], []]
costs = {0: 5, 1: 4, 2: 7, 3: 7, 4: 11, 5: 11, 6: 8, 7: 3, 8: 7, 9: 9}

transfer_pairs = []
total_cost = 0

for i, stack in enumerate(stacks):
    if stack:
        block = stack.pop(0)
        min_cost = float('inf')
        min_cost_stack = None
        
        for j, target_stack in enumerate(stacks):
            if not target_stack or target_stack[0] == block:
                if costs[j] < min_cost:
                    min_cost = costs[j]
                    min_cost_stack = j
        
        transfer_pairs.append((i, min_cost_stack))
        total_cost += min_cost
        stacks[min_cost_stack].insert(0, block)

print(transfer_pairs)
print("Total cost:", total_cost)
