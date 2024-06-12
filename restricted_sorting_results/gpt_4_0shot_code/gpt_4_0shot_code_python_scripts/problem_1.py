
from collections import deque
from copy import deepcopy

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

def get_moves(stacks):
    moves = []
    for i in range(6):
        if stacks[i]:
            for j in range(6):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 4:
                    moves.append((i, j))
    return moves

def bfs(stacks):
    queue = deque([(stacks, [])])
    visited = set([str(stacks)])
    while queue:
        current, path = queue.popleft()
        if is_sorted(current):
            return path
        for move in get_moves(current):
            next_state = deepcopy(current)
            next_state[move[1]].append(next_state[move[0]].pop())
            if str(next_state) not in visited:
                visited.add(str(next_state))
                queue.append((next_state, path + [move]))
    return []

stacks = [[], [], [], ['Blue', 'Yellow', 'Blue', 'Blue'], ['Red', 'Green', 'Yellow', 'Green'], ['Red', 'Red', 'Yellow', 'Green']]
print(bfs(stacks))
