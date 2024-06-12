
import heapq

# Define the initial state of the stacks
initial_state = [['Green', 'Green', 'Blue', 'Green'], [], ['Yellow', 'Red', 'Red', 'Blue'], [], [], ['Yellow', 'Yellow', 'Blue', 'Red']]

# Define the cost of moving a block to each stack
cost = {0: 6, 1: 5, 2: 2, 3: 3, 4: 3, 5: 6}

# Define a function to calculate the heuristic cost (number of misplaced blocks)
def heuristic_cost(state):
    misplaced_blocks = 0
    for stack in state:
        if stack:
            shade = stack[0]
            for block in stack:
                if block != shade:
                    misplaced_blocks += 1
    return misplaced_blocks

# Define a function to generate possible moves from a given state
def generate_moves(state):
    moves = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][0] == state[i][0]):
                    moves.append((i, j))
    return moves

# Define the A* search algorithm
def astar_search(initial_state, cost):
    frontier = [(0, initial_state, [])]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        current_cost, current_state, current_path = heapq.heappop(frontier)

        if current_state not in explored:
            explored.add(current_state)

            if heuristic_cost(current_state) == 0:
                return current_path

            for move in generate_moves(current_state):
                new_state = [stack.copy() for stack in current_state]
                new_state[move[1]].insert(0, new_state[move[0]].pop(0))
                new_cost = current_cost + cost[move[1]]
                new_path = current_path + [move]
                heapq.heappush(frontier, (new_cost, new_state, new_path))

    return None

# Find the optimal sequence of moves
optimal_moves = astar_search(initial_state, cost)
print(optimal_moves)
