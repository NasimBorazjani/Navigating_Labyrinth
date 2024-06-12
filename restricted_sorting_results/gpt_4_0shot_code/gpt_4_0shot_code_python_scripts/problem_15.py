
from collections import deque
from copy import deepcopy

def bfs(start):
    queue = deque([(start, [], 0)])
    visited = set([tuple(map(tuple, start))])
    while queue:
        state, moves, cost = queue.popleft()
        if is_goal(state):
            return moves
        for next_state, move, next_cost in get_next_states(state, cost):
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, moves + [move], next_cost))
                visited.add(tuple(map(tuple, next_state)))
    return []

def is_goal(state):
    for stack in state:
        if len(set(stack)) > 1:
            return False
    return True

def get_next_states(state, cost):
    next_states = []
    for i in range(6):
        if state[i]:
            for j in range(6):
                if i != j and (not state[j] or state[j][-1] == state[i][-1]) and len(state[j]) < 4:
                    next_state = deepcopy(state)
                    next_state[j].append(next_state[i].pop())
                    next_states.append((next_state, (i, j), cost + costs[j]))
    return next_states

costs = {0: 4, 1: 5, 2: 5, 3: 2, 4: 5, 5: 2}
start = [[], [], [], ['Red', 'Green', 'Green', 'Red'], ['Yellow', 'Blue', 'Yellow', 'Blue'], ['Yellow', 'Green', 'Red', 'Blue']]
print(bfs(start))
