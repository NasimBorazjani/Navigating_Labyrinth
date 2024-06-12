
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1),
                   (0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0),
                   (1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1),
                   (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
                   (0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
                   (1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1),
                   (1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0),
                   (0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1),
                   (1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0),
                   (1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1),
                   (1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1))
   num_rows = 14
   num_cols = 14
   # The destination is at position (3, 13)
   destination = (3, 13)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the destination state
       if actions[-1] == destination:
           return actions


       # Generate all possible actions from the current state, which involves jumping to any of the 8 adjacent trampolines
       for row_diff in range(-1, 2):
           for col_diff in range(-1, 2):
               # Check if the new position is valid, ie within the grid and not broken
               new_row, new_col = actions[-1][0] + row_diff, actions[-1][1] + col_diff
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] == 0:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[new_row][new_col] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, destination)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, destination):
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the destination
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it allows Alex to jump to any of the 8 adjacent trampolines
   # It is admissible because it never overestimates the cost to reach the goal, as the shortest path to the goal is always a straight line
   # It's consistent because moving to a neighboring cell increases the heuristic cost of the successor node by a max of 1 (if the moved cell is on the diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(state.index(1) // 14 - destination[0]) + abs(state.index(1) % 14 - destination[1])
   return h


print(a_star())
