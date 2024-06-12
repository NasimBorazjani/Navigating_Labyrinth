
from collections import deque

def move_ball(tubes, from_tube, to_tube):
    # Move the ball from the 'from_tube' to the 'to_tube'
    ball = tubes[from_tube].pop()
    tubes[to_tube].append(ball)
    return tubes

def is_sorted(tubes):
    # Check if the tubes are sorted
    for tube in tubes:
        if len(set(tube)) != 1:
            return False
    return True

def shortest_path(tubes):
    # BFS to find the shortest path
    queue = deque([(tubes, [])])
    visited = set()

    while queue:
        tubes, path = queue.popleft()
        if is_sorted(tubes):
            return path

        for i in range(len(tubes)):
            for j in range(len(tubes)):
                if i != j and len(tubes[j]) < 9:
                    new_tubes = move_ball(list(map(list, tubes)), i, j)
                    new_state = tuple(map(tuple, new_tubes))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_tubes, path + [(i, j)]))

initial_tubes = [['Blue', 'Green', 'Red', 'Red', 'Blue', 'Green'], 
                 ['Blue', 'Red', 'Green', 'Green', 'Green', 'Red'], 
                 ['Blue', 'Blue', 'Blue', 'Red', 'Red', 'Green']]

print(shortest_path(initial_tubes))
