
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1),
                   (0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0),
                   (1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0),
                   (1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0),
                   (0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1),
                   (0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0),
                   (1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1),
                   (0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0),
                   (0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
                   (1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0),
                   (0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0),
                   (0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0),
                   (1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0),
                   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1))
   num_rows = 14
   num_cols = 14
   # The goal state is at position (13, 0)
   goal_state = (13, 0)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state[goal_state[0]][goal_state[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which involves jumping to any of the 8 adjacent trampolines
       for row_ind in range(max(0, goal_state[0] - 1), min(num_rows, goal_state[0] + 2)):
           for col_ind in range(max(0, goal_state[1] - 1), min(num_cols, goal_state[1] + 2)):
               # Check if the new state would be valid, ie the new position is not out of the grid and the trampoline is not broken
               if (row_ind, col_ind) != goal_state and state[row_ind][col_ind] == 0:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[row_ind][col_ind] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_ind, col_ind)], new_state))
   return None


def heuristic(state, goal_state):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it does not consider the number of diagonal jumps made
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the current state
   # It's consistent because moving to a neighboring position in the grid increases the heuristic cost of the successor node by a max of 1 (if the moved position is not the goal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(goal_state[0] - state[goal_state[0]][goal_state[1]]) + abs(goal_state[1] - state[goal_state[0]][goal_state[1]])
   return h


print(a_star())
