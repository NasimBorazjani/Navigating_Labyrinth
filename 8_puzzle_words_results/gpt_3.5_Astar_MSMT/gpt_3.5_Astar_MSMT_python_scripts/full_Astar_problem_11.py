
import heapq

def initialize():
   # Define the initial state of the board as a 2d tuple
   initial_state = (('o', 'b', 'e', 'd'),
                   ('c', 'o', 'd', 'u'),
                   ('w', 'a', '_', 'p'),
                   ('y', 'u', 'l', 'p'))
   num_rows = 4
   num_cols = 4
   target_words = ['bud', 'codo', 'waup', 'yelp']

   visited_costs = {}
   visited_costs[initial_state] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, target_words, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If the state matches the target words, return the actions
       if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
           return actions

       # Find the position of the blank space
       blank_pos = [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_'][0]
       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
       for d_row, d_col in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
           new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
           # Check if the new position for the blank space is within the bounds of the board
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the blank space with the diagonal neighbor
               new_state = [list(row[:]) for row in state]
               new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required 
               new_cost = g + 1

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))
   return None

print(a_star())
