
import heapq

def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = ((23, 30, 43), (12, 31, 19), (6, 68, '_'))
   num_rows = 3
   num_cols = 3

   visited_costs = {}
   visited_costs[initial_state] = 0

   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state, where all tiles are in descending order and the empty spot is in the bottom right corner
       if all(state[i][j] == i*num_cols + j + 1 for i in range(num_rows) for j in range(num_cols)):
           return actions

       # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
       for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
           new_row, new_col = None, None
           # Find the coordinates of the empty spot
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == '_':
                       new_row, new_col = i + d_row, j + d_col
           # Check if the new coordinates are valid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the empty spot with the neighboring tile
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[i][j] = new_state[i][j], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost of the new state is the number on the tile that was swapped with the empty spot
               new_cost = g + new_state[new_row][new_col]

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [new_state[new_row][new_col]], new_state))
   return None

print(a_star())
