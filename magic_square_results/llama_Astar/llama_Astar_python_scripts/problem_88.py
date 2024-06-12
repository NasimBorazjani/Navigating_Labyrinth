
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[27, 48, None, None], [None, None, 63, None], [28, None, 33, 26], [None, None, None, 39]]
   # Define the goal state, with the sums of rows and columns
   goal_state = (None, 183, 202, None, 190, 154, None, None, 183)
   # Define the range of numbers that can be used to replace 'x's
   num_range = range(22, 69)


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


       # Generate all possible actions from the current state, which includes replacing an 'x' with a number from the range
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
                           heapq.heappush(queue, (new_cost + heuristic(state_sums(new_state), goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def state_sums(state):
   # Calculate the sums of rows and columns and the sum of the diagonal from the top right to the bottom left corner
   sums = [None] * 9
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               if row_ind == col_ind:
                   sums[8] = sums[8] + state[row_ind][col_ind] if sums[8] is not None else state[row_ind][col_ind]
               elif row_ind < col_ind:
                   sums[row_ind * 2 + col_ind - 1] = sums[row_ind * 2 + col_ind - 1] + state[row_ind][col_ind] if sums[row_ind * 2 + col_ind - 1] is not None else state[row_ind][col_ind]
   return tuple(sums)


def heuristic(state_sums, goal_state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of rows, columns, and the diagonal in the current state and the goal state
   # This heuristic relaxes the constraint that the sums of rows and columns must be equal to the given amounts and the sum of the diagonal must be equal to 183
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one cell to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is part of the sum), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state_sums)):
       if state_sums[i] is not None and goal_state[i] is not None:
           h += abs(state_sums[i] - goal_state[i])
   return h


print(a_star())
