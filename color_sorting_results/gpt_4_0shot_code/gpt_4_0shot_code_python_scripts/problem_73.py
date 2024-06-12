
from collections import deque
from copy import deepcopy

def bfs(start):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, moves = queue.popleft()
        if is_goal(state):
            return moves
        for next_state, move in get_moves(state):
            if str(next_state) not in visited:
                visited.add(str(next_state))
                queue.append((next_state, moves + [move]))

def is_goal(state):
    return all(len(set(tube)) <= 1 for tube in state)

def get_moves(state):
    moves = []
    for i, tube in enumerate(state):
        if tube:
            for j, other_tube in enumerate(state):
                if i != j and (not other_tube or tube[-1] == other_tube[-1]):
                    next_state = deepcopy(state)
                    next_state[j].append(next_state[i].pop())
                    moves.append((next_state, (i, j)))
    return moves

start = [['Red', 'Green', 'Red', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Blue', 'Blue'], ['Green', 'Red', 'Red', 'Green', 'Blue']]
print(bfs(start))
