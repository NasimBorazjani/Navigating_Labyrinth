
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of integers and 'x's
   initial_state = (('x', 'x', 'x'), (30, 'x', 'x'), ('x', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's in the grid
   available_numbers = set(range(20, 40))
   # The sum of the numbers in the specified row, column, and diagonal
   row_1_sum = 87
   col_1_sum = 82
   diagonal_sum = 94


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state has no 'x's, ie all of the numbers in the grid are known, check if the state is the goal state
       if all(cell != 'x' for row in state for cell in row):
           # Convert the elements of the grid to integers to calculate the sum of the specified row, column, and diagonal
           state_int = tuple(tuple(int(cell) for cell in row) for row in state)
           # If the sum of the numbers in the specified row, column, and diagonal equal the given amounts, return the actions taken to reach this state
           if sum(state_int[1]) == row_1_sum and sum(row[1] for row in state_int) == col_1_sum and sum(state_int[i][2 - i] for i in range(num_rows)) == diagonal_sum:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Find the coordinate of the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       x_row, x_col = i, j
                       break
           # Generate the set of numbers that are currently in the grid
           current_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
           # The set of numbers that can replace the 'x' are the numbers in the range that are not currently in the grid
           available_numbers = set(range(20, 40)) - current_numbers
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = number
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = g + number


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # In the problem statement the grid is indexed starting from 1, thus must add 1 to the row and column indices
                   heappush(queue, (new_cost + heuristic(state, available_numbers), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None




def heuristic(state, available_numbers):
   # An admissible and consistent heuristic for this problem is the sum of the smallest available numbers that can replace the remaining 'x's in the grid
   # This heuristic is admissible because it always opts for the action that results in the smallest increase in the sum of the numbers in the grid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most the smallest available number (equal to the cost of reaching the successor node, ie the number added to the grid) as the minimum amount that can be added to the grid is the smallest available number, which is exactly the number used to replace the 'x' in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the smallest available number) + h(n’)
   h = 0
   # Sort the available numbers in increasing order
   available_numbers = sorted(list(available_numbers))
   # Count the number of 'x's in the grid
   num_x = sum(cell == 'x' for row in state for cell in row)
   # Add the smallest available numbers to the estimate
   for i in range(num_x):
       h += available_numbers[i]
   return h


print(a_star())
