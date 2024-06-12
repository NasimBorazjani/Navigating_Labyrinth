
import heapq


def initialize():
   # Define the initial state of the grid, as a 2d list with 'x' representing unknown numbers
   initial_state = [['x', 'x', 'x'],
                    ['x', 'x', 'x'],
                    ['41', 'x', 'x']]

   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 135
   goal_row_sum = 134
   goal_diag_sum = 122


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of the numbers in the specified rows, columns, and diagonal equals the given amounts
       if sum(state[0][0], state[1][1], state[2][2]) == goal_diag_sum and sum(state[0][i] for i in range(num_cols)) == goal_col_sum and sum(state[i][0] for i in range(num_rows)) == goal_row_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   for num in range(31, 76):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = num
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required to reach the goal state
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if tuple(tuple(row) for row in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(row) for row in new_state)]:
                           visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of the specified rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is the largest in its row, column, or diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] == 'x':
               h += 1
   return h


print(a_star())
