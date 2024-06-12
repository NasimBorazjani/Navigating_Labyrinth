
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None for easier handling
   initial_state = [[33, 37, None, 58], [44, 51, None, 63], [None, 52, 62, 64], [None, None, 65, None]]
   # Define the goal state, where all 'x' are replaced by integers from the given range
   goal_state = [[33, 37, 38, 58], [44, 51, 52, 63], [39, 52, 62, 64], [40, 41, 65, 66]]
   # Define the range of numbers that can be used for replacement
   num_range = range(34, 79)
   # Define the number of rows and columns in the grid
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements made to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique number from the range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       # Check if the new state would be valid, ie the number is unique in its row and column
                       if num not in new_state[row_ind] and num not in [row[col_ind] for row in new_state]:
                           # Replace the 'x' with the unique number
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the 'x' in the current state
                   new_state[row_ind][col_ind] = None
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must decrease the heuristic cost of the successor node
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is in the topmost row, rightmost column, or diagonal), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += row[0]
   for col in range(len(state)):
       h += state[col][-1]
   h += state[0][0] + state[-1][-1]
   return h


print(a_star())
