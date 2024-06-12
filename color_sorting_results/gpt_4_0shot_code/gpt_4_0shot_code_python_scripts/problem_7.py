
from collections import deque
from copy import deepcopy

def is_goal(state):
    return all(len(set(tube)) <= 1 for tube in state)

def get_moves(state):
    moves = []
    for i, src in enumerate(state):
        if src:
            for j, dst in enumerate(state):
                if len(dst) < 6 and (not dst or dst[-1] == src[-1]):
                    moves.append((i, j))
    return moves

def sort_it(state):
    queue = deque([(state, [])])
    seen = set([str(state)])
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

initial_state = [['Red', 'Red', 'Blue', 'Green'], ['Blue', 'Red', 'Blue', 'Green'], ['Blue', 'Green', 'Red', 'Green']]
print(sort_it(initial_state))
