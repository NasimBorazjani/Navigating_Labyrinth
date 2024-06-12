
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' replaced by None for easier handling
   initial_state = [[41, None, None], [42, 57, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the sum of the numbers in the topmost row, the rightmost column, and the diagonal
   # The initial state of the grid is the given initial state, and the initial sum is the sum of the numbers in the initial state
   initial_state_info = (initial_state, 41 + 42 + 57)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, sum_so_far = state_info


       # If the current state of the grid is the goal state, where all cells are filled, return the actions taken
       if all(cell is not None for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       # Iterate through the cells in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               # Check if the current cell is an 'x'
               if state[row_ind][col_ind] is None:
                   # Iterate through the possible numbers for the cell
                   for num in range(26, 75):
                       # Check if the number is valid, ie if it maintains the consecutive order in the row and column
                       if (row_ind > 0 and state[row_ind - 1][col_ind] < num < state[row_ind][col_ind - 1]) or (row_ind == 0 or col_ind == 0):
                           # Generate the new state
                           new_state = [row[:] for row in state]
                           new_state[row_ind][col_ind] = num
                           # Calculate the new sum
                           new_sum = sum_so_far - sum(row) + sum(new_state)
                           # The cost so far is the sum of the numbers in the new state, as the task is to minimize the sum
                           new_cost = new_sum


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, new_state), new_cost, actions + [(row_ind, col_ind, num)], (new_state, new_sum)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the difference between the current sum of the numbers in the grid and the goal sum
   # This heuristic relaxes the constraint that the numbers must be unique and the sum of the numbers in the topmost row, the rightmost column, and the diagonal must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each action taken reduces the heuristic cost of the successor node
   # It's consistent because moving a number from one cell to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the same in the old and new state), which is equal to the cost of reaching the successor node
   return sum(goal) - sum(state)


print(a_star())
