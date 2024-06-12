
from collections import deque

def bfs(capacities, targets):
    initial_state = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    queue = deque([(initial_state, None)])
    parents = {initial_state: None}
    while queue:
        state, action = queue.popleft()
        if state == tuple(targets):
            return retrieve_solution(parents, action)
        for i in range(len(state)):
            for j in range(len(capacities)):
                for sign in [-1, 1]:
                    new_state = list(state)
                    new_state[i] += sign * capacities[j]
                    if 0 <= new_state[i] <= targets[i] and new_state not in parents:
                        queue.append((tuple(new_state), action))
                        parents[tuple(new_state)] = (state, (sign, capacities[j], i+1))
    return None

def retrieve_solution(parents, action):
    solution = []
    while action is not None:
        solution.append(action[2])
        action = parents[action[0]]
    return solution[::-1]

capacities = [22, 98, 38, 116, 140, 115, 21, 80, 92]
targets = [279, 488, 578]

print(bfs(capacities, targets))
