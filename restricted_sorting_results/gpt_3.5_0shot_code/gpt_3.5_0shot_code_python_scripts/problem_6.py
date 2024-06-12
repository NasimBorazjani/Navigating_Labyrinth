
# Initial state of the stacks
stacks = [['Yellow', 'Blue', 'Blue', 'Green'], [], ['Yellow', 'Green', 'Red', 'Red'], ['Green', 'Red', 'Yellow', 'Blue'], [], []]

# Cost of moving one block to the top of each stack
cost = {0: 7, 1: 3, 2: 5, 3: 5, 4: 1, 5: 3}

transfer_pairs = []

# Helper function to calculate the cost of moving a block to a specific stack
def calculate_cost(block, dest_stack):
    if not stacks[dest_stack] or stacks[dest_stack][-1] == block:
        return 1
    else:
        return cost[dest_stack]

# Iterate through each block in each stack
for i, stack in enumerate(stacks):
    if stack:
        block = stack[-1]
        min_cost = float('inf')
        min_dest = None
        
        # Calculate the cost of moving the block to each possible destination stack
        for dest in range(len(stacks)):
            if dest == i or (stacks[dest] and stacks[dest][-1] != block):
                continue
            c = calculate_cost(block, dest)
            if c < min_cost:
                min_cost = c
                min_dest = dest
        
        # Update the transfer pairs and the stacks
        transfer_pairs.append((i, min_dest))
        stacks[min_dest].append(stacks[i].pop())

print(transfer_pairs)
