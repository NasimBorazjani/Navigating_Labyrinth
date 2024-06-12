
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', 'x'), ('x', 'x', 'x'), ('40', 'x', '71'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's in the grid
   available_numbers = set(str(i) for i in range(40, 90))
   # The sum of the specified rows, columns, and diagonal
   row_1_sum = 194
   col_1_sum = 183
   diagonal_sum = 161


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if 'x' in state:
           # Find the first 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate all possible actions from the current state, which includes replacing the 'x' with any of the available unique integers
                       for number in available_numbers:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j] = number
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                           new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(new_state, row_1_sum, col_1_sum, diagonal_sum)
                               # In the problem statement the grid is indexed starting from 0, thus must add 1 to the bucket_ind
                               heappush(queue, (new_cost + h, new_cost, actions + [(i, j, int(number))], new_state))
       # If the state has no remaining 'x's, ie all of the numbers in the grid are known, check if the state is the goal state
       else:
           # The goal state is where the sum of the specified rows, columns, and diagonal equals the given amounts
           if sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][1]) for i in range(num_rows)) == col_1_sum and sum(int(state[i][num_rows - 1 - i]) for i in range(num_rows)) == diagonal_sum:
               return actions
   return None


def heuristic(state, row_1_sum, col_1_sum, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sum of the specified rows, columns, and diagonal in the current state and the given amounts
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of all of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the given sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the sum of the specified rows, columns, and diagonal in the current state and the given amounts
   h = 0
   h += abs(sum(int(cell) for cell in state[1]) - row_1_sum)
   h += abs(sum(int(state[i][1]) for i in range(len(state))) - col_1_sum)
   h += abs(sum(int(state[i][len(state) - 1 - i]) for i in range(len(state))) - diagonal_sum)
   return h


print(a_star())
