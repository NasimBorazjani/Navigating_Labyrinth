
import heapq


def a_star():
   # Define the initial state of the magic square problem, with the grid represented as a 2D tuple
   initial_state = (('x', 16, 'x'), ('x', 'x', 'x'), (45, 'x', 'x'))
   # Define the goal state, which is the sum of the specified rows, columns, and diagonal
   goal_state = (67, 60, 89)
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   num_values = 40  # Number of unique integers in the given range


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state satisfies the goal state, return the actions taken
       if check_goal_state(state, goal_state):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with any unique integer in the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for value in range(9, 49):
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = value
                       new_state = tuple(tuple(row) for row in new_state)
                       new_cost = g + value
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row, col, value)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the current sum of rows, columns, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must equal the goal sum, as it presumes we can adjust the numbers to reach the goal sum
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be adjusted to reach the goal sum
   # It is consistent because the estimated cost of the next node is higher if the sum of the rows, columns, and diagonal is further from the goal sum, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to the sum is 1, which is exactly the decrease in the heuristic estimate for the successor node
   h = 0
   for i in range(len(state)):
       # Calculate the sum of each row and compare it to the goal sum
       row_sum = sum(state[i])
       h += abs(row_sum - goal[i])
       # Calculate the sum of each column and compare it to the goal sum
       col_sum = sum(row[i] for row in state)
       h += abs(col_sum - goal[i])
   # Calculate the sum of the diagonal from the top right to the bottom left corner and compare it to the goal sum
   diagonal_sum = sum(state[i][len(state)-1-i] for i in range(len(state)))
   h += abs(diagonal_sum - goal[len(goal)-1])
   return h


def check_goal_state(state, goal):
   # Check if the current state satisfies the goal state, ie the sum of the specified rows, columns, and diagonal equals the given amounts
   for i in range(len(state)):
       row_sum = sum(state[i])
       if row_sum != goal[i]:
           return False
       col_sum = sum(row[i] for row in state)
       if col_sum != goal[i]
           return False
   diagonal_sum = sum(state[i][len(state)-1-i] for i in range(len(state)))
   if diagonal_sum != goal[len(goal)-1]:
       return False
   return True


print(a_star())
