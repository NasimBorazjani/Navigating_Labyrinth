
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
                if i != j and (not other_tube or tube[-1] == other_tube[-1]) and len(other_tube) < 9:
                    moves.append((i, j))
    return moves

def sort_it(tubes):
    queue = deque([(tubes, [])])
    visited = set([str(tubes)])
    while queue:
        tubes, path = queue.popleft()
        if is_sorted(tubes):
            return path
        for move in get_moves(tubes):
            new_tubes = [list(tube) for tube in tubes]
            new_tubes[move[1]].append(new_tubes[move[0]].pop())
            str_tubes = str(new_tubes)
            if str_tubes not in visited:
                queue.append((new_tubes, path + [move]))
                visited.add(str_tubes)

tubes = [['Blue', 'Red', 'Red', 'Green', 'Blue', 'Green'], ['Blue', 'Red', 'Red', 'Red', 'Green', 'Green'], ['Blue', 'Red', 'Blue', 'Blue', 'Green', 'Green']]
print(sort_it(tubes))