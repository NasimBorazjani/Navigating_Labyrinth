
# Initial state of the stacks
stacks = [['Blue', 'Yellow', 'Red', 'Yellow'], ['Green', 'Red', 'Green', 'Red'], ['Blue', 'Green', 'Blue', 'Yellow'], [], [], []]

# Cost of moving one block to the top of each stack
cost = {0: 4, 1: 4, 2: 7, 3: 7, 4: 5, 5: 6}

# Initialize variables
transfer_pairs = []
total_cost = 0

# Helper function to get the shade of the top block in a stack
def get_top_block(stack):
    if stack:
        return stack[-1]
    else:
        return None

# Iterate through each block in the stacks
for i in range(len(stacks)):
    while stacks[i]:
        block = stacks[i].pop()
        min_cost = float('inf')
        target_stack = None
        
        # Find the optimal stack to transfer the block
        for j in range(len(stacks)):
            if not stacks[j] or get_top_block(stacks[j]) == block:
                if cost[j] < min_cost:
                    min_cost = cost[j]
                    target_stack = j
        
        # Transfer the block to the target stack
        stacks[target_stack].append(block)
        transfer_pairs.append((i, target_stack))
        total_cost += min_cost

# Print the list of transfer pairs and the total cost
print("List of transfer pairs:", transfer_pairs)
print("Total cost:", total_cost)
