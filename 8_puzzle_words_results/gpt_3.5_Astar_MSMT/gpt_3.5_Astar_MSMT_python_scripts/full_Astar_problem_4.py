
import heapq

def initialize():
   # Define the initial state of the board as a 2d list
   initial_state = [['_', 'm', 'u', 'p'],
                    ['c', 'e', 'r', 'a'],
                    ['d', 'r', 'e', 'b'],
                    ['v', 'e', 'l', 'o']]
   num_rows = 4
   num_cols = 4
   target_words = ['map', 'cere', 'drub', 'velo']

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Convert the current state to a string to check against the target words
       state_str = str(state)
       # Check if the current state matches the target words
       if state_str in target_words:
           return actions

       # Find the position of the blank space in the current state
       blank_row, blank_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]

       # Generate all possible actions from the current state, which includes swapping the blank space with its 4 diagonal neighbors
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = blank_row + d_row, blank_col + d_col
           # Check if the new position of the blank space is valid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighboring tile
               new_state = [list(row[:]) for row in state]
               new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
               # Convert the new state to a string
               new_state_str = str(new_state)
               # The cost of this state is the number of swaps made, as we aim to minimize the number of swaps required to reach the goal state
               new_cost = g + 1

               if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                   visited_costs[new_state_str] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(new_row, new_col)], new_state))
   return None

print(a_star())
