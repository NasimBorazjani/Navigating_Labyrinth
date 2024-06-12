
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[62, 82, None], [None, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sum = 233
   row_sum = 207
   diagonal_sum = 185


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of the specified rows, columns, and diagonal equals the given amounts
       if sum(state[i][j] for i in range(num_rows) for j in range(num_cols)) == column_sum + row_sum + diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the next integer in the range that has not been used in the grid
                   new_value = next(x for x in range(50, 85) if x not in new_state)
                   new_state[row][col] = new_value
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of unique integers used, as the task is to minimize the number of unique integers used
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, new_value)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the unique integers must be in the given range and the sum of all of the numbers in the grid is as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a unique integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved integer is the same in the current and goal states), which is equal to the cost of reaching the successor node
   h = 0
   for row in range(num_rows):
       for col in range(num_cols):
           h += abs(state[row][col] - goal_state[row][col])
   return h


print(a_star())
