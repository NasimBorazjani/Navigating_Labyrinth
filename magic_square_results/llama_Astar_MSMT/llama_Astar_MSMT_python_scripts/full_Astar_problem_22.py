
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing the unknown numbers
   initial_state = [['x', 'x', 'x'],
                    ['x', 'x', 'x'],
                    ['x', '43', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = [120, 99, 105]


   visited_costs = {}
   visited_costs[tuple(row[:] for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of the numbers in the grid equals the sum of the numbers in the goal state
       if sum(sum(row) for row in state) == sum(goal_col_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   for num in range(12, 47):
                       # Check if the new state would be valid, ie the sum of the numbers in the row, column, and diagonal is as required
                       if (sum(state[row_ind]) + num == goal_col_sum[row_ind] and
                           sum(state[col][col_ind] for col in range(num_cols)) + num == goal_col_sum[num_cols] and
                           sum(state[i][i] for i in range(num_rows)) + num == goal_col_sum[num_rows]):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, goal_col_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal_col_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of the numbers in the grid and the goal sum
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must equal the sum of the numbers in the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's correct value is the same as the current value), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] != goal_col_sum[row_ind]:
               h += abs(state[row_ind][col_ind] - goal_col_sum[row_ind])
   return h


print(a_star())
