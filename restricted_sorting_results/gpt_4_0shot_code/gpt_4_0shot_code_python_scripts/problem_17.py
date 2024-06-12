
from collections import deque
from copy import deepcopy

def is_goal_state(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

def get_possible_moves(stacks):
    moves = []
    for i in range(6):
        if stacks[i]:
            for j in range(6):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 4:
                    moves.append((i, j))
    return moves

def bfs(stacks):
    queue = deque([(stacks, [], 0)])
    visited = set()
    while queue:
        current_stacks, path, cost = queue.popleft()
        if str(current_stacks) in visited:
            continue
        visited.add(str(current_stacks))
        if is_goal_state(current_stacks):
            return path
        for move in get_possible_moves(current_stacks):
            new_stacks = deepcopy(current_stacks)
            block = new_stacks[move[0]].pop()
            new_stacks[move[1]].append(block)
            new_cost = cost + {0: 2, 1: 3, 2: 3, 3: 6, 4: 1, 5: 6}[move[1]]
            queue.append((new_stacks, path + [move], new_cost))
    return []

stacks = [['Blue', 'Red', 'Green', 'Yellow'], [], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Blue', 'Blue', 'Green', 'Red'], []]
print(bfs(stacks))
