
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
            if not tubes[i]:
                continue
            for j in range(3):
                if i != j and (not tubes[j] or tubes[j][-1] == tubes[i][-1]) and len(tubes[j]) < 6:
                    new_tubes = deepcopy(tubes)
                    new_tubes[j].append(new_tubes[i].pop())
                    new_state = tuple(map(tuple, new_tubes))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, moves + [(i, j)]))

def is_sorted(tubes):
    for tube in tubes:
        if tube and len(set(tube)) > 1:
            return False
    return True

tubes = [['Green', 'Blue', 'Blue', 'Blue'], ['Red', 'Green', 'Red', 'Red'], ['Green', 'Red', 'Green', 'Blue']]
print(sort_it(tubes))
