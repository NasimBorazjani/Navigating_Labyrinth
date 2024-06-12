
# Initial state of the stacks
stacks = [['Red', 'Yellow', 'Red', 'Yellow', 'Black'],
          ['Black', 'Blue', 'Green', 'Green', 'Blue'],
          [],
          [],
          [],
          [],
          ['Black', 'Blue', 'Green', 'Black', 'Yellow'],
          ['Blue', 'Green', 'Yellow', 'Red', 'Red']]

# Cost of moving a block to each stack
cost = {0: 2, 1: 3, 2: 5, 3: 9, 4: 8, 5: 5, 6: 8, 7: 1}

# Initialize variables
transfer_pairs = []
total_cost = 0

# Helper function to find the cheapest transfer option for a block
def find_cheapest_transfer(block, current_stacks):
    min_cost = float('inf')
    from_stack = -1
    to_stack = -1
    
    for i, stack in enumerate(current_stacks):
        if stack and stack[-1] == block:
            continue
        
        for j, target_stack in enumerate(current_stacks):
            if len(target_stack) < 5 or (len(target_stack) == 5 and target_stack[-1] == block):
                if cost[j] < min_cost:
                    min_cost = cost[j]
                    from_stack = i
                    to_stack = j
    
    return min_cost, from_stack, to_stack

# Iterate through each block in each stack
for stack in stacks:
    for block in stack:
        cheapest_cost, from_stack, to_stack = find_cheapest_transfer(block, stacks)
        
        if cheapest_cost < float('inf'):
            transfer_pairs.append((from_stack, to_stack))
            total_cost += cheapest_cost
            stacks[to_stack].append(stacks[from_stack].pop())
            
# Print the list of transfer pairs with the least possible cost
print(transfer_pairs)
print("Total cost:", total_cost)
