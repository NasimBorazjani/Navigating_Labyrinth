
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[None, 52, None], [None, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = [166, 192, 184]


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the magic square and the total sum of all the numbers in the magic square
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, state_sum = state_info


       # If the sum of all the numbers in the magic square in the current state is equal to the goal sum, return the actions taken
       if state_sum == sum(goal_col_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   for num in range(48, 78):
                       # Check if the new state would be valid, ie the new state must maintain the constraint on the sum of each row, column, and diagonal
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       new_state_sum = state_sum + num
                       if all(sum(row) == goal_col_sum[i] for i, row in enumerate(new_state)) and all(sum(new_state[i][j] for i in range(num_rows)) == goal_col_sum[j] for j in range(num_cols)) and sum(new_state[i][i] for i in range(num_rows)) == goal_col_sum[2] and sum(new_state[i][num_rows - i - 1] for i in range(num_rows)) == goal_col_sum[2]:
                           # Generate the new state
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the magic square
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_info, goal_col_sum), new_cost, actions + [(row, col, num)], (new_state, new_state_sum)))
   return None


def heuristic(state_info, goal_col_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be equal to the goal sum
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of the difference between the goal sum and the current sum, which is equal to the cost of reaching the successor node
   h = 0
   state, state_sum = state_info
   for i in range(num_rows):
       h += abs(sum(state[i]) - goal_col_sum[i])
       h += abs(sum(state[j][i] for j in range(num_rows)) - goal_col_sum[i])
   h += abs(sum(state[i][i] for i in range(num_rows)) - goal_col_sum[2])
   h += abs(sum(state[i][num_rows - i - 1] for i in range(num_rows)) - goal_col_sum[2])
   return h


print(a_star())
