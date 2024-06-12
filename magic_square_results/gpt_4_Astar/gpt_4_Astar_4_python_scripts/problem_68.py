
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of integers and 'x's
   initial_state = (('x', 40, 'x', 'x'), ('x', 58, 'x', 37), (47, 'x', 'x', 44), (45, 'x', 'x', 42))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The sums of the rows, columns, and diagonal
   row_sums = [None, 220, 216, None]
   col_sums = [None, 224, 226, None]
   diagonal_sum = 211
   # The range of unique integers that can be used to replace 'x's
   available_numbers = set(range(31, 68))


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
       # The goal state is where all 'x's have been replaced with unique integers and the sums of the rows, columns, and diagonal equal the given amounts
       if all(cell != 'x' for row in state for cell in row) and all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows) if state[i][num_cols - 1 - i] != 'x') == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # For each available number, generate a new state
                   for number in available_numbers:
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The new number must be removed from the set of available numbers
                           new_available_numbers = available_numbers - {number}
                           heapq.heappush(queue, (new_cost + heuristic(new_state, new_available_numbers, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, number)], new_state))
                   # Return from the function after the first 'x' is replaced to avoid replacing multiple 'x's in one action
                   return
   return None


def heuristic(state, available_numbers, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the smallest available numbers that can be used to replace the remaining 'x's in the grid
   # This heuristic is admissible because it always opts for the action that minimizes the sum of the numbers in the grid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a number is removed from the grid, or equal or less by at most the smallest available number (equal to the cost of reaching the successor node, ie one action) as the maximum number that can be added to the grid is the largest available number, which is always greater than the smallest available number. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the available numbers in increasing order
   available_numbers = sorted(list(available_numbers))
   # Count the number of 'x's in the grid
   num_xs = sum(cell == 'x' for row in state for cell in row)
   # Add the smallest available numbers to the estimate
   for i in range(num_xs):
       h += available_numbers[i]
   return h


print(a_star())
