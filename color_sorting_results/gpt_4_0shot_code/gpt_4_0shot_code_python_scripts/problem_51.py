
from collections import deque

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    goal = (tuple(sorted(tubes[0])), tuple(sorted(tubes[1])), tuple(sorted(tubes[2])))
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, moves = queue.popleft()
        if state == goal:
            return moves
        for i in range(3):
            if not state[i]: continue
            for j in range(3):
                if i == j or len(state[j]) == 5: continue
                new_state = list(map(list, state))
                new_state[j].append(new_state[i].pop())
                new_state = tuple(map(tuple, new_state))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + [(i, j)]))

tubes = [['Green', 'Green', 'Red', 'Blue', 'Blue'], ['Blue', 'Green', 'Green', 'Red', 'Red'], ['Red', 'Red', 'Blue', 'Green', 'Blue']]
print(sort_it(tubes))
