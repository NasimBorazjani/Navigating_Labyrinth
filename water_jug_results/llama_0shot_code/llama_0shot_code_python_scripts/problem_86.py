
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
                if state[i] + capacities[j] <= targets[i]:
                    next_state = list(state)
                    next_state[i] += capacities[j]
                    next_state[j] -= capacities[j]
                    next_state = tuple(next_state)
                    if next_state not in parents:
                        queue.append((next_state, ('+', capacities[j], i+1)))
                        parents[next_state] = action
                if state[i] >= capacities[j]:
                    next_state = list(state)
                    next_state[i] -= capacities[j]
                    next_state[j] += capacities[j]
                    next_state = tuple(next_state)
                    if next_state not in parents:
                        queue.append((next_state, ('-', capacities[j], i+1)))
                        parents[next_state] = action

def retrieve_solution(parents, action):
    solution = []
    while action is not None:
        solution.append(action)
        action = parents[tuple(map(lambda x: x[0]-x[1], zip(action[2][2][:4], action[2][2][4:])))]
    return solution[::-1]

capacities = [87, 13, 27, 106, 18, 91, 17, 138]
targets = [205, 365, 391, 414]

print(bfs(capacities, targets))
