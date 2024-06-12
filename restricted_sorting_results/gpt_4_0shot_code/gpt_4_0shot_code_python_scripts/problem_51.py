
from collections import deque

def bfs(initial_state, goal_state, costs):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        for next_state, move in get_neighbors(state, costs):
            if next_state not in visited:
                queue.append((next_state, path + [move]))
                visited.add(next_state)
    return None

def get_neighbors(state, costs):
    neighbors = []
    for i, stack in enumerate(state):
        if stack:
            block = stack[-1]
            for j, next_stack in enumerate(state):
                if i != j and (not next_stack or next_stack[-1] == block) and len(next_stack) < 5:
                    next_state = state[:]
                    next_state[i] = stack[:-1]
                    next_state[j] = next_stack + [block]
                    move = (i, j)
                    cost = costs[j]
                    neighbors.append((next_state, move))
    return neighbors

initial_state = [[], [], [], ['Green', 'Blue', 'Blue', 'Green', 'Black'], ['Red', 'Green', 'Blue', 'Blue', 'Red'], ['Black', 'Black', 'Yellow', 'Red', 'Yellow'], [], ['Yellow', 'Black', 'Green', 'Red', 'Yellow']]
goal_state = [['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Black', 'Black', 'Black', 'Black'], ['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], []]
costs = {0: 7, 1: 8, 2: 2, 3: 8, 4: 9, 5: 6, 6: 8, 7: 1}

print(bfs(initial_state, goal_state, costs))
