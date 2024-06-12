
from collections import deque

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

def get_moves(tubes):
    moves = []
    for i, tube in enumerate(tubes):
        if tube:
            for j, other_tube in enumerate(tubes):
                if i != j and (not other_tube or tube[-1] == other_tube[-1]):
                    moves.append((i, j))
    return moves

def sort_it(tubes):
    queue = deque([(tubes, [])])
    visited = set()

    while queue:
        tubes, path = queue.popleft()
        if str(tubes) in visited:
            continue
        visited.add(str(tubes))
        if is_sorted(tubes):
            return path
        for move in get_moves(tubes):
            new_tubes = [list(tube) for tube in tubes]
            ball = new_tubes[move[0]].pop()
            new_tubes[move[1]].append(ball)
            queue.append((new_tubes, path + [move]))

tubes = [['Blue', 'Green', 'Red', 'Green', 'Green', 'Red'], ['Green', 'Blue', 'Red', 'Blue', 'Blue', 'Red'], ['Red', 'Green', 'Blue', 'Blue', 'Green', 'Red']]
print(sort_it(tubes))
