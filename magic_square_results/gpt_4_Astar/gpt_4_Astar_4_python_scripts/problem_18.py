
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('x', 'x', 'x'), ('x', 'x', 'x'), ('x', '70', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's in the grid
   available_numbers = set(range(48, 78))
   # The sum of the numbers in the specified row, column, and diagonal
   row_1_sum = 194
   col_1_sum = 191
   diagonal_sum = 186


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
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][1]) for i in range(num_rows)) == col_1_sum and sum(int(state[i][num_rows - 1 - i]) for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # For each available number, generate a new state
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The set of available numbers must be updated after each number is added to the grid
                           new_available_numbers = available_numbers - {number}
                           heapq.heappush(queue, (new_cost + heuristic(new_state, new_available_numbers), new_cost, actions + [(i, j, number)], new_state))
                   # After generating all possible states from replacing the current 'x', break the loop to avoid generating states from replacing multiple 'x's at once
                   break
           else:
               continue
           break
   return None


def heuristic(state, available_numbers):
   # An admissible and consistent heuristic for this problem is the sum of the smallest available numbers that can be used to replace the remaining 'x's in the grid
   # This heuristic is admissible because it always opts for the action that results in the lowest sum of the numbers in the grid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a number is removed from the grid, or equal or less by at most the smallest available number (equal to the cost of reaching the successor node, ie the smallest available number) as the minimum number that can be added to the grid is the smallest available number, which is exactly the number used to replace the 'x' in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the smallest available number) + h(n’)
   h = 0
   # Sort the available numbers in ascending order
   available_numbers = sorted(list(available_numbers))
   # Count the number of 'x's in the grid
   num_x = sum(1 for row in state for cell in row if cell == 'x')
   # Add the smallest available numbers to the estimate
   for i in range(num_x):
       h += available_numbers[i]
   return h


print(a_star())
