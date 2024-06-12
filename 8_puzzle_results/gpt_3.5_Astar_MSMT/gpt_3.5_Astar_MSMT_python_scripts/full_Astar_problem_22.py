
import heapq

def initialize():
   # Define the initial state of the puzzle grid as a 2d tuple
   initial_state = ((81, 25, '_'), (19, 56, 14), (61, 41, 39))
   num_rows = 3
   num_cols = 3
   goal_state = ((81, 56, 39), (61, 41, 25), (19, 14, '_'))

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
           empty_row, empty_col = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]
           new_row, new_col = empty_row + d_row, empty_col + d_col
           # Check if the new coordinate is valid, ie within the bounds of the grid
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the empty spot with the neighboring tile
               new_state = [list(row[:]) for row in state]
               new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost of the new state is the number on the tile that was swapped with the empty spot
               new_cost = g + new_state[new_row][new_col]

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [new_state[new_row][new_col]], new_state))
   return None

print(a_star())
