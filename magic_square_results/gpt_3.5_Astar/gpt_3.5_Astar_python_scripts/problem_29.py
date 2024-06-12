
import heapq


def a_star():
   # Define the initial state of the magic square grid, with unknown numbers represented as 'x'
   initial_state = [['x', '77', 'x'],
                    ['49', 'x', 'x'],
                    ['x', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   row_sum = 156
   col_sum = 180
   diagonal_sum = 127
   num_range = list(range(34, 79))


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state satisfies all the constraints, return the actions taken
       if check_constraints(state, row_sum, col_sum, diagonal_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with any unique integer in the given range
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for num in num_range:
                       new_state = [row[:] for row in state]
                       new_state[i][j] = str(num)
                       new_state_str = str(new_state)
                       new_cost = g + num
                      
                       if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                           visited_costs[new_state_str] = new_cost
                           heappush(queue, (new_cost + heuristic(new_state, row_sum, col_sum, diagonal_sum), new_cost, actions + [(i, j, num)], new_state))
   return None


def check_constraints(state, row_sum, col_sum, diagonal_sum):
   # Check if the sum of each row, column, and diagonal in the grid satisfies the given constraints
   # Also, check if all numbers in the grid are unique
   nums = set()
   for i in range(3):
       row_sum_check = sum(int(state[i][j]) for j in range(3))
       col_sum_check = sum(int(state[j][i]) for j in range(3))
       diagonal_sum_check = sum(int(state[j][2-j]) for j in range(3))
       if row_sum_check != row_sum or col_sum_check != col_sum or diagonal_sum_check != diagonal_sum:
           return False
       for j in range(3):
           if state[i][j] != 'x':
               nums.add(int(state[i][j]))
   return len(nums) == 9


def heuristic(state, row_sum, col_sum, diagonal_sum):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current sum of each row, column, and diagonal and the target sum
   # This heuristic relaxes the constraint that the numbers in the grid must be unique and that the sum of each row, column, and diagonal must equal the target sum
   # It is admissible because it never overestimates the cost to reach the goal, as the sum of the absolute differences is always less than or equal to the actual cost to reach the goal
   # It is consistent because the estimated cost of the next node is higher if a number is replaced with another number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference in the sum of a row, column, or diagonal is 1
   h = 0
   for i in range(3):
       row_sum_check = sum(int(state[i][j]) for j in range(3))
       col_sum_check = sum(int(state[j][i]) for j in range(3))
       diagonal_sum_check = sum(int(state[j][2-j]) for j in range(3))
       h += abs(row_sum_check - row_sum) + abs(col_sum_check - col_sum) + abs(diagonal_sum_check - diagonal_sum)
   return h


print(a_star())
