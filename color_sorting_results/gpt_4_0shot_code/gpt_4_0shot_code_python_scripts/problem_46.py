
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, moves = queue.popleft()
        if is_sorted(state):
            return moves
        for move in possible_moves(state):
            new_state = apply_move(state, move)
            if new_state not in visited:
                queue.append((new_state, moves + [move]))
                visited.add(new_state)

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

def possible_moves(tubes):
    moves = []
    for i, tube in enumerate(tubes):
        if tube:
            for j, other_tube in enumerate(tubes):
                if i != j and (not other_tube or tube[-1] == other_tube[-1]):
                    moves.append((i, j))
    return moves

def apply_move(tubes, move):
    tubes = deepcopy(tubes)
    i, j = move
    tubes[j].append(tubes[i].pop())
    return tuple(map(tuple, tubes))

tubes = [['Red', 'Blue', 'Red', 'Red'], ['Blue', 'Green', 'Green', 'Blue'], ['Green', 'Blue', 'Green', 'Red']]
print(sort_it(tubes))
