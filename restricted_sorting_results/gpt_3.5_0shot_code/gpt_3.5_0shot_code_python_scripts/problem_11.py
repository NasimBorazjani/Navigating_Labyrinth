
stacks = [[], ['Blue', 'Blue', 'Green', 'Red'], [], ['Green', 'Red', 'Yellow', 'Yellow'], [], ['Green', 'Red', 'Blue', 'Yellow']]
costs = {0: 3, 1: 5, 2: 1, 3: 6, 4: 7, 5: 4}
min_cost = float('inf')
best_moves = []

def is_valid_move(src, dest):
    if not src or (dest and src[-1] != dest[-1]):
        return False
    if len(dest) == 4:
        return False
    return True

def move_block(src_idx, dest_idx):
    global min_cost, best_moves
    cost = costs[dest_idx]
    src = stacks[src_idx]
    dest = stacks[dest_idx]
    
    block = src.pop()
    dest.append(block)
    
    if len(src) == 0:
        del stacks[src_idx]
    
    if len(src) == 0 and all(len(stack) == 4 for stack in stacks if stack):
        if cost < min_cost:
            min_cost = cost
            best_moves = [(src_idx, dest_idx)]
        elif cost == min_cost:
            best_moves.append((src_idx, dest_idx))
    
    for i in range(6):
        if i != src_idx and is_valid_move(stacks[i], stacks[src_idx]):
            move_block(i, src_idx)
    
    src.append(dest.pop())
    src.append(block)
    if len(dest) == 0:
        del stacks[dest_idx]

for i in range(6):
    for j in range(6):
        if i != j and is_valid_move(stacks[i], stacks[j]):
            move_block(i, j)

print(best_moves)
