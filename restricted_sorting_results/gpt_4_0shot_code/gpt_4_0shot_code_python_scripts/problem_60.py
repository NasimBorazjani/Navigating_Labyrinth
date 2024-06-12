
from collections import deque

def bfs(initial_state, cost):
    queue = deque([(initial_state, [], 0)])
    visited = set()
    while queue:
        state, path, total_cost = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if is_goal(state):
            return path
        for next_state, move, move_cost in get_moves(state, cost):
            if next_state not in visited:
                queue.append((next_state, path + [move], total_cost + move_cost))

def is_goal(state):
    for stack in state:
        if len(set(stack)) > 1:
            return False
    return True

def get_moves(state, cost):
    moves = []
    for i, stack in enumerate(state):
        if stack:
            block = stack[-1]
            for j, next_stack in enumerate(state):
                if i != j and (not next_stack or next_stack[-1] == block):
                    next_state = state[:]
                    next_state[i] = stack[:-1]
                    next_state[j] = next_stack + [block]
                    moves.append((next_state, (i, j), cost[j]))
    return moves

initial_state = [['Yellow', 'Green', 'Green', 'Black', 'Black'], [], ['Yellow', 'Green', 'Black', 'Green', 'Red'], ['Red', 'Black', 'Blue', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Yellow', 'Blue', 'Red'], []]
cost = {0: 6, 1: 1, 2: 8, 3: 8, 4: 1, 5: 6, 6: 4, 7: 1}
print(bfs(initial_state, cost))
