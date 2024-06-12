
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [30, None, None], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sum = 82
   row_sum = 87
   diagonal_sum = 94


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
       if sum(row) == row_sum and sum(state[0]) == column_sum and state[0][0] + state[1][1] + state[2][2] == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the next integer in the range that is not already in the grid
                   new_value = next(x for x in range(20, 40) if x not in new_state[row_ind] + new_state[1][col_ind] + new_state[2][col_ind])
                   new_state[row_ind][col_ind] = new_value
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of unique integers used, as the task is to minimize the number of unique integers used
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, new_value)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the unique integers must be in the given range and presumes we can use any unique integer in the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one state to an adjacent state is the absolute difference between the states, which is always greater than or equal to 0
   h = 0
   for row_ind in range(num_rows):
       for col_ind in range(num_cols):
           if state[row_ind][col_ind] is None:
               h += 1
           else:
               h += abs(state[row_ind][col_ind] - goal_state[row_ind][col_ind])
   return h


print(a_star())
