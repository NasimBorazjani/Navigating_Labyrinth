
import heapq

# Define the initial state of the stacks
initial_state = [[], ['Blue', 'Pink', 'Red', 'Red', 'Yellow', 'White', 'Green'], [], [], ['White', 'Black', 'Blue', 'Yellow', 'Yellow', 'Pink', 'White'], ['Green', 'Pink', 'White', 'Blue', 'Pink', 'Red', 'Pink'], ['Black', 'Green', 'Yellow', 'White', 'Yellow', 'Red', 'Blue'], [], ['Red', 'White', 'Black', 'Blue', 'Black', 'Yellow', 'Green'], [], ['Green', 'Black', 'Pink', 'Black', 'Red', 'Green', 'Blue'], []]

# Define the cost of moving one block to the top of each stack
cost = {0: 2, 1: 7, 2: 5, 3: 11, 4: 6, 5: 13, 6: 12, 7: 7, 8: 8, 9: 6, 10: 7, 11: 7}

# Define a function to calculate the heuristic cost (h-value) for a given state
def heuristic(state):
    h = 0
    for stack in state:
        if len(stack) > 0:
            h += len(set(stack)) - 1
    return h

# Define a function to generate the possible next states from a given state
def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        if len(state[i]) > 0:
            for j in range(len(state)):
                if i != j and (len(state[j]) == 0 or state[j][-1] == state[i][-1]):
                    new_state = [stack.copy() for stack in state]
                    new_state[j].append(new_state[i].pop())
                    next_states.append(new_state)
    return next_states

# Define the A* search algorithm
def astar_search(initial_state, cost):
    open_list = [(heuristic(initial_state), 0, initial_state, [])]
    closed_list = set()

    while open_list:
        _, g, current_state, path = heapq.heappop(open_list)

        if current_state == [[], [], [], [], [], [], [], [], [], [], [], []]:
            return path

        closed_list.add(tuple(tuple(stack) for stack in current_state))

        for next_state in generate_next_states(current_state):
            if tuple(tuple(stack) for stack in next_state) not in closed_list:
                new_g = g + cost[path[-1][1]] if path else 0
                new_path = path + [(current_state.index(stack), next_state.index(stack)) for stack in zip(current_state, next_state) if stack[0] != stack[1]]
                heapq.heappush(open_list, (new_g + heuristic(next_state), new_g, next_state, new_path))

    return None

# Find the optimal sequence of moves
optimal_path = astar_search(initial_state, cost)

# Print the optimal sequence of moves
print(optimal_path)
