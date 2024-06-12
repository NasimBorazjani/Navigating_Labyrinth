
from collections import deque

def bfs(initial_state, goal_state, costs):
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        for next_state, cost in get_neighbors(state, costs):
            if next_state not in visited:
                queue.append((next_state, path + [cost]))
                visited.add(next_state)
    return []

def get_neighbors(state, costs):
    neighbors = []
    for i, stack in enumerate(state):
        if stack:
            for j, next_stack in enumerate(state):
                if i != j and (not next_stack or next_stack[-1] == stack[-1]) and len(next_stack) < 4:
                    next_state = state[:]
                    next_state[i] = stack[:-1]
                    next_state[j] = next_stack + [stack[-1]]
                    neighbors.append((next_state, (i, j, costs[j])))
    return neighbors

def solve(stacks):
    initial_state = [list(reversed(stack)) for stack in stacks]
    goal_state = [['Green', 'Green', 'Green'], [], ['Blue', 'Blue', 'Blue'], [], ['Red', 'Red', 'Red'], []]
    costs = {0: 3, 1: 6, 2: 5, 3: 5, 4: 3, 5: 1}
    path = bfs(initial_state, goal_state, costs)
    return [(i, j) for i, j, cost in path]

stacks = [['Green', 'Yellow', 'Red', 'Yellow'], [], ['Blue', 'Blue', 'Blue', 'Red'], [], ['Green', 'Green', 'Red', 'Yellow'], []]
print(solve(stacks))
