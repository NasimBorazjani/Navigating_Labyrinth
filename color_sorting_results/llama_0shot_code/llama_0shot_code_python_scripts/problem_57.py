
from collections import deque

def move(tubes, source, target):
    new_tubes = [tube.copy() for tube in tubes]
    ball = new_tubes[source].pop()
    new_tubes[target].append(ball)
    return new_tubes

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
        for i in range(len(tubes)):
            for j in range(len(tubes)):
                if i != j and len(tubes[j]) < 8:
                    new_tubes = move(tubes, i, j)
                    new_state = tuple(tuple(tube) for tube in new_tubes)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((path + [(i, j)], new_tubes))

initial_tubes = [['Red', 'Green', 'Blue', 'Green', 'Green'], 
                 ['Green', 'Red', 'Blue', 'Blue', 'Blue'], 
                 ['Red', 'Red', 'Blue', 'Green', 'Red']]

print(shortest_path(initial_tubes))
