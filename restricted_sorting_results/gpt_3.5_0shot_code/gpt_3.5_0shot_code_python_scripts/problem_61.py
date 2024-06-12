
stacks = [[], [], ['Green', 'Red', 'White', 'Green', 'Black', 'White'], [], ['Red', 'Red', 'Yellow', 'White', 'Blue', 'Black'], ['Blue', 'Yellow', 'Red', 'Blue', 'Blue', 'Green'], [], [], ['Black', 'White', 'Black', 'White', 'Yellow', 'Blue'], ['Yellow', 'Black', 'Green', 'Red', 'Green', 'Yellow']]
costs = {0: 7, 1: 11, 2: 8, 3: 10, 4: 5, 5: 6, 6: 10, 7: 10, 8: 4, 9: 11}

transfer_pairs = []
total_cost = 0

for i, stack in enumerate(stacks):
    if stack:
        block = stack.pop()
        min_cost = float('inf')
        min_stack = None
        
        for j, target_stack in enumerate(stacks):
            if not target_stack or target_stack[-1] == block:
                if costs[j] < min_cost:
                    min_cost = costs[j]
                    min_stack = j
        
        transfer_pairs.append((i, min_stack))
        total_cost += min_cost
        stacks[min_stack].append(block)

print(transfer_pairs)
print("Total cost:", total_cost)
