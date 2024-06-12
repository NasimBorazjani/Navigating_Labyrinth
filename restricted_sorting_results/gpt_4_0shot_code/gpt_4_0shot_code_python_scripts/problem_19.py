
from collections import deque

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

def get_moves(stacks):
    moves = []
    for i, stack in enumerate(stacks):
        if stack:
            for j, target in enumerate(stacks):
                if i != j and (not target or target[-1] == stack[-1]):
                    moves.append((i, j))
    return moves

def solve(stacks):
    queue = deque([(stacks, [], 0)])
    visited = set()
    while queue:
        stacks, path, cost = queue.popleft()
        if str(stacks) in visited:
            continue
        visited.add(str(stacks))
        if is_sorted(stacks):
            return path
        for move in get_moves(stacks):
            new_stacks = [list(stack) for stack in stacks]
            block = new_stacks[move[0]].pop()
            new_stacks[move[1]].append(block)
            new_cost = cost + {0: 2, 1: 4, 2: 6, 3: 6, 4: 6, 5: 7}[move[1]]
            queue.append((new_stacks, path + [move], new_cost))
    return []

stacks = [[], [], ['Green', 'Blue', 'Green', 'Yellow'], [], ['Red', 'Red', 'Yellow', 'Blue'], ['Green', 'Red', 'Blue', 'Yellow']]
print(solve(stacks))
