
stacks = [[], [], [], ['Red', 'Green', 'Green', 'Red'], ['Yellow', 'Blue', 'Yellow', 'Blue'], ['Yellow', 'Green', 'Red', 'Blue']]
costs = {0: 4, 1: 5, 2: 5, 3: 2, 4: 5, 5: 2}

def is_sorted():
    for stack in stacks:
        if len(stack) > 0 and len(set(stack)) != 1:
            return False
    return True

def move_block(from_stack, to_stack):
    block = stacks[from_stack].pop()
    stacks[to_stack].append(block)
    return (from_stack, to_stack)

def backtrack(cost):
    if is_sorted():
        return []
    
    min_cost = float('inf')
    best_moves = []
    
    for from_stack in range(6):
        for to_stack in range(6):
            if from_stack == to_stack or (len(stacks[to_stack]) > 0 and stacks[to_stack][-1] != stacks[from_stack][-1]):
                continue
            
            move_cost = costs[to_stack]
            if from_stack != to_stack:
                move_cost += 1
            
            if len(stacks[from_stack]) == 0:
                continue
            
            move_block(from_stack, to_stack)
            next_moves = backtrack(cost + move_cost)
            if cost + move_cost + len(next_moves) < min_cost:
                min_cost = cost + move_cost + len(next_moves)
                best_moves = [move_block(from_stack, to_stack)] + next_moves
            
            move_block(to_stack, from_stack)
    
    return best_moves

solution = backtrack(0)
print(solution)
