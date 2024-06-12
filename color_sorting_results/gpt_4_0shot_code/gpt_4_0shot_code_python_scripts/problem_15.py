
from collections import deque

def sort_it(tubes):
    start = [deque(tube) for tube in tubes]
    goal = [deque(sorted(tube)) for tube in start]
    visited = set()
    stack = [(start, [])]
    while stack:
        state, moves = stack.pop()
        if state == goal:
            return moves
        for i, tube in enumerate(state):
            if tube:
                ball = tube[-1]
                for j, target in enumerate(state):
                    if i != j and (len(target) < 6 or target[-1] == ball):
                        new_state = [deque(t) for t in state]
                        new_state[i].pop()
                        new_state[j].append(ball)
                        new_moves = moves + [(i, j)]
                        if tuple(new_state) not in visited:
                            visited.add(tuple(new_state))
                            stack.append((new_state, new_moves))

tubes = [['Blue', 'Red', 'Red', 'Blue'], ['Green', 'Green', 'Red', 'Red'], ['Green', 'Green', 'Blue', 'Blue']]
print(sort_it(tubes))
