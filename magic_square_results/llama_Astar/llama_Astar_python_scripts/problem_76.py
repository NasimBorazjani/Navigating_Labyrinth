
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None for easier manipulation
   initial_state = [[26, 38, 27, None], [None, None, None, 19], [None, 43, None, None], [42, None, 34, 20]]
   # Define the constraints on the rows and columns
   row_constraints = [None, 94, 109, None]
   col_constraints = [None, 128, 80, None]
   diagonal_constraint = 99
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
       # The goal state is when the sums of the rows, columns, and diagonal are as required
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
                       # The cost so far is the number of numbers placed in the grid, as the task is to minimize the number of numbers placed in the grid
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_constraints, col_constraints, diagonal_constraint), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def check_goal(state, row_constraints, col_constraints, diagonal_constraint):
   # Check if the sums of the rows, columns, and diagonal are as required
   if sum(state[i][j] for i in range(len(state)) for j in range(len(state[i])) if state[i][j] is not None) != 225:
       return False
   for i in range(len(state)):
       if sum(state[i][j] for j in range(len(state[i])) if state[i][j] is not None) != row_constraints[i]:
           return False
   for i in range(len(state[0])):
       if sum(state[j][i] for j in range(len(state))) != col_constraints[i]:
           return False
   if sum(state[i][i] for i in range(len(state))) != diagonal_constraint:
       return False
   return True


def heuristic(state, row_constraints, col_constraints, diagonal_constraint):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the required sums
   # This heuristic relaxes the constraint that the sums of rows, columns, and diagonal must be as required
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by a positive amount
   # It's consistent because moving a number from one cell to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is part of the incorrect sum), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       h += abs(sum(state[i][j] for j in range(len(state[i])) if state[i][j] is not None) - row_constraints[i])
   for i in range(len(state[0])):
       h += abs(sum(state[j][i] for j in range(len(state))) - col_constraints[i])
   h += abs(sum(state[i][i] for i in range(len(state))) - diagonal_constraint)
   return h


print(a_star())
