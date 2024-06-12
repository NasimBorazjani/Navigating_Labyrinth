
from collections import deque
from copy import deepcopy

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

def get_moves(stacks):
    moves = []
    for i in range(len(stacks)):
        if stacks[i]:
            for j in range(len(stacks)):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 4:
                    moves.append((i, j))
    return moves

def bfs(stacks):
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
            new_stacks = deepcopy(stacks)
            new_stacks[move[1]].append(new_stacks[move[0]].pop())
            new_cost = cost + {0: 5, 1: 3, 2: 5, 3: 6, 4: 5, 5: 7}[move[1]]
            queue.append((new_stacks, path + [move], new_cost))
    return []

stacks = [[], [], [], ['Yellow', 'Green', 'Blue', 'Blue'], ['Red', 'Blue', 'Green', 'Green'], ['Red', 'Red', 'Yellow', 'Yellow']]
print(bfs(stacks))
