
# Initial state of the stacks
stacks = [['Black', 'Blue', 'Red', 'White', 'Red', 'Green'],
          ['Red', 'Black', 'Red', 'Green', 'Blue', 'Black'],
          ['Black', 'Yellow', 'Yellow', 'White', 'White', 'Yellow'],
          [], [], ['White', 'Green', 'Green', 'Red', 'Green', 'Yellow'],
          [], ['Blue', 'Blue', 'Blue', 'Black', 'White', 'Yellow'], [], []]

# Cost of moving a block to each stack
cost = {0: 3, 1: 8, 2: 5, 3: 10, 4: 8, 5: 2, 6: 3, 7: 4, 8: 11, 9: 3}

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
            for j, cost_val in cost.items():
                if cost_val < min_cost and (not stacks[j] or stacks[j][-1] == block):
                    min_cost = cost_val
                    from_stack = i
                    to_stack = j
    
    return min_cost, from_stack, to_stack

# Iterate through each block in each stack
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
