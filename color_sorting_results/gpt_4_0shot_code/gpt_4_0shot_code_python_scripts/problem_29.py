
from collections import deque

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
                if i != j and (not tubes[j] or tubes[j][-1] == tubes[i][-1] and len(tubes[j]) < 7):
                    new_tubes = list(map(list, tubes))
                    new_tubes[j].append(new_tubes[i].pop())
                    new_tubes = tuple(map(tuple, new_tubes))
                    if new_tubes not in visited:
                        visited.add(new_tubes)
                        queue.append((new_tubes, moves + [(i, j)]))

def is_sorted(tubes):
    for tube in tubes:
        if tube and len(set(tube)) > 1:
            return False
    return True

tubes = [['Red', 'Blue', 'Blue', 'Red'], ['Blue', 'Green', 'Blue', 'Green'], ['Green', 'Red', 'Green', 'Red']]
print(sort_it(tubes))
