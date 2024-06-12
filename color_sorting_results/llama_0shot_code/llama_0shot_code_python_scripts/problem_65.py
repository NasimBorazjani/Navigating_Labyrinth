
from collections import deque

def move_ball(tubes, from_tube, to_tube):
    # Check if the target tube is full
    if len(tubes[to_tube]) == 8:
        return tubes

    # Move the ball
    ball = tubes[from_tube].pop()
    tubes[to_tube].append(ball)

    return tubes

def generate_next_states(tubes):
    next_states = []

    for i in range(len(tubes)):
        for j in range(len(tubes)):
            if i != j:
                new_tubes = move_ball(list(map(list, tubes)), i, j)
                next_states.append((new_tubes, (i, j)))

    return next_states

def bfs(initial_tubes):
    queue = deque([(initial_tubes, [])])
    visited = set()

    while queue:
        tubes, path = queue.popleft()

        if tubes in visited:
            continue

        visited.add(tubes)

        if all(len(set(tube)) == 1 for tube in tubes):
            return path

        for next_tubes, move in generate_next_states(tubes):
            new_path = list(path)
            new_path.append(move)
            queue.append((next_tubes, new_path))

    return None

initial_tubes = [['Blue', 'Green', 'Blue', 'Red', 'Red'], ['Red', 'Red', 'Blue', 'Green', 'Blue'], ['Green', 'Green', 'Red', 'Blue', 'Green']]

print(bfs(initial_tubes))
