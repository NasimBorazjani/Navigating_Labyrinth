
from collections import deque

def pour_water(jugs, target):
    visited = set()
    queue = deque([(0, [0, 0, 0, 0])])  # (cost, state)

    while queue:
        cost, state = queue.popleft()

        if state == target:
            return cost

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        for i in range(len(jugs)):
            for j in range(len(jugs)):
                if i != j:
                    new_state = state[:]
                    pour_amount = min(new_state[i], jugs[j] - new_state[j])
                    new_state[i] -= pour_amount
                    new_state[j] += pour_amount
                    queue.append((cost + 1, new_state))

    return -1

jugs = [128, 67, 44, 31, 127, 15]
targets = [258, 261, 415, 430]
actions = []

for i in range(len(targets)):
    target = [0, 0, 0, 0]
    target[-1] = targets[i]
    for j in range(len(jugs)):
        if pour_water(jugs, target) != -1:
            actions.append(pour_water(jugs, target))
            break

print(actions)
