
from collections import deque

def bfs(start, target):
    queue = deque([start])
    visited = set([start])
    parent = {start: (None, None)}
    while queue:
        state = queue.popleft()
        if state == target:
            path = []
            while state:
                state, action = parent[state]
                if action:
                    path.append(action)
            return path[::-1]
        blank = state.index('_')
        for action in ['up-right', 'down-right', 'up-left', 'down-left']:
            new_state = swap(state, blank, action)
            if new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
                parent[new_state] = (state, action)
    return None

def swap(state, blank, action):
    new_state = state[:]
    if action == 'up-right':
        new_state[blank], new_state[blank-1] = new_state[blank-1], new_state[blank]
    elif action == 'down-right':
        new_state[blank], new_state[blank+1] = new_state[blank+1], new_state[blank]
    elif action == 'up-left':
        new_state[blank], new_state[blank-1] = new_state[blank-1], new_state[blank]
    elif action == 'down-left':
        new_state[blank], new_state[blank+1] = new_state[blank+1], new_state[blank]
    return new_state

start = ['m', 's', '_', 'n', 'g', 'a', 'o', 'i', 'e', 'h', 'h', 'i', 'p', 'e', 's', 'a', 'g', 'l', 'r', 'y']
target = ['_', 's', 'o', 'n', 'g', 'a', 'm', 'i', 's', 'h', 'h', 'i', 'p', 'e', 'r', 'a', 'g', 'l', 'e', 'y']
print(bfs(start, target))
