
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    start = tubes
    goal = sorted(deepcopy(tubes), key=lambda x: x[0] if x else 'ZZZ')
    queue = deque([(start, [])])
    visited = set([str(start)])

    while queue:
        state, moves = queue.popleft()
        if state == goal:
            return moves
        for i in range(len(state)):
            if not state[i]:
                continue
            for j in range(len(state)):
                if i == j:
                    continue
                if len(state[j]) < 7 and (not state[j] or state[i][-1] == state[j][-1]):
                    new_state = deepcopy(state)
                    new_state[j].append(new_state[i].pop())
                    if str(new_state) not in visited:
                        visited.add(str(new_state))
                        queue.append((new_state, moves + [(i, j)]))

tubes = [['Blue', 'Red', 'Red', 'Red'], ['Green', 'Blue', 'Green', 'Green'], ['Blue', 'Blue', 'Green', 'Red']]
print(sort_it(tubes))
