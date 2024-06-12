
import heapq

def initialize():
    # Define the initial state of the board and the target words
    initial_state = [['o', 'm', 'y', 'i'], ['g', 'd', 'o', 'e'], ['_', 'o', 'b', 'd'], ['p', 'o', 'c', 'k']]
    target_words = ['moi', 'good', 'boyd', 'peck']

    # Encode other variables given in the problem
    num_rows = len(initial_state)
    num_cols = len(initial_state[0])
    num_words = len(target_words)
    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_state))] = 0

    # Initialize a priority queue to store states not yet visited
    # The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    return initial_state, target_words, num_rows, num_cols, num_words, visited_costs, queue

def a_star():
  
   initial_state, target_words, num_rows, num_cols, num_words, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Convert the state to a tuple of tuples for easy comparison
       current_state = tuple(map(tuple, state))

       # Check if the current state matches the target words
       if all(''.join(row).replace('_', '') == target_words[i] for i, row in enumerate(state)):
           return actions

       # Generate all possible actions from the current state
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == '_':
                   for dr, dc, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
                       new_i, new_j = i + dr, j + dc
                       # Check if the new position is within bounds
                       if 0 <= new_i < num_rows and 0 <= new_j < num_cols:
                           new_state = [list(row) for row in state]
                           new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                           new_state = tuple(map(tuple, new_state))
                           new_cost = g + 1

                           # Check if the new state is unvisited or we found a new path with a lower cost to reach this state
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (g + heuristic(new_state, target_words), new_cost, actions + [(direction)], new_state))
   return None

def heuristic(state, target_words):
    # A consistent and admissible heuristic is to calculate the number of characters that are not in the correct position for each target word
    # This heuristic provides a lower bound on the remaining cost to reach the goal state
    h = 0
    for i in range(len(target_words)):
        for j in range(len(state[i])):
            # Count the number of characters that are not in the correct position
            if state[i][j] != target_words[i][j]:
                h += 1
    return h

print(a_star())
