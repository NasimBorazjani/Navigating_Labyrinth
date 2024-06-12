
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
        if all(len(set(tube)) <= 1 for tube in tubes):
            return moves
        for i, src in enumerate(tubes):
            if not src:
                continue
            for j, dst in enumerate(tubes):
                if i != j and (len(dst) < 6 or dst[-1] == src[-1]):
                    new_tubes = deepcopy(tubes)
                    new_tubes[j].append(new_tubes[i].pop())
                    new_moves = moves + [(i, j)]
                    queue.append((new_tubes, new_moves))

print(sort_it([['Green', 'Blue', 'Blue', 'Green'], ['Red', 'Green', 'Red', 'Blue'], ['Red', 'Green', 'Blue', 'Red']]))
