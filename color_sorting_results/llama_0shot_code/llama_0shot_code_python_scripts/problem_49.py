
from collections import deque

def sort_it(tubes):
    colors = {'Red': 0, 'Blue': 1, 'Green': 2}
    init_state = tuple(tuple(sorted([colors[ball] for ball in tube]) for tube in tubes))
    final_state = ((0, 0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), (2, 2, 2, 2, 2, 2, 2))
    visited = {init_state: []}
    q = deque([(init_state, [])])
    while q:
        state, moves = q.popleft()
        if state == final_state:
            return moves
        for i in range(3):
            for j in range(3):
                if i != j and len(state[i]) < 7 and len(state[j]) > 0:
                    new_state = list(state)
                    new_state[i] = state[i] + (state[j][-1],)
                    new_state[j] = state[j][:-1]
                    new_state = tuple(tuple(sorted(tube)) for tube in new_state)
                    if new_state not in visited:
                        visited[new_state] = moves + [(i, j)]
                        q.append((new_state, moves + [(i, j)]))
    return []

tubes = [['Red', 'Blue', 'Blue', 'Green'], ['Green', 'Green', 'Red', 'Blue'], ['Red', 'Red', 'Blue', 'Green']]
print(sort_it(tubes))
