
import heapq


def a_star():
   # Define the initial state of the magic square grid, with some numbers given and others unknown
   initial_state = ((37, 'x', 26), ('x', 'x', 'x'), ('x', 'x', 'x'))
   # Define the goal sums for each row, column, and diagonal
   goal_sums = [94, 111, 82]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(19, 44))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state satisfies all the constraints, return the actions taken
       if check_constraints(state, goal_sums):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with any of the unique integers in the grid
       for i in range(3):
           for j in range(3):
               if state[i][j] == 'x':
                   for num in unique_integers:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       new_cost = g + num
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(i, j, num)], new_state))
   return None


def check_constraints(state, goal_sums):
   # Check if the sums of each row, column, and diagonal in the grid match the goal sums
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diag_sum1 = state[0][2] + state[1][1] + state[2][0]
   diag_sum2 = sum(state[i][i] for i in range(3))
   return row_sums == goal_sums and col_sums == goal_sums and diag_sum1 == goal_sums[2] and diag_sum2 == goal_sums[2]


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic is the sum of the differences between the current sums of rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the numbers in the grid must be unique, and presumes we can replace 'x' with any of the unique integers to reach the goal state
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the differences is always less than or equal to the actual cost to reach the goal
   # The heuristic is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum value that can be added to the grid is the largest unique integer, which is exactly the decrease in the heuristic estimate
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diag_sum1 = state[0][2] + state[1][1] + state[2][0]
   diag_sum2 = sum(state[i][i] for i in range(3))
   h = sum(abs(row_sum - goal_sum) for row_sum, goal_sum in zip(row_sums, goal_sums))
   h += sum(abs(col_sum - goal_sum) for col_sum, goal_sum in zip(col_sums, goal_sums))
   h += abs(diag_sum1 - goal_sums[2]) + abs(diag_sum2 - goal_sums[2])
   return h


print(a_star())
