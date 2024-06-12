
# Initial state of the stacks
stacks = [['Blue', 'Yellow', 'Yellow', 'Green', 'Black'], [], [], [], ['Blue', 'Red', 'Black', 'Yellow', 'Green'], ['Black', 'Red', 'Green', 'Blue', 'Red'], ['Green', 'Yellow', 'Black', 'Red', 'Blue'], []]

# Cost of moving one block to the top of each stack
cost = {0: 4, 1: 4, 2: 7, 3: 1, 4: 8, 5: 8, 6: 8, 7: 4}

# Helper function to calculate the cost of moving a block from one stack to another
def move_cost(from_stack, to_stack):
    if not stacks[to_stack] or stacks[to_stack][-1] == stacks[from_stack][-1]:
        return 1
    else:
        return cost[to_stack]

# List to store the transfer pairs
transfers = []

# Iterate through each block in each stack
for i, stack in enumerate(stacks):
    if stack:
        min_cost = float('inf')
        min_cost_stack = None
        for j in range(len(stacks)):
            if i != j and (not stacks[j] or stacks[j][-1] == stack[-1]):
                current_cost = move_cost(i, j)
                if current_cost < min_cost:
                    min_cost = current_cost
                    min_cost_stack = j
        transfers.append((i, min_cost_stack))
        stacks[min_cost_stack].append(stacks[i].pop())

print(transfers)
