
import heapq


def a_star():
   # Define the initial state of the magic square grid, with unknown numbers represented as 'x'
   initial_state = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', '70', 'x']]
   # Define the goal sums for each row, column, and diagonal
   goal_sums = [194, 191, 186]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(48, 78))


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the sum of each row, column, and diagonal in the current state equals the goal sums, return the actions taken
       if check_sums(state, goal_sums):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with any unique integer in the range
       for i in range(3):
           for j in range(3):
               if state[i][j] == 'x':
                   for num in unique_integers:
                       new_state = [row[:] for row in state]
                       new_state[i][j] = str(num)
                       new_cost = g + num
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(i, j, num)], new_state))
   return None


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the numbers must be unique and that the sum of each row, column, and diagonal must equal the goal sum
   # It is admissible because it never overestimates the cost to reach the goal, as the sum of the absolute differences is always less than or equal to the actual cost to reach the goal
   # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference in the sum of a row, column, or diagonal is 1
   h = 0
   for i in range(3):
       # Calculate the sum of each row, column, and diagonal in the current state
       row_sum = sum([int(num) for num in state[i] if num != 'x'])
       col_sum = sum([int(state[row][i]) for row in range(3) if state[row][i] != 'x'])
       diag1_sum = sum([int(state[i][i]) for i in range(3) if state[i][i] != 'x'])
       diag2_sum = sum([int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x'])
       # Add the absolute differences between the current sum and the goal sum to the heuristic estimate
       h += abs(row_sum - goal_sums[0]) + abs(col_sum - goal_sums[1]) + abs(diag1_sum - goal_sums[2]) + abs(diag2_sum - goal_sums[2])
   return h


def check_sums(state, goal_sums):
   # Check if the sum of each row, column, and diagonal in the current state equals the goal sums
   row_sums = [sum([int(num) for num in row if num != 'x']) for row in state]
   col_sums = [sum([int(state[row][col]) for row in range(3) if state[row][col] != 'x']) for col in range(3)]
   diag1_sum = sum([int(state[i][i]) for i in range(3) if state[i][i] != 'x'])
   diag2_sum = sum([int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x'])
   return row_sums == goal_sums[:3] and col_sums == goal_sums[:3] and diag1_sum == goal_sums[2] and diag2_sum == goal_sums[2]


print(a_star())
