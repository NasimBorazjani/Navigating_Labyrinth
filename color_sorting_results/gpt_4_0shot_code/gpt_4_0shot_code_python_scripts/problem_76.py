
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        tubes, moves = queue.popleft()
        if is_sorted(tubes):
            return moves
        for i in range(3):
            if not tubes[i]: continue
            for j in range(3):
                if i == j or len(tubes[j]) == 9: continue
                new_tubes = deepcopy(tubes)
                new_tubes[j].append(new_tubes[i].pop())
                state = tuple(map(tuple, new_tubes))
                if state not in visited:
                    visited.add(state)
                    queue.append((state, moves + [(i, j)]))

def is_sorted(tubes):
    for tube in tubes:
        if tube and len(set(tube)) > 1:
            return False
    return True

tubes = [['Blue', 'Green', 'Red', 'Red', 'Green', 'Blue'], ['Green', 'Blue', 'Blue', 'Blue', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Blue', 'Red', 'Red']]
print(sort_it(tubes))
