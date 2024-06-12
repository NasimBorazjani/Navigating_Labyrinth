
from collections import deque

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        tubes, moves = queue.popleft()
        if is_sorted(tubes):
            return moves
        for i, tube in enumerate(tubes):
            if not tube:
                continue
            for j in range(len(tubes)):
                if i == j or len(tubes[j]) == 7:
                    continue
                new_tubes = list(map(list, tubes))
                new_tubes[j].append(new_tubes[i].pop())
                new_state = tuple(map(tuple, new_tubes))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + [(i, j)]))

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

tubes = [['Green', 'Blue', 'Red', 'Blue'], ['Red', 'Green', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Red']]
print(sort_it(tubes))
