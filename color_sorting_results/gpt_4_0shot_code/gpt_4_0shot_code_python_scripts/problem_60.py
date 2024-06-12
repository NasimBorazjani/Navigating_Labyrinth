
from collections import deque

def bfs(tubes):
    queue = deque([(tubes, [])])
    visited = set([tuple(map(tuple, tubes))])

    while queue:
        tubes, moves = queue.popleft()
        if is_sorted(tubes):
            return moves
        for i in range(3):
            if tubes[i]:
                for j in range(3):
                    if i != j and (not tubes[j] or tubes[j][-1] == tubes[i][-1]) and len(tubes[j]) < 8:
                        new_tubes = [list(t) for t in tubes]
                        new_tubes[j].append(new_tubes[i].pop())
                        if tuple(map(tuple, new_tubes)) not in visited:
                            queue.append((new_tubes, moves + [(i, j)]))
                            visited.add(tuple(map(tuple, new_tubes)))

def is_sorted(tubes):
    for tube in tubes:
        if tube and len(set(tube)) > 1:
            return False
    return True

tubes = [['Green', 'Red', 'Blue', 'Blue', 'Green'], ['Red', 'Green', 'Blue', 'Red', 'Green'], ['Blue', 'Red', 'Blue', 'Green', 'Red']]
print(bfs(tubes))
