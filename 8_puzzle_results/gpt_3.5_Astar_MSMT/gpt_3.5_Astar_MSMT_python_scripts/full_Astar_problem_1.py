
import heapq

def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = ((12, 55, '_'), (35, 97, 43), (17, 25, 9))
   num_rows = 3
   num_cols = 3
   goal_state = ((97, 55, 43), (35, 25, 12), (17, 9, '_'))

   visited_costs = {}
   visited_costs[initial_state] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_state, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions

       # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
       for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
           new_row, new_col = None, None
           # Find the position of the empty spot in the current state
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == '_':
                       new_row, new_col = i + d_row, j + d_col
           # Check if the new position of the empty spot is valid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the empty spot with the neighboring tile
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[i][j] = new_state[i][j], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number on the tile that the empty spot is swapped with
               new_cost = g + state[new_row][new_col]
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [state[new_row][new_col]], new_state))
   return None

print(a_star())
