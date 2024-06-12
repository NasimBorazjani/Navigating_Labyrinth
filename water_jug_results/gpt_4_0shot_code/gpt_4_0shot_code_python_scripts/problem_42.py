
from collections import deque

def solve(jugs, goals):
    def get_state(buckets):
        return tuple(sorted(buckets))

    def get_actions(buckets):
        actions = []
        for i, bucket in enumerate(buckets):
            for j, jug in enumerate(jugs):
                if bucket + jug <= goals[i]:
                    new_buckets = list(buckets)
                    new_buckets[i] += jug
                    actions.append(('+', j+1, i+1, get_state(new_buckets)))
                if bucket >= jug:
                    new_buckets = list(buckets)
                    new_buckets[i] -= jug
                    actions.append(('-', j+1, i+1, get_state(new_buckets)))
        return actions

    start = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set([start])
    while queue:
        buckets, path = queue.popleft()
        for action in get_actions(buckets):
            if action[3] not in visited:
                if action[3] == goals:
                    return path + [action[:3]]
                queue.append((action[3], path + [action[:3]]))
                visited.add(action[3])
    return None

jugs = [36, 72, 16, 80, 45, 67, 38, 32, 149, 37]
goals = (201, 202, 233)
print(solve(jugs, goals))
