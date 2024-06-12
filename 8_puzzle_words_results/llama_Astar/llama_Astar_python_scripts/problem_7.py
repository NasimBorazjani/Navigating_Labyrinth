
import heapq


def a_star():
   # Define the initial state of the board
   initial_state = (['u', 'c', 'r', 'y'], ['d', 'n', 'n', 'r'], ['_', 'u', 'm', 'p'], ['k', 'e', 'e', 'e'])
   # Define the target words
   target_words = ['cry', 'dune', 'rump', 'knee']
   # Define the possible swap directions
   swap_directions = ['up-right', 'down-right', 'up-left', 'down-left']
   # Define the dimensions of the board
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(word.split() for word in target_words):
           return actions


       # Generate all possible actions from the current state
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == '_':
                   for swap_direction in swap_directions:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       # Swap the blank space with its neighbor in the given direction
                       if swap_direction == 'up-right':
                           new_state[row][col], new_state[row - 1][col + 1] = new_state[row - 1][col + 1], new_state[row][col]
                       elif swap_direction == 'down-right':
                           new_state[row][col], new_state[row + 1][col + 1] = new_state[row + 1][col + 1], new_state[row][col]
                       elif swap_direction == 'up-left':
                           new_state[row][col], new_state[row - 1][col - 1] = new_state[row - 1][col - 1], new_state[row][col]
                       elif swap_direction == 'down-left':
                           new_state[row][col], new_state[row + 1][col - 1] = new_state[row + 1][col - 1], new_state[row][col]
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic function is not needed in this problem as the cost of the goal state is 0, and the cost of each state is the number of swaps made to reach it
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(row, col, swap_direction)], new_state))
   return None


print(a_star())
