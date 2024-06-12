
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 57], [None, None, None], [33, 43, 47]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 23
   range_end = 66


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current grid state and the sum of the numbers in the topmost row, the rightmost column, and the diagonal
   # Calculate the initial sum
   initial_sum = sum(initial_state[0]) + sum(row[-1] for row in initial_state) + initial_state[0][0] + initial_state[2][2]
   initial_state_info = (initial_state, initial_sum)
   # The cost of the initial state is 0, as no replacements have been made
   queue = [(initial_sum, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, state_sum = state_info


       # If the grid is completely filled with unique integers, return the actions taken
       if all(None not in row for row in state):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with an integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Iterate through the range of possible numbers
                   for num in range(range_start, range_end + 1):
                       # Check if the number is valid, ie if it maintains the consecutive order in each row and column
                       if (row_ind > 0 and state[row_ind - 1][col_ind] < num < state[row_ind][col_ind]) or (row_ind < num_rows - 1 and state[row_ind][col_ind] < num < state[row_ind + 1][col_ind]) or (col_ind > 0 and state[row_ind][col_ind - 1] < num < state[row_ind][col_ind]) or (col_ind < num_cols - 1 and state[row_ind][col_ind] < num < state[row_ind][col_ind + 1]) or (row_ind > 0 and col_ind > 0 and state[row_ind - 1][col_ind - 1] < num < state[row_ind][col_ind]) or (row_ind < num_rows - 1 and col_ind < num_cols - 1 and state[row_ind][col_ind] < num < state[row_ind + 1][col_ind + 1]):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # Calculate the new sum
                           new_sum = state_sum - (range_end - num)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_sum + heuristic(new_state, state_sum), new_cost, actions + [(row_ind, col_ind, num)], (new_state, new_sum)))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the difference between the current sum of the numbers in the grid and the goal sum
   # This heuristic relaxes the constraint that the numbers in the grid must be unique, as it only measures the difference between the current and goal sums
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must decrease the heuristic cost of the successor node
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of the difference between the current and goal sums, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return goal_sum - sum(state[0]) - sum(row[-1] for row in state) - state[0][0] - state[-1][-1]


print(a_star())
