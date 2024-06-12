
import heapq

# Define the initial state of the stacks
initial_state = [[], [], [], ['Green', 'Blue', 'Blue', 'Green', 'Black'], ['Red', 'Green', 'Blue', 'Blue', 'Red'], ['Black', 'Black', 'Yellow', 'Red', 'Yellow'], [], ['Yellow', 'Black', 'Green', 'Red', 'Yellow']]

# Define the cost of moving a block to each stack
cost = {0: 7, 1: 8, 2: 2, 3: 8, 4: 9, 5: 6, 6: 8, 7: 1}

# Define the goal state where all blocks are sorted
goal_state = [[], [], [], ['Black', 'Black', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Red', 'Red'], ['Red', 'Red', 'Yellow', 'Yellow', 'Yellow'], [], []]

# Define a function to calculate the cost of a state
def calculate_cost(state):
    total_cost = 0
    for i in range(len(state)):
        for block in state[i]:
            total_cost += cost[i]
    return total_cost

# Define a function to generate possible moves from a state
def generate_moves(state):
    moves = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][-1] == state[i][-1]):
                    new_state = [stack.copy() for stack in state]
                    new_state[j].append(new_state[i].pop())
                    moves.append((i, j, new_state))
    return moves

# Define the A* search algorithm
def astar_search(initial_state, goal_state):
    heap = [(calculate_cost(initial_state), 0, initial_state)]
    while heap:
        _, cost_so_far, current_state = heapq.heappop(heap)
        if current_state == goal_state:
            return cost_so_far
        for move in generate_moves(current_state):
            move_cost = calculate_cost(move[2])
            total_cost = cost_so_far + move_cost
            heapq.heappush(heap, (total_cost, total_cost, move[2]))

# Find the optimal transfer pairs
optimal_cost = astar_search(initial_state, goal_state)
print(optimal_cost)
