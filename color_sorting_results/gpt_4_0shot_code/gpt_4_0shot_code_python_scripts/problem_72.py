
from collections import deque

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

def possible_moves(tubes):
    moves = []
    for i in range(len(tubes)):
        if tubes[i]:
            for j in range(len(tubes)):
                if i != j and (not tubes[j] or tubes[j][-1] == tubes[i][-1]):
                    new_tubes = [list(tube) for tube in tubes]
                    new_tubes[j].append(new_tubes[i].pop())
                    moves.append((new_tubes, (i, j)))
    return moves

def sort_it(tubes):
    queue = deque([(tubes, [])])
    visited = set()
    while queue:
        tubes, path = queue.popleft()
        if str(tubes) in visited:
            continue
        if is_sorted(tubes):
            return path
        visited.add(str(tubes))
        for new_tubes, move in possible_moves(tubes):
            queue.append((new_tubes, path + [move]))
    return None

tubes = [['Red', 'Red', 'Blue', 'Green', 'Red'], ['Blue', 'Green', 'Green', 'Red', 'Red'], ['Blue', 'Blue', 'Green', 'Green', 'Blue']]
print(sort_it(tubes))
