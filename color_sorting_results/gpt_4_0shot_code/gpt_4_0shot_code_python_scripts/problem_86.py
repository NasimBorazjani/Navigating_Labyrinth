
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
    visited = set([str(tubes)])
    while queue:
        tubes, path = queue.popleft()
        if is_sorted(tubes):
            return path
        for move in get_moves(tubes):
            new_tubes = [list(tube) for tube in tubes]
            ball = new_tubes[move[0]].pop()
            new_tubes[move[1]].append(ball)
            new_state = str(new_tubes)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_tubes, path + [move]))

tubes = [['Red', 'Red', 'Blue', 'Red', 'Blue', 'Green'], ['Green', 'Red', 'Green', 'Green', 'Blue', 'Blue'], ['Red', 'Green', 'Blue', 'Red', 'Blue', 'Green']]
print(sort_it(tubes))
