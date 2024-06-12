
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[38, None, None, None], [None, None, None, None], [None, 39, 40, 27], [32, 46, None, 25]]
   # Define the goal state, with the sums of the rows, columns, and diagonal
   goal_state = (None, 149, 178, None, 135, 130, None, 151)
   # Define the range of the integers that can be placed in the grid
   integer_range = range(24, 51)
   # Define the number of rows and columns in the grid
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state_sums(state) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes placing a unique integer in any of the 'x' positions in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Place a unique integer in the 'x' position
                   new_state[row_ind][col_ind] = integer_range.pop(0)
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of integers placed, as the task is to minimize the number of integers placed in the grid
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state_sums(new_state), goal_state), g + 1, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def state_sums(state):
   # Calculate the sums of the rows, columns, and diagonal of the current state
   sums = [None] * (num_rows + num_cols + 1)
   for row_ind in range(num_rows):
       sums[row_ind] = sum(state[row_ind])
   for col_ind in range(num_cols):
       sums[num_rows + col_ind] = sum(state[row_ind][col_ind] for row_ind in range(num_rows))
   sums[-1] = sum(state[row_ind][col_ind] for row_ind, col_ind in zip(range(num_rows - 1, -1, -1), range(num_cols - 1, -1, -1)))
   return tuple(sums)


def heuristic(state_sums, goal_state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of the rows, columns, and diagonal of the current state and the goal state
   # This heuristic relaxes the constraint that the sums of the rows, columns, and diagonal must be equal to the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is part of the sum that is exceeding the goal sum), which is equal to the cost of reaching the successor node
   return sum(abs(state_sum - goal_sum) for state_sum, goal_sum in zip(state_sums, goal_state) if goal_sum is not None)


print(a_star())
