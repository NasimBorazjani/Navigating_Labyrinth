
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('55', 'x', '53', 'x'), ('x', '50', '52', 'x'), ('x', 'x', 'x', '35'), ('x', '62', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The sum of the numbers in the diagonal from the top right to the bottom left corner of the grid
   diagonal_sum = 221
   # The sums of the columns and rows
   column_sums = [None, 218, 203, None]
   row_sums = [None, 186, 174, None]
   # The range of unique integers that can be used to fill the grid
   available_numbers = set(range(28, 65))


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
       # The goal state is where all the 'x's in the grid are replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
       if 'x' not in [cell for row in state for cell in row]:
           # Check if the sums of the rows, columns, and diagonal in the current state match the given sums
           # Convert any element of the grid equal to 'x' to a 0, to avoid these error "ValueError: invalid literal for int() with base 10: 'x'" and "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sums[i] or row_sums[i] is None for i, row in enumerate(state)) and \
              all(sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x') == column_sums[i] or column_sums[i] is None for i in range(num_cols)) and \
              sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') == diagonal_sum:
               return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers - set(cell for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                   # If the state has at least 1 remaining unknown number, ie 'x', break the loop after generating all possible actions from the current state
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # This heuristic is admissible because it always chooses the smallest available number to replace the 'x's, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a number is removed from the available numbers, or equal or less by at most the smallest available number (equal to the cost of reaching the successor node, ie the smallest available number) as the maximum number that can be added to the grid is the largest available number, which is always greater than the smallest available number. Thus h(n) can never be greater than c(n, n’)(equal to the smallest available number) + h(n’)
   return sum(sorted(set(range(28, 65)) - set(int(cell) for row in state for cell in row if cell != 'x'))[:sum(1 for row in state for cell in row if cell == 'x')])


print(a_star())
