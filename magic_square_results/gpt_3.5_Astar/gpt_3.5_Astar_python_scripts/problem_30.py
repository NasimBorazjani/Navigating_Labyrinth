
import heapq


def a_star():
   # Define the initial state of the magic square grid, with unknown numbers represented as 'x'
   initial_state = [['x', 'x', 59], ['x', 'x', 'x'], [38, 'x', 'x']]
   # Define the goal sums for the rows, columns, and diagonal
   goal_sums = [212, 172, 165]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(34, 79))


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
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(i, j, num)], new_state))
   return None


def check_constraints(state, goal_sums):
   # Check if the sums of rows, columns, and diagonal match the goal sums
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diag_sum1 = state[0][2] + state[1][1] + state[2][0]
   diag_sum2 = sum(state[i][i] for i in range(3))
   return row_sums == goal_sums and col_sums == goal_sums and diag_sum1 == goal_sums[2] and diag_sum2 == goal_sums[2]


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the numbers must be unique and presumes we can place any number in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences is always less than or equal to the actual cost to reach the goal
   # It is consistent because the estimated cost of the next node is higher if a number is placed in the grid, or equal or less by at most the difference between the current sum and the goal sum, which is equal to the cost of reaching the successor node
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diag_sum1 = state[0][2] + state[1][1] + state[2][0]
   diag_sum2 = sum(state[i][i] for i in range(3))
   h = sum(abs(row_sum - goal_sum) for row_sum, goal_sum in zip(row_sums, goal_sums))
   h += sum(abs(col_sum - goal_sum) for col_sum, goal_sum in zip(col_sums, goal_sums))
   h += abs(diag_sum1 - goal_sums[2]) + abs(diag_sum2 - goal_sums[2])
   return h


print(a_star())
