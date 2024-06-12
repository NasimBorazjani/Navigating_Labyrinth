
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
                ball = tube[-1]
                for j, target in enumerate(tubes):
                    if i != j and (not target or target[-1] == ball) and len(target) < 8:
                        new_tubes = deepcopy(tubes)
                        new_tubes[j].append(new_tubes[i].pop())
                        new_moves = moves + [(i, j)]
                        queue.append((new_tubes, new_moves))

def is_sorted(tubes):
    for tube in tubes:
        if tube and len(set(tube)) > 1:
            return False
    return True

tubes = [['Blue', 'Green', 'Blue', 'Blue', 'Blue'], ['Blue', 'Green', 'Red', 'Red', 'Green'], ['Green', 'Red', 'Red', 'Green', 'Red']]
print(sort_it(tubes))
