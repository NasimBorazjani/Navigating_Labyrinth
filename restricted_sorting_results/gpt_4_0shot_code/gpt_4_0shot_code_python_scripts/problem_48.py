
from collections import deque
from itertools import combinations

def bfs(start):
    queue = deque([(start, [])])
    visited = set([start])
    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path
        for next_state, action in get_actions(state):
            if next_state not in visited:
                queue.append((next_state, path + [action]))
                visited.add(next_state)

def is_goal(state):
    for stack in state:
        if len(set(stack)) > 1:
            return False
    return True

def get_actions(state):
    actions = []
    for i, j in combinations(range(8), 2):
        if state[i] and (not state[j] or state[i][-1] == state[j][-1]):
            next_state = state[:]
            next_state[i] = state[i][:-1]
            next_state[j] = state[j] + [state[i][-1]]
            actions.append((next_state, (i, j)))
    return actions

start = [[], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], ['Green', 'Red', 'Black', 'Yellow', 'Blue'], ['Red', 'Green', 'Red', 'Black', 'Yellow']]
print(bfs(start))
