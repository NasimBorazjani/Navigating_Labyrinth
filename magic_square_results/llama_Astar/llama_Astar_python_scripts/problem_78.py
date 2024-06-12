
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 22, None, None], [28, 47, 42, None], [16, None, 30, 24], [None, None, None, None]]
   # Define the goal state of the grid, with the sums of rows, columns, and the diagonal
   goal_state = (None, 135, 153, None, 158, 87, None, None, 140)
   # Define the range of the integers that can be placed in the grid
   num_range = range(13, 55)


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


       # Generate all possible actions from the current state, which includes placing a unique integer from the range in any of the 'x' positions in the grid
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       # Check if the new state would be valid, ie the number is not already in the state
                       if num not in flatten(new_state):
                           new_state[row_ind][col_ind] = num
                           # The cost so far is the number of numbers placed in the state, as the task is to minimize the number of numbers placed in the state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_sums(new_state), goal_state), g + 1, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the position in the grid to 'x' for the next number in the range
                   new_state[row_ind][col_ind] = None


def state_sums(state):
   # Calculate the sums of rows, columns, and the diagonal of the state
   sums = [None] * 9
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               sums[row_ind] = sums[row_ind] + state[row_ind][col_ind] if sums[row_ind] is not None else state[row_ind][col_ind]
               sums[col_ind + len(state)] = sums[col_ind + len(state)] + state[row_ind][col_ind] if sums[col_ind + len(state)] is not None else state[row_ind][col_ind]
   sums[8] = sums[0] + sums[4] - 2 * state[1][1]
   return tuple(sums)


def heuristic(state_sums, goal_state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of the rows, columns, and the diagonal of the state and the goal state
   # This heuristic relaxes the constraint that the sums of the rows, columns, and the diagonal must be equal to the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 * the difference between the old and new sums, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state_sums)):
       h += abs(state_sums[i] - goal_state[i])
   return h


def flatten(state):
   # Flatten the state to a 1d list
   return [num for row in state for num in row if num is not None]


print(a_star())
