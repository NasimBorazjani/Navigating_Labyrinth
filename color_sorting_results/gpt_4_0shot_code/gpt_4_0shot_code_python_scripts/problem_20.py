
from collections import deque

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    goal = (tuple(sorted(tube, reverse=True)) for tube in start)
    goal = tuple(sorted(goal, reverse=True))
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, moves = queue.popleft()
        if state == goal:
            return moves
        for move in possible_moves(state):
            new_state = apply_move(state, move)
            if new_state not in visited:
                queue.append((new_state, moves + [move]))
                visited.add(new_state)

def possible_moves(state):
    moves = []
    for i, tube in enumerate(state):
        if tube:
            for j in range(len(state)):
                if i != j and (not state[j] or tube[0] >= state[j][0]):
                    moves.append((i, j))
    return moves

def apply_move(state, move):
    state = list(map(list, state))
    i, j = move
    state[j].insert(0, state[i].pop(0))
    return tuple(map(tuple, state))

tubes = [['Red', 'Red', 'Green', 'Blue'], ['Green', 'Green', 'Red', 'Green'], ['Blue', 'Blue', 'Red', 'Blue']]
print(sort_it(tubes))
