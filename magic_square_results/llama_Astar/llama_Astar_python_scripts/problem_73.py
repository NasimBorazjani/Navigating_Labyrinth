
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, None], [None, 41, 17, None], [None, None, 13, 43], [9, 24, 27, 11]]
   # Define the constraints for the rows and columns
   row_constraints = [None, 116, 124, None]
   col_constraints = [None, 144, 76, None]
   diagonal_constraint = 75
   # Define the range of the integers that can be placed in the grid
   num_range = range(6, 48)


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


       # Generate all possible actions from the current state, which includes placing a unique integer in each 'x' position
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Place a unique integer in the current 'x' position
                   new_state[row_ind][col_ind] = next(num for num in num_range if num not in new_state[row_ind])
                   # The cost so far is the number of unique integers placed, as the task is to minimize the number of unique integers required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, row_constraints, col_constraints, diagonal_constraint), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def check_goal(state, row_constraints, col_constraints, diagonal_constraint):
   # Check if the current state is the goal state by verifying the sums of the rows, columns, and diagonal
   if row_constraints[1] != sum(state[1]) or row_constraints[2] != sum(state[2]) or col_constraints[1] != sum(state[i][1] for i in range(4)) or col_constraints[2] != sum(state[i][2] for i in range(4)) or diagonal_constraint != sum(state[i][i] for i in range(4)) + sum(state[i][3 - i] for i in range(4)):
       return False
   return True


def heuristic(state, row_constraints, col_constraints, diagonal_constraint):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the required sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the difference between the current and required sums
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by a unique integer
   # It's consistent because moving a unique integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved unique integer is the only one in its row, column, or diagonal), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(4):
       h += abs(row_constraints[i] - sum(state[i])) if i != 0 else 0
       h += abs(col_constraints[i] - sum(state[j][i] for j in range(4))) if i != 0 else 0
   h += abs(diagonal_constraint - sum(state[i][i] for i in range(4)) - sum(state[i][3 - i] for i in range(4)))
   return h


print(a_star())
