
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing the unknown numbers
   initial_state = [['x', 'x', 'x'],
                    ['x', 'x', 66],
                    ['x', 'x', 'x']]

   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_column_sum = 200
   goal_row_sum = 191
   goal_diagonal_sum = 201


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_column_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_column_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of the specified rows, columns, and diagonal equals the given amounts
       if sum(state[0][2], state[1][2], state[2][0]) == goal_column_sum and sum(state[0][0], state[1][0], state[2][2]) == goal_row_sum and state[0][0] + state[1][1] + state[2][2] == goal_diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for num in range(48, 78):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_column_sum, goal_row_sum, goal_diagonal_sum), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state, goal_column_sum, goal_row_sum, goal_diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of the specified rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's correct value is the same as the current one), which is equal to the cost of reaching the successor node
   h = abs(sum(state[0][2], state[1][2], state[2][0]) - goal_column_sum) + abs(sum(state[0][0], state[1][0], state[2][2]) - goal_row_sum) + abs(state[0][0] + state[1][1] + state[2][2] - goal_diagonal_sum)
   return h


print(a_star())
