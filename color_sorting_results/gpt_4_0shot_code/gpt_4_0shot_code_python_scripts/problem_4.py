
from collections import deque
from copy import deepcopy

def is_goal(state):
    return all(len(set(tube)) <= 1 for tube in state)

def get_moves(state):
    moves = []
    for i, src in enumerate(state):
        if src:
            for j, dst in enumerate(state):
                if i != j and (len(dst) < 6 and (not dst or src[-1] == dst[-1])):
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
            next_state[move[1]].append(next_state[move[0]].pop())
            if str(next_state) not in seen:
                queue.append((next_state, path + [move]))
                seen.add(str(next_state))

tubes = [['Red', 'Red', 'Blue', 'Blue'], ['Red', 'Blue', 'Red', 'Green'], ['Green', 'Blue', 'Green', 'Green']]
print(sort_it(tubes))
