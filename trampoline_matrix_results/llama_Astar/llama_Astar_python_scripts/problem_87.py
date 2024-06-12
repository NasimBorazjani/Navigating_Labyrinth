
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1),
                   (1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1),
                   (1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1),
                   (0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1),
                   (1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1),
                   (1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1),
                   (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1),
                   (0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1),
                   (0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                   (1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1),
                   (1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0),
                   (0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0),
                   (1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0),
                   (1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1))
   num_rows = 14
   num_cols = 14
   # The destination is at position (12, 2)
   destination = (12, 2)
   # The number of diagonal jumps required
   num_diagonal_jumps = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the destination state
       if (len(actions) == num_diagonal_jumps and
           actions[-1][0] == destination[0] and
           actions[-1][1] == destination[1]):
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
       for row_diff in range(-1, 2):
           for col_diff in range(-1, 2):
               # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
               if (0 <= actions[-1][0] + row_diff < num_rows and
                   0 <= actions[-1][1] + col_diff < num_cols and
                   state[actions[-1][0] + row_diff][actions[-1][1] + col_diff] == 0):
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[actions[-1][0] + row_diff][actions[-1][1] + col_diff] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the destination
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, destination)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(actions[-1][0] + row_diff, actions[-1][1] + col_diff)], new_state))
   return None


def heuristic(state, destination):
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the destination
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it does not consider the number of diagonal jumps made
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the current state
   # It's consistent because moving to a neighboring position in the grid increases the heuristic cost of the successor node by a max of 1 (if the moved position is not the destination), which is equal to the cost of reaching the successor node
   h = abs(destination[0] - actions[-1][0]) + abs(destination[1] - actions[-1][1])
   return h


print(a_star())
