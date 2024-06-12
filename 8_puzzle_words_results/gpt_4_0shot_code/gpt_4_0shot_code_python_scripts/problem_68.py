
from collections import deque

def generate_states(state):
    i, j = [(i, j) for i in range(len(state)) for j in range(len(state[0])) if state[i][j] == '_'][0]
    directions = [(i-1, j+1), (i+1, j+1), (i-1, j-1), (i+1, j-1)]
    states = []
    for x, y in directions:
        if 0 <= x < len(state) and 0 <= y < len(state[0]):
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
            states.append(new_state)
    return states

def is_goal(state, goal):
    return state == goal

def bfs(start, goal):
    queue = deque([(start, [])])
    seen = set([str(start)])
    while queue:
        state, path = queue.popleft()
        if is_goal(state, goal):
            return path
        for new_state in generate_states(state):
            if str(new_state) not in seen:
                queue.append((new_state, path + [new_state]))
                seen.add(str(new_state))

start = [['e', 's', '_', 't'], ['l', 'o', 'e', 'm'], ['c', 'a', 'o', 'k'], ['p', 'p', 'g', 'e'], ['d', 'r', 'a', 'w']]
goal = [['_', 's', 'a', 't'], ['l', 'e', 'e', 'p'], ['m', 'a', 'c', 'k'], ['p', 'o', 'g', 'o'], ['d', 'r', 'e', 'w']]
print(bfs(start, goal))
