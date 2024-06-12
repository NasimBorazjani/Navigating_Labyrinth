
stacks = [[], [], [], ['Yellow', 'Green', 'Blue', 'Blue'], ['Red', 'Blue', 'Green', 'Green'], ['Red', 'Red', 'Yellow', 'Yellow']]
costs = {0: 5, 1: 3, 2: 5, 3: 6, 4: 5, 5: 7}

def get_block_shade(block):
    if block == 'Red':
        return 0
    elif block == 'Green':
        return 1
    elif block == 'Blue':
        return 2
    elif block == 'Yellow':
        return 3

def get_cost(move):
    return costs[move[0]] + 1

def find_cheapest_move():
    min_cost = float('inf')
    cheapest_move = None
    for i in range(len(stacks)):
        if stacks[i]:
            for j in range(len(stacks)):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]):
                    move_cost = get_cost((i, j))
                    if move_cost < min_cost:
                        min_cost = move_cost
                        cheapest_move = (i, j)
    return cheapest_move

transfers = []
while any(stacks):
    move = find_cheapest_move()
    transfers.append(move)
    block = stacks[move[0]].pop()
    stacks[move[1]].append(block)

print(transfers)
