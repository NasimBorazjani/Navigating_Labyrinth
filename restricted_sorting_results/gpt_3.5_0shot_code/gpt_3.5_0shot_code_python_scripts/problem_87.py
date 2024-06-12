
# Initial state of the stacks
stacks = [['Black', 'Blue', 'Pink', 'Green', 'Blue', 'Red', 'Red'],
          ['Yellow', 'White', 'White', 'Black', 'Yellow', 'Green', 'Green'],
          ['Yellow', 'Pink', 'White', 'Pink', 'Black', 'Red', 'Black'],
          [],
          ['Pink', 'Red', 'Blue', 'White', 'Blue', 'Blue', 'Red'],
          ['Blue', 'Yellow', 'White', 'Pink', 'Pink', 'Green', 'Green'],
          [],
          [],
          ['Yellow', 'Black', 'Yellow', 'White', 'Red', 'Black', 'Green'],
          [],
          [],
          []]

# Cost of moving a block to each stack
cost = {0: 11, 1: 13, 2: 4, 3: 4, 4: 13, 5: 7, 6: 12, 7: 6, 8: 4, 9: 6, 10: 11, 11: 4}

# Initialize variables
total_cost = 0
transfer_pairs = []

# Iterate through each block in each stack
for i, stack in enumerate(stacks):
    if stack:
        block = stack.pop(0)
        min_cost = float('inf')
        min_cost_index = None
        
        # Find the cheapest possible transfer option
        for j, c in cost.items():
            if not stacks[j] or stacks[j][0] == block:
                if c < min_cost:
                    min_cost = c
                    min_cost_index = j
        
        # Update total cost and transfer pairs
        total_cost += min_cost
        transfer_pairs.append((i, min_cost_index))
        stacks[min_cost_index].insert(0, block)

print("Total cost:", total_cost)
print("Transfer pairs:", transfer_pairs)
