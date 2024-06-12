
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

        for i, jug in enumerate(jugs):
            for j, other_jug in enumerate(jugs):
                if i != j:
                    new_state = state[:]
                    amount = min(jug, state[i] + state[j]) - state[i]
                    new_state[i] += amount
                    new_state[j] -= amount

                    if new_state[i] <= jug and new_state[j] >= 0:
                        queue.append((cost + 1, new_state))

    return -1

jugs = [141, 92, 12, 77, 49, 140]
targets = [304, 333, 349, 413]

actions = []

for i in range(len(targets)):
    target = [0, 0, 0, 0]
    target[i] = targets[i]
    cost = pour_water(jugs, target)

    if cost == -1:
        print("No solution found for target", i+1)
        break

    state = [0, 0, 0, 0]
    queue = deque([(0, [0, 0, 0, 0])])

    while state != target:
        cost, new_state = queue.popleft()

        for j, jug in enumerate(jugs):
            if new_state[j] < state[j]:
                actions.append(('-', jug, j+1))
            elif new_state[j] > state[j]:
                actions.append(('+', jug, j+1))

        state = new_state

        for j, jug in enumerate(jugs):
            for k, other_jug in enumerate(jugs):
                if j != k:
                    amount = min(jug, state[j] + state[k]) - state[j]
                    new_state = state[:]
                    new_state[j] += amount
                    new_state[k] -= amount

                    if new_state[j] <= jug and new_state[k] >= 0 and new_state != state:
                        queue.append((cost + 1, new_state))

print(actions)
