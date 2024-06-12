
import heapq


def initialize():
   # Define the initial state of the grid with 'x's replaced by None for easier manipulation
   initial_state = [[None, 53, None, 79], [46, 51, None, 78], [45, None, 73, 77], [42, 47, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   grid_range = (40, 80)


   visited_costs = {}
   visited_costs[initial_state] = 0
  
   # The information we must encode for each state includes the current state of the grid and the sum of the numbers in the topmost row, rightmost column, and the diagonal
   # The initial state has the maximum possible sum, as the hidden numbers are between 40 to 80 and the shown numbers are smaller
   initial_state_sum = 53 + 79 + 46 + 78 + 45 + 77 + 42 + 47 + 73 + 78 + 79 + 46 + 73 + 42 + 45 + 46 + 77 + 78 + 79 + 80
   initial_state_info = (initial_state, initial_state_sum)
   # Since we are minimizing the sum, the priority queue is ordered by the negative of the sum
   queue = [(-initial_state_sum, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, grid_range, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, grid_range, visited_costs, queue = initialize()
  
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == (None, 0):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       # Iterating through the range and the indices of the 'x's
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[0][row_ind][col_ind] is None:
                   for num in range(grid_range[0], grid_range[1]):
                       # Check if the replacement is valid, ie if the number is unique and maintains the consecutive order in each row and column
                       if (all(num not in row for row in state[0]) and
                           all(num not in col for col in zip(*state[0])) and
                           (row_ind == 0 or num > state[0][row_ind - 1][col_ind]) and
                           (col_ind == 0 or num > state[0][row_ind][col_ind - 1]) and
                           (row_ind == 0 or col_ind == 0 or num > state[0][row_ind - 1][col_ind - 1]) and
                           (row_ind == num_rows - 1 or col_ind == num_cols - 1 or num < state[0][row_ind + 1][col_ind + 1])):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state[0]]
                           new_state[row_ind][col_ind] = num
                           new_state = (tuple(tuple(row) for row in new_state), state[1] - num)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost - new_state[1], g + 1, actions + [(row_ind, col_ind, num)], new_state))
   return None


print(a_star())
