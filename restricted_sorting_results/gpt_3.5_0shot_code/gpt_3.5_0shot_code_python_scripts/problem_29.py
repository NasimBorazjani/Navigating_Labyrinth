
stacks = [['Yellow', 'Green', 'Green', 'Blue'], [], [], ['Red', 'Green', 'Blue', 'Yellow'], [], ['Yellow', 'Blue', 'Red', 'Red']]
costs = {0: 1, 1: 5, 2: 6, 3: 7, 4: 7, 5: 5}
min_cost = float('inf')
best_moves = []

def is_sorted():
    for stack in stacks:
        if len(stack) > 0 and len(set(stack)) != 1:
            return False
    return True

def move_block(from_stack, to_stack):
    global min_cost, best_moves
    cost = costs[to_stack]
    if len(stacks[from_stack]) == 0:
        return
    if len(stacks[to_stack]) == 0 or stacks[to_stack][-1] == stacks[from_stack][-1]:
        stacks[to_stack].append(stacks[from_stack].pop())
        if is_sorted():
            total_cost = sum([costs[m[1]] for m in best_moves])
            if total_cost < min_cost:
                min_cost = total_cost
                best_moves = list(m for m in best_moves)
        else:
            for i in range(6):
                for j in range(6):
                    move_block(i, j)
        stacks[from_stack].append(stacks[to_stack].pop())

for i in range(6):
    for j in range(6):
        move_block(i, j)

print(best_moves)
