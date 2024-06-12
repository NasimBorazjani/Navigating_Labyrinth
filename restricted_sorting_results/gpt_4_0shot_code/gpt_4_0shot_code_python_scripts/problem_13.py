
from collections import deque
from copy import deepcopy

# Define the cost of moving a block to each stack
costs = {0: 4, 1: 2, 2: 2, 3: 7, 4: 4, 5: 5}

# Define the initial state of the stacks
initial_state = [['Green', 'Red', 'Blue', 'Blue'], [], ['Yellow', 'Red', 'Green', 'Green'], [], [], ['Red', 'Yellow', 'Blue', 'Yellow']]

# Define the goal state
goal_state = [['Green', 'Green', 'Green'], ['Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue'], ['Yellow', 'Yellow', 'Yellow'], [], []]

# Define a function to check if a block can be moved from one stack to another
def can_move(state, from_stack, to_stack):
    if not state[from_stack]:
        return False
    if not state[to_stack]:
        return True
    if state[from_stack][-1] == state[to_stack][-1] and len(state[to_stack]) < 4:
        return True
    return False

# Define a function to move a block from one stack to another
def move(state, from_stack, to_stack):
    new_state = deepcopy(state)
    block = new_state[from_stack].pop()
    new_state[to_stack].append(block)
    return new_state

# Define a function to find the shortest path using BFS
def bfs():
    queue = deque([(initial_state, [], 0)])
    visited = set()
    while queue:
        state, path, cost = queue.popleft()
        if state == goal_state:
            return path
        for from_stack in range(6):
            for to_stack in range(6):
                if can_move(state, from_stack, to_stack):
                    new_state = move(state, from_stack, to_stack)
                    new_cost = cost + costs[to_stack]
                    new_path = path + [(from_stack, to_stack)]
                    if str(new_state) not in visited:
                        visited.add(str(new_state))
                        queue.append((new_state, new_path, new_cost))
    return []

# Print the shortest path
print(bfs())
