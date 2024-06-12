
from collections import deque

def move_ball(tubes, move):
    src, dest = move
    if not tubes[src] or len(tubes[dest]) == 8:
        return None
    ball = tubes[src].pop()
    tubes[dest].append(ball)
    return tubes

def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) != 1:
            return False
    return True

def shortest_path(tubes):
    queue = deque([([], tubes)])
    visited = set()
    while queue:
        path, tubes = queue.popleft()
        if is_sorted(tubes):
            return path
        for i in range(3):
            for j in range(3):
                if i != j:
                    move = (i, j)
                    new_tubes = move_ball(list(map(list, tubes)), move)
                    if new_tubes and tuple(map(tuple, new_tubes)) not in visited:
                        visited.add(tuple(map(tuple, new_tubes)))
                        queue.append((path + [move], new_tubes))

initial_tubes = [['Red', 'Green', 'Red', 'Blue', 'Green'], 
                 ['Red', 'Blue', 'Green', 'Blue', 'Blue'], 
                 ['Green', 'Red', 'Red', 'Green', 'Blue']]

print(shortest_path(initial_tubes))
