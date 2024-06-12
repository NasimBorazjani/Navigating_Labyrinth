
import heapq

# Define the initial state of the stacks
initial_state = [[], [], ['Blue', 'Blue', 'Green', 'Black', 'Red'], [], ['Red', 'Green', 'Red', 'Black', 'Yellow'], [], ['Blue', 'Yellow', 'Green', 'Yellow', 'Black'], ['Yellow', 'Green', 'Black', 'Red', 'Blue']]

# Define the cost of moving blocks between stacks
cost = {0: 6, 1: 2, 2: 7, 3: 1, 4: 1, 5: 5, 6: 3, 7: 2}

# Define a function to calculate the cost of a state
def calculate_cost(state):
    total_cost = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            total_cost += cost[i]
    return total_cost

# Define a function to check if the state is sorted
def is_sorted(state):
    for stack in state:
        if stack != [] and len(set(stack)) != 1:
            return False
    return True

# Define a function to generate possible moves from a state
def generate_moves(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and (state[i] == [] or state[j] == [] or state[i][-1] == state[j][-1]):
                moves.append((i, j))
    return moves

# Define the A* search algorithm
def astar(initial_state):
    heap = [(calculate_cost(initial_state), initial_state, [])]
    while heap:
        _, state, path = heapq.heappop(heap)
        if is_sorted(state):
            return path
        for move in generate_moves(state):
            new_state = [stack.copy() for stack in state]
            new_state[move[1]].append(new_state[move[0]].pop())
            new_cost = calculate_cost(new_state)
            heapq.heappush(heap, (new_cost, new_state, path + [move]))

# Find the optimal transfer pairs
optimal_transfers = astar(initial_state)
print(optimal_transfers)
