
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
                for j, other_tube in enumerate(tubes):
                    if i != j and (not other_tube or tube[-1] == other_tube[-1]):
                        new_tubes = list(list(t) for t in tubes)
                        new_tubes[j].append(new_tubes[i].pop())
                        new_state = tuple(tuple(t) for t in new_tubes)
                        if new_state not in visited:
                            queue.append((new_state, moves + [(i, j)]))
                            visited.add(new_state)

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

tubes = [['Red', 'Green', 'Blue', 'Red', 'Green'], ['Green', 'Red', 'Green', 'Red', 'Blue'], ['Blue', 'Red', 'Green', 'Blue', 'Blue']]
print(sort_it(tubes))
