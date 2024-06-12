
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 60, 63], [35, None, None, None], [None, None, None, 50], [34, None, 37, None]]
   # Define the goal state, with the sums of rows and columns and the diagonal
   goal_state = (None, 157, 200, None, 193, 158, None, 183)
   # Define the range of the numbers that can be placed in the grid
   num_range = range(28, 65)


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
       if state_sums(state) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes placing a number from the range in any of the 'x' positions in the grid
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
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def state_sums(state):
   # Calculate the sums of rows, columns, and the diagonal of the state
   sums = [None]
   for row in state:
       sums.append(sum(row))
   sums.append(sum(state[i][i] for i in range(len(state))))
   return tuple(sums)


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of rows, columns, and the diagonal of the state and the goal
   # This heuristic relaxes the constraint that the sums of rows and columns and the diagonal must be equal in the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 times the difference between the old and new sums, which is equal to the cost of reaching the successor node
   h = 0
   state_sums_vals = state_sums(state)
   for i in range(1, len(state_sums_vals)):
       h += abs(state_sums_vals[i] - goal[i])
   return h


print(a_star())
