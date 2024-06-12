
stacks = [[], [], ['Blue', 'Blue', 'Green', 'Black', 'Red'], [], ['Red', 'Green', 'Red', 'Black', 'Yellow'], [], ['Blue', 'Yellow', 'Green', 'Yellow', 'Black'], ['Yellow', 'Green', 'Black', 'Red', 'Blue']]
costs = [6, 2, 7, 1, 1, 5, 3, 2]

def get_stack_index(color):
    for i, stack in enumerate(stacks):
        if stack and stack[-1] == color:
            return i
    return -1

def get_min_cost_index(color):
    min_cost = float('inf')
    min_index = -1
    for i, stack in enumerate(stacks):
        if len(stack) < 4 and (not stack or stack[-1] == color):
            cost = costs[i]
            if cost < min_cost:
                min_cost = cost
                min_index = i
    return min_index if min_index >= 0 else -1

def sort_blocks():
    moves = []
    for color in ['Blue', 'Green', 'Black', 'Red', 'Yellow']:
        src = get_stack_index(color)
        while src >= 0:
            dest = get_min_cost_index(color)
            if dest < 0:
                break
            moves.append((src, dest))
            stacks[src].pop()
            stacks[dest].append(color)
            src = get_stack_index(color)
    return moves

print(sort_blocks())
