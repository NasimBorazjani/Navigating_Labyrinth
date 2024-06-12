
from collections import deque

jugs = [76, 63, 111, 59, 11, 108, 16, 66, 75, 67]
goal = (191, 269, 328)
actions = []
visited = set()

def is_valid(state):
    return state[0] <= state[1] <= state[2]

def bfs():
    queue = deque([(0, 0, 0)])
    while queue:
        state = queue.popleft()
        if state == goal:
            return backtrack(state)
        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= goal[j]:
                    new_state = list(state)
                    new_state[j] += jug
                    new_state = tuple(new_state)
                    if is_valid(new_state) and new_state not in visited:
                        queue.append(new_state)
                        visited.add(new_state)
                        actions.append(('+', i+1, j+1))
                if state[j] - jug >= 0:
                    new_state = list(state)
                    new_state[j] -= jug
                    new_state = tuple(new_state)
                    if is_valid(new_state) and new_state not in visited:
                        queue.append(new_state)
                        visited.add(new_state)
                        actions.append(('-', i+1, j+1))
    return []

def backtrack(state):
    sequence = []
    while state != (0, 0, 0):
        action = actions[visited.index(state)]
        sequence.append(action)
        if action[0] == '+':
            state = (state[0] - jugs[action[1]-1] if action[2] == 1 else state[0],
                     state[1] - jugs[action[1]-1] if action[2] == 2 else state[1],
                     state[2] - jugs[action[1]-1] if action[2] == 3 else state[2])
        else:
            state = (state[0] + jugs[action[1]-1] if action[2] == 1 else state[0],
                     state[1] + jugs[action[1]-1] if action[2] == 2 else state[1],
                     state[2] + jugs[action[1]-1] if action[2] == 3 else state[2])
    return sequence[::-1]

print(bfs())
