
stacks = [['Green', 'Yellow', 'Red', 'Red'], [], ['Yellow', 'Green', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Green', 'Blue']]
costs = {0: 3, 1: 7, 2: 7, 3: 7, 4: 2, 5: 4}
min_cost = float('inf')
min_moves = []

def is_valid_move(from_stack, to_stack):
    if not from_stack or (to_stack and from_stack[-1] != to_stack[-1]):
        return False
    if len(to_stack) == 4:
        return False
    return True

def transfer_blocks(curr_stacks, moves, total_cost):
    global min_cost, min_moves

    if total_cost >= min_cost:
        return

    if all(len(stack) == 0 or len(set(stack)) == 1 for stack in curr_stacks):
        min_cost = total_cost
        min_moves = moves
        return

    for i in range(6):
        for j in range(6):
            if i != j and is_valid_move(curr_stacks[i], curr_stacks[j]):
                new_stacks = [stack.copy() for stack in curr_stacks]
                new_stacks[j].append(new_stacks[i].pop())
                new_cost = total_cost + costs[j]
                transfer_blocks(new_stacks, moves + [(i, j)], new_cost)

transfer_blocks(stacks, [], 0)

print(min_moves)
