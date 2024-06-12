
import heapq

def initialize():
   # Define the initial state of the board
   initial_state = [['_', 'a', 't', 'n'], ['b', 'i', 'r', 'n'], ['k', 'r', 'e', 'y'], ['b', 'a', 'l', 'i']]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   words = ['ann', 'birk', 'trey', 'bali']

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   # Encode the initial state of the board, the number of rows and columns, the list of words, and the visited costs in a single tuple
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, words, visited_costs, queue


def a_star():
  
   initial_state, num_rows, num_cols, words, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Convert the current state of the board to a string to check if we have reached the goal state
       state_str = str(state)
       if all(''.join(row) == word for row, word in zip(state, words)):
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row = None
           new_col = None
           # Find the position of the blank space
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == '_':
                       new_row = i + d_row
                       new_col = j + d_col
                       break
               if new_row is not None:
                   break
          
           # Check if the new position is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighboring tile
               new_state = [list(row) for row in state]
               new_state[new_row][new_col], new_state[i][j] = new_state[i][j], new_state[new_row][new_col]
               # Convert the new state to a string for comparison and add the move to the path
               new_state_str = str(new_state)
               new_cost = g + 1

               if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                   visited_costs[new_state_str] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))
   return None

print(a_star())
