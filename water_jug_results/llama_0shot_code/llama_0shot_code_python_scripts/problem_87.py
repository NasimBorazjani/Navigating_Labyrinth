
from collections import deque

def bfs(jugs, buckets, goal):
    # Initial state
    start = (0, 0, 0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (a, b, c, d), actions = queue.popleft()
        state = (a, b, c, d)

        # If this state is the goal state, return the actions to reach it
        if state == goal:
            return actions

        # If this state has been visited before, skip it
        if state in visited:
            continue
        visited.add(state)

        # Try to fill each bucket from the available jugs
        for i, (jug, capacity) in enumerate(jugs):
            if a >= capacity:
                queue.append(((a - capacity, b, c, d), actions + [('+', i+1, 1)]))
            if b >= capacity:
                queue.append(((a, b - capacity, c, d), actions + [('+', i+1, 2)]))
            if c >= capacity:
                queue.append(((a, b, c - capacity, d), actions + [('+', i+1, 3)]))
            if d >= capacity:
                queue.append(((a, b, c, d - capacity), actions + [('+', i+1, 4)]))

            # Try to empty each bucket to the available jugs
            if a < capacity:
                queue.append(((a + min(capacity - a, b), b - min(capacity - a, b), c, d), actions + [('-', i+1, 1)]))
            if b < capacity:
                queue.append(((a, b + min(capacity - b, c), c - min(capacity - b, c), d), actions + [('-', i+1, 2)]))
            if c < capacity:
                queue.append(((a, b, c + min(capacity - c, d), d - min(capacity - c, d)), actions + [('-', i+1, 3)]))
            if d < capacity:
                queue.append(((a, b, c, d + min(capacity - d, a)), actions + [('-', i+1, 4)]))

    # If there is no solution, return an empty list
    return []

# Test the function
jugs = [(36, 0), (95, 1), (47, 2), (149, 3), (58, 4), (96, 5), (81, 6), (148, 7)]
buckets = [252, 307, 412, 431]
goal = (252, 307, 412, 431)

actions = bfs(jugs, buckets, goal)
print(actions)
