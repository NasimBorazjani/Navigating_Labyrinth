
stacks = [[], [], ['Blue', 'Green', 'Yellow', 'Green'], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Red', 'Blue', 'Red', 'Blue']]
costs = {0: 7, 1: 6, 2: 2, 3: 7, 4: 7, 5: 4}
min_cost = float('inf')
min_moves = []

def is_valid_move(src, dest):
    if not src or (dest and src[-1] != dest[-1]):
        return False
    if len(dest) == 4:
        return False
    return True

def move_blocks(curr_stacks, moves, total_cost):
    global min_cost, min_moves

    if total_cost >= min_cost:
        return

    if all(not stack for stack in curr_stacks):
        min_cost = total_cost
        min_moves = moves
        return

    for src_idx, src_stack in enumerate(curr_stacks):
        if not src_stack:
            continue
        for dest_idx, dest_stack in enumerate(curr_stacks):
            if is_valid_move(src_stack, dest_stack):
                new_stacks = [stack.copy() for stack in curr_stacks]
                new_stacks[src_idx].pop()
                new_stacks[dest_idx].append(src_stack[-1])
                move_blocks(new_stacks, moves + [(src_idx, dest_idx)], total_cost + costs[dest_idx])

move_blocks(stacks, [], 0)
print(min_moves)
