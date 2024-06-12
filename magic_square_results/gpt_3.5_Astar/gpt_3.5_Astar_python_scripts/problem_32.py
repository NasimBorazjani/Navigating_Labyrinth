
import heapq


def a_star():
   # Define the initial state of the magic square grid, with 'x' representing unknown values
   initial_state = [['x', 'x', 'x'], ['x', 'x', 'x'], [41, 'x', 'x']]
   # Define the goal sums for each row, column, and diagonal
   goal_sums = [134, 135, 122]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(31, 76))


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state satisfies all the constraints, return the actions taken
       if check_constraints(state, goal_sums):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the grid
       for i in range(3):
           for j in range(3):
               if state[i][j] == 'x':
                   for num in unique_integers:
                       new_state = [row[:] for row in state]
                       new_state[i][j] = num
                       new_cost = g + num
                       # Encode the new state as a string to store in the visited_costs dictionary
                       new_state_str = str(new_state)


                       if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                           visited_costs[new_state_str] = new_cost
                           heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(i, j, num)], new_state))
   return None


def check_constraints(state, goal_sums):
   # Check if the sum of each row, column, and diagonal in the grid matches the goal sums
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diag_sum1 = state[0][2] + state[1][1] + state[2][0]
   diag_sum2 = state[0][0] + state[1][1] + state[2][2]
   return row_sums == goal_sums and col_sums == goal_sums and diag_sum1 == goal_sums[2] and diag_sum2 == goal_sums[2]


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the goal sum
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the goal
   # It's consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum decrease in the difference is 1
   h = 0
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diag_sum1 = state[0][2] + state[1][1] + state[2][0]
   diag_sum2 = state[0][0] + state[1][1] + state[2][2]
   for i in range(3):
       h += abs(row_sums[i] - goal_sums[i])
       h += abs(col_sums[i] - goal_sums[i])
   h += abs(diag_sum1 - goal_sums[2])
   h += abs(diag_sum2 - goal_sums[2])
   return h


print(a_star())
