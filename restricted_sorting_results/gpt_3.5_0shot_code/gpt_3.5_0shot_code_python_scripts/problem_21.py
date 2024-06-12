
stacks = [['Red', 'Yellow', 'Blue', 'Yellow'], [], [], ['Green', 'Blue', 'Green', 'Red'], [], ['Yellow', 'Red', 'Green', 'Blue']]
costs = {0: 4, 1: 5, 2: 3, 3: 3, 4: 3, 5: 5}

def is_sorted():
    for stack in stacks:
        if len(stack) > 0 and len(set(stack)) != 1:
            return False
    return True

def move_block(from_stack, to_stack):
    block = stacks[from_stack].pop()
    stacks[to_stack].append(block)
    return (from_stack, to_stack)

def move_blocks():
    if is_sorted():
        return []
    
    min_cost = float('inf')
    best_moves = []
    
    for from_stack in range(6):
        if len(stacks[from_stack]) == 0:
            continue
        for to_stack in range(6):
            if from_stack == to_stack or (len(stacks[to_stack]) > 0 and stacks[to_stack][-1] != stacks[from_stack][-1]):
                continue
            move_cost = costs[to_stack]
            if len(stacks[to_stack]) == 0:
                move_cost += 1
            move_block(from_stack, to_stack)
            next_moves = move_blocks()
            total_cost = move_cost + sum(cost for cost, _ in next_moves)
            if total_cost < min_cost:
                min_cost = total_cost
                best_moves = [(from_stack, to_stack)] + next_moves
            move_block(to_stack, from_stack)
    
    return best_moves

solution = move_blocks()
print(solution)
