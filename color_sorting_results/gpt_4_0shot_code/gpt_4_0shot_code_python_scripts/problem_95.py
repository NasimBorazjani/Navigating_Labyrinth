
from collections import deque

def valid_moves(state):
    moves = []
    for i, tube in enumerate(state):
        if tube:
            for j, other_tube in enumerate(state):
                if i != j and (not other_tube or tube[-1] == other_tube[-1] or len(other_tube) < 9):
                    moves.append((i, j))
    return moves

def make_move(state, move):
    state = [list(tube) for tube in state]
    ball = state[move[0]].pop()
    state[move[1]].append(ball)
    return tuple(tuple(tube) for tube in state)

def is_solved(state):
    for tube in state:
        if tube and len(set(tube)) > 1:
            return False
    return True

def solve_sort_it(state):
    state = tuple(tuple(tube) for tube in state)
    queue = deque([(state, [])])
    seen = set([state])
    while queue:
        state, moves = queue.popleft()
        if is_solved(state):
            return moves
        for move in valid_moves(state):
            new_state = make_move(state, move)
            if new_state not in seen:
                queue.append((new_state, moves + [move]))
                seen.add(new_state)

initial_state = [['Green', 'Green', 'Green', 'Red', 'Blue', 'Blue'], ['Blue', 'Red', 'Red', 'Red', 'Green', 'Green'], ['Blue', 'Green', 'Blue', 'Red', 'Red', 'Blue']]
print(solve_sort_it(initial_state))
