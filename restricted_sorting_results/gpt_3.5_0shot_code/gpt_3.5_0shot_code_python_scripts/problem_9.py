
def restricted_sorting(stacks, cost, moves, min_cost, min_moves):
    if all(len(stack) == 0 or len(set(stack)) == 1 for stack in stacks):
        if cost < min_cost:
            min_cost = cost
            min_moves = moves.copy()
        return min_cost, min_moves
    
    for i in range(len(stacks)):
        for j in range(len(stacks)):
            if i != j and (len(stacks[i]) == 0 or stacks[i][-1] == stacks[j][-1] or len(stacks[j]) == 0):
                if len(stacks[i]) > 0:
                    new_stacks = [stack.copy() for stack in stacks]
                    new_stacks[j].append(new_stacks[i].pop())
                    new_cost = cost + 1
                    new_moves = moves + [(i, j)]
                    min_cost, min_moves = restricted_sorting(new_stacks, new_cost, new_moves, min_cost, min_moves)
    return min_cost, min_moves

initial_state = [['Yellow', 'Yellow', 'Red', 'Red'], [], ['Blue', 'Yellow', 'Red', 'Green'], [], ['Green', 'Blue', 'Green', 'Blue'], []]
costs = {0: 7, 1: 1, 2: 4, 3: 7, 4: 4, 5: 4}

min_cost, min_moves = restricted_sorting(initial_state, 0, [], float('inf'), [])

print(min_moves)
