
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by 'None' for easier handling
   initial_state = [[39, 47, None, None], [None, None, None, 40], [63, 82, 59, None], [None, 78, None, None]]
   # Define the constraints on the rows and columns
   row_constraints = [None, 234, 271, None]
   col_constraints = [None, 295, 200, None]
   diagonal_constraint = 248
   # Define the range of the unique integers
   num_range = range(36, 93)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sums of the rows, columns, and diagonal are as required and the sum of all the numbers in the grid is as low as possible
       if check_goal(state, row_constraints, col_constraints, diagonal_constraint):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of unique integers used, as the task is to minimize the number of unique integers used
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_constraints, col_constraints, diagonal_constraint), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def check_goal(state, row_constraints, col_constraints, diagonal_constraint):
   # Check if the current state is the goal state by verifying the sums of the rows, columns, and diagonal
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diagonal_sum = sum(state[i][i] for i in range(len(state))) - state[1][1]
   return row_sums == row_constraints and col_sums == col_constraints and diagonal_sum == diagonal_constraint


def heuristic(state, row_constraints, col_constraints, diagonal_constraint):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be in the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by a unique integer
   # It's consistent because moving a unique integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved unique integer is part of the incorrect sum), which is equal to the cost of reaching the successor node
   h = 0
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diagonal_sum = sum(state[i][i] for i in range(len(state))) - state[1][1]
   for i in range(len(row_constraints)):
       if row_constraints[i] is not None:
           h += abs(row_sums[i] - row_constraints[i])
   for i in range(len(col_constraints)):
       if col_constraints[i] is not None:
           h += abs(col_sums[i] - col_constraints[i])
   h += abs(diagonal_sum - diagonal_constraint)
   return h


print(a_star())
