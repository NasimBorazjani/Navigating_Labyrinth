
from collections import deque

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    goal = tuple(sorted(start))
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, moves = queue.popleft()
        if state == goal:
            return moves
        for i in range(3):
            if not state[i]:
                continue
            for j in range(3):
                if i != j and (len(state[j]) < 6 or state[j][-1] == state[i][-1]):
                    new_state = list(map(list, state))
                    new_state[j].append(new_state[i].pop())
                    new_state = tuple(map(tuple, new_state))
                    if new_state not in visited:
                        queue.append((new_state, moves + [(i, j)]))
                        visited.add(new_state)

tubes = [['Blue', 'Green', 'Green', 'Red'], ['Red', 'Blue', 'Green', 'Red'], ['Blue', 'Red', 'Green', 'Blue']]
print(sort_it(tubes))
