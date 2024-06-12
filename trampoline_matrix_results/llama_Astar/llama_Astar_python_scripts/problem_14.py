
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((1, 0, 0, 0, 0, 1, 1, 0, 0),
                   (1, 0, 0, 1, 0, 1, 1, 0, 0),
                   (0, 0, 1, 0, 1, 0, 0, 0, 1),
                   (1, 0, 0, 1, 1, 0, 0, 0, 0),
                   (0, 0, 0, 0, 1, 1, 1, 0, 1),
                   (0, 0, 0, 1, 1, 0, 1, 1, 0),
                   (0, 1, 1, 0, 1, 1, 0, 1, 0),
                   (0, 1, 0, 0, 1, 0, 0, 0, 0),
                   (0, 0, 0, 0, 1, 0, 1, 1, 0))
   num_rows = 9
   num_cols = 9
   # The goal state is at position (7, 0)
   goal_state = (7, 0)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [(0, 7)], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if actions[-1] == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for row_ind in range(max(0, actions[-1][0] - 1), min(num_rows, actions[-1}[0] + 2)):
           for col_ind in range(max(0, actions[-1][1] - 1), min(num_cols, actions[-1][1] + 2)):
               # Check if the new position is valid, ie it is not the same as the current position and it is not broken
               if (row_ind, col_ind) != actions[-1] and state[row_ind][col_ind] == 0:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[row_ind][col_ind] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind)], new_state))
   return None


def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # It is consistent because moving to a neighboring state always increases the heuristic cost of the successor node by a max of 1 (if the moved position's row and column are both lower than the current position's row and column), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])
   return h


print(a_star())
