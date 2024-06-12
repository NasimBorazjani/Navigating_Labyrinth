
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 56, None, 40], [None, None, 44, 60], [None, 52, None, 45], [None, None, 62, 47]]
   # Define the goal state of the grid, with the sums of rows and columns
   goal_state = (None, 227, 215, None, 207, 218, None)
   # Define the sum of the diagonal
   diagonal_sum = 195
   # Define the range of the integers
   num_range = range(40, 67)
   # Define the number of rows and columns
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
       if check_goal(state, goal_state, diagonal_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [row[:] for row in state]
                   for num in num_range:
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                           visited_costs[tuple(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, diagonal_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def check_goal(state, goal_state, diagonal_sum):
   # Check if the current state is the goal state
   # The goal state is when the sums of rows, columns, and the diagonal equal the given amounts
   sums = [sum(row) for row in state]
   sums.append(sum(state[i][i] for i in range(len(state))))
   sums.append(sum(state[i][len(state) - 1 - i] for i in range(len(state))))
   return sums == goal_state and sums[0] + sums[2] == diagonal_sum


def heuristic(state, goal_state, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and the diagonal and the goal sums
   # This heuristic relaxes the constraint that the sums of rows and columns must be equal to the given amounts, and the sum of the diagonal must equal the given amount
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be non-negative
   # It's consistent because moving a number from one cell to another results in a decrease in the heuristic cost of the successor node by a max of the difference between the current sum and the goal sum, which is equal to the cost of reaching the successor node
   h = 0
   sums = [sum(row) for row in state]
   sums.append(sum(state[i][i] for i in range(len(state))))
   sums.append(sum(state[i][len(state) - 1 - i] for i in range(len(state))))
   for i in range(len(sums)):
       h += abs(sums[i] - goal_state[i])
   return h


print(a_star())
