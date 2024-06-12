
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, 60], [47, None, 62, 65], [None, 58, 67, 68], [54, None, 74, None]]
   # The range of numbers that can be used for replacement
   num_range = range(36, 76)
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the grid configuration and the cost of reaching that configuration
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_range, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_range, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, where all cells in the grid are filled with unique numbers
       if all(x is not None for row in state for x in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique number from the range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   for num in num_range:
                       # Check if the new number is valid, ie it does not violate the conditions of the grid (strictly increasing/decreasing rows/columns)
                       if is_valid_placement(state, row, col, num):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, num_range)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row, col, num)], new_state))
   return None


def is_valid_placement(state, row, col, num):
   # Check if placing the new number in the current state would violate the conditions of the grid
   # This function checks if placing num in state[row][col] would result in a strictly increasing or decreasing row, column, or diagonal
   # It returns True if the placement is valid, False otherwise
   # This function is a helper function to the a_star function and is used to filter the valid actions generated in the a_star function
   if row > 0 and state[row - 1][col] > num:
       return False
   if row < num_rows - 1 and state[row + 1][col] < num:
       return False
   if col > 0 and state[row][col - 1] > num:
       return False
   if col < num_cols - 1 and state[row][col + 1] < num:
       return False
   if row > col and state[row - 1][col + 1] > num:
       return False
   if row < num_rows - 1 - col and state[row + 1][col + 1] < num:
       return False
   return True


def heuristic(state, num_range):
   # An admissible and consistent heuristic for this problem is the sum of the numbers that are not yet placed in the grid
   # This heuristic relaxes the constraint that the number of replacements must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each unplaced number must be placed at least once
   # It's consistent because the estimated cost of the next node is higher if a number is placed, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum amount of unplaced numbers that can be placed in the grid is by using the largest number that has not been placed yet. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = sum(num for num in num_range if num not in state)
   return h


print(a_star())
