
from collections import deque

def bfs(capacities, targets):
    initial_state = (0, 0, 0)
    queue = deque([(initial_state, [])])
    while queue:
        (a, b, c), actions = queue.popleft()
        if a == targets[0] and b == targets[1] and c == targets[2]:
            return actions
        for i in range(3):
            for j in range(len(capacities)):
                if i == 0:
                    queue.append(((min(a + capacities[j], targets[0]), b, c), actions + [('+', capacities[j], i+1)]))
                else:
                    queue.append(((a, min(b + capacities[j], targets[i]), c), actions + [('+', capacities[j], i+1)]))
                if a >= capacities[j]:
                    queue.append(((max(a - capacities[j], 0), b, c), actions + [('-', capacities[j], i+1)]))
                if b >= capacities[j]:
                    queue.append(((a, max(b - capacities[j], 0), c), actions + [('-', capacities[j], i+1)]))
                if c >= capacities[j]:
                    queue.append(((a, b, max(c - capacities[j], 0)), actions + [('-', capacities[j], i+1)]))
    return None

capacities = [103, 109, 146, 101, 17, 145, 68]
targets = [448, 466, 509]
print(bfs(capacities, targets))
