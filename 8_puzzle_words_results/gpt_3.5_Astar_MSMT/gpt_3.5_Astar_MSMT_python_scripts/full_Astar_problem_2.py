
import heapq

def initialize():
   # Define the initial board state, target words, and other variables given in the problem
   initial_state = [['o', 'a', 'u', 'o'], ['p', 'r', 'l', 'e'], ['f', 'a', '_', 'f'], ['m', 'k', 'd', 'd']]
   target_words = ['ako', 'pole', 'raff', 'mudd']
   num_rows = 4
   num_cols = 4

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, target_words, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Unpack the state to get the position of the blank space
       blank_row = 0
       blank_col = 0
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == '_':
                   blank_row = i
                   blank_col = j

       # Check if the current state matches the target words
       if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
           return actions

       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = blank_row + d_row, blank_col + d_col
           # Check if the new position of the blank space is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the neighbor
               new_state = [list(row[:]) for row in state]
               new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
               new_state = str(new_state)  # Convert the new state to a string to use it as a key in the visited_costs dictionary
               # The cost of this new state is the number of swaps made, as we aim to minimize the number of swaps required
               new_cost = g + 1

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))
   return None

print(a_star())
