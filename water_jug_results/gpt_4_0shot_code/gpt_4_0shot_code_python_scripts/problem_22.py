
from collections import deque

jugs = [16, 124, 57, 40, 99, 45, 72, 98]
buckets = [263, 341, 360]
actions = [(i, j) for i in range(len(jugs)) for j in range(len(buckets))]

def bfs():
    start = (0, 0, 0)
    goal = tuple(buckets)
    visited = {start: None}
    queue = deque([start])

    while queue:
        state = queue.popleft()
        if state == goal:
            return path(visited, start, goal)
        for action in actions:
            new_state = apply_action(state, action)
            if new_state not in visited:
                visited[new_state] = (state, action)
                queue.append(new_state)
    return None

def apply_action(state, action):
    jug, bucket = action
    new_state = list(state)
    if new_state[bucket] + jugs[jug] <= buckets[bucket]:
        new_state[bucket] += jugs[jug]
        return tuple(new_state)
    else:
        return state

def path(visited, start, goal):
    current = goal
    result = []
    while current != start:
        state, action = visited[current]
        jug, bucket = action
        if state[bucket] < current[bucket]:
            result.append(('+', jugs[jug], bucket+1))
        else:
            result.append(('-', jugs[jug], bucket+1))
        current = state
    return result[::-1]

print(bfs())
