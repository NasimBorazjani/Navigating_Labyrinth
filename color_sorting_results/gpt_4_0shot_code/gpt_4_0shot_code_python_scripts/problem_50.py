
from collections import deque

def sort_it(tubes):
    start = tuple(tuple(tube) for tube in tubes)
    goal = tuple(sorted(tube) for tube in start)
    visited = set([start])
    queue = deque([(start, [])])

    while queue:
        state, moves = queue.popleft()
        if state == goal:
            return moves
        for move in possible_moves(state):
            if move not in visited:
                visited.add(move)
                queue.append((move, moves + [move]))

def possible_moves(state):
    moves = []
    for i, tube in enumerate(state):
        if tube:
            for j, other_tube in enumerate(state):
                if i != j and (not other_tube or tube[-1] == other_tube[-1]):
                    new_state = list(state)
                    new_state[i] = tuple(tube[:-1])
                    new_state[j] = tuple([tube[-1]] + list(other_tube))
                    moves.append((i, j, tuple(new_state)))
    return moves

tubes = [['Blue', 'Green', 'Red', 'Red'], ['Red', 'Blue', 'Green', 'Red'], ['Blue', 'Blue', 'Green', 'Green']]
print(sort_it(tubes))
