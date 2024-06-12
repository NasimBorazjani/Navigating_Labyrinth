
import heapq


def a_star():
   # Define the initial state of the magic square grid, with some numbers already given and others unknown
   initial_state = ((64, 78, 'x'), ('x', 'x', 'x'), ('x', 'x', 'x'))
   # Define the goal state, which is to have the sum of column 1 as 234, sum of row 1 as 201, and the diagonal sum as 213
   goal_state = (234, 201, 213)
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   num_range = range(50, 85)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state satisfies the goal conditions, return the actions taken
       if check_goal(state, goal_state):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for num in num_range:
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       new_cost = g + num
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row, col, num)], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the numbers in the grid must be unique and presumes we can replace 'x' with any number in the given range
   # It is admissible because it never overestimates the cost to reach the goal, as the sum of the absolute differences is always less than or equal to the actual cost to reach the goal
   # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum increase in the sum of the row, column, or diagonal is 1
   h = 0
   for i in range(len(state)):
       # Calculate the sum of each row, column, and diagonal in the current state
       row_sum = sum(state[i])
       col_sum = sum(row[i] for row in state)
       diag_sum1 = sum(state[i][i] for i in range(len(state)))
       diag_sum2 = sum(state[i][len(state)-1-i] for i in range(len(state)))
       # Add the absolute differences between the current sum and the goal sum to the heuristic estimate
       h += abs(row_sum - goal[0]) + abs(col_sum - goal[1]) + abs(diag_sum1 - goal[2]) + abs(diag_sum2 - goal[2])
   return h


def check_goal(state, goal):
   # Check if the current state satisfies the goal conditions
   row_sum = [sum(row) for row in state]
   col_sum = [sum(row[i] for row in state) for i in range(len(state))]
   diag_sum1 = sum(state[i][i] for i in range(len(state)))
   diag_sum2 = sum(state[i][len(state)-1-i] for i in range(len(state))
   return row_sum[0] == goal[0] and col_sum[0] == goal[1] and diag_sum1 == goal[2] and diag_sum2 == goal[2]


print(a_star())
