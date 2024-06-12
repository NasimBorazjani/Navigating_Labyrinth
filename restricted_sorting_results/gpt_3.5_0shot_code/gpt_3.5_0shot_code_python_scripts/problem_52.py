
# Initial state of the stacks
stacks = [[], [], [], ['Blue', 'Yellow', 'Red', 'Blue', 'Black'], ['Red', 'Yellow', 'Blue', 'Yellow', 'Blue'], ['Green', 'Red', 'Black', 'Red', 'Yellow'], [], ['Green', 'Green', 'Black', 'Green', 'Black']]

# Cost of moving one block to the top of each stack
cost = {0: 6, 1: 4, 2: 3, 3: 8, 4: 7, 5: 5, 6: 9, 7: 9}

# Helper function to calculate the cost of transferring a block from one stack to another
def transfer_cost(from_stack, to_stack):
    if len(stacks[to_stack]) == 0:
        return cost[to_stack]
    elif stacks[from_stack][-1] == stacks[to_stack][-1]:
        return 1
    else:
        return cost[to_stack]

# Helper function to find the stack with the minimum cost to transfer a block to
def find_min_cost_stack(from_stack):
    min_cost = float('inf')
    min_cost_stack = None
    for i in range(len(stacks)):
        if i != from_stack and (len(stacks[i]) == 0 or stacks[from_stack][-1] == stacks[i][-1]):
            current_cost = transfer_cost(from_stack, i)
            if current_cost < min_cost:
                min_cost = current_cost
                min_cost_stack = i
    return min_cost_stack

# Main algorithm to sort the blocks
transfers = []
while any(stacks):
    min_cost = float('inf')
    min_cost_transfer = None
    for i in range(len(stacks)):
        if len(stacks[i]) > 0:
            to_stack = find_min_cost_stack(i)
            current_cost = transfer_cost(i, to_stack)
            if current_cost < min_cost:
                min_cost = current_cost
                min_cost_transfer = (i, to_stack)
    transfers.append(min_cost_transfer)
    stacks[min_cost_transfer[1]].append(stacks[min_cost_transfer[0]].pop())

# Print the list of transfer pairs with the least possible cost
print(transfers)
