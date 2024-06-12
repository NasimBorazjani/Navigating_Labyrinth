
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    tubes = [deque(tube) for tube in tubes]
    visited = set()
    queue = deque([(tubes, [])])
    while queue:
        tubes, moves = queue.popleft()
        if str(tubes) in visited:
            continue
        visited.add(str(tubes))
        if is_sorted(tubes):
            return moves
        for i, tube in enumerate(tubes):
            if tube:
                for j, target in enumerate(tubes):
                    if i != j and (not target or target[-1] == tube[-1]) and len(target) < 9:
                        new_tubes = deepcopy(tubes)
                        new_tubes[j].append(new_tubes[i].pop())
                        queue.append((new_tubes, moves + [(i, j)]))

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True
