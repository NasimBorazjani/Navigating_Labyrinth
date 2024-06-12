
from collections import deque

def bfs(capacities, targets):
    initial_state = ([0]*4, [0]*7, capacities)
    queue = deque([([0]*4, [0]*7, capacities, [], 0)])
    while queue:
        (buckets, jugs, capacities, actions, num_actions) = queue.popleft()
        if buckets == targets:
            return actions
        for i in range(4):
            for j in range(7):
                for action in [('+', j, i), ('-', j, i)]:
                    new_buckets = list(buckets)
                    new_jugs = list(jugs)
                    new_actions = list(actions)
                    if action[0] == '+':
                        if new_jugs[j] > 0 and new_buckets[i] < targets[i]:
                            amount = min(capacities[j] - new_jugs[j], targets[i] - new_buckets[i])
                            new_jugs[j] += amount
                            new_buckets[i] += amount
                            new_actions.append(action)
                    else:
                        if new_buckets[i] > 0 and new_jugs[j] < capacities[j]:
                            amount = min(new_buckets[i], capacities[j] - new_jugs[j])
                            new_jugs[j] += amount
                            new_buckets[i] -= amount
                            new_actions.append(action)
                    queue.append((new_buckets, new_jugs, capacities, new_actions, num_actions + 1))

capacities = [82, 91, 135, 11, 12, 19, 143, 60]
targets = [231, 288, 342, 410]
actions = bfs(capacities, targets)
print(actions)
