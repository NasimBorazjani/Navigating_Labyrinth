
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 59, None], [47, None, 62], [None, 50, 63]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 41
   range_end = 79


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the sum of the numbers in the topmost row, the rightmost column, and the diagonal
   # The initial state has a sum of 0, as all numbers are hidden
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, state_sum = state_info


       # If the sum of the numbers in the state is equal to the sum of the numbers in the range, return the actions taken
       if state_sum == range_start + range_end:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   for num in range(range_start, range_end + 1):
                       # Check if the new state would be valid, ie the number is not already in the row, column, or diagonal
                       if num not in state[row] and num not in [row[col] for row in state] and num not in [state[i][i] for i in range(num_rows)]:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1
                           # The sum of the numbers in the new state is the sum of the numbers in the current state plus the new number
                           new_state_sum = state_sum + num


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, range_start, range_end) - new_state_sum, new_cost, actions + [(row, col, num)], (new_state, new_state_sum)))
   return None


def heuristic(state, range_start, range_end):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the state minus the sum of the numbers in the range
   # This heuristic relaxes the constraint that the numbers in the state must be unique and in the range
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one state to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is in the range), which is equal to the cost of reaching the successor node
   return sum(sum(row) for row in state) - (range_end - range_start + 1) * (range_end - range_start) // 2


print(a_star())
