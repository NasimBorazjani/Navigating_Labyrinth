
import heapq

# Define the initial state of the stacks
initial_state = [[], ['White', 'Black', 'Yellow', 'Black', 'Green', 'Blue', 'Pink'], ['Black', 'Red', 'Yellow', 'White', 'Yellow', 'Black', 'Green'], ['Yellow', 'White', 'Green', 'White', 'White', 'Black', 'Blue'], ['Blue', 'Pink', 'Red', 'Pink', 'Green', 'Yellow', 'Black'], ['White', 'Red', 'Pink', 'Blue', 'Blue', 'Pink', 'Green'], [], [], [], ['Red', 'Pink', 'Red', 'Blue', 'Red', 'Green', 'Yellow'], [], []]

# Define the cost of moving blocks between stacks
cost = {0: 5, 1: 3, 2: 3, 3: 4, 4: 2, 5: 2, 6: 12, 7: 9, 8: 5, 9: 11, 10: 11, 11: 10}

# Define a function to calculate the cost of moving a block from one stack to another
def move_cost(from_stack, to_stack):
    return cost[to_stack]

# Define a function to calculate the heuristic cost (estimated cost to reach the goal) for a state
def heuristic_cost(state):
    total_cost = 0
    for stack in state:
        if stack:
            shade = stack[0]
            total_cost += sum(move_cost(stack.index(shade), i) for i in range(len(stack)))
    return total_cost

# Define a function to generate possible moves from a given state
def generate_moves(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and (not state[i] or not state[j] or state[i][0] == state[j][0]):
                moves.append((i, j))
    return moves

# Define the A* search algorithm to find the optimal solution
def astar_search(initial_state):
    frontier = [(heuristic_cost(initial_state), 0, initial_state, [])]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        _, cost_so_far, current_state, path = heapq.heappop(frontier)

        if all(not stack or len(set(stack)) == 1 for stack in current_state):
            return path

        if tuple(map(tuple, current_state)) in explored:
            continue

        explored.add(tuple(map(tuple, current_state)))

        for move in generate_moves(current_state):
            new_state = [stack.copy() for stack in current_state]
            new_state[move[1]].insert(0, new_state[move[0]].pop(0))
            new_cost = cost_so_far + move_cost(move[0], move[1])
            new_path = path + [(move[0], move[1])]
            heapq.heappush(frontier, (new_cost + heuristic_cost(new_state), new_cost, new_state, new_path))

    return None

# Find the optimal solution
optimal_solution = astar_search(initial_state)
print(optimal_solution)
