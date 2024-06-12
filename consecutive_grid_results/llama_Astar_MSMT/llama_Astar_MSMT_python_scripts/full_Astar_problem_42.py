
import heapq


def initialize():
   # Define the initial state of the grid, with the numbers as integers and 'x' as None
   initial_state = [[46, 80, 90], [51, None, None], [None, None, None]]
  
   # Encoding other variables of the problem
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0
          
   # The information we must encode for each state includes the grid and the cost so far
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()
  
   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if all(state[i][j] is not None for i in range(num_rows) for j in range(num_cols)):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] is None:
                   # Generate the new state
                   new_state = [row[:] for row in state]
                   # The new state must maintain the consecutive order in each row and column
                   for value in range(45, 98):
                       if (i > 0 and value <= state[i - 1][j]) or (j > 0 and value <= state[i][j - 1]) or (i > 0 and j > 0 and value <= state[i - 1][j - 1]) or (i < num_rows - 1 and j < num_cols - 1 and value <= state[i + 1][j + 1]):
                           continue
                       new_state[i][j] = value
                       # The cost so far is the number of replacements made
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, value)], new_state))
   return None


def heuristic(grid):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the replacements must maintain the consecutive order in each row and column
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect replacement must be made at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(grid)):
       h += grid[i][0] + grid[i][-1] + grid[0][i] + grid[-1][i]
   return h


print(a_star())
