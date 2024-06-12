
from collections import deque
from copy import deepcopy

def bfs(start):
    queue = deque([(start, [])])
    visited = set([str(start)])
    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path
        for next_state, action in get_actions(state):
            if str(next_state) not in visited:
                queue.append((next_state, path + [action]))
                visited.add(str(next_state))

def is_goal(state):
    for stack in state:
        if len(set(stack)) > 1:
            return False
    return True

def get_actions(state):
    actions = []
    for i, stack in enumerate(state):
        if stack:
            block = stack[-1]
            for j, target in enumerate(state):
                if i != j and (not target or target[-1] == block):
                    next_state = deepcopy(state)
                    next_state[i] = next_state[i][:-1]
                    next_state[j] = next_state[j] + [block]
                    actions.append((next_state, (i, j)))
    return actions

start = [[], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], ['Green', 'Red', 'Black', 'Yellow', 'Blue'], ['Red', 'Green', 'Red', 'Black', 'Yellow']]
print(bfs(start))
