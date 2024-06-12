
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [39, None, 50], [32, None, 55]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the cost to reach that state
   # Since the initial state is the starting point, the cost to reach it is 0
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all the 'x's in the grid are replaced with unique integers from the given range, ensuring that each number only appears once in the grid
       if all(isinstance(cell, int) for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind, row in enumerate(state):
           for col_ind, cell in enumerate(row):
               if cell is None:
                   for num in range(29, 83):
                       # Check if the number is valid, ie it is not already in the same row, column, or diagonal
                       # And the number is not greater than the neighboring cells in the row and column
                       if (num not in state[row_ind] and num not in [row[i] for i in range(num_cols)] and num not in [state[i][col_ind] for i in range(num_rows)] and
                           (row_ind == col_ind or num <= max(state[row_ind])) and (row_ind != col_ind or num <= max(state[i][i] for i in range(num_rows))) and
                           (row_ind == num_rows - col_ind - 1 or num <= max(state[i][num_cols - i - 1] for i in range(num_rows)))):
                           # Generate the new state
                           new_state = [row[:] for row in state]
                           new_state[row_ind][col_ind] = num
                           new_state = [row[:] for row in new_state]
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each number can only be replaced by a number that is not greater than its neighboring cells in the row and column, and the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner can only decrease
   # It's consistent because moving a number results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved number is replaced by a number that is not greater than its neighboring cells in the row and column), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = sum(state[0]) + sum([row[-1] for row in state]) + sum([state[i][i] for i in range(len(state))])
   return h


print(a_star())
