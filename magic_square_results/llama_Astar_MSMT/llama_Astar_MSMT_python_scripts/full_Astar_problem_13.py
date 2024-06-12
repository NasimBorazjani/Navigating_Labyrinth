
import heapq


def initialize():
   # Define the initial state of the grid, with the given numbers represented as integers and 'x' as 'x'
   initial_state = [['41', 'x', 'x'], ['34', 'x', 'x'], ['x', 'x', 'x']]
  
   # Encoding other variables of the problem
   num_rows = 3
   num_cols = 3
   goal_col_sum = 129
   goal_row_sum = 133
   goal_diag_sum = 136


   visited_costs = {}
   visited_costs[tuple(row[:] for row in initial_state)] = 0


   # The information we must encode for each state includes the current state of the grid and the total sum of all numbers in the grid
   initial_state_info = (initial_state, 0)
   # The priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the total sum of all numbers in the grid
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, initial_state_info, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, initial_state_info, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, total_sum = state_info


       # If the current state satisfies all the given conditions, return the actions taken
       if sum(int(row[0]) for row in state) == goal_row_sum and sum(int(col[0]) for col in zip(*state)) == goal_col_sum and int(state[0][0]) + int(state[1][1]) + int(state[2][2]) == goal_diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   for num in range(28, 58):
                       # Check if the new state would be valid, ie the new number must not be in the same row, column, or diagonal
                       if num not in state[row_ind] and num not in zip(*state)[col_ind] and num not in [state[i][i] for i in range(num_rows)] and num not in [state[i][num_rows - i - 1] for i in range(num_rows)]:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the total sum of all numbers in the grid, as the task is to minimize the total sum of all numbers in the grid
                           new_cost = g + num


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_info, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row_ind, col_ind, num)], (new_state, new_cost)))
   return None


def heuristic(state_info, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of the absolute difference between the goal sum and the current sum, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the absolute difference between the goal sum and the current sum) + h(n)
   state, total_sum = state_info
   h = abs(sum(int(row[0]) for row in state) - goal_row_sum) + abs(sum(int(col[0]) for col in zip(*state)) - goal_col_sum) + abs(int(state[0][0]) + int(state[1][1]) + int(state[2][2]) - goal_diag_sum)
   return h


print(a_star())
