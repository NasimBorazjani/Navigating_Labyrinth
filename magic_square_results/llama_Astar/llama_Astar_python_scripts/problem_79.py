
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 46, None, 22],
                    [None, None, 36, 15],
                    [47, None, None, 25],
                    [None, None, 53, None]]
   # Define the goal state, with the sums of rows and columns
   goal_state = ([None, 146, 168, None], [None, None, 36, 15], [47, None, None, 25], [None, None, 53, None])
   # Define the constraints on the sums of rows and columns
   row_constraints = [None, 118, 120, None]
   col_constraints = [None, 146, 168, None]
   diagonal_constraint = 91
   # Define the range of numbers that can be used to replace 'x'
   num_range = range(13, 55)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   for num in num_range:
                       # Generate the new state
                       new_state = [row[:] for row in state]
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of numbers replaced, as the task is to minimize the number of numbers replaced
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, row_constraints, col_constraints, diagonal_constraint), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal, row_constraints, col_constraints, diagonal_constraint):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the sums of rows and columns must be equal to the given amounts and the sum of the numbers in the grid is as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is the largest difference), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               # Calculate the difference between the current state and the goal state
               row_diff = abs(sum(state[row_ind]) - row_constraints[row_ind])
               col_diff = abs(sum(state[col_ind]) - col_constraints[col_ind])
               diagonal_diff = abs(sum(state[i][i] for i in range(len(state))) - diagonal_constraint)
               h += row_diff + col_diff + diagonal_diff
   return h


print(a_star())
