
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 64, None], [34, 54, None, None], [None, 56, 53, None], [36, None, None, 49]]
   # Define the goal state, with the sums of the specified rows, columns, and diagonal
   goal_state = (None, 217, 193, None, None, 156, 208, None, None, 166)
   # Define the range of the unique integers
   unique_integers = list(range(31, 68))


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


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for integer in unique_integers:
                       new_state[row_ind][col_ind] = integer
                       # The cost so far is the number of unique integers used, as the task is to minimize the number of unique integers used
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(state_sums(new_state), goal_state), new_cost, actions + [(row_ind, col_ind, integer)], new_state))
   return None


def state_sums(state):
   # Calculate the sums of the specified rows, columns, and diagonal of the state
   sums = [None] * 9
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               if row_ind == 0:
                   sums[col_ind] = (sums[col_ind] if sums[col_ind] else 0) + state[row_ind][col_ind]
               if col_ind == 0:
                   sums[4 + row_ind] = (sums[4 + row_ind] if sums[4 + row_ind] else 0) + state[row_ind][col_ind]
               if row_ind == col_ind:
                   sums[8] = (sums[8] if sums[8] else 0) + state[row_ind][col_ind]
   return tuple(sums)


def heuristic(state_sums, goal_state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of the specified rows, columns, and diagonal of the state and the goal state
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only cares about the sums of the numbers in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one cell to another results in a decrease in the heuristic cost of the successor node by a max of 2 times the difference between the old and new sums, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state_sums)):
       if state_sums[i] is not None and goal_state[i] is not None:
           h += abs(state_sums[i] - goal_state[i])
   return h


print(a_star())
