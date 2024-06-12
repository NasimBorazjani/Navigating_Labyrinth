
from collections import deque

def bfs(capacities, targets):
    initial_state = (0, 0, 0, 0) + tuple(capacities)
    queue = deque([(initial_state, None)])
    parents = {initial_state: None}
    while queue:
        state, action = queue.popleft()
        if state[4:] == targets:
            return retrieve_solution(parents, action)
        for i in range(4):
            for j in range(4, 7):
                for amount in [0, state[i], state[j]]:
                    if amount == state[i] or amount == state[j]:
                        continue
                    if state[i] + amount <= targets[i]:
                        new_state = list(state)
                        new_state[i] += amount
                        new_state[j] -= amount
                        new_state = tuple(new_state)
                        if new_state not in parents:
                            queue.append((new_state, (amount, i+1, j+1)))
                            parents[new_state] = action
    return None

def retrieve_solution(parents, action):
    solution = []
    while action is not None:
        solution.append(action)
        action = parents[tuple(solution[-1])]
    return solution[::-1]

capacities = [91, 141, 56, 65, 89, 40, 39, 92]
targets = [294, 375, 459, 466]

solution = bfs(capacities, targets)
print(solution)
