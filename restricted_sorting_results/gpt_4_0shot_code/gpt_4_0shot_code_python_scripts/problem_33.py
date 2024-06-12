
from collections import deque

def bfs(initial_state, goal_state, costs):
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        for next_state, move in get_moves(state, costs):
            if next_state not in visited:
                queue.append((next_state, path + [move]))
                visited.add(next_state)
    return []

def get_moves(state, costs):
    moves = []
    for i, stack in enumerate(state):
        if stack:
            for j, next_stack in enumerate(state):
                if i != j and (not next_stack or next_stack[-1] == stack[-1]) and len(next_stack) < 5:
                    next_state = state[:]
                    next_state[i] = stack[:-1]
                    next_state[j] = next_stack + [stack[-1]]
                    moves.append((next_state, (i, j, costs[j])))
    return moves

initial_state = [['Black', 'Yellow', 'Green', 'Red', 'Black'], [], ['Red', 'Yellow', 'Green', 'Blue', 'Green'], [], ['Blue', 'Red', 'Blue', 'Green', 'Yellow'], ['Red', 'Blue', 'Yellow', 'Black', 'Black'], [], []]
goal_state = [['Black', 'Black', 'Black', 'Black'], [], ['Red', 'Red', 'Red', 'Red'], [], ['Blue', 'Blue', 'Blue', 'Blue'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Green', 'Green', 'Green', 'Green'], []]
costs = {0: 1, 1: 6, 2: 6, 3: 2, 4: 9, 5: 2, 6: 9, 7: 6}

print(bfs(initial_state, goal_state, costs))
