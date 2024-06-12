
from collections import deque
from copy import deepcopy

def is_valid_move(state, from_stack, to_stack):
    if not state[from_stack] or (state[to_stack] and state[from_stack][-1] != state[to_stack][-1]):
        return False
    return True

def generate_moves(state):
    moves = []
    for from_stack in range(8):
        for to_stack in range(8):
            if from_stack != to_stack and is_valid_move(state, from_stack, to_stack):
                new_state = deepcopy(state)
                new_state[to_stack].append(new_state[from_stack].pop())
                moves.append((new_state, (from_stack, to_stack)))
    return moves

def is_goal_state(state):
    for stack in state:
        if stack and len(set(stack)) > 1:
            return False
    return True

def bfs(initial_state):
    queue = deque([(initial_state, [], 0)])
    visited = set()
    while queue:
        state, path, cost = queue.popleft()
        if str(state) in visited:
            continue
        visited.add(str(state))
        if is_goal_state(state):
            return path
        for new_state, move in generate_moves(state):
            new_cost = cost + {0: 4, 1: 4, 2: 7, 3: 1, 4: 8, 5: 8, 6: 8, 7: 4}[move[1]]
            queue.append((new_state, path + [move], new_cost))
    return []

initial_state = [['Blue', 'Yellow', 'Yellow', 'Green', 'Black'], [], [], [], ['Blue', 'Red', 'Black', 'Yellow', 'Green'], ['Black', 'Red', 'Green', 'Blue', 'Red'], ['Green', 'Yellow', 'Black', 'Red', 'Blue'], []]
print(bfs(initial_state))
