
stacks = [[], [], [], ['Blue', 'Yellow', 'Blue', 'Blue'], ['Red', 'Green', 'Yellow', 'Green'], ['Red', 'Red', 'Yellow', 'Green']]
costs = {0: 5, 1: 5, 2: 3, 3: 1, 4: 5, 5: 1}
min_cost = float('inf')
min_moves = []

def is_sorted():
    for stack in stacks:
        if len(stack) > 0 and len(set(stack)) != 1:
            return False
    return True

def move_block(from_stack, to_stack):
    global min_cost, min_moves
    cost = costs[to_stack]
    if len(stacks[from_stack]) == 0:
        return
    block = stacks[from_stack].pop()
    stacks[to_stack].append(block)
    if is_sorted():
        total_cost = sum([costs[from_stack] for from_stack in min_moves])
        if total_cost < min_cost:
            min_cost = total_cost
            min_moves = min_moves.copy()
    else:
        for i in range(6):
            if i != from_stack and (len(stacks[i]) == 0 or stacks[i][-1] == block):
                min_moves.append((from_stack, i))
                move_block(i, from_stack)
                min_moves.pop()

for i in range(6):
    move_block(i, i)

print(min_moves)
