
# Initial state of the stacks
stacks = [['Red', 'Green', 'Blue', 'Yellow', 'Yellow', 'Blue'], [], [], [], ['White', 'Black', 'White', 'Red', 'White', 'Blue'], ['Black', 'Green', 'Red', 'Black', 'Green', 'Yellow'], [], ['Red', 'White', 'Yellow', 'Black', 'Green', 'White'], [], ['Blue', 'Blue', 'Black', 'Green', 'Red', 'Yellow']]

# Cost of moving a block to each stack
cost = {0: 11, 1: 5, 2: 9, 3: 5, 4: 2, 5: 2, 6: 6, 7: 6, 8: 6, 9: 2}

# Initialize variables
transfer_pairs = []
total_cost = 0

# Helper function to find the cheapest transfer option for a block
def find_cheapest_transfer(block, stacks):
    min_cost = float('inf')
    from_stack = -1
    to_stack = -1
    
    for i, stack in enumerate(stacks):
        if stack and stack[-1] == block:
            continue
        
        for j, target_stack in enumerate(stacks):
            if i == j or (target_stack and target_stack[-1] != block):
                continue
            
            current_cost = cost[j]
            if current_cost < min_cost:
                min_cost = current_cost
                from_stack = i
                to_stack = j
    
    return min_cost, from_stack, to_stack

# Greedy algorithm to find the cheapest transfer pairs
for stack in stacks:
    for block in stack:
        block_cost, from_stack, to_stack = find_cheapest_transfer(block, stacks)
        transfer_pairs.append((from_stack, to_stack))
        total_cost += block_cost
        stacks[from_stack].pop()
        stacks[to_stack].append(block)

print("List of transfer pairs with the least possible cost:")
print(transfer_pairs)
print("Total cost:", total_cost)
