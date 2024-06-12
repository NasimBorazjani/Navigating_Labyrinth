
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0),
                   (1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1),
                   (1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0),
                   (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0),
                   (0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1),
                   (1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0),
                   (1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1),
                   (0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0),
                   (1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1),
                   (0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0),
                   (1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1),
                   (0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1))
   num_rows = 15
   num_cols = 15
   # The goal state is at position (1, 12)
   goal_state = (1, 12)
   # The number of diagonal jumps Alex must make
   num_diagonal_jumps = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[10][0] == 1 and state[1][12] == 1:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               # Check if the new state would be valid, ie the trampoline is not broken and the number of diagonal jumps does not exceed the goal number
               if state[row_ind][col_ind] == 1 and abs(row_ind - 10) + abs(col_ind - 0) <= num_diagonal_jumps + 1:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[row_ind][col_ind] = 0
                   new_state[10][0] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_ind, col_ind)], new_state))
   return None


def heuristic(state, goal_state):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
   # This heuristic relaxes the constraint that Alex must make exactly 5 diagonal jumps, as it allows Alex to jump to any of the eight adjacent trampolines
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving to a neighboring trampoline reduces the heuristic cost of the successor node by a max of 1 (if the moved trampoline is closer to the goal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(10 - goal_state[0]) + abs(0 - goal_state[1])
   return h


print(a_star())
