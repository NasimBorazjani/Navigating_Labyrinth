
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   initial_state = (('x', 'x', 'x', 'x', '9', '20', '3', '9'),
                   ('17', '11', '17', 'x', '9', '2', '7', 'x', '15'),
                   ('x', '4', '2', '19', '12', '6', 'x', '4', '17'),
                   ('15', 'x', 'x', '15', '11', '19', 'x', '9', '5'),
                   ('3', '9', '19', '15', '2', 'x', 'x', '18', 'x'),
                   ('19', '5', '9', '11', '9', 'x', 'x', '3', 'x'),
                   ('x', 'x', '2', '8', '8', 'x', 'x', 'x', '19'),
                   ('x', 'x', '14', 'x', 'x', 'x', '18', 'x', '18'),
                   ('x', '14', '18', '7', '8', 'x', '10', '15', 'x'))
   num_rows = 9
   num_cols = 9
   start_position = (3, 7)
   end_position = (5, 0)
   # Create the set of the valid numbers that could be in the grid
   numbers = set(range(1, 21))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_position, end_position, numbers, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_position, end_position, numbers, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if start_position in actions and end_position in actions:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells in the city map
       for row_change, col_change in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_row, new_col = start_position[0] + row_change, start_position[1] + col_change
           # Check if the new position is valid, ie within the bounds of the city map and not a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != 'x':
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               number_to_be_moved = new_state[new_row][new_col]
               # Do the move
               new_state[start_position[0]][start_position[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[start_position[0]][start_position[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end_position), new_cost, actions + [(start_position, (new_row, new_col))], new_state))
                  
   return None


def heuristic(state, end_position):
   # An admissible and consistent heuristic is the Manhattan distance from the current position to the end position
   # This heuristic relaxes the constraint that Ben can only move to neighboring cells
   # It is admissible because it never overestimates the cost to reach the goal, as each move in the heuristic cost of the successor node is a max of 1
   # It's consistent because moving to a neighboring cell reduces the heuristic cost of the successor node by a max of 1 (if the moved cell is closer to the end position), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(start_position[0] - end_position[0]) + abs(start_position[1] - end_position[1])
   return h


print(a_star())
