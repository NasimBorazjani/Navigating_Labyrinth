
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
                   (1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0),
                   (1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0),
                   (1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1),
                   (1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),
                   (0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1),
                   (0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1),
                   (0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0),
                   (1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0),
                   (1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1),
                   (0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1),
                   (1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1))
   num_rows = 14
   num_cols = 14
   start_pos = (0, 11)
   goal_pos = (9, 1)
   # The number of diagonal jumps Alex must make
   num_diagonal_jumps = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if actions[-1] == goal_pos:
           return actions


       # Generate all possible actions from the current state, which involves jumping to any of the 8 adjacent trampolines
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new position is valid, ie within the grid and not a broken trampoline
               new_row, new_col = actions[-1][0] + row_offset, actions[-1][1] + col_offset
               if (0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0):
                   # Calculate the number of diagonal jumps made so far
                   diagonal_jumps = abs(row_offset) + abs(col_offset) - 1
                   # Check if the new state would be valid, ie the number of diagonal jumps does not exceed the limit
                   if abs(row_offset) == abs(col_offset) and g + 1 + diagonal_jumps <= num_diagonal_jumps:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[new_row][new_col] = 1
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, goal_pos, num_diagonal_jumps)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, goal_pos, num_diagonal_jumps):
   # An admissible and consistent heuristic is the Manhattan distance to the goal position, plus the number of diagonal jumps made so far
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it allows Alex to make more or fewer diagonal jumps than required
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving to a neighboring position requires a diagonal jump, which increases the heuristic cost of the successor node by a max of 1 (if the moved position is not diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in range(len(state)):
       for col in range(len(state[row])):
           if state[row][col] == 0:
               h += abs(row - goal_pos[0]) + abs(col - goal_pos[1])
   return h


print(a_star())
