
# Define the initial state of the stacks
stacks = [[], ['Yellow', 'Green', 'Red', 'Red'], ['Blue', 'Green', 'Red', 'Green'], ['Yellow', 'Blue', 'Yellow', 'Blue'], [], []]

# Define the cost of moving one block to the top of each stack
cost = {0: 3, 1: 6, 2: 5, 3: 6, 4: 1, 5: 1}

# Initialize a list to store the transfer pairs
transfer_pairs = []

# Define a function to find the index of the stack with the top block of a specific shade
def find_stack_index(shade):
    for i in range(len(stacks)):
        if len(stacks[i]) > 0 and stacks[i][0] == shade:
            return i
    return -1

# Define a function to find the index of the stack with the least cost to move a block to the top
def find_min_cost_stack():
    min_cost = float('inf')
    min_cost_stack = -1
    for i in range(len(stacks)):
        if len(stacks[i]) < 4:
            if cost[i] < min_cost:
                min_cost = cost[i]
                min_cost_stack = i
    return min_cost_stack

# Sort the blocks by shade
for shade in ['Yellow', 'Green', 'Red', 'Blue']:
    while find_stack_index(shade) != -1:
        stack_index = find_stack_index(shade)
        min_cost_stack = find_min_cost_stack()
        transfer_pairs.append((stack_index, min_cost_stack))
        stacks[min_cost_stack].insert(0, stacks[stack_index].pop(0))

# Print the list of transfer pairs with the least possible cost
print(transfer_pairs)
