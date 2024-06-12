
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing the unknown values
   initial_state = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 19]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = [71, 82, 70]
   total_sum = 19 + 71 + 82 + 70


   visited_costs = {}
   visited_costs[initial_state] = 0
  
   # The information we must encode for each state includes the current state of the grid and the current total sum of the grid
   initial_state_info = (initial_state, 0)
   # Since we are trying to minimize the total sum, we use a priority queue to pop the state with the lowest total sum
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, total_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, total_sum, visited_costs, queue = initialize()
  
   while queue:
       _, g, actions, (state, total_sum) = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if the sum of the specified rows, columns, and diagonal equals the given amounts
       if all(sum(row) == goal_col_sum[i] and sum(state[i]) == goal_col_sum[i] for i in range(num_rows)) and sum(state) == total_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   for num in range(12, 47):
                       # Check if the new state would be valid, ie the sum of the specified rows, columns, and diagonal remains equal to the given amounts
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = num
                       new_total_sum = total_sum + num
                       new_state_info = (new_state, new_total_sum)
                       # If the new state is unvisited or we found a new path with a lower total sum, add it to the queue of un-visited states
                       if new_state_info not in visited_costs or new_total_sum < visited_costs[new_state_info]:
                           visited_costs[new_state_info] = new_total_sum
                           heapq.heappush(queue, (new_total_sum + heuristic(new_state_info, goal_col_sum, total_sum), g + 1, actions + [(row_ind, col_ind, num)], new_state_info))
   return None


def heuristic(state_info, goal_col_sum, total_sum):
   # An admissible and consistent heuristic for this problem is the difference between the current total sum and the lowest possible total sum, which is the sum of the given amounts
   # This heuristic relaxes the constraint that the sum of the specified rows, columns, and diagonal must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect value must be replaced at least once
   # It's consistent because moving a value from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved value is the incorrect one), which is equal to the cost of reaching the successor node
   return total_sum - sum(goal_col_sum)


print(a_star())
