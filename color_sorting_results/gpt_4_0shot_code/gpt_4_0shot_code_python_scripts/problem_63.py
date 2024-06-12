
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
                if i == j or len(tubes[j]) == 8:
                    continue
                new_tubes = list(map(list, tubes))
                new_tubes[j].append(new_tubes[i].pop())
                new_tubes = tuple(map(tuple, new_tubes))
                if new_tubes not in visited:
                    visited.add(new_tubes)
                    queue.append((new_tubes, moves + [(i, j)]))

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

tubes = [['Blue', 'Green', 'Blue', 'Red', 'Green'], ['Blue', 'Green', 'Green', 'Red', 'Blue'], ['Red', 'Blue', 'Red', 'Red', 'Green']]
print(sort_it(tubes))
