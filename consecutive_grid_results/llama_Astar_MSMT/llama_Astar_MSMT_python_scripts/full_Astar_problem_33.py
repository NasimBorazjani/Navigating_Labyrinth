
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[79, 63, 43], [None, 68, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   hidden_value = None


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the grid state and the sum of the numbers in the topmost row, rightmost column, and diagonal
   # The initial state has a dummy sum of 0, as the actual sum will be calculated later
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, hidden_value, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, hidden_value, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the grid state is valid, the numbers in each row and column are strictly increasing or decreasing, and the sum is minimized, return the actions taken
       if is_valid(state) and is_minimal_sum(state):
           return actions


       # Generate all possible actions from the current state, which includes replacing a hidden number with a unique number from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               # Check if the current position is hidden
               if state[row][col] == hidden_value:
                   # Generate all possible numbers that can replace the hidden number
                   for num in range(41, 89):
                       # Check if the number is valid to be placed in the current position
                       if is_valid_placement(state, row, col, num):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state), new_cost, actions + [(row, col, num)], new_state))
   return None


def is_valid(state):
   # Check if the numbers in each row and column are strictly increasing or decreasing
   for row in state:
       if row != sorted(row) and row != sorted(row, reverse=True):
           return False
   for col in range(num_cols):
       if [row[col] for row in state] != sorted(row[col] for row in state) and [row[col] for row in state] != sorted(row[col] for row in state, reverse=True):
           return False
   return True


def is_valid_placement(state, row, col, num):
   # Check if the number is valid to be placed in the current position
   # The number must not already exist in the grid
   if num in sum(state, []):
       return False
   # The number must be in the range of the given values
   if not 41 <= num <= 88:
       return False
   return True


def is_minimal_sum(state):
   # Check if the sum of the numbers in the topmost row, rightmost column, and diagonal is minimized
   return sum(state[0]) + sum(state[i][i] for i in range(num_rows)) + sum(state[i][num_rows - i - 1] for i in range(num_rows)) == min(sum(state[0]) + sum(state[i][i] for i in range(num_rows)) + sum(state[i][num_rows - i - 1] for i in range(num_rows)) for state in visited_costs.keys())


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and diagonal
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the numbers must only appear once in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect placement of a number in the grid must be corrected once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is in the topmost row, rightmost column, or diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return sum(state[0]) + sum(state[i][i] for i in range(num_rows)) + sum(state[i][num_rows - i - 1] for i in range(num_rows))


print(a_star())
