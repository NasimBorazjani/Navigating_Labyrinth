
import heapq


def initialize():
   # Define the initial state of the grid, with 'x's represented as None
   initial_state = [[None, None, None], [None, None, None], [37, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sums = [125, 157, 138]


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the total sum of all the numbers in the grid
   initial_state_info = (initial_state, 37)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sums, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sums, visited_costs, queue = initialize()


   while queue:
       _, g, actions, (state, total_sum) = heapq.heappop(queue)


       # Check if the current state is the goal state
       if all(sum(row) == goal_col_sums[i] for i, row in enumerate(state)) and total_sum == sum(goal_col_sums):
           return actions


       # Generate all possible actions from the current state, which includes placing a unique integer in each 'x' position in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to be placed is the smallest integer that has not been placed in the grid yet
                   new_integer = next(i for i in range(35, 60) if i not in new_state[row_ind] and i not in sum(new_state, []))
                   new_state[row_ind][col_ind] = new_integer
                   new_total_sum = total_sum + new_integer
                   new_state_info = (new_state, new_total_sum)
                   # The cost so far is the total sum of all the numbers in the grid, as the task is to minimize the total sum
                   new_cost = new_total_sum


                   if new_state_info not in visited_costs or new_cost < visited_costs[new_state_info]:
                       visited_costs[new_state_info] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state_info, goal_col_sums), new_cost, actions + [(row_ind, col_ind, new_integer)], new_state_info))
   return None


def heuristic(state_info, goal_col_sums):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current column sums and the goal column sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it does not take into account the uniqueness of the integers
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched column sum must be adjusted at least once
   # It's consistent because moving a unique integer from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved integer is the only one in its column, and the column sum is now equal to the goal sum), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   state, _ = state_info
   for i in range(len(goal_col_sums)):
       h += abs(sum(row[i] for row in state) - goal_col_sums[i])
   return h


print(a_star())
