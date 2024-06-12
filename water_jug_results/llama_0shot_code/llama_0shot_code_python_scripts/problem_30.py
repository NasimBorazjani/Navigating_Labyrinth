
from collections import deque

def bfs(initial_state, goal_state, jugs):
    queue = deque([([0, 0, 0], [])])
    visited = set([(0, 0, 0)])
    while queue:
        state, actions = queue.popleft()
        if state == goal_state:
            return actions
        for next_state, action in generate_next_states(state, jugs):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, actions + [action]))
    return None

def generate_next_states(state, jugs):
    next_states = []
    for i in range(3):
        for j in range(len(jugs)):
            if state[i] + jugs[j] <= 1000:  # limit for unlabeled buckets
                next_state = list(state)
                next_state[i] += jugs[j]
                action = ('+', jugs[j], i+1)
                next_states.append((tuple(next_state), action))
            if state[i] >= jugs[j]:  # can't remove more water than there is
                next_state = list(state)
                next_state[i] -= jugs[j]
                action = ('-', jugs[j], i+1)
                next_states.append((tuple(next_state), action))
    return next_states

initial_state = [0, 0, 0]
goal_state = [253, 280, 448]
jugs = [111, 84, 17, 22, 63, 75, 148, 64]

actions = bfs(initial_state, goal_state, jugs)
print(actions)
