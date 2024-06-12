
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[37, None, 26], [None, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sums = [111, 94, 82]


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the magic square and the total sum of the numbers in the square
   initial_state_info = (initial_state, 0)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_col_sums, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_col_sums, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, total_sum = state_info


       # If the current state of the magic square satisfies the given conditions, return the actions taken
       if all(sum(row) == goal_col_sums[i] for i, row in enumerate(state)) and total_sum == sum(goal_col_sums):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   for num in range(19, 44):
                       # Check if the new state would be valid, ie the total sum of the numbers in the square does not exceed the sum of the given amounts
                       if total_sum + num <= sum(goal_col_sums):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the magic square
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_info, goal_col_sums), new_cost, actions + [(row_ind, col_ind, num)], (new_state, total_sum + num)))
   return None


def heuristic(state_info, goal_col_sums):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each column and the goal sum for that column
   # This heuristic relaxes the constraint that the total sum of the numbers in the square must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be non-negative
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of the difference between the goal sum and the current sum for that column, which is equal to the cost of reaching the successor node
   h = 0
   state, total_sum = state_info
   for i in range(len(state)):
       h += abs(sum(state[i]) - goal_col_sums[i])
   return h


print(a_star())
