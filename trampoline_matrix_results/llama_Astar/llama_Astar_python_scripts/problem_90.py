
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1),
                   (0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
                   (1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0),
                   (1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1),
                   (0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0),
                   (0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1),
                   (0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0),
                   (1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1),
                   (0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1),
                   (0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1),
                   (1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0),
                   (1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0),
                   (1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0),
                   (0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1))
   num_rows = 14
   num_cols = 14
   # The destination is at position (0, 4)
   destination = (0, 4)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the destination state
       if state[11][12] == 0:
           return actions


       # Generate all possible actions from the current state, which involves jumping to any of the 8 adjacent trampolines
       for row_ind in range(max(0, 11 - 2), min(14, 11 + 2)):
           for col_ind in range(max(0, 12 - 2), min(14, 12 + 2)):
               # Check if the new state would be valid, ie the new position is not out of the grid and the trampoline is not broken
               if (row_ind, col_ind) != (11, 12) and state[row_ind][col_ind] == 0:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[row_ind][col_ind] = 1
                   new_state[11][12] = 0
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the destination
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, destination)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_ind, col_ind)], new_state))
   return None


def heuristic(state, destination):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current state to the destination
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the current state
   # It is consistent because moving to a neighboring state always increases the heuristic cost of the successor node by a max of 1 (if the moved position is closer to the destination), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(11 - destination[0]) + abs(12 - destination[1])
   return h


print(a_star())
