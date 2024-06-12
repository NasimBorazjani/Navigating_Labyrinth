
import heapq


def a_star():
   # Define the initial state of the grid, as a 3x3 tuple
   initial_state = (('x', 'x', 'x'), ('x', 'x', 'x'), ('x', 'x', 57))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's in the grid
   numbers = set(range(35, 60))
   # The sum of the numbers in the specified row, column, and diagonal
   row_1_sum = 151
   col_1_sum = 154
   diag_sum = 133


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


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of the unique integers in the range
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # For each unique integer in the range, generate a new state
                   for number in numbers:
                       # The new state is a copy of the current state, with the next 'x' replaced with the current number
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The action to get to the new state is a tuple of the coordinate of the 'x' replaced and the number used to replace it
                           # In the problem statement the grid is indexed starting from 1, thus must add 1 to the row and column indices
                           heapq.heappush(queue, (new_cost + heuristic(new_state, numbers - {number}, row_1_sum, col_1_sum, diag_sum), new_cost, actions + [(i+1, j+1, number)], new_state))
                   # Once we have generated all possible states from replacing the current 'x', break the loop to avoid replacing the other 'x's in the grid multiple times
                   break
           else:
               continue
           break
   return None


def heuristic(state, numbers, row_1_sum, col_1_sum, diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the smallest numbers in the range that can be used to replace the remaining 'x's in the grid
   # This heuristic relaxes the constraints that the sum of the specified row, column, and diagonal must equal the given amounts and that each number can be in the final grid only once; ie It presumes we can replace the remaining 'x's with any of the numbers in the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the smallest number in the range, the decrease in the heuristic cost
   return sum(sorted(numbers)[:sum(1 for row in state for cell in row if cell == 'x')])


print(a_star())
