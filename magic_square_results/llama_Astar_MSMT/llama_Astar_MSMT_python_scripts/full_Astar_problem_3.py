
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[25, None, None], [None, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 99
   goal_row_sum = 86
   goal_diag_sum = 76


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the magic square and the sum of all the numbers in the magic square
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diag_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, state_sum = state_info


       # If the current state of the magic square satisfies all the given conditions, return the actions taken
       if state[0][1] is not None and state[0][2] is not None and state[1][0] is not None and state[1][1] is not None and state[1][2] is not None and state[2][0] is not None and state[2][1] is not None and state[2][2] is not None and sum(state[0]) == goal_row_sum and sum(state[1]) == goal_row_sum and sum(state[2]) == goal_row_sum and state[0][0] + state[1][1] + state[2][2] == goal_diag_sum and state[0][2] + state[1][1] + state[2][0] == goal_diag_sum and sum(state[i][1] for i in range(num_rows)) == goal_col_sum and state_sum == 20 + 21 + 22 + 23 + 24 + 26 + 27 + 28 + 29 + 30 + 31 + 32 + 33 + 34 + 35 + 36 + 37 + 38 + 39:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   for num in range(20, 40):
                       # Check if the new state would be valid, ie the number is unique and does not violate any of the given conditions
                       if num not in state[0] and num not in state[1] and num not in state[2]:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the magic square
                           new_cost = g + 1
                           new_state_sum = state_sum + num


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum, goal_row_sum, goal_diag_sum), new_cost, actions + [(row, col, num)], (new_state, new_state_sum)))
   return None


def heuristic(state, goal_col_sum, goal_row_sum, goal_diag_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal conditions
   # This heuristic relaxes the constraint that the numbers in the magic square must be unique and in the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's value matches the goal condition for that position but not in the old one), which is equal to the cost of reaching the successor node
   h = 0
   for row in range(len(state)):
       h += abs(sum(state[row]) - goal_row_sum)
       h += abs(sum(state[i][row] for i in range(len(state))) - goal_col_sum)
   h += abs(state[0][0] + state[1][1] + state[2][2] - goal_diag_sum)
   h += abs(state[0][2] + state[1][1] + state[2][0] - goal_diag_sum)
   return h


print(a_star())
