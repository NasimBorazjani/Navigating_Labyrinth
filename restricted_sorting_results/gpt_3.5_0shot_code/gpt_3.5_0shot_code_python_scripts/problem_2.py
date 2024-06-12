
def get_cost(stack, target):
    return abs(stack - target)

def find_cheapest_move(stacks, costs):
    min_cost = float('inf')
    move = None
    for i in range(len(stacks)):
        for j in range(len(stacks)):
            if i != j and (not stacks[i] or stacks[i][-1] == stacks[j][-1]):
                cost = get_cost(i, j)
                if cost < min_cost:
                    min_cost = cost
                    move = (i, j)
    return move

def restricted_sorting(stacks, costs):
    transfers = []
    while any(stacks):
        move = find_cheapest_move(stacks, costs)
        transfers.append(move)
        stacks[move[1]].append(stacks[move[0]].pop())
    return transfers

# Initial state of the stacks
stacks = [['Red', 'Green', 'Red', 'Blue'], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Blue', 'Yellow', 'Green', 'Blue'], [], []]

# Cost of moving a block to each stack
costs = {0: 5, 1: 3, 2: 3, 3: 1, 4: 3, 5: 2}

# Solve the problem
transfers = restricted_sorting(stacks, costs)

# Print the list of transfer pairs
print(transfers)
