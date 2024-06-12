
import heapq

# Define the initial state of the stacks
initial_state = [['Yellow', 'Green', 'White', 'Pink', 'Black', 'Pink', 'Pink'],
                 ['Pink', 'Red', 'White', 'Black', 'Green', 'White', 'Pink'],
                 ['Red', 'Black', 'Green', 'Blue', 'Red', 'Black', 'Yellow'],
                 ['Blue', 'White', 'Blue', 'Blue', 'Black', 'White', 'Blue'],
                 ['Yellow', 'Blue', 'Green', 'Green', 'Red', 'Red', 'Yellow'],
                 [],
                 [],
                 [],
                 ['Black', 'Yellow', 'Red', 'Green', 'Yellow', 'Pink', 'White'],
                 [],
                 [],
                 []]

# Define the cost of moving a block to each stack
cost = {0: 11, 1: 11, 2: 12, 3: 4, 4: 12, 5: 2, 6: 10, 7: 8, 8: 6, 9: 10, 10: 8, 11: 3}

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
        for j in range(len(state)):
            if i != j and (not state[i] or state[i][0] == state[j][0] or not state[j]):
                moves.append((i, j))
    return moves

# Define the A* search algorithm
def astar_search(initial_state, cost):
    open_list = [(0, initial_state, [])]
    closed_list = set()

    while open_list:
        current_cost, current_state, current_path = heapq.heappop(open_list)

        if current_state not in closed_list:
            closed_list.add(current_state)

            if heuristic_cost(current_state) == 0:
                return current_path

            for move in generate_moves(current_state):
                new_state = [stack.copy() for stack in current_state]
                new_state[move[1]].insert(0, new_state[move[0]].pop(0))
                new_cost = current_cost + cost[move[1]]
                new_path = current_path + [(move[0], move[1])]

                heapq.heappush(open_list, (new_cost, new_state, new_path))

    return None

# Find the optimal sequence of moves
optimal_moves = astar_search(initial_state, cost)
print(optimal_moves)
