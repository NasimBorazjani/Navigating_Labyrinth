
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by 'None' for easier handling
   initial_state = [[46, 30, None, 49], [43, None, None, 53], [None, None, 37, None], [None, 34, 33, None]]
   # Define the goal state, with the sums of rows and columns and the diagonal
   goal_state = (None, 154, 157, None, 173, 194, None, 208)
   # Define the range of the integers that can be placed in the grid
   num_range = range(30, 67)


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


       # Generate all possible actions from the current state, which includes placing a unique integer from the range in any of the 'x' positions
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of unique integers placed in the grid, as the task is to minimize the number of unique integers required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(state_sums(new_state), goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def state_sums(state):
   # Calculate the sums of rows, columns, and the diagonal of the current state
   sums = [None] * 8
   for row_ind in range(len(state)):
       sums[row_ind] = sum(state[row_ind])
   for col_ind in range(len(state)):
       sums[col_ind + 4] = sum(state[row_ind][col_ind] for row_ind in range(len(state)))
   sums[7] = sum(state[row_ind][col_ind] for row_ind, col_ind in enumerate(range(len(state) - 1, -1, -1)))
   return tuple(sums)


def heuristic(state_sums, goal_state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of the current state and the goal state
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only cares about the sums of the numbers in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number's value is equal to the difference between the sums of the current state and the goal state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state_sums)):
       h += abs(state_sums[i] - goal_state[i])
   return h


print(a_star())
