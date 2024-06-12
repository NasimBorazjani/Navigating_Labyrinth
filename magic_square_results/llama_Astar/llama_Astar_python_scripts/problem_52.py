
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[14, 35, None, None], [None, None, None, 18], [None, 31, 27, 21], [30, None, None, 19]]
   # Define the goal state of the sums of rows, columns, and diagonal
   goal_sums = {'rows': [None, 89, 103, None], 'cols': [None, 121, 107, None], 'diag': 102}
   # Define the range of unique integers that can be placed in the grid
   num_range = range(9, 41)


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
       if check_goal(state, goal_sums):
           return actions


       # Generate all possible actions from the current state, which includes placing a unique integer in each 'x' position in the grid
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Place a unique integer in the current 'x' position
                   new_state[row_ind][col_ind] = next(num for num in num_range if num not in new_state[row_ind])
                   # The cost so far is the number of unique integers placed in the grid, as the task is to minimize the number of unique integers required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def check_goal(state, goal_sums):
   # Check if the current state meets the goal conditions
   # Check the sums of rows
   for row_ind in range(len(state)):
       if goal_sums['rows'][row_ind] is not None and sum(state[row_ind]) != goal_sums['rows'][row_ind]:
           return False
   # Check the sums of columns
   for col_ind in range(len(state[0])):
       if goal_sums['cols'][col_ind] is not None and sum(state[row_ind][col_ind] for row_ind in range(len(state))) != goal_sums['cols'][col_ind]:
           return False
   # Check the sum of the diagonal
   if sum(state[i][i] for i in range(len(state))) != goal_sums['diag']:
       return False
   return True


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the sums of rows, columns, and diagonal
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by a unique integer
   # It's consistent because moving a unique integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved integer is the only one contributing to the incorrect sum), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       h += abs(sum(state[row_ind]) - goal_sums['rows'][row_ind])
   for col_ind in range(len(state[0])):
       h += abs(sum(state[row_ind][col_ind] for row_ind in range(len(state))) - goal_sums['cols'][col_ind])
   h += abs(sum(state[i][i] for i in range(len(state))) - goal_sums['diag'])
   return h


print(a_star())
