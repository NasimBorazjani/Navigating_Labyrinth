
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('37', 'x', 'x', '56'), ('52', 'x', 'x', 'x'), ('x', '50', 'x', 'x'), ('x', 'x', 'x', '46'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The sum of the numbers in the grid must be as low as possible, thus the numbers in the grid must be as low as possible
   # The numbers in the grid must be unique, thus the numbers that can replace 'x' in the grid are all numbers in the range that are not already in the grid
   available_numbers = set(range(34, 61)) - set(int(cell) for row in initial_state for cell in row if cell != 'x')
   # The sums of the rows, columns, and diagonal are given in the problem statement
   row_sums = [None, 169, 190, None]
   col_sums = [None, 165, 155, None]
   diagonal_sum = 201


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state, available_numbers))


   while queue:
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if the state is the goal state
       if 'x' not in state:
           # The goal state is where the sum of the numbers in each row, column, and diagonal equals the given amounts
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and sum(int(state[i][num_rows - 1 - i]) for i in range(num_rows) if state[i][num_rows - 1 - i] != 'x') == diagonal_sum:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of the numbers in the grid
                       new_cost = g + number


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The set of available numbers must be updated after each number is added to the grid
                           new_available_numbers = available_numbers - {number}
                           # In the problem statement the grid is indexed starting from 1, thus must add 1 to the i and j
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, number)], new_state, new_available_numbers))
                   break
           else:
               continue
           break
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the current sum of the numbers in each row, column, and diagonal and the given amounts
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the given amounts
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the difference between the current sum of the numbers in each row, column, and diagonal and the given amounts
   h = 0
   for row, row_sum in zip(state, row_sums):
       if row_sum is not None:
           h += row_sum - sum(int(cell) for cell in row if cell != 'x')
   for j, col_sum in enumerate(col_sums):
       if col_sum is not None:
           h += col_sum - sum(int(state[i][j]) for i in range(len(state)) if state[i][j] != 'x')
   h += diagonal_sum - sum(int(state[i][len(state) - 1 - i]) for i in range(len(state)) if state[i][len(state) - 1 - i] != 'x')
   return h


print(a_star())