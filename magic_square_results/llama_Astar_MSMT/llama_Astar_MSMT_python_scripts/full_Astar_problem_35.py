
import heapq


def initialize():
   # Define the initial state of the magic square, as a 2d list of integers and 'x'
   initial_state = [['x', 'x', 'x'], ['80', '48', 'x'], ['x', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_row_1 = 186
   goal_col_1 = 153
   goal_diag = 188


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_row_1, goal_col_1, goal_diag, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_row_1, goal_col_1, goal_diag, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of the specified rows, columns, and diagonal equals the given amounts
       if sum(state[0][i] for i in range(num_cols)) == goal_row_1 and sum(state[i][0] for i in range(num_rows)) == goal_col_1 and state[0][0] + state[1][1] + state[2][2] == goal_diag:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with an integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for num in range(40, 90):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the sum of all the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's difference with the goal is the same or less), which is equal to the cost of reaching the successor node
   h = 0
   for row in range(num_rows):
       for col in range(num_cols):
           if state[row][col] != 'x':
               h += abs(state[row][col] - goal_state[row][col])
   return h


print(a_star())
