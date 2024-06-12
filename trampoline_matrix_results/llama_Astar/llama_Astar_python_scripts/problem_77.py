
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0),
                   (0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0),
                   (1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0),
                   (1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0),
                   (0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0),
                   (1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0),
                   (1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0),
                   (1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1),
                   (1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1),
                   (1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0),
                   (0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1),
                   (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0),
                   (1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1))
   num_rows = 14
   num_cols = 14
   # The goal state is at position (8, 1)
   goal_state = (8, 1)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state[0][13] == 0 and state[8][1] == 0:
           return actions


       # Generate all possible actions from the current state, which involves jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for row_ind in range(max(0, state[0][13] - 1), min(num_rows, state[0][13] + 2)):
           for col_ind in range(max(0, state[1][13] - 1), min(num_cols, state[1][13] + 2)):
               # Check if the new state would be valid, ie the new position is not broken and the number of diagonal jumps does not change
               if state[row_ind][col_ind] == 0 and (abs(row_ind - state[0][13]) + abs(col_ind - state[1][13]) == 1 or abs(row_ind - state[0][13]) == abs(col_ind - state[1][13]) == 1):
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[0][13], new_state[1][13] = row_ind, col_ind
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
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as it allows Alex to jump to any of the 8 adjacent trampolines
   # It is admissible because it never overestimates the cost to reach the goal, as the shortest path to the goal state is always a straight line
   # It's consistent because moving a jump from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved jump is diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(state[0][13] - goal_state[0]) + abs(state[1][13] - goal_state[1])
   return h


print(a_star())
