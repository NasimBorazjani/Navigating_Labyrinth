
from collections import deque

def sort_it(tubes):
    start = tuple(tuple(tube) for tube in tubes)
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        tubes, moves = queue.popleft()
        if is_sorted(tubes):
            return moves
        for i, tube in enumerate(tubes):
            if tube:
                for j in range(len(tubes)):
                    if i != j and (not tubes[j] or tubes[j][-1] == tube[-1]) and len(tubes[j]) < 9:
                        new_tubes = list(list(t) for t in tubes)
                        new_tubes[j].append(new_tubes[i].pop())
                        state = tuple(tuple(t) for t in new_tubes)
                        if state not in visited:
                            queue.append((state, moves + [(i, j)]))
                            visited.add(state)

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

tubes = [['Blue', 'Green', 'Red', 'Red', 'Blue', 'Green'], ['Blue', 'Red', 'Green', 'Green', 'Green', 'Red'], ['Blue', 'Blue', 'Blue', 'Red', 'Red', 'Green']]
print(sort_it(tubes))
