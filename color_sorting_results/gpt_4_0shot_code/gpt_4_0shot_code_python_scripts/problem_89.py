
from collections import deque
from copy import deepcopy

def get_moves(state):
    moves = []
    for i, tube in enumerate(state):
        if not tube:
            continue
        for j, target in enumerate(state):
            if i == j:
                continue
            if not target or tube[-1] == target[-1] and len(target) < 9:
                moves.append((i, j))
    return moves

def apply_move(state, move):
    new_state = deepcopy(state)
    i, j = move
    new_state[j].append(new_state[i].pop())
    return new_state

def is_solved(state):
    for tube in state:
        if tube and len(set(tube)) > 1:
            return False
    return True

def solve(state):
    queue = deque([(state, [])])
    seen = set([str(state)])
    while queue:
        state, path = queue.popleft()
        if is_solved(state):
            return path
        for move in get_moves(state):
            new_state = apply_move(state, move)
            if str(new_state) not in seen:
                queue.append((new_state, path + [move]))
                seen.add(str(new_state))

initial_state = [['Blue', 'Green', 'Blue', 'Red', 'Red', 'Green'], ['Blue', 'Green', 'Blue', 'Blue', 'Red', 'Green'], ['Blue', 'Green', 'Red', 'Red', 'Green', 'Red']]
print(solve(initial_state))
