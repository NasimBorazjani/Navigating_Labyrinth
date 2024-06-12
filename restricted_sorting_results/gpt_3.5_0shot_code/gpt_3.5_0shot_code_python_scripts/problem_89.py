
import heapq

# Define the initial state of the stacks
initial_state = [[], ['Blue', 'Yellow', 'Pink', 'Green', 'Pink', 'Red', 'Red'], [], ['Pink', 'White', 'Pink', 'Black', 'White', 'Black', 'Pink'], ['Yellow', 'Green', 'White', 'Red', 'Yellow', 'Yellow', 'Red'], ['Green', 'Pink', 'White', 'Blue', 'Red', 'White', 'Red'], [], [], ['Blue', 'Blue', 'Yellow', 'Blue', 'Black', 'Blue', 'Green'], ['Yellow', 'Black', 'Black', 'White', 'Green', 'Green', 'Black'], [], []]

# Define the cost of moving one block to the top of each stack
cost = {0: 10, 1: 8, 2: 6, 3: 4, 4: 11, 5: 5, 6: 11, 7: 5, 8: 7, 9: 7, 10: 10, 11: 10}

# Define a function to calculate the heuristic cost (h-value) for a given state
def heuristic_cost(state):
    h_cost = 0
    for stack in state:
        if len(stack) > 0:
            shade = stack[0]
            h_cost += sum(1 for block in stack if block != shade)
    return h_cost

# Define a function to generate possible moves from a given state
def generate_moves(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and (len(state[i]) == 0 or state[i][0] == state[j][0] or len(state[j]) == 0):
                moves.append((i, j))
    return moves

# Define the A* search algorithm
def astar_search(initial_state, cost):
    open_list = [(0, initial_state, [])]
    closed_list = set()

    while open_list:
        f_cost, current_state, path = heapq.heappop(open_list)

        if current_state == [[], [], [], [], [], [], [], [], [], [], [], []]:
            return path

        closed_list.add(tuple(current_state))

        for move in generate_moves(current_state):
            new_state = [stack.copy() for stack in current_state]
            block = new_state[move[0]].pop(0)
            new_state[move[1]].insert(0, block)
            g_cost = len(path) + cost[move[0]]
            h_cost = heuristic_cost(new_state)
            f_cost = g_cost + h_cost

            if tuple(new_state) not in closed_list:
                heapq.heappush(open_list, (f_cost, new_state, path + [move]))

    return None

# Find the optimal sequence of moves
optimal_moves = astar_search(initial_state, cost)
print(optimal_moves)
