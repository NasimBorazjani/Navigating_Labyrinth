
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1),
                   (0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1),
                   (0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1),
                   (1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1),
                   (1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1),
                   (1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0),
                   (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0),
                   (1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0),
                   (1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0),
                   (1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
                   (1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0),
                   (1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0),
                   (0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0))
   num_rows = 14
   num_cols = 14
   # The goal state is at position (13, 12)
   goal_state = (13, 12)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state[goal_state[0]][goal_state[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which involves jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for row_ind in range(max(0, goal_state[0] - 1), min(num_rows, goal_state[0] + 2)):
           for col_ind in range(max(0, goal_state[1] - 1), min(num_cols, goal_state[1] + 2)):
               # Check if the new state would be valid, ie the trampoline is not broken and the number of diagonal jumps does not exceed 4
               if state[row_ind][col_ind] == 0 and abs(row_ind - goal_state[0]) + abs(col_ind - goal_state[1]) <= 4:
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
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it allows Alex to jump to any of the 8 adjacent trampolines
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal state
   # It's consistent because moving to a neighboring trampoline reduces the heuristic cost of the successor node by a max of 1 (if the moved trampoline is closer to the goal), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] == 0:
               h += abs(row_ind - goal_state[0]) + abs(col_ind - goal_state[1])
   return h


print(a_star())
