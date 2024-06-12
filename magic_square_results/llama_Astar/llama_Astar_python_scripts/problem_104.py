
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 69, None, None],
                    [None, 62, None, None],
                    [None, 82, 40, None],
                    [None, 87, 78, 80]]

   # Define the constraints for the rows and columns
   row_constraints = [None, 214, None, None]
   col_constraints = [None, 300, 191, None]
   diagonal_constraint = 249

   # Define the range of numbers that can be used to replace 'x'
   num_range = range(36, 93)

   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]

   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state
       # The goal state is when the sums of the rows, columns, and diagonal are equal to the given amounts
       if all(sum(row) == row_constraints[i] for i, row in enumerate(state)) and all(sum(col) == col_constraints[i] for i, col in enumerate(zip(*state))) and sum(state[i][i] for i in range(len(state))) == diagonal_constraint:
           return actions

       # Generate all possible actions from the current state, which includes replacing an 'x' with a number from the range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   for num in num_range:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = num
                       new_state = [tuple(row) for row in new_state]
                       # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                       new_cost = g + 1

                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_constraints, col_constraints, diagonal_constraint), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, row_constraints, col_constraints, diagonal_constraint):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the given amounts
   # This heuristic relaxes the constraint that the sums of rows, columns, and diagonal must be equal to the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by a replacement
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is part of the incorrect sum), which is equal to the cost of reaching the successor node
   h = 0
   for i, row in enumerate(state):
       h += abs(sum(row) - row_constraints[i])
   for i, col in enumerate(zip(*state)):
       h += abs(sum(col) - col_constraints[i])
   h += abs(sum(state[i][i] for i in range(len(state))) - diagonal_constraint)
   return h


print(a_star())
