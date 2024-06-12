
from collections import deque

def bfs(start, target):
    queue = deque([start])
    visited = set([start])
    parent = {start: (None, None)}
    while queue:
        state = queue.popleft()
        if state == target:
            path = []
            while state != start:
                state, action = parent[state]
                path.append(action)
            path.reverse()
            return path
        blank = state.index('_')
        for action in ['up-right', 'down-right', 'up-left', 'down-left']:
            new_state = swap(state, blank, action)
            if new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
                parent[new_state] = (state, action)
    return None

def swap(state, blank, action):
    new_state = list(state)
    if action == 'up-right':
        new_state[blank], new_state[blank-1] = new_state[blank-1], new_state[blank]
    elif action == 'down-right':
        new_state[blank], new_state[blank+1] = new_state[blank+1], new_state[blank]
    elif action == 'up-left':
        new_state[blank], new_state[blank-1] = new_state[blank-1], new_state[blank]
    elif action == 'down-left':
        new_state[blank], new_state[blank+1] = new_state[blank+1], new_state[blank]
    return ''.join(new_state)

start = 'ocaaankhmrligthiotugtnrtacz_ythum'
target = 'chankhormictigtagtornalzythum'
print(bfs(start, target))
