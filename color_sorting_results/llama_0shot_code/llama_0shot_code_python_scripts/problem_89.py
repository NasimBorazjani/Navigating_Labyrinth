
from collections import deque

def move(tubes, move):
    src, dest = move
    tubes[dest].append(tubes[src].pop())
    return tubes

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) != 1:
            return False
    return True

def shortest_sort(tubes):
    queue = deque([([0, 0], tubes)])
    visited = {tuple(map(tuple, tubes)): ([], tubes)}
    while queue:
        moves, tubes = queue.popleft()
        if is_sorted(tubes):
            return moves
        for i in range(3):
            for j in range(3):
                if i != j and len(tubes[i]) > 0 and len(tubes[j]) < 9:
                    new_tubes = move(list(map(list, tubes)), (i, j))
                    new_state = tuple(map(tuple, new_tubes))
                    if new_state not in visited:
                        visited[new_state] = (moves + [(i, j)], new_tubes)
                        queue.append(visited[new_state])
    return []

initial_tubes = [['Blue', 'Green', 'Blue', 'Red', 'Red', 'Green'], 
                 ['Blue', 'Green', 'Blue', 'Blue', 'Red', 'Green'], 
                 ['Blue', 'Green', 'Red', 'Red', 'Green', 'Red']]

print(shortest_sort(initial_tubes))
