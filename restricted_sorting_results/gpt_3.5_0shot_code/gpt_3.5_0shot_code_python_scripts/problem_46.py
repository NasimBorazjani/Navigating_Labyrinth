
stacks = [[], [], [], ['Yellow', 'Black', 'Yellow', 'Black', 'Green'], ['Red', 'Yellow', 'Blue', 'Black', 'Black'], [], ['Red', 'Blue', 'Green', 'Red', 'Blue'], ['Green', 'Blue', 'Red', 'Yellow', 'Green']]
costs = {0: 2, 1: 1, 2: 6, 3: 3, 4: 1, 5: 5, 6: 4, 7: 2}

transfer_pairs = []

def get_top_block_color(stack):
    if stack:
        return stack[-1]
    return None

def get_cost(source, target):
    if not stacks[target] or get_top_block_color(stacks[target]) == get_top_block_color(stacks[source]):
        return 1
    return costs[target]

def find_cheapest_move():
    min_cost = float('inf')
    move = None
    for i in range(len(stacks)):
        for j in range(len(stacks)):
            if i != j and stacks[i]:
                cost = get_cost(i, j)
                if cost < min_cost:
                    min_cost = cost
                    move = (i, j)
    return move

while any(stacks):
    move = find_cheapest_move()
    if move:
        block = stacks[move[0]].pop()
        stacks[move[1]].append(block)
        transfer_pairs.append(move)

print(transfer_pairs)
