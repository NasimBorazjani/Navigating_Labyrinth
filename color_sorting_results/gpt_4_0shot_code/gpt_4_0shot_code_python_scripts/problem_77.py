
from collections import deque

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

def get_moves(tubes):
    visited = set()
    queue = deque([(tubes, [])])
    while queue:
        tubes, moves = queue.popleft()
        if is_sorted(tubes):
            return moves
        for i in range(3):
            if tubes[i]:
                for j in range(3):
                    if i != j and (len(tubes[j]) < 9 or tubes[j][-1] == tubes[i][-1]):
                        new_tubes = [list(tube) for tube in tubes]
                        new_tubes[j].append(new_tubes[i].pop())
                        state = tuple(tuple(tube) for tube in new_tubes)
                        if state not in visited:
                            visited.add(state)
                            queue.append((new_tubes, moves + [(i, j)]))
    return []

tubes = [['Red', 'Blue', 'Green', 'Red', 'Blue', 'Green'], ['Blue', 'Green', 'Green', 'Blue', 'Red', 'Blue'], ['Green', 'Red', 'Red', 'Green', 'Blue', 'Red']]
print(get_moves(tubes))
