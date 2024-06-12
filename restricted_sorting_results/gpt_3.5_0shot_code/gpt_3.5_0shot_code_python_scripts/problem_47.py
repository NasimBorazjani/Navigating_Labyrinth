
import heapq

# Define the initial state of the stacks
initial_state = [[], [], ['Red', 'Yellow', 'Black', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Red', 'Black'], [], ['Black', 'Blue', 'Yellow', 'Blue', 'Black'], [], ['Green', 'Green', 'Yellow', 'Blue', 'Green']]

# Define the cost of moving blocks between stacks
cost = {0: 4, 1: 6, 2: 8, 3: 2, 4: 4, 5: 7, 6: 7, 7: 5}

# Define a function to calculate the cost of a state
def calculate_cost(state):
    total_cost = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            total_cost += cost[i]
    return total_cost

# Define a function to check if a state is the goal state
def is_goal_state(state):
    for stack in state:
        if len(stack) > 0 and len(set(stack)) > 1:
            return False
    return True

# Define a function to generate possible moves from a state
def generate_moves(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and (len(state[j]) == 0 or state[j][-1] == state[i][-1]):
                moves.append((i, j))
    return moves

# Define the A* search algorithm
def astar_search(initial_state):
    heap = [(calculate_cost(initial_state), 0, initial_state, [])]
    heapq.heapify(heap)
    
    while heap:
        _, cost_so_far, state, path = heapq.heappop(heap)
        
        if is_goal_state(state):
            return path
        
        for move in generate_moves(state):
            new_state = [stack.copy() for stack in state]
            new_state[move[1]].append(new_state[move[0]].pop())
            new_cost = cost_so_far + cost[move[1]]
            new_path = path + [(move[0], move[1])]
            heapq.heappush(heap, (new_cost + calculate_cost(new_state), new_cost, new_state, new_path))

# Find the optimal transfer pairs
optimal_transfers = astar_search(initial_state)
print(optimal_transfers)
