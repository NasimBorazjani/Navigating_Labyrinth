
import heapq


def initialize():
   # Define the initial state of the grid as a 2d tuple
   initial_state = ((0, 1, 0, 1, 0, 1, 1, 1, 1),
                   (0, 0, 1, 1, 0, 0, 0, 0, 1),
                   (0, 0, 0, 1, 1, 1, 0, 0, 1),
                   (0, 0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 0, 0, 0, 1, 1, 1, 1),
                   (0, 0, 1, 1, 1, 1, 0, 1, 1),
                   (0, 0, 0, 1, 1, 1, 1, 1, 0),
                   (1, 0, 1, 1, 1, 1, 1, 0, 1),
                   (0, 1, 1, 1, 1, 1, 0, 1, 0))
   num_rows = 9
   num_cols = 9
   start_position = (8, 0)
   end_position = (2, 7)


   visited_costs = {}
   visited_costs[start_position] = 0


   queue = [(0, 0, [], start_position)]
  
   return initial_state, num_rows, num_cols, start_position, end_position, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_position, end_position, visited_costs, queue = initialize()


   while queue:
       _, g, actions, position = heapq.heappop(queue)


       # If the current position is the destination, return the actions taken
       if position == end_position:
           return actions


       # Generate all possible actions from the current position, which includes moving to any of the eight adjacent trampolines
       for d_row in [-1, 0, 1]:
           for d_col in [-1, 0, 1]:
               # Check if the new position is within the bounds of the grid and the trampoline is functional
               new_row, new_col = position[0] + d_row, position[1] + d_col
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
                   # Check if the move is diagonal, if so, increment the diagonal move count
                   if abs(d_row) == 1 and abs(d_col) == 1:
                       new_diagonal_moves = actions.count('diagonal') + 1
                   else:
                       new_diagonal_moves = actions.count('diagonal')
                   # If the number of diagonal moves is exactly 3, the move is valid
                   if new_diagonal_moves == 3:
                       new_position = (new_row, new_col)
                       new_cost = g + 1
                       if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                           visited_costs[new_position] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_position, end_position), new_cost, actions + [(new_row, new_col)], new_position))
                   # If the number of diagonal moves is less than 3, the move is valid
                   elif new_diagonal_moves < 3:
                       new_position = (new_row, new_col)
                       new_cost = g + 1
                       if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                           visited_costs[new_position] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_position, end_position), new_cost, actions + [(new_row, new_col)], new_position))
   return None




def heuristic(position, end_position):
   # The heuristic is the Manhattan distance between the current position and the end position
   # This heuristic is admissible as it never overestimates the cost to reach the goal, as Alex can only move in four directions
   # The heuristic is consistent because the cost of moving from one position to an adjacent position is always 1, which is exactly the decrease in the Manhattan distance
   return abs(position[0] - end_position[0]) + abs(position[1] - end_position[1])


print(a_star())
