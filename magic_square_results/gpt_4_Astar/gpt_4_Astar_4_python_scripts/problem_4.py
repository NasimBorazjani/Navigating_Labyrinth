
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('21', 'x', 'x'), ('x', 'x', 'x'), ('x', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's in the grid
   numbers = set(str(i) for i in range(20, 40))
   # The sum of the numbers in the specified row, column, and diagonal
   row_1_sum = 95
   col_1_sum = 72
   diag_sum = 71


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all 'x's in the grid have been replaced with unique integers such that the sum of the specified row, column, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][1]) for i in range(num_rows)) == col_1_sum and sum(int(state[i][num_rows - 1 - i]) for i in range(num_rows)) == diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of the available unique integers
       # The available unique integers are all numbers in the range - numbers present in the current state
       available_numbers = numbers - set(cell for row in state for cell in row if cell != 'x')
       for number in available_numbers:
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + int(number)


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(new_state, row_1_sum, col_1_sum, diag_sum)
                           # In the problem statement the grid is indexed starting from 0, thus must add 1 to the bucket_ind
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(i, j, int(number))], new_state))
                       # Once the next 'x' is replaced with a number, break the loop to avoid replacing all 'x's in the grid in one action
                       break
               else:
                   continue
               break
   return None


def heuristic(state, row_1_sum, col_1_sum, diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of the specified row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of all of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the goal sum
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' in the grid with a number is the number itself, which is always greater than or equal to 20, the decrease in the absolute difference between the current sum and the goal sum
   h = 0
   # When calculating the sum of the specified row, column, and diagonal, first convert any element of the grid equal to 'x' to a 0, to avoid these error "ValueError: invalid literal for int() with base 10: 'x'" and "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
   h += abs(sum(int(cell) if cell != 'x' else 0 for cell in state[1]) - row_1_sum)
   h += abs(sum(int(state[i][1]) if state[i][1] != 'x' else 0 for i in range(num_rows)) - col_1_sum)
   h += abs(sum(int(state[i][num_rows - 1 - i]) if state[i][num_rows - 1 - i] != 'x' else 0 for i in range(num_rows)) - diag_sum)
   return h


print(a_star())
