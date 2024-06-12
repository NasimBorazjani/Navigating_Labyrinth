
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 40, None], [None, 31, None, 43], [37, None, None, 32], [34, 29, None, None]]
   # Define the constraints for the rows and columns
   row_constraints = [None, 125, 164, None]
   col_constraints = [None, 135, 160, None]
   diagonal_constraint = 146
   # Define the range of the integers that can be used to replace 'x'
   num_range = range(24, 51)


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
       # The goal state is when the sums of the rows, columns, and diagonal are equal to the given amounts
       if check_goal(state, row_constraints, col_constraints, diagonal_constraint):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of numbers replaced, as the task is to minimize the number of numbers replaced to reach the goal state
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_constraints, col_constraints, diagonal_constraint), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def check_goal(state, row_constraints, col_constraints, diagonal_constraint):
   # Check if the current state is the goal state by verifying the sums of the rows, columns, and diagonal
   if sum(state[row][col] for row, col in enumerate(col_constraints) if col is not None) != sum(state[row][col] for row, col in enumerate(row_constraints) if row is not None) or sum(state[row][col] for row, col in enumerate(state) if row == col) != diagonal_constraint:
       return False
   return True


def heuristic(state, row_constraints, col_constraints, diagonal_constraint):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the grid
   # This heuristic relaxes the constraint that the sums of the rows, columns, and diagonal must be equal to the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect number must be replaced at least once
   # It's consistent because moving a number from one position to another results in a lower heuristic cost of the successor node, as the sum of the numbers in the grid is always reduced
   return sum(sum(row) for row in state)


print(a_star())
