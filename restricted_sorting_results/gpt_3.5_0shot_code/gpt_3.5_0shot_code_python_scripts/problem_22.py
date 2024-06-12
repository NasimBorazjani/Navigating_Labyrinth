
stacks = [[], ['Blue', 'Yellow', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Green', 'Green', 'Red', 'Red']]
costs = {0: 1, 1: 4, 2: 2, 3: 7, 4: 6, 5: 6}
min_cost = float('inf')
best_moves = []

def is_valid_move(from_stack, to_stack, block):
    if not stacks[from_stack]:
        return False
    if not stacks[to_stack]:
        return True
    if stacks[to_stack][-1] == block:
        return True
    return False

def move_block(from_stack, to_stack):
    block = stacks[from_stack].pop()
    stacks[to_stack].append(block)
    return costs[to_stack]

def undo_move(from_stack, to_stack):
    block = stacks[to_stack].pop()
    stacks[from_stack].append(block)

def solve(current_cost, moves):
    global min_cost, best_moves

    if current_cost >= min_cost:
        return

    if all(len(stack) == 0 or len(set(stack)) == 1 for stack in stacks):
        min_cost = current_cost
        best_moves = moves.copy()
        return

    for from_stack in range(6):
        for to_stack in range(6):
            if from_stack != to_stack and is_valid_move(from_stack, to_stack, stacks[from_stack][-1]):
                cost = move_block(from_stack, to_stack)
                moves.append((from_stack, to_stack))
                solve(current_cost + cost, moves)
                undo_move(from_stack, to_stack)
                moves.pop()

solve(0, [])
print(best_moves)
