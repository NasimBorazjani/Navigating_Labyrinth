
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None for easier manipulation
   initial_state = [[46, None, 58, 45], [None, None, 54, None], [None, None, None, None], [28, 53, 34, None]]
   # Define the goal state of the grid, with the sums of rows, columns, and diagonal
   goal_state = (None, 162, 195, None, 168, 168, None, 168)
   # Define the range of the integers that can be placed in the grid
   integer_range = range(28, 60)
   # Define the number of rows and columns in the grid
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(row[:] for row in initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state_to_goal_sum(state) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes placing a unique integer in any of the 'x' positions in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [row[:] for row in state]
                   # Place a unique integer in the current position
                   new_state[row_ind][col_ind] = integer_range.pop(0)
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of integers placed, as the task is to minimize the number of integers placed to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state, goal_state), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the sums of rows, columns, and diagonal must be equal to the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched integer must be replaced by a unique integer from the range once
   # It's consistent because moving a integer from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved integer's value is equal to the value of the moved integer in the new position), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               h += abs(state[row_ind][col_ind] - goal[row_ind * num_cols + col_ind])
   return h


def state_to_goal_sum(state):
   # Convert the state to a format that can be compared with the goal state
   state_sum = [None] * (num_rows * num_cols)
   for row_ind in range(num_rows):
       for col_ind in range(num_cols):
           state_sum[row_ind * num_cols + col_ind] = state[row_ind][col_ind]
   return tuple(state_sum)


print(a_star())
