
import heapq


def a_star():
   # Define the initial state of the magic square grid, with unknown values represented as 'x'
   initial_state = [['x', 'x', 'x'], ['x', '73', '47'], ['x', 'x', 'x']]
   # Define the goal sums for each row, column, and diagonal
   goal_sums = [180, 177, 183]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(34, 79))


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


       # Generate all possible actions from the current state, which includes replacing 'x' with any of the unique integers in the grid
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


def check_sums(state, goal_sums):
   # Check if the sum of each row, column, and diagonal in the current state equals the goal sums
   row_sums = [sum([int(num) for num in row if num != 'x']) for row in state]
   col_sums = [sum([int(state[i][j]) for i in range(3) if state[i][j] != 'x']) for j in range(3)]
   diag_sum1 = sum([int(state[i][i]) for i in range(3) if state[i][i] != 'x'])
   diag_sum2 = sum([int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x'])
   return row_sums == goal_sums and col_sums == goal_sums and diag_sum1 == goal_sums[0] and diag_sum2 == goal_sums[2]


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the goal sums
   # This heuristic relaxes the constraint that each number must be unique, and the sum of the numbers in the grid is minimized
   # It is admissible because it underestimates the cost to reach the goal, as the sum of the differences can only decrease as we replace 'x' with unique integers
   # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum value that can be added to the sum is the difference between the current sum and the goal sum
   h = 0
   row_sums = [sum([int(num) for num in row if num != 'x']) for row in state]
   col_sums = [sum([int(state[i][j]) for i in range(3) if state[i][j] != 'x']) for j in range(3)]
   diag_sum1 = sum([int(state[i][i]) for i in range(3) if state[i][i] != 'x'])
   diag_sum2 = sum([int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x'])
   for i in range(3):
       h += abs(row_sums[i] - goal_sums[i])
       h += abs(col_sums[i] - goal_sums[i])
   h += abs(diag_sum1 - goal_sums[0])
   h += abs(diag_sum2 - goal_sums[2])
   return h


print(a_star())
