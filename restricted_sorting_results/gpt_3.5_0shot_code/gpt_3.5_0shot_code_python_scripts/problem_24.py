
stacks = [[], [], ['Green', 'Yellow', 'Green', 'Red'], ['Green', 'Red', 'Blue', 'Yellow'], [], ['Blue', 'Red', 'Yellow', 'Blue']]
costs = {0: 5, 1: 1, 2: 6, 3: 7, 4: 7, 5: 7}
min_cost = float('inf')
min_path = []

def is_valid_move(src, dest):
    if not src or (dest and src[-1] != dest[-1]):
        return False
    if len(dest) == 4:
        return False
    return True

def move_block(src, dest):
    dest.append(src.pop())

def backtrack(path, cost):
    global min_cost, min_path
    if all(not stack for stack in stacks):
        if cost < min_cost:
            min_cost = cost
            min_path = path.copy()
        return

    for i in range(6):
        for j in range(6):
            if i != j and is_valid_move(stacks[i], stacks[j]):
                move_block(stacks[i], stacks[j])
                path.append((i, j))
                backtrack(path, cost + costs[j])
                move_block(stacks[j], stacks[i])
                path.pop()

backtrack([], 0)
print(min_path)
