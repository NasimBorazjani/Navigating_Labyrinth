
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0),
                   (1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0),
                   (1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1),
                   (1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1),
                   (0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1),
                   (1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1),
                   (0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0),
                   (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0),
                   (1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1),
                   (1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0),
                   (1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0),
                   (1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1),
                   (1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1))
   num_rows = 13
   num_cols = 13
   start_pos = (11, 5)
   goal_pos = (0, 12)
   # The maximum number of diagonal jumps allowed
   max_diagonal_jumps = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], start_pos)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_pos:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
               new_row, new_col = state[0] + row_offset, state[1] + col_offset
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
                   # Calculate the number of diagonal jumps made from the start position to the new position
                   diagonal_jumps = abs(new_row - start_pos[0]) + abs(new_col - start_pos[1]) - abs(new_row - new_col)
                   # Check if the number of diagonal jumps is within the allowed limit
                   if diagonal_jumps <= max_diagonal_jumps:
                       # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
                       new_cost = g + 1
                       if (new_row, new_col) not in visited_costs or new_cost < visited_costs[new_row, new_col]:
                           visited_costs[new_row, new_col] = new_cost
                           h = heuristic(new_row, new_col, goal_pos)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], (new_row, new_col)))
   return None


def heuristic(row, col, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # It is consistent because moving to a neighboring position increases the heuristic cost of the successor node by a max of 1 (if the moved position is closer to the goal), which is equal to the cost of reaching the successor node
   return abs(row - goal[0]) + abs(col - goal[1])


print(a_star())
