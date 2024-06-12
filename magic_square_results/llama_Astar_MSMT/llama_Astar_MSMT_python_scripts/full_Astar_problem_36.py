
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, None], [69, 71, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = [198, 152, 195]
   goal_row_sum = [198, 152, 195]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, number of rows and columns, and the goal sums)
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of all columns, rows, and the diagonal equals the goal sums
       if all(sum(state[i][j] for i in range(num_rows)) == goal_col_sum[j] for j in range(num_cols)) and all(sum(state[i][j] for j in range(num_cols)) == goal_row_sum[i] for i in range(num_rows)) and sum(state[i][i] for i in range(num_rows)) == goal_col_sum[-1] and sum(state[i][num_cols - i - 1] for i in range(num_rows)) == goal_row_sum[-1]:
           return actions


       # Generate all valid actions from the current state, which includes replacing one of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   for num in range(40, 90):
                       # Check if the unique integer is valid, ie if it does not violate the goal sums
                       if all(sum(state[i][j] for i in range(num_rows)) + num <= goal_col_sum[j] for j in range(num_cols)) and all(sum(state[i][j] for j in range(num_cols)) + num <= goal_row_sum[i] for i in range(num_rows)) and sum(state[i][i] for i in range(num_rows)) + num <= goal_col_sum[-1] and sum(state[i][num_cols - i - 1] for i in range(num_rows)) + num <= goal_row_sum[-1]:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of unique integers replaced, as the task is to minimize the number of unique integers replaced
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum, goal_row_sum), new_cost, actions + [(row, col, num)], new_state))
                              
   return None


def heuristic(state, goal_col_sum, goal_row_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of columns, rows, and the diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be unique in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected by at least one unique integer
   # It's consistent because moving a unique integer from one cell to another reduces the heuristic cost of the successor node by a max of 1 (if the moved unique integer's sum matches the goal sum for that cell), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Calculate the current sum of the column
           col_sum = sum(state[k][j] for k in range(len(state)))
           # Calculate the current sum of the row
           row_sum = sum(state[i][k] for k in range(len(state[i])))
           # Calculate the current sum of the diagonal
           diagonal_sum = sum(state[k][k] for k in range(len(state)))
           # Calculate the current sum of the counter-diagonal
           counter_diagonal_sum = sum(state[k][len(state) - k - 1] for k in range(len(state)))
           # Add the absolute difference between the current sum and the goal sum to the estimate
           h += abs(col_sum - goal_col_sum[j]) + abs(row_sum - goal_row_sum[i]) + abs(diagonal_sum - goal_col_sum[-1]) + abs(counter_diagonal_sum - goal_row_sum[-1])
   return h


print(a_star())
