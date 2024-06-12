
import heapq

def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = ((87, 50, 82), (68, '_', 74), (23, 61, 11))
   num_rows = 3
   num_cols = 3

   visited_costs = {}
   visited_costs[initial_state] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Unpack the state to find the coordinates of the empty spot
       empty_spot = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]

       # If the state is the goal state, return the actions taken
       if state == ((87, 82, 74), (68, 61, 50), (23, 11, '_')):
           return actions

       # Generate all possible actions from the current state, which includes swapping the empty spot with a neighboring tile
       for d_row, d_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
           new_row, new_col = empty_spot[0] + d_row, empty_spot[1] + d_col
           # Check if the new coordinate is valid, ie if the new position is within the bounds of the puzzle
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
               # Generate the new state by swapping the empty spot with the neighboring tile
               new_state = [list(row[:]) for row in state]
               new_state[empty_spot[0]][empty_spot[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_spot[0]][empty_spot[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost of the new state is the number on the tile swapped with the empty spot
               new_cost = g + new_state[new_row][new_col]

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + 1, new_cost, actions + [new_state[new_row][new_col]], new_state))
   return None

print(a_star())
