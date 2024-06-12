
import heapq

# Define the initial state of the stacks
initial_state = [['Black', 'Black', 'Yellow', 'Blue', 'Black', 'Black', 'Green'], [], ['Blue', 'Yellow', 'Green', 'Black', 'White', 'White', 'Blue'], ['Red', 'White', 'Pink', 'White', 'Pink', 'Green', 'Pink'], ['Green', 'Blue', 'Black', 'Green', 'Red', 'Green', 'Yellow'], [], [], ['Red', 'White', 'Blue', 'Yellow', 'Blue', 'White', 'Red'], ['Yellow', 'Yellow', 'Red', 'Pink', 'Red', 'Pink', 'Pink'], [], [], []]

# Define the goal state
goal_state = [[], ['Black', 'Black', 'Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green', 'Green', 'Green'], ['Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink'], ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], []]

# Define the cost of moving a block to each stack
cost = {0: 10, 1: 7, 2: 7, 3: 7, 4: 9, 5: 3, 6: 8, 7: 5, 8: 4, 9: 10, 10: 7, 11: 7}

# Define a function to calculate the heuristic cost (h-value) for a given state
def heuristic_cost(state):
    h_cost = 0
    for i in range(len(state)):
        if state[i]:
            h_cost += len(set(state[i])) - 1
    return h_cost

# Define a function to generate the possible next states from a given state
def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][-1] == state[i][-1]):
                    new_state = [stack.copy() for stack in state]
                    new_state[j].append(new_state[i].pop())
                    next_states.append((new_state, i, j))
    return next_states

# Define the A* search algorithm
def astar_search(initial_state, goal_state, cost):
    open_list = [(heuristic_cost(initial_state), 0, initial_state, [])]
    closed_list = set()

    while open_list:
        _, g_cost, current_state, path = heapq.heappop(open_list)

        if current_state == goal_state:
            return path

        closed_list.add(tuple(tuple(stack) for stack in current_state))

        for next_state, i, j in generate_next_states(current_state):
            if tuple(tuple(stack) for stack in next_state) not in closed_list:
                new_g_cost = g_cost + cost[j]
                new_h_cost = heuristic_cost(next_state)
                heapq.heappush(open_list, (new_g_cost + new_h_cost, new_g_cost, next_state, path + [(i, j)]))

    return None

# Find the optimal solution
optimal_solution = astar_search(initial_state, goal_state, cost)
print(optimal_solution)
