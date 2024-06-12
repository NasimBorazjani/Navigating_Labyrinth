
import heapq


def initialize():
   # Define the initial state of the magic square, as a 2d list of strings, representing the numbers or 'x'
   initial_state = [['38', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x'],
                    ['x', '39', '40', '27'],
                    ['32', '46', 'x', '25']]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   row_constraints = [None, 149, 178, None]
   col_constraints = [None, 135, 130, None]
   diagonal_constraint = 151


   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, row_constraints, col_constraints, diagonal_constraint, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, row_constraints, col_constraints, diagonal_constraint, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state satisfies all the constraints, return the actions taken
       if constraints_satisfied(state, row_constraints, col_constraints, diagonal_constraint):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Try placing a unique integer in the current position
                   for num in range(24, 51):
                       if num not in map(int, new_state[row_ind]) and num not in map(int, zip(*new_state)[col_ind]):
                           new_state[row_ind][col_ind] = str(num)
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to satisfy the constraints
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, row_constraints, col_constraints, diagonal_constraint)
                               # In the problem statement the grid is indexed starting from 0
                               heappush(queue, (new_cost + h, new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def constraints_satisfied(state, row_constraints, col_constraints, diagonal_constraint):
   # Check if the current state satisfies all the constraints
   # Check the row constraints
   for row_ind in range(len(row_constraints)):
       if row_constraints[row_ind] is not None and sum(map(int, state[row_ind])) != row_constraints[row_ind]:
           return False
   # Check the column constraints
   for col_ind in range(len(col_constraints)):
       if col_constraints[col_ind] is not None and sum(map(int, zip(*state)[col_ind])) != col_constraints[col_ind]:
           return False
   # Check the diagonal constraint
   if diagonal_constraint is not None and sum(map(int, [state[i][i] for i in range(len(state))])) != diagonal_constraint:
       return False
   return True


def heuristic(state, row_constraints, col_constraints, diagonal_constraint):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that each number can be in the final grid only once
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced with its correct value
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number's correct value is not in the grid, and the old value is not in the same row, column, or diagonal as the new value), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(row_constraints)):
       if row_constraints[row_ind] is not None:
           h += abs(sum(map(int, state[row_ind])) - row_constraints[row_ind])
   for col_ind in range(len(col_constraints)):
       if col_constraints[col_ind] is not None:
           h += abs(sum(map(int, zip(*state)[col_ind])) - col_constraints[col_ind])
   if diagonal_constraint is not None:
       h += abs(sum(map(int, [state[i][i] for i in range(len(state))])) - diagonal_constraint)
   return h


print(a_star())
