
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the specified row, column, and diagonal
   initial_state = (('25', 'x', 'x'), ('x', 'x', 'x'), ('x', 'x', 'x'))
   unique_integers = set(str(i) for i in range(20, 40))
   row_1_sum = 86
   col_1_sum = 99
   diagonal_sum = 76
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all of the 'x's in the grid are replaced with unique integers such that the sum of the specified row, column, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][1]) for i in range(num_rows)) == col_1_sum and sum(int(state[i][num_rows - i - 1]) for i in range(num_rows)) == diagonal_sum:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Get the coordinate of the next 'x' in the grid
           x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
           # Get the set of available unique integers
           available_numbers = unique_integers - set(cell for row in state for cell in row if cell != 'x')
           for number in available_numbers:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[x_row][x_col] = number
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
               new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # In the problem statement the grid is indexed starting from 1, thus must add 1 to the row and column indices
                   heapq.heappush(queue, (new_cost + heuristic(new_state, row_1_sum, col_1_sum, diagonal_sum), new_cost, actions + [(x_row, x_col, int(number))], new_state))
   return None


def heuristic(state, row_1_sum, col_1_sum, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sum of the specified row, column, and diagonal in the current state and their goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the specified row, column, and diagonal must equal the given amounts; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 20, the decrease in the absolute difference between the sum of the specified row, column, and diagonal in the current state and their goal sums
   h = 0
   h += abs(sum(int(cell) for cell in state[1] if cell != 'x') - row_1_sum)
   h += abs(sum(int(state[i][1]) for i in range(len(state)) if state[i][1] != 'x') - col_1_sum)
   h += abs(sum(int(state[i][len(state) - i - 1]) for i in range(len(state)) if state[i][len(state) - i - 1] != 'x') - diagonal_sum)
   return h


print(a_star())
