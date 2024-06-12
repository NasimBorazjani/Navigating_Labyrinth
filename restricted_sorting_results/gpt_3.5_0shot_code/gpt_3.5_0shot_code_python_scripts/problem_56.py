
import heapq

# Define the initial state of the stacks
initial_state = [[], ['Yellow', 'Red', 'Black', 'Yellow', 'Green'], [], [], ['Green', 'Red', 'Blue', 'Blue', 'Black'], ['Green', 'Blue', 'Yellow', 'Red', 'Yellow'], [], ['Blue', 'Green', 'Black', 'Red', 'Black']]

# Define the cost of moving one block to the top of each stack
cost = {0: 5, 1: 5, 2: 5, 3: 6, 4: 5, 5: 5, 6: 9, 7: 6}

# Define a function to calculate the heuristic cost
def heuristic(state):
    # Count the number of blocks that are not in the correct position
    count = 0
    for stack in state:
        for i in range(len(stack)):
            if stack[i] != stack[-1]:
                count += 1
    return count

# Define a function to generate the next possible states
def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][-1] == state[i][-1]):
                    new_state = [stack.copy() for stack in state]
                    new_state[j].append(new_state[i].pop())
                    next_states.append((new_state, cost[i] + cost[j]))
    return next_states

# Define the A* search algorithm
def astar(initial_state):
    heap = [(heuristic(initial_state), 0, initial_state, [])]
    while heap:
        _, cost_so_far, state, path = heapq.heappop(heap)
        if heuristic(state) == 0:
            return path
        for next_state, next_cost in generate_next_states(state):
            new_cost = cost_so_far + next_cost
            new_heuristic = new_cost + heuristic(next_state)
            heapq.heappush(heap, (new_heuristic, new_cost, next_state, path + [(state.index(next_state[-1]), state.index(next_state)]))

# Find the optimal sequence of moves
optimal_path = astar(initial_state)

# Print the list of transfer pairs with the least possible cost
print(optimal_path)
