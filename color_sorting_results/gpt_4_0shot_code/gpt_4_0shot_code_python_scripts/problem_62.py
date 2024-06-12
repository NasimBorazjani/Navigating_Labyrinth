
from collections import deque
from copy import deepcopy

def bfs(start):
    queue = deque([(start, [])])
    visited = set([str(start)])

    while queue:
        state, moves = queue.popleft()
        if is_goal(state):
            return moves
        for next_state, move in get_next_states(state):
            if str(next_state) not in visited:
                queue.append((next_state, moves + [move]))
                visited.add(str(next_state))

def is_goal(state):
    return all(len(set(tube)) <= 1 for tube in state)

def get_next_states(state):
    next_states = []
    for i, src in enumerate(state):
        if not src:
            continue
        for j, dst in enumerate(state):
            if i == j or len(dst) == 8:
                continue
            next_state = deepcopy(state)
            next_state[j].append(next_state[i].pop())
            next_states.append((next_state, (i, j)))
    return next_states

start = [['Blue', 'Green', 'Green', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Blue', 'Green'], ['Red', 'Blue', 'Red', 'Red', 'Red']]
print(bfs(start))
