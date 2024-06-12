
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['a', 'j', '_', 'k', 'e'],
                   ['t', 's', 'w', 'y', 'e'],
                   ['t', 'r', 'a', 'p', 'a'],
                   ['s', 'e', 'a', 'm', 'h'],
                   ['c', 'r', 's', 'e', 'p'])

   # Define the target words
   target_words = ['jake', 'tawse', 'trypa', 'smash', 'creep']

   # Define the possible swap directions
   swap_directions = ['up-right', 'down-right', 'up-left', 'down-left']

   # Define the dimensions of the board
   num_rows = 5
   num_cols = 5

   # Initialize the visited costs dictionary
   visited_costs = {}
   visited_costs[initial_state] = 0

   # Initialize the priority queue with the initial state
   queue = [(0, 0, [], initial_state)]

   # While there are un-visited states
   while queue:
       # Pop the state with the lowest cost from the queue
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state
       if state == tuple(list(word) for word in target_words):
           return actions

       # Generate all possible actions from the current state
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               # Check if the current tile is the blank tile
               if state[row_ind][col_ind] == '_':
                   # Generate all possible swaps from the current tile
                   for swap_direction in swap_directions:
                       # Calculate the new row and column indices after the swap
                       new_row_ind, new_col_ind = row_ind, col_ind
                       if swap_direction == 'up-right':
                           new_row_ind -= 1
                           new_col_ind += 1
                       elif swap_direction == 'down-right':
                           new_row_ind += 1
                           new_col_ind += 1
                       elif swap_direction == 'up-left':
                           new_row_ind -= 1
                           new_col_ind -= 1
                       elif swap_direction == 'down-left':
                           new_row_ind += 1
                           new_col_ind -= 1

                       # Check if the new indices are within the bounds of the board
                       if 0 <= new_row_ind < num_rows and 0 <= new_col_ind < num_cols:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind], new_state[new_row_ind][new_col_ind] = new_state[new_row_ind][new_col_ind], new_state[row_ind][col_ind]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost of the new state is the number of swaps made
                           new_cost = g + 1

                           # If the new state is unvisited or we found a new path with a lower cost to reach the goal, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, target_words), new_cost, actions + [(row_ind, col_ind, swap_direction)], new_state))
   return None


def heuristic(state, target_words):
   # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target words
   h = 0
   for row_ind, word in enumerate(target_words):
       for col_ind, char in enumerate(word):
           if state[row_ind][col_ind] != char:
               h += 1
   return h


print(a_star())
