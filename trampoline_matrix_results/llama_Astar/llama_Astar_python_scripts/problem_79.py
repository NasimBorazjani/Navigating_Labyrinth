
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0),
                   (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),
                   (0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0),
                   (1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0),
                   (1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1),
                   (0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0),
                   (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
                   (0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1),
                   (0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0),
                   (0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1),
                   (0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0),
                   (1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1),
                   (1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1))
   num_rows = 14
   num_cols = 14
   start = (10, 10)
   goal = (1, 0)
   # The number of diagonal jumps Alex must make
   num_diagonal_jumps = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[goal[0]][goal[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which involves jumping to any of the 8 adjacent trampolines
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new position is valid, ie within the grid and not broken
               new_row, new_col = start[0] + row_offset, start[1] + col_offset
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
                   # Count the number of diagonal jumps made in this action
                   num_diagonal_jumps_new = abs(row_offset) + abs(col_offset) - 1
                   # Check if the number of diagonal jumps is valid
                   if num_diagonal_jumps_new >= num_diagonal_jumps:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[new_row][new_col] = 1
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, goal, num_diagonal_jumps)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, goal, num_diagonal_jumps):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each trampoline from the goal position
   # The heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as the heuristic estimate for the goal state is 0, as the distance of each trampoline from the goal position would be 0 in the goal state
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 0:
               h += abs(i - goal[0]) + abs(j - goal[1])
   return h


print(a_star())
