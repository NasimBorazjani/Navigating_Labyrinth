
from collections import deque

def move_ball(tubes, move):
    src, dest = move
    if tubes[src]:
        ball = tubes[src].pop()
        tubes[dest].append(ball)
    return tubes

def is_sorted(tube):
    return tube == sorted(tube)

def shortest_path(tubes):
    queue = deque([(tubes, [])])
    visited = set()
    while queue:
        tubes, path = queue.popleft()
        if all(is_sorted(tube) for tube in tubes):
            return path
        for i in range(len(tubes)):
            for j in range(len(tubes)):
                if i != j:
                    new_tubes = move_ball(list(map(list, tubes)), (i, j))
                    new_state = tuple(map(tuple, new_tubes))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_tubes, path + [(i, j)]))

initial_tubes = [['Blue', 'Red', 'Red', 'Green', 'Blue', 'Green'], 
                 ['Blue', 'Red', 'Red', 'Red', 'Green', 'Green'], 
                 ['Blue', 'Red', 'Blue', 'Blue', 'Green', 'Green']]

print(shortest_path(initial_tubes))
