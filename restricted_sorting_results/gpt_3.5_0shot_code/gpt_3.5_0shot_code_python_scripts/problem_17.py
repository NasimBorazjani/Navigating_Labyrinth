
stacks = [['Blue', 'Red', 'Green', 'Yellow'], [], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Blue', 'Blue', 'Green', 'Red'], []]
costs = {0: 2, 1: 3, 2: 3, 3: 6, 4: 1, 5: 6}
min_cost = float('inf')
best_moves = []

def is_valid_move(from_stack, to_stack):
    if not from_stack or (to_stack and from_stack[-1] != to_stack[-1]):
        return False
    if len(to_stack) == 4:
        return False
    return True

def move_block(from_stack_idx, to_stack_idx):
    global min_cost, best_moves
    cost = costs[to_stack_idx]
    if from_stack_idx != to_stack_idx:
        cost += 1
    if cost >= min_cost:
        return
    if len(stacks[5]) == 12:
        min_cost = cost
        best_moves = list(moves)
        return
    for i in range(6):
        if is_valid_move(stacks[i], stacks[to_stack_idx]):
            block = stacks[i].pop()
            stacks[to_stack_idx].append(block)
            moves.append((i, to_stack_idx))
            move_block(i, to_stack_idx)
            moves.pop()
            stacks[to_stack_idx].pop()
            stacks[i].append(block)

moves = []
move_block(0, 0)

print(best_moves)
