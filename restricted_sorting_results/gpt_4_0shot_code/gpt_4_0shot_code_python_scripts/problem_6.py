
from collections import deque

def bfs(stacks, costs):
    queue = deque([(stacks, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if is_goal(state):
            return path
        for next_state, move in get_moves(state, costs):
            queue.append((next_state, path + [move]))

def is_goal(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

def get_moves(stacks, costs):
    moves = []
    for i, stack in enumerate(stacks):
        if stack:
            block = stack[-1]
            for j, target in enumerate(stacks):
                if not target or target[-1] == block:
                    next_state = stacks[:]
                    next_state[i] = stack[:-1]
                    next_state[j] = target + [block]
                    move = (i, j, costs[j])
                    moves.append((next_state, move))
    return moves

stacks = [['Yellow', 'Blue', 'Blue', 'Green'], [], ['Yellow', 'Green', 'Red', 'Red'], ['Green', 'Red', 'Yellow', 'Blue'], [], []]
costs = {0: 7, 1: 3, 2: 5, 3: 5, 4: 1, 5: 3}
print(bfs(stacks, costs))
