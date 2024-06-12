
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    start = tubes
    goal = sorted(tubes, key=lambda x: (-len(x), x[0] if x else ''))
    visited = set()
    queue = deque([([], start)])

    while queue:
        path, tubes = queue.popleft()
        if tubes == goal:
            return path
        for i, tube in enumerate(tubes):
            if tube:
                for j, target in enumerate(tubes):
                    if i != j and (not target or target[-1] == tube[-1] and len(target) < 9):
                        new_tubes = deepcopy(tubes)
                        new_tubes[j].append(new_tubes[i].pop())
                        new_tubes_tuple = tuple(tuple(x) for x in new_tubes)
                        if new_tubes_tuple not in visited:
                            visited.add(new_tubes_tuple)
                            queue.append((path + [(i, j)], new_tubes))

tubes = [['Red', 'Green', 'Blue', 'Blue', 'Blue', 'Red'], ['Red', 'Red', 'Green', 'Blue', 'Green', 'Blue'], ['Red', 'Red', 'Green', 'Green', 'Blue', 'Green']]
print(sort_it(tubes))
