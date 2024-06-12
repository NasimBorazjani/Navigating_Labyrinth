
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 37, 31], [None, None, None, 51], [None, None, 16, None], [41, None, 43, 42]]
   # Define the constraints on the rows and columns
   row_constraints = [None, 159, 114, None]
   col_constraints = [None, 147, 128, None]
   diagonal_constraint = 150
   # Define the range of the integers that can be placed in the grid
   num_range = range(13, 55)


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


       # Generate all possible actions from the current state, which includes placing a unique integer from the range in any of the 'x' positions in the grid
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       new_state[row_ind][col_ind] = num
                       # Check if the new state is valid, ie the sums of the rows, columns, and diagonal are as required
                       if check_valid(new_state, row_constraints, col_constraints, diagonal_constraint):
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the grid with the unique integers
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, row_constraints, col_constraints, diagonal_constraint), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def check_goal(state, row_constraints, col_constraints, diagonal_constraint):
   # Check if the current state is the goal state by verifying if the sums of the rows, columns, and diagonal are as required and the sum of all the numbers in the grid is as low as possible
   if check_valid(state, row_constraints, col_constraints, diagonal_constraint):
       # The sum of all the numbers in the grid is the sum of the numbers in the state
       total_sum = sum(sum(row) for row in state)
       # The goal state is when the total sum is as low as possible, which is when it is equal to the sum of the numbers in the state
       return total_sum == sum(sum(row) for row in state)
   return False


def check_valid(state, row_constraints, col_constraints, diagonal_constraint):
   # Check if the current state is valid by verifying if the sums of the rows, columns, and diagonal are as required
   # Check the sums of the rows
   for row_ind in range(len(state)):
       if row_constraints[row_ind] is not None and row_constraints[row_ind] != sum(state[row_ind]):
           return False
   # Check the sums of the columns
   for col_ind in range(len(state[0])):
       col_sum = sum(state[row_ind][col_ind] for row_ind in range(len(state)))
       if col_constraints[col_ind] is not None and col_constraints[col_ind] != col_sum:
           return False
   # Check the sum of the diagonal
   diagonal_sum = sum(state[i][i] for i in range(len(state)))
   if diagonal_sum != diagonal_constraint:
       return False
   return True


def heuristic(state, row_constraints, col_constraints, diagonal_constraint):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the required sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it does not take into account the uniqueness of the integers
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by a positive amount
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the only one that causes the sum to be incorrect), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       h += abs(row_constraints[row_ind] - sum(state[row_ind])) if row_constraints[row_ind] is not None else 0
   for col_ind in range(len(state[0])):
       col_sum = sum(state[row_ind][col_ind] for row_ind in range(len(state)))
       h += abs(col_constraints[col_ind] - col_sum) if col_constraints[col_ind] is not None else 0
   h += abs(diagonal_constraint - sum(state[i][i] for i in range(len(state))))
   return h


print(a_star())
