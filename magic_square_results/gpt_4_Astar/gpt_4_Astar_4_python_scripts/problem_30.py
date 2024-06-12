
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the specified rows, columns, and diagonal
   initial_state = (('x', 'x', '59'), ('x', 'x', 'x'), ('38', 'x', 'x'))
   num_rows = 3
   num_cols = 3
   unique_integers = set(range(34, 79))
   col_1_sum = 172
   row_1_sum = 212
   diagonal_sum = 165


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
       # The goal state is where all of the numbers in the grid are unique integers in the given range, and the sum of the specified rows, columns, and diagonal equal the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][1]) for i in range(num_rows)) == col_1_sum and sum(int(state[i][num_rows - 1 - i]) for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of the unique integers in the range
       # Generate the coordinates of the next x in the grid
       x_row, x_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == 'x'][0]
       # Generate the set of available unique integers, which includes all numbers in the range that are not present in the current state
       available_unique_integers = unique_integers - set(int(cell) for row in state for cell in row if cell != 'x')
       for number in available_unique_integers:
           # Generate the new state
           new_state = [list(row[:]) for row in state]
           new_state[x_row][x_col] = str(number)
           new_state = tuple(tuple(row) for row in new_state)
           # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
           new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               # In the problem statement the grid is indexed starting from 1, thus must add 1 to the x_row and x_col
               heapq.heappush(queue, (new_cost + heuristic(new_state, row_1_sum, col_1_sum, diagonal_sum), new_cost, actions + [(x_row, x_col, number)], new_state))
   return None


def heuristic(state, row_1_sum, col_1_sum, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sum of the specified rows, columns, and diagonal in the current state and the given amounts
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of all of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the given sums
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the sum of the specified rows, columns, and diagonal in the current state and the given amounts
   h = 0
   h += abs(sum(int(cell) for cell in state[1]) - row_1_sum)
   h += abs(sum(int(state[i][1]) for i in range(len(state))) - col_1_sum)
   h += abs(sum(int(state[i][len(state) - 1 - i]) for i in range(len(state))) - diagonal_sum)
   return h


print(a_star())
