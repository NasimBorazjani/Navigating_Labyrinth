
from collections import deque

def generate_moves(state):
    moves = []
    for i, tube in enumerate(state):
        if tube:
            for j, other_tube in enumerate(state):
                if i != j and (not other_tube or tube[-1] == other_tube[-1]) and len(other_tube) < 7:
                    new_state = [list(t) for t in state]
                    new_state[j].append(new_state[i].pop())
                    moves.append((new_state, (i, j)))
    return moves

def is_goal(state):
    for tube in state:
        if tube and len(set(tube)) > 1:
            return False
    return True

def sort_it(state):
    queue = deque([(state, [])])
    seen = set([str(state)])
    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path
        for new_state, move in generate_moves(state):
            if str(new_state) not in seen:
                queue.append((new_state, path + [move]))
                seen.add(str(new_state))

initial_state = [['Red', 'Green', 'Green', 'Blue'], ['Blue', 'Red', 'Red', 'Red'], ['Blue', 'Green', 'Green', 'Blue']]
print(sort_it(initial_state))
