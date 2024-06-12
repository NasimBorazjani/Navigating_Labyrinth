
from collections import deque

def perform_move(tubes, move):
    source, dest = move
    tubes[dest].append(tubes[source].pop())
    return tubes

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) != 1 or max(tube.count(c) for c in set(tube)) > 9:
            return False
    return True

def shortest_path(initial_tubes):
    queue = deque([(initial_tubes, [])])
    visited = set()

    while queue:
        tubes, moves = queue.popleft()
        if is_sorted(tubes):
            return moves

        for i in range(len(tubes)):
            for j in range(len(tubes)):
                if i != j and tubes[i] and tubes[i][-1] != tubes[j][-1]:
                    new_tubes = perform_move(list(map(list, tubes)), (i, j))
                    new_state = tuple(map(tuple, new_tubes))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_tubes, moves + [(i, j)]))

    return None

initial_tubes = [['Blue', 'Green', 'Red', 'Red', 'Green', 'Blue'], 
                 ['Green', 'Blue', 'Blue', 'Blue', 'Red', 'Red'], 
                 ['Green', 'Green', 'Green', 'Blue', 'Red', 'Red']]

print(shortest_path(initial_tubes))
