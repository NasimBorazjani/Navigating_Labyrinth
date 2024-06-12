
from collections import deque

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, moves = queue.popleft()
        if is_sorted(state):
            return moves
        for next_state, move in possible_moves(state):
            if next_state not in visited:
                queue.append((next_state, moves + [move]))
                visited.add(next_state)

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True

def possible_moves(tubes):
    moves = []
    for i, tube in enumerate(tubes):
        if tube:
            for j, other_tube in enumerate(tubes):
                if i != j and (not other_tube or tube[-1] == other_tube[-1]) and len(other_tube) < 6:
                    next_tubes = list(map(list, tubes))
                    next_tubes[j].append(next_tubes[i].pop())
                    moves.append((tuple(map(tuple, next_tubes)), (i, j)))
    return moves

tubes = [['Red', 'Blue', 'Blue', 'Red'], ['Red', 'Blue', 'Blue', 'Green'], ['Green', 'Green', 'Red', 'Green']]
print(sort_it(tubes))
