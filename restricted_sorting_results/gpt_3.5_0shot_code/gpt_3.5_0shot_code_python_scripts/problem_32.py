
import heapq

# Define the initial state of the stacks
initial_state = [['Black', 'Yellow', 'Blue', 'Yellow', 'Red'], [], [], [], [], ['Blue', 'Green', 'Blue', 'Green', 'Blue'], ['Yellow', 'Black', 'Green', 'Yellow', 'Black'], ['Red', 'Red', 'Red', 'Green', 'Black']]

# Define the cost of moving one block to the top of each stack
cost = {0: 5, 1: 8, 2: 1, 3: 6, 4: 8, 5: 2, 6: 1, 7: 8}

# Define a heuristic function to estimate the cost of reaching the goal state
def heuristic(state):
    total_cost = 0
    for stack in state:
        if stack:
            shade = stack[0]
            cost_to_move = min([cost[i] for i in range(len(state)) if not state[i] or state[i][0] == shade])
            total_cost += cost_to_move
    return total_cost

# Define a function to generate the possible next states from a given state
def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][0] == state[i][0]) and len(state[j]) < 5:
                    new_state = [stack.copy() for stack in state]
                    new_state[j].insert(0, new_state[i].pop(0))
                    next_states.append((new_state, cost[i]))
    return next_states

# Implement the A* search algorithm to find the optimal sequence of moves
def restricted_sorting(initial_state):
    heap = [(heuristic(initial_state), initial_state, [], 0)]
    while heap:
        _, state, path, cost_so_far = heapq.heappop(heap)
        if all(not stack or len(stack) == 5 for stack in state):
            return path
        for next_state, move_cost in generate_next_states(state):
            new_cost = cost_so_far + move_cost
            new_path = path + [(state.index(next_state) if state.index(next_state) != -1 else 0, state.index(next_state))]
            heapq.heappush(heap, (new_cost + heuristic(next_state), next_state, new_path, new_cost))

# Find the optimal sequence of moves
optimal_moves = restricted_sorting(initial_state)
print(optimal_moves)
