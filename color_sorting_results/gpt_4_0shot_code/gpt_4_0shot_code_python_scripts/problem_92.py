
from collections import deque

def bfs(tubes):
    queue = deque([(tubes, [])])
    visited = set([tuple(map(tuple, tubes))])

    while queue:
        tubes, moves = queue.popleft()
        if is_sorted(tubes):
            return moves
        for i, tube in enumerate(tubes):
            if tube:
                for j, target in enumerate(tubes):
                    if i != j and (not target or target[-1] == tube[-1]) and len(target) < 9:
                        new_tubes = [list(t) for t in tubes]
                        new_tubes[j].append(new_tubes[i].pop())
                        state = tuple(map(tuple, new_tubes))
                        if state not in visited:
                            queue.append((new_tubes, moves + [(i, j)]))
                            visited.add(state)

def is_sorted(tubes):
    for tube in tubes:
        if tube and len(set(tube)) > 1:
            return False
    return True

tubes = [['Red', 'Green', 'Blue', 'Red', 'Red', 'Blue'], ['Green', 'Red', 'Green', 'Green', 'Blue', 'Red'], ['Green', 'Blue', 'Green', 'Blue', 'Blue', 'Red']]
print(bfs(tubes))
