
stacks = [[], [], ['Green', 'Blue', 'Green', 'Yellow'], [], ['Red', 'Red', 'Yellow', 'Blue'], ['Green', 'Red', 'Blue', 'Yellow']]
costs = {0: 2, 1: 4, 2: 6, 3: 6, 4: 6, 5: 7}
min_cost = float('inf')
best_moves = []

def is_valid_move(from_stack, to_stack):
    if not stacks[from_stack]:
        return False
    if not stacks[to_stack]:
        return True
    if stacks[from_stack][-1] == stacks[to_stack][-1]:
        return True
    return False

def move_block(from_stack, to_stack):
    block = stacks[from_stack].pop()
    stacks[to_stack].append(block)

def calculate_cost(moves):
    total_cost = 0
    for move in moves:
        total_cost += costs[move[0]]
    return total_cost

def solve(current_moves):
    global min_cost, best_moves

    if all(len(stack) == 0 or len(set(stack)) == 1 for stack in stacks):
        current_cost = calculate_cost(current_moves)
        if current_cost < min_cost:
            min_cost = current_cost
            best_moves = current_moves.copy()
        return

    for from_stack in range(6):
        for to_stack in range(6):
            if from_stack != to_stack and is_valid_move(from_stack, to_stack):
                move_block(from_stack, to_stack)
                current_moves.append((from_stack, to_stack))
                solve(current_moves)
                move_block(to_stack, from_stack)
                current_moves.pop()

solve([])
print(best_moves)
