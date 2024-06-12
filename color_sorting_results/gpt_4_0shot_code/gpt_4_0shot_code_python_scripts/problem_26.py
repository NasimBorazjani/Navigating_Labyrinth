
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
    return all(len(set(tube)) <= 1 for tube in tubes)

def possible_moves(tubes):
    for i, tube in enumerate(tubes):
        if tube:
            for j, other_tube in enumerate(tubes):
                if i != j and (not other_tube or tube[-1] == other_tube[-1]):
                    next_tubes = list(map(list, tubes))
                    next_tubes[j].append(next_tubes[i].pop())
                    yield tuple(map(tuple, next_tubes)), (i, j)

tubes = [['Red', 'Blue', 'Blue', 'Red'], ['Green', 'Green', 'Blue', 'Blue'], ['Green', 'Green', 'Red', 'Red']]
print(sort_it(tubes))
