
import heapq

# Define the initial state of the stacks
initial_state = [['Red', 'Pink', 'Pink', 'Pink', 'Red', 'Black', 'Pink'], [], ['Green', 'Green', 'Blue', 'White', 'Yellow', 'Blue', 'Blue'], [], ['Green', 'Blue', 'White', 'Red', 'Blue', 'Black', 'Red'], ['Pink', 'White', 'Yellow', 'Black', 'Yellow', 'Green', 'White'], [], ['Red', 'Green', 'Black', 'White', 'Green', 'Red', 'Black'], [], [], ['Yellow', 'White', 'Yellow', 'Blue', 'Black', 'Yellow', 'Pink'], []]

# Define the cost of moving one block to the top of each stack
cost = {0: 10, 1: 4, 2: 5, 3: 4, 4: 7, 5: 3, 6: 11, 7: 5, 8: 9, 9: 3, 10: 11, 11: 2}

# Define a function to calculate the heuristic cost (in this case, the number of blocks out of place)
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
    heap = [(0, 0, initial_state, [])]  # (total_cost, heuristic_cost, state, path)
    visited = set()

    while heap:
        total_cost, heuristic_cost, state, path = heapq.heappop(heap)

        if state == [[], [], [], [], [], [], [], [], [], [], [], []]:
            return path

        if tuple(map(tuple, state)) in visited:
            continue

        visited.add(tuple(map(tuple, state)))

        for move in generate_moves(state):
            new_state = [stack.copy() for stack in state]
            block, dest = move
            new_state[dest].insert(0, new_state[block].pop(0))
            new_total_cost = total_cost + cost[dest]
            new_heuristic_cost = heuristic_cost(new_state)
            heapq.heappush(heap, (new_total_cost + new_heuristic_cost, new_heuristic_cost, new_state, path + [move]))

    return None

# Find the optimal sequence of moves
optimal_moves = astar_search(initial_state, cost)
print(optimal_moves)
