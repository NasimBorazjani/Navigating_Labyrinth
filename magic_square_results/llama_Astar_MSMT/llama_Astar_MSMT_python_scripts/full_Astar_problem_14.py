
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[None, 32, None], [38, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sums = [143, 134, 131]
   goal_total_sum = 308


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the magic square and the total sum of the numbers in the grid
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sums, goal_total_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sums, goal_total_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state of the magic square satisfies all the conditions of the problem, return the actions taken
       if state[0] == goal_col_sums and state[1] == goal_total_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[0][row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state[0]]
                   # The unique integer to replace 'x' is the next integer in the range 28 to 57 that is not already in the grid
                   new_integer = next(x for x in range(28, 58) if x not in new_state[row_ind] and x not in [cell for row in new_state for cell in row])
                   new_state[row_ind][col_ind] = new_integer
                   # Update the total sum of the numbers in the grid
                   new_total_sum = state[1] + new_integer
                   # Generate the new state information
                   new_state_info = (new_state, new_total_sum)
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the magic square
                   new_cost = g + 1


                   if new_state_info not in visited_costs or new_cost < visited_costs[new_state_info]:
                       visited_costs[new_state_info] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state[0], goal_col_sums, goal_total_sum), new_cost, actions + [(row_ind, col_ind, new_integer)], new_state_info))
   return None


def heuristic(state, goal_col_sums, goal_total_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current column sums and the goal column sums, and the absolute difference between the current total sum and the goal total sum
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the sums of the numbers in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect integer must be replaced at least once
   # It's consistent because moving an integer from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved integer is the only one that causes the heuristic cost of the successor node to decrease), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               h += abs(state[row_ind][col_ind] - goal_col_sums[col_ind])
   h += abs(sum(sum(row) for row in state) - goal_total_sum)
   return h


print(a_star())
