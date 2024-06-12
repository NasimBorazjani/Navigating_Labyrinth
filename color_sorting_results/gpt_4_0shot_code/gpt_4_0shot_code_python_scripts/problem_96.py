
from collections import deque
from copy import deepcopy

def is_goal(state):
    return all(len(set(tube)) <= 1 for tube in state)

def get_moves(state):
    moves = []
    for i, src in enumerate(state):
        if src:
            for j, dst in enumerate(state):
                if i != j and (len(dst) < 9 and (not dst or src[-1] == dst[-1])):
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
            i, j = move
            new_state[j].append(new_state[i].pop())
            if str(new_state) not in seen:
                queue.append((new_state, path + [move]))
                seen.add(str(new_state))

tubes = [['Blue', 'Green', 'Red', 'Red', 'Green', 'Blue'], ['Green', 'Blue', 'Blue', 'Blue', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Blue', 'Red', 'Red']]
print(sort_it(tubes))
