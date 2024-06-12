
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, None], [None, 43, None]]
   # Define the goal state of the grid, with the given sums of the specified rows, columns, and diagonal
   goal_state = [[120, 105, 99]]
   # Define the range of the integers that can be placed in the grid
   integer_range = range(12, 47)
   # Define the number of rows and columns in the grid
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the integers placed in the grid to get to each state in a list; no integers placed in the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, integers, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of all the integers in the grid is as low as possible, and the sums of the specified rows, columns, and diagonal equal the given amounts
       if sum(sum(row) for row in state) == sum(goal_state) and all(sum(row) == goal_state[0][i] for i, row in enumerate(state)):
           return integers


       # Generate all possible actions from the current state, which includes placing a unique integer in each 'x' position in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Place a unique integer in the current 'x' position
                   new_state[row_ind][col_ind] = integer_range.pop(0)
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of integers placed in the grid, as the task is to minimize the number of integers placed in the grid to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, integers + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of the specified rows, columns, and diagonal in the current state and the goal state
   # This heuristic relaxes the constraint that the sums of the specified rows, columns, and diagonal must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving an integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved integer is the largest one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       h += abs(sum(state[row_ind]) - goal[0][row_ind])
   for col_ind in range(len(state[0])):
       h += abs(sum(state[row_ind][col_ind] for row_ind in range(len(state))) - goal[0][col_ind])
   h += abs(sum(state[row_ind][col_ind] for row_ind, col_ind in enumerate(range(len(state) - 1, -1, -1))) - goal[0][-1])
   return h


print(a_star())
