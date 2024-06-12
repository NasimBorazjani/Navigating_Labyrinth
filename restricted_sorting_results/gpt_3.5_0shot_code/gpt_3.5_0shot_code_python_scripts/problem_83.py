
import heapq

# Initial state of the stacks
stacks = [[], ['Black', 'Green', 'White', 'Pink', 'Yellow', 'Blue', 'Red'], [], ['Green', 'Red', 'Red', 'Red', 'White', 'Black', 'Black'], [], ['Blue', 'Blue', 'Pink', 'Yellow', 'Pink', 'Green', 'Red'], ['Blue', 'Black', 'White', 'Green', 'White', 'Yellow', 'Yellow'], ['White', 'Blue', 'Pink', 'Green', 'Yellow', 'Green', 'Pink'], [], ['Yellow', 'Black', 'White', 'Red', 'Blue', 'Black', 'Pink'], [], []]

# Cost dictionary for moving blocks
cost_dict = {0: 10, 1: 8, 2: 12, 3: 3, 4: 5, 5: 11, 6: 5, 7: 12, 8: 3, 9: 3, 10: 11, 11: 6}

# Define a state as a tuple of the current configuration of the stacks and the total cost
initial_state = (tuple(tuple(stack) for stack in stacks), 0)

# Priority queue to explore states with the lowest cost first
priority_queue = []
heapq.heappush(priority_queue, initial_state)

# Set to keep track of visited states
visited = set()

# Dictionary to keep track of the cost of reaching each state
cost_so_far = {initial_state[0]: 0}

# Dictionary to keep track of the parent state of each state
parent = {initial_state[0]: None}

# Function to calculate the cost of moving a block from one stack to another
def calculate_cost(from_stack, to_stack):
    return cost_dict[from_stack] if from_stack != to_stack else 1

# Function to get possible moves from a given state
def get_possible_moves(state):
    current_stacks, current_cost = state
    possible_moves = []
    for from_stack, stack in enumerate(current_stacks):
        if stack:
            for to_stack in range(len(current_stacks)):
                if from_stack != to_stack and (not current_stacks[to_stack] or current_stacks[to_stack][-1] == stack[-1]):
                    move_cost = calculate_cost(from_stack, to_stack)
                    new_cost = current_cost + move_cost
                    new_stacks = [list(s) for s in current_stacks]
                    new_stacks[to_stack].append(new_stacks[from_stack].pop())
                    new_state = (tuple(tuple(s) for s in new_stacks), new_cost)
                    possible_moves.append((new_state, move_cost))
    return possible_moves

# A* search algorithm
while priority_queue:
    current_state = heapq.heappop(priority_queue)
    current_stacks, current_cost = current_state

    if all(not stack for stack in current_stacks):
        break

    visited.add(current_stacks)

    for next_state, move_cost in get_possible_moves(current_state):
        next_stacks, next_cost = next_state
        if next_stacks not in visited and (next_stacks not in cost_so_far or next_cost < cost_so_far[next_stacks]):
            cost_so_far[next_stacks] = next_cost
            heapq.heappush(priority_queue, next_state)
            parent[next_stacks] = current_state

# Reconstruct the path
path = []
while current_stacks:
    parent_state = parent[current_stacks]
    if parent_state:
        for i, (stack1, stack2) in enumerate(zip(parent_state[0], current_stacks)):
            if stack1 != stack2:
                path.append((i, current_stacks.index(stack2)))
    current_stacks = parent_state[0]

# Print the list of transfer pairs with the least possible cost
print(path[::-1])
