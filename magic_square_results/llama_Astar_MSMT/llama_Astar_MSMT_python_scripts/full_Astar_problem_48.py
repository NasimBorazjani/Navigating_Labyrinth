
import heapq


def initialize():
   # Define the initial state of the magic square, as a 4x4 2d list of integers or 'x'
   initial_state = [['x', 'x', 'x', 'x'],
                    ['x', 46, 'x', 41],
                    ['x', 57, 55, 'x'],
                    ['x', 37, 'x', 'x']]


   # Define the constraints on the sums of rows and columns
   row_constraints = [None, 179, 190, None]
   col_constraints = [None, 179, 194, None]
   diagonal_constraint = 205


   # Encoding other variables of the problem
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, row_constraints, col_constraints, diagonal_constraint, num_rows, num_cols, visited_costs, queue


def a_star():
  
   initial_state, row_constraints, col_constraints, diagonal_constraint, num_rows, num_cols, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all the 'x's in the grid are replaced with unique integers that satisfy all the constraints
       if all(all(row) for row in state) and check_constraints(state, row_constraints, col_constraints, diagonal_constraint):
           return actions


       # Generate all valid actions from the current state, which includes replacing an 'x' with a unique integer
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   # Generate the new state
                   new_state = [list(row) for row in state]
                   # Replace the 'x' with a unique integer
                   new_state[row_ind][col_ind] = find_unique_integer(new_state)
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, row_constraints, col_constraints, diagonal_constraint), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
                  
   return None


def heuristic(state, row_constraints, col_constraints, diagonal_constraint):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sum of each row/column and the goal sum constraint for that row/column
   # This heuristic relaxes the constraint that the sum of the numbers in each row and column must be equal to the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as the sum of the absolute differences is always equal to or less than the sum of the absolute differences from the current state to the goal state
   # It's consistent because moving a number from one bucket to another reduces the heuristic cost of the successor node by a max of the absolute difference between the current sum and the goal sum for each row/column, which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       row_sum = sum(state[row_ind])
       if row_constraints[row_ind] is not None:
           h += abs(row_sum - row_constraints[row_ind])
   for col_ind in range(len(state[0])):
       col_sum = sum(state[row_ind][col_ind] for row_ind in range(len(state)))
       if col_constraints[col_ind] is not None:
           h += abs(col_sum - col_constraints[col_ind])
   diagonal_sum = sum(state[i][i] for i in range(len(state)))
   h += abs(diagonal_sum - diagonal_constraint)
   return h


print(a_star())
