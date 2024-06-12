
from collections import deque
from copy import deepcopy

# Define the cost of moving a block to each stack
costs = {0: 6, 1: 5, 2: 2, 3: 3, 4: 3, 5: 6}

# Define the initial state of the stacks
initial_state = [['Green', 'Green', 'Blue', 'Green'], [], ['Yellow', 'Red', 'Red', 'Blue'], [], [], ['Yellow', 'Yellow', 'Blue', 'Red']]

def is_valid_move(state, src, dest):
    if not state[src]:
        return False
    if not state[dest] or state[dest][-1] == state[src][-1] and len(state[dest]) < 4:
        return True
    return False

def calculate_cost(src, dest):
    return costs[dest]

def generate_moves(state):
    moves = []
    for src in range(6):
        for dest in range(6):
            if src != dest and is_valid_move(state, src, dest):
                new_state = deepcopy(state)
                new_state[dest].append(new_state[src].pop())
                moves.append((new_state, (src, dest), calculate_cost(src, dest)))
    return moves

def is_goal_state(state):
    for stack in state:
        if stack and (len(stack) != 3 or len(set(stack)) != 1):
            return False
    return True

def bfs():
    queue = deque([(initial_state, [], 0)])
    while queue:
        state, path, cost = queue.popleft()
        if is_goal_state(state):
            return path
        for new_state, move, move_cost in generate_moves(state):
            queue.append((new_state, path + [move], cost + move_cost))

print(bfs())
