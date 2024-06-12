
from collections import deque
from copy import deepcopy

def is_goal_state(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

def get_possible_moves(stacks):
    moves = []
    for i in range(6):
        if stacks[i]:
            for j in range(6):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]):
                    moves.append((i, j))
    return moves

def bfs(stacks, costs):
    queue = deque([(stacks, [], 0)])
    visited = set()
    while queue:
        state, path, cost = queue.popleft()
        if str(state) in visited:
            continue
        visited.add(str(state))
        if is_goal_state(state):
            return path
        for move in get_possible_moves(state):
            new_state = deepcopy(state)
            block = new_state[move[0]].pop()
            new_state[move[1]].append(block)
            new_path = path + [move]
            new_cost = cost + costs[move[1]]
            queue.append((new_state, new_path, new_cost))
    return []

stacks = [['Yellow', 'Yellow', 'Red', 'Red'], [], ['Blue', 'Yellow', 'Red', 'Green'], [], ['Green', 'Blue', 'Green', 'Blue'], []]
costs = {0: 7, 1: 1, 2: 4, 3: 7, 4: 4, 5: 4}
print(bfs(stacks, costs))
