
import heapq

# Define the initial state of the stacks
initial_state = [['Black', 'Green', 'Red', 'Yellow', 'Black'], [], ['Blue', 'Red', 'Black', 'Black', 'Yellow'], ['Green', 'Red', 'Yellow', 'Blue', 'Green'], [], [], ['Green', 'Blue', 'Red', 'Yellow', 'Blue'], []]

# Define the cost of moving a block to each stack
cost = {0: 4, 1: 4, 2: 1, 3: 9, 4: 7, 5: 8, 6: 9, 7: 7}

# Define a heuristic function to estimate the cost of reaching the goal state
def heuristic(state):
    total_cost = 0
    for stack in state:
        if stack:
            shade = stack[0]
            cost_to_move = min([cost[i] for i in range(8) if i != state.index(stack) and (not state[i] or state[i][0] == shade)])
            total_cost += cost_to_move
    return total_cost

# Define a function to generate possible next states
def generate_next_states(state):
    next_states = []
    for i in range(8):
        for j in range(8):
            if i != j and state[i]:
                new_state = [stack.copy() for stack in state]
                block = new_state[i].pop(0)
                if not new_state[j] or new_state[j][0] == block:
                    new_state[j].insert(0, block)
                    next_states.append((new_state, cost[i]))
    return next_states

# Implement the A* search algorithm
def astar_search(initial_state):
    frontier = [(initial_state, 0, heuristic(initial_state), [])]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        current_state, current_cost, current_heuristic, path = heapq.heappop(frontier)

        if current_state == [[], [], [], [], ['Black', 'Black', 'Green', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Red', 'Yellow'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Black', 'Black', 'Green', 'Green', 'Red']]:
            return path

        explored.add(tuple(map(tuple, current_state)))

        for next_state, cost_to_move in generate_next_states(current_state):
            new_cost = current_cost + cost_to_move
            new_heuristic = heuristic(next_state)
            new_path = path + [(current_state.index(next_state), current_state.index(next_state))]

            if tuple(map(tuple, next_state)) not in explored:
                heapq.heappush(frontier, (next_state, new_cost, new_heuristic, new_path))

    return None

# Find the optimal sequence of moves
optimal_path = astar_search(initial_state)
print(optimal_path)
