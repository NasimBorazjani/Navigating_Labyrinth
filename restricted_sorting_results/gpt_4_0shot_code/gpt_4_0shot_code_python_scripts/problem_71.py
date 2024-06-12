
from collections import deque
from copy import deepcopy

def get_moves(state, costs):
    moves = []
    for i, stack in enumerate(state):
        if stack:
            block = stack[-1]
            for j, target in enumerate(state):
                if i != j and (not target or target[-1] == block) and len(target) < 6:
                    new_state = deepcopy(state)
                    new_state[i] = new_state[i][:-1]
                    new_state[j] = new_state[j] + [block]
                    moves.append((new_state, (i, j), costs[j]))
    return moves

def solve(initial_state, costs):
    queue = deque([(initial_state, [], 0)])
    visited = set()
    while queue:
        state, path, cost = queue.popleft()
        if str(state) in visited:
            continue
        visited.add(str(state))
        if all(len(set(stack)) <= 1 for stack in state if stack):
            return path
        for new_state, move, move_cost in get_moves(state, costs):
            queue.append((new_state, path + [move], cost + move_cost))
    return None

initial_state = [[], [], ['White', 'Yellow', 'Yellow', 'Green', 'Blue', 'Green'], ['Red', 'Yellow', 'White', 'Blue', 'Black', 'Black'], ['Black', 'Red', 'Blue', 'Black', 'Green', 'Green'], ['Green', 'Black', 'Yellow', 'Red', 'White', 'Red'], ['White', 'Blue', 'Red', 'Blue', 'White', 'Yellow'], [], [], []]
costs = {0: 4, 1: 1, 2: 1, 3: 9, 4: 2, 5: 9, 6: 1, 7: 9, 8: 6, 9: 4}
print(solve(initial_state, costs))
