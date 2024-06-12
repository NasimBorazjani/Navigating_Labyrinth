
from collections import deque
from copy import deepcopy

def is_goal(state):
    return all(len(set(tube)) <= 1 for tube in state)

def get_moves(state):
    moves = []
    for i, src in enumerate(state):
        if not src:
            continue
        for j, dst in enumerate(state):
            if i == j or len(dst) == 9:
                continue
            if not dst or dst[-1] == src[-1]:
                moves.append((i, j))
    return moves

def bfs(start):
    queue = deque([(start, [])])
    seen = set([str(start)])
    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path
        for move in get_moves(state):
            new_state = deepcopy(state)
            src, dst = move
            new_state[dst].append(new_state[src].pop())
            if str(new_state) not in seen:
                queue.append((new_state, path + [move]))
                seen.add(str(new_state))

start = [['Red', 'Red', 'Blue', 'Red', 'Blue', 'Green'], ['Red', 'Green', 'Blue', 'Blue', 'Green', 'Red'], ['Blue', 'Green', 'Green', 'Red', 'Blue', 'Green']]
start = [list(reversed(tube)) for tube in start]
print(bfs(start))
