
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1),
                   (1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1),
                   (1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1),
                   (1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0),
                   (0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1),
                   (0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1),
                   (0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1),
                   (0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0),
                   (0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1),
                   (0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1),
                   (1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1),
                   (1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0),
                   (1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1),
                   (1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0))
   num_rows = 14
   num_cols = 14
   start_pos = (13, 10)
   goal_pos = (4, 0)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[goal_pos[0]][goal_pos[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which involves jumping to any of the 8 adjacent trampolines
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new position is valid, ie within the grid and not broken
               new_pos = (start_pos[0] + row_offset, start_pos[1] + col_offset)
               if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and state[new_pos[0]][new_pos[1]] == 0):
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[new_pos[0]][new_pos[1]] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_pos)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_pos], new_state))
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic is the Manhattan distance from the current position to the goal position
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it does not consider the number of diagonal jumps made
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the current state
   # It is consistent because moving to a neighboring position in the grid increases the heuristic cost of the successor node by a max of 1 (if the moved position is not diagonal to the goal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return abs(goal_pos[0] - start_pos[0]) + abs(goal_pos[1] - start_pos[1])


print(a_star())