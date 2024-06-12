
from collections import deque
from copy import deepcopy

def valid_move(state, from_tube, to_tube):
    if not state[from_tube] or (state[to_tube] and state[to_tube][-1] != state[from_tube][-1]):
        return False
    if len(state[to_tube]) == 8:
        return False
    return True

def make_move(state, from_tube, to_tube):
    new_state = deepcopy(state)
    new_state[to_tube].append(new_state[from_tube].pop())
    return new_state

def is_goal(state):
    for tube in state:
        if tube and len(set(tube)) > 1:
            return False
    return True

def solve(state):
    queue = deque([(state, [])])
    seen = set([str(state)])

    while queue:
        state, moves = queue.popleft()
        if is_goal(state):
            return moves
        for from_tube in range(3):
            for to_tube in range(3):
                if from_tube != to_tube and valid_move(state, from_tube, to_tube):
                    new_state = make_move(state, from_tube, to_tube)
                    if str(new_state) not in seen:
                        queue.append((new_state, moves + [(from_tube, to_tube)]))
                        seen.add(str(new_state))

initial_state = [['Red', 'Blue', 'Green', 'Blue', 'Blue'], ['Green', 'Red', 'Green', 'Red', 'Blue'], ['Blue', 'Green', 'Red', 'Red', 'Green']]
print(solve(initial_state))
