
from collections import deque

def next_states(state, jugs):
    next_states = []
    for i, (jug, next_jug) in enumerate(zip(jugs, jugs[1:])):
        if state[i] < jug and state[i+1] + jug - state[i] >= next_jug:
            new_state = list(state)
            new_state[i] = jug
            new_state[i+1] -= jug - state[i]
            next_states.append((new_state, ('+', jug, i+1)))
        if state[i] > 0 and state[i] <= state[i+1]:
            new_state = list(state)
            new_state[i] = 0
            new_state[i+1] += state[i]
            next_states.append((new_state, ('-', jug, i+1)))
    return next_states

def shortest_path(initial_state, goal_state, jugs):
    queue = deque([(initial_state, [])])
    seen = set()
    while queue:
        state, actions = queue.popleft()
        if state not in seen:
            seen.add(state)
            if state == goal_state:
                return actions
            for next_state, action in next_states(state, jugs):
                queue.append((next_state, actions + [action]))

jugs = [139, 143, 17, 138, 133, 19, 126, 102, 65]
initial_state = [0, 0, 0]
goal_state = [349, 415, 458]

actions = shortest_path(initial_state, goal_state, jugs)
print(actions)
