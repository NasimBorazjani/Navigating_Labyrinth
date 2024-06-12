
from collections import deque

def sort_it(tubes):
    tubes = [deque(tube) for tube in tubes]
    visited = set()
    queue = deque([(tubes, [])])
    while queue:
        tubes, moves = queue.popleft()
        if is_sorted(tubes):
            return moves
        for i, tube in enumerate(tubes):
            if tube:
                for j, other_tube in enumerate(tubes):
                    if i != j and (len(other_tube) < 8 or other_tube[-1] == tube[-1]):
                        new_tubes = [deque(t) for t in tubes]
                        new_tubes[j].append(new_tubes[i].pop())
                        state = tuple(tuple(t) for t in new_tubes)
                        if state not in visited:
                            visited.add(state)
                            queue.append((new_tubes, moves + [(i, j)]))

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

tubes = [['Red', 'Green', 'Green', 'Red', 'Blue'], ['Red', 'Blue', 'Green', 'Red', 'Green'], ['Green', 'Blue', 'Blue', 'Blue', 'Red']]
print(sort_it(tubes))
