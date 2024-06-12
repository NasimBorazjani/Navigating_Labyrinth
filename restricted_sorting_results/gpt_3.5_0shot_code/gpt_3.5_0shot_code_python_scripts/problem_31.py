
import heapq

# Define the initial state of the stacks
initial_state = [[], [], ['Yellow', 'Yellow', 'Green', 'Black', 'Red'], ['Black', 'Green', 'Black', 'Blue', 'Yellow'], ['Green', 'Blue', 'Yellow', 'Red', 'Blue'], [], [], ['Black', 'Red', 'Green', 'Red', 'Blue']]

# Define the cost of moving one block to the top of each stack
cost = {0: 7, 1: 2, 2: 1, 3: 1, 4: 9, 5: 4, 6: 2, 7: 7}

# Define the heuristic function
def heuristic(state):
    # Calculate the total cost of moving blocks to the correct stacks
    total_cost = 0
    for i, stack in enumerate(state):
        if stack:
            correct_stack = [block for block in stack if block == stack[0]]
            total_cost += len(stack) - len(correct_stack)
    return total_cost

# Define the A* search algorithm
def astar(initial_state):
    heap = [(heuristic(initial_state), 0, initial_state, [])]
    while heap:
        _, cost_so_far, state, path = heapq.heappop(heap)
        if all(not stack or len(set(stack)) == 1 for stack in state):
            return path
        for i in range(len(state)):
            for j in range(len(state)):
                if i != j and state[i] and (not state[j] or state[i][0] == state[j][0]):
                    new_state = [stack.copy() for stack in state]
                    new_state[j].insert(0, new_state[i].pop(0))
                    new_cost = cost_so_far + cost[i]
                    new_path = path + [(i, j)]
                    heapq.heappush(heap, (new_cost + heuristic(new_state), new_cost, new_state, new_path))

# Find the optimal sequence of moves
optimal_path = astar(initial_state)
print(optimal_path)
