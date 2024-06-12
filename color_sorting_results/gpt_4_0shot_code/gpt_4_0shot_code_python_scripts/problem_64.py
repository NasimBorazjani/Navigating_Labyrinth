
from collections import deque
from copy import deepcopy

def bfs(tubes):
    queue = deque([(tubes, [])])
    visited = set([str(tubes)])

    while queue:
        tubes, moves = queue.popleft()

        if is_sorted(tubes):
            return moves

        for i in range(3):
            if not tubes[i]:
                continue
            for j in range(3):
                if i == j or len(tubes[j]) == 5:
                    continue
                new_tubes = deepcopy(tubes)
                new_tubes[j].append(new_tubes[i].pop())
                if str(new_tubes) not in visited:
                    visited.add(str(new_tubes))
                    queue.append((new_tubes, moves + [(i, j)]))

def is_sorted(tubes):
    for tube in tubes:
        if tube and len(set(tube)) > 1:
            return False
    return True

tubes = [['Red', 'Blue', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Green', 'Green'], ['Red', 'Green', 'Green', 'Green', 'Blue']]
print(bfs(tubes))
