
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[42, 53, 43, 72], [None, 82, 54, None], [None, 62, 44, None], [None, None, None, None]]
   # Define the goal state, with the sums of the rows and columns
   goal_state = ([None, 253, 221, None], [277, 204, None, None], [None, None, None, None], [None, None, None, None])
   # Define the sum of the diagonal
   diagonal_sum = 252
   # Define the range of the integers
   integer_range = range(37, 84)
   # Define the number of rows and columns
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for integer in integer_range:
                       # Check if the new state would be valid, ie the integer is not already in the row or column
                       if integer not in new_state[row_ind] and integer not in new_state[col_ind]:
                           # Replace the 'x' with the integer
                           new_state[row_ind][col_ind] = integer
                           # Generate the new state
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, diagonal_sum), new_cost, actions + [(row_ind, col_ind, integer)], new_state))
   return None


def heuristic(state, goal, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the same in the new and old positions), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           # Calculate the absolute difference between the current state and the goal state
           h += abs(state[row_ind][col_ind] - goal[row_ind][col_ind])
   # Add the absolute difference between the current diagonal sum and the goal diagonal sum
   h += abs(sum(state[i][i] for i in range(len(state))) - diagonal_sum)
   return h


print(a_star())
