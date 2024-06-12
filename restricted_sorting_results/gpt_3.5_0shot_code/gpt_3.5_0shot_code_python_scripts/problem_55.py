
import heapq

# Define the initial state of the stacks
initial_state = [['Red', 'Red', 'Red', 'Green', 'Yellow'],
                  ['Black', 'Red', 'Green', 'Yellow', 'Yellow'],
                  [],
                  [],
                  [],
                  ['Black', 'Blue', 'Black', 'Yellow', 'Green'],
                  [],
                  ['Blue', 'Green', 'Blue', 'Black', 'Blue']]

# Define the cost of moving a block to each stack
cost = {0: 8, 1: 2, 2: 7, 3: 6, 4: 7, 5: 1, 6: 5, 7: 3}

# Define the goal state
goal_state = [['Red', 'Red', 'Red', 'Red', 'Red'],
              ['Black', 'Black', 'Black', 'Black', 'Black'],
              ['Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
              ['Green', 'Green', 'Green', 'Green', 'Green'],
              ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'],
              [],
              [],
              []]

# Define a function to calculate the cost of a state
def calculate_cost(state):
    total_cost = 0
    for i in range(len(state)):
        for block in state[i]:
            total_cost += cost[i]
    return total_cost

# Define a function to generate possible moves from a given state
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
    frontier = [(calculate_cost(initial_state), 0, initial_state)]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        _, cost_so_far, current_state = heapq.heappop(frontier)

        if current_state == goal_state:
            return cost_so_far

        explored.add(tuple(tuple(stack) for stack in current_state))

        for move in generate_moves(current_state):
            move_cost = calculate_cost(move[2])
            if tuple(tuple(stack) for stack in move[2]) not in explored:
                heapq.heappush(frontier, (move_cost + cost_so_far, cost_so_far + 1, move[2]))

    return None

# Find the optimal sequence of moves
optimal_cost = astar_search(initial_state, goal_state)
print(optimal_cost)
