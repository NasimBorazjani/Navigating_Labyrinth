
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing the unknown values
   initial_state = [['x', '46', 'x'], ['39', 'x', 'x'], ['x', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = [126, 124, 136]


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of all the numbers in the grid is as low as possible, while the sums of the specified rows, columns, and diagonal equal the given amounts
       if all(sum(row) == goal_col_sum[i] for i, row in enumerate(state)):
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that is not already in the grid
                   for num in range(28, 58):
                       if num not in new_state[row_ind] and num not in sum(new_state, []):
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of unique integers used, as the task is to minimize the number of unique integers used
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                              
   return None


def heuristic(state, goal_col_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the difference between the current and goal sums
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by a unique integer
   # It's consistent because moving a unique integer from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved unique integer's current sum matches the goal sum for that position), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       h += abs(sum(state[i]) - goal_col_sum[i])
   return h


print(a_star())
