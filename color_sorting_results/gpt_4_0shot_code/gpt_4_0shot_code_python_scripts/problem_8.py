
from collections import deque
from copy import deepcopy

def is_goal(state):
    return all(len(set(tube)) <= 1 for tube in state)

def get_moves(state):
    moves = []
    for i, src in enumerate(state):
        if src:
            for j, dst in enumerate(state):
                if i != j and (not dst or dst[-1] == src[-1]):
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
            next_state = deepcopy(state)
            src, dst = move
            next_state[dst].append(next_state[src].pop())
            if str(next_state) not in seen:
                queue.append((next_state, path + [move]))
                seen.add(str(next_state))

tubes = [['Green', 'Blue', 'Red', 'Red'], ['Red', 'Green', 'Green', 'Blue'], ['Red', 'Green', 'Blue', 'Blue']]
print(sort_it(tubes))
