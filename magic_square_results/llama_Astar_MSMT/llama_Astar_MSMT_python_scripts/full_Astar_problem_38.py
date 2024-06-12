
import heapq


def initialize():
   # Define the initial state of the grid as a 2d list
   initial_state = [['x', '56', 'x', '40'],
                    ['x', 'x', '44', '60'],
                    ['x', '52', 'x', '45'],
                    ['x', 'x', '62', '47']]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   column_sums = [None, 227, 215, None]
   row_sums = [None, 207, 218, None]
   diagonal_sum = 195


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coordinates and values of the numbers replaced with 'x' in each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, column_sums, row_sums, diagonal_sum, visited_costs, queue


def a_star():
  
   initial_state, num_rows, num_cols, column_sums, row_sums, diagonal_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where the sums of the specified rows, columns, and diagonal are equal to the given amounts
       if all(sum(row) == row_sums[i] for i, row in enumerate(state) if row_sums[i] is not None) and all(sum(state[i][j] for i in range(num_rows)) == column_sums[j] for j in range(num_cols) if column_sums[j] is not None) and sum(state[i][i] for i in range(num_rows)) - sum(state[i][num_rows - i - 1] for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' must be within the given range
                   for num in range(40, 67):
                       new_state[row_ind][col_ind] = num
                       # Check if the new state is valid, ie if the sums of the specified rows, columns, and diagonal are equal to the given amounts
                       if all(sum(row) == row_sums[i] for i, row in enumerate(new_state) if row_sums[i] is not None) and all(sum(new_state[i][j] for i in range(num_rows)) == column_sums[j] for j in range(num_cols) if column_sums[j] is not None) and sum(new_state[i][i] for i in range(num_rows)) - sum(new_state[i][num_rows - i - 1] for i in range(num_rows)) == diagonal_sum:
                           # Generate the new state
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of all the numbers in the grid
   # This heuristic relaxes the constraint that the unique integers must be in the given range
   # It is admissible because it never overestimates the cost to reach the goal
   # It's consistent because moving a number from one position to another in the grid does not change the heuristic cost of the successor node
   return sum(sum(row) for row in state)


print(a_star())
