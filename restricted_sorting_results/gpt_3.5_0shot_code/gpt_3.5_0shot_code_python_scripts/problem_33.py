
# Initial state of the stacks
stacks = [['Black', 'Yellow', 'Green', 'Red', 'Black'], [], ['Red', 'Yellow', 'Green', 'Blue', 'Green'], [], ['Blue', 'Red', 'Blue', 'Green', 'Yellow'], ['Red', 'Blue', 'Yellow', 'Black', 'Black'], [], []]

# Cost of moving one block to the top of each stack
cost = {0: 1, 1: 6, 2: 6, 3: 2, 4: 9, 5: 2, 6: 9, 7: 6}

# Helper function to calculate the cost of moving a block from one stack to another
def move_cost(from_stack, to_stack):
    if not stacks[to_stack] or stacks[to_stack][-1] == stacks[from_stack][-1]:
        return 1
    else:
        return cost[to_stack]

# Initialize list to store transfer pairs
transfer_pairs = []

# Iterate through each block in each stack
for i in range(len(stacks)):
    while stacks[i]:
        min_cost = float('inf')
        min_cost_stack = None
        for j in range(len(stacks)):
            if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]):
                current_cost = move_cost(i, j)
                if current_cost < min_cost:
                    min_cost = current_cost
                    min_cost_stack = j
        transfer_pairs.append((i, min_cost_stack))
        stacks[min_cost_stack].append(stacks[i].pop())

# Print the list of transfer pairs with the least possible cost
print(transfer_pairs)
