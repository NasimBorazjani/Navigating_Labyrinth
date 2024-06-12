
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

def shortest_path(tubes):
    queue = deque([([], tubes)])
    visited = set(str(tubes))
    while queue:
        path, tubes = queue.popleft()
        if is_sorted(tubes):
            return path
        for i in range(len(tubes)):
            for j in range(len(tubes)):
                if i != j and tubes[i] and len(tubes[j]) < 8:
                    new_tubes = move(list(map(list, tubes)), (i, j))
                    new_state = str(new_tubes)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((path + [(i, j)], new_tubes))

initial_tubes = [['Blue', 'Green', 'Green', 'Blue', 'Green'], 
                 ['Red', 'Blue', 'Green', 'Blue', 'Green'], 
                 ['Red', 'Blue', 'Red', 'Red', 'Red']]

print(shortest_path(initial_tubes))
