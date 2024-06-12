
import heapq

# Define the initial state of the stacks
initial_state = [['Yellow', 'Green', 'Green', 'Black', 'Black'], [], ['Yellow', 'Green', 'Black', 'Green', 'Red'], ['Red', 'Black', 'Blue', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Yellow', 'Blue', 'Red'], []]

# Define the cost of moving a block to each stack
cost = {0: 6, 1: 1, 2: 8, 3: 8, 4: 1, 5: 6, 6: 4, 7: 1}

# Define a function to calculate the cost of a state
def state_cost(state):
    total_cost = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            total_cost += cost[i]
    return total_cost

# Define a heuristic function to estimate the cost of reaching the goal state
def heuristic(state):
    misplaced_blocks = 0
    for stack in state:
        if stack:
            shade = stack[0]
            for block in stack:
                if block != shade:
                    misplaced_blocks += 1
    return misplaced_blocks

# Define a function to generate possible next states
def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][0] == state[i][0]):
                    new_state = [stack.copy() for stack in state]
                    new_state[j].insert(0, new_state[i].pop(0))
                    next_states.append(new_state)
    return next_states

# Implement the A* search algorithm
def astar_search(initial_state):
    open_list = [(state_cost(initial_state) + heuristic(initial_state), initial_state)]
    closed_list = set()

    while open_list:
        current_cost, current_state = heapq.heappop(open_list)

        if current_state == [[], [], [], [], ['Black', 'Black', 'Green', 'Green', 'Yellow'], ['Blue', 'Blue', 'Red', 'Red', 'Yellow'], ['Blue', 'Red', 'Red', 'Yellow', 'Yellow'], ['Blue', 'Blue', 'Green', 'Green', 'Yellow']]:
            return current_state

        closed_list.add(tuple(map(tuple, current_state)))

        for next_state in generate_next_states(current_state):
            if tuple(map(tuple, next_state)) not in closed_list:
                next_cost = state_cost(next_state) + heuristic(next_state)
                heapq.heappush(open_list, (next_cost, next_state))

# Find the optimal sequence of moves
optimal_state = astar_search(initial_state)

# Print the list of transfer pairs with the least possible cost
for i in range(len(initial_state)):
    if initial_state[i] != optimal_state[i]:
        print((i, optimal_state.index(initial_state[i])))
