
import heapq

# Define the initial state of the stacks
initial_state = [[], ['Blue', 'Black', 'Blue', 'Yellow', 'Red'], ['Red', 'Green', 'Black', 'Green', 'Black'], [], ['Red', 'Red', 'Green', 'Yellow', 'Yellow'], [], [], ['Blue', 'Yellow', 'Green', 'Black', 'Blue']]

# Define the cost of moving one block to the top of each stack
cost = {0: 3, 1: 2, 2: 1, 3: 7, 4: 5, 5: 5, 6: 6, 7: 4}

# Define a function to calculate the heuristic cost
def heuristic(state):
    # Count the number of blocks that are not correctly sorted
    count = 0
    for stack in state:
        if stack:
            shade = stack[0]
            count += sum(1 for block in stack if block != shade)
    return count

# Define a function to generate the possible next states
def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][0] == state[i][0]):
                    new_state = [stack.copy() for stack in state]
                    block = new_state[i].pop(0)
                    new_state[j].insert(0, block)
                    next_states.append((new_state, cost[i]))
    return next_states

# Define the A* search algorithm
def astar_search(initial_state):
    heap = [(heuristic(initial_state), 0, initial_state, [])]
    while heap:
        _, cost_so_far, state, path = heapq.heappop(heap)
        if heuristic(state) == 0:
            return path
        for next_state, move_cost in generate_next_states(state):
            new_cost = cost_so_far + move_cost
            new_path = path + [(state.index(next_state) - 1, state.index(state) - 1)]
            heapq.heappush(heap, (new_cost + heuristic(next_state), new_cost, next_state, new_path))

# Find the optimal sequence of moves
optimal_path = astar_search(initial_state)

# Print the list of transfer pairs
print(optimal_path)
