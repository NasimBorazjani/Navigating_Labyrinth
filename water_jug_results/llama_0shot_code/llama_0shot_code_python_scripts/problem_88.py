
from collections import deque

def bfs(jugs, buckets, goal):
    queue = deque([([0]*len(buckets), jugs)])
    seen = set()
    while queue:
        (state, jugs_left) = queue.popleft()
        if tuple(state) not in seen:
            seen.add(tuple(state))
            if state == goal:
                return construct_path(queue)
            for i in range(len(buckets)):
                for cap, amount in jugs_left.items():
                    if amount > 0:
                        new_state = list(state)
                        new_state[i] += min(amount, cap)
                        queue.append((new_state, {k: v-min(amount, cap) for k, v in jugs_left.items() if k != cap}))
                    if state[i] > 0:
                        new_state = list(state)
                        new_state[i] -= min(state[i], cap)
                        queue.append((new_state, {k: v+min(state[i], cap) for k, v in jugs_left.items() if k != cap}))
    return None

def construct_path(queue):
    path = []
    while queue:
        (state, action) = queue.pop()
        if state not in queue:
            path.append(action)
    return path[::-1]

jugs = {95: 0, 111: 0, 144: 0, 57: 0, 13: 0, 58: 0, 12: 0}
buckets = [0]*4
goal = [226, 271, 331, 394]

solution = bfs(jugs, buckets, goal)
print(solution)
