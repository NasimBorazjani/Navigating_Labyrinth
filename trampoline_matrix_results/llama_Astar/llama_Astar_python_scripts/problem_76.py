
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                   (1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1),
                   (1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0),
                   (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1),
                   (0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0),
                   (1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1),
                   (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0),
                   (1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0),
                   (1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1),
                   (1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1))
   num_rows = 14
   num_cols = 14
   start_pos = (2, 12)
   goal_pos = (10, 1)
   # The number of diagonal jumps Alex must make
   num_diagonal_jumps = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], start_pos)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_pos:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
       for row_diff in range(-1, 2):
           for col_diff in range(-1, 2):
               # Check if the new state would be valid, ie the new position is within the grid and there is no broken trampoline
               if 0 <= state[0] + row_diff < num_rows and 0 <= state[1] + col_diff < num_cols and initial_state[state[0] + row_diff][state[1] + col_diff] == 0:
                   # Calculate the number of diagonal jumps made in the new state
                   new_diagonal_jumps = abs(row_diff) + abs(col_diff)
                   # Check if the number of diagonal jumps is valid
                   if new_diagonal_jumps == num_diagonal_jumps:
                       # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
                       new_cost = g + 1
                       new_state = (state[0] + row_diff, state[1] + col_diff)
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, goal_pos)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal_pos):
   # An admissible and consistent heuristic is the Euclidean distance between the current state and the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # It is consistent because moving to a neighboring state always increases the heuristic cost of the successor node by a value that is equal to or less than the cost of reaching the successor node
   # Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   return math.sqrt((state[0] - goal_pos[0]) ** 2 + (state[1] - goal_pos[1]) ** 2)


print(a_star())
