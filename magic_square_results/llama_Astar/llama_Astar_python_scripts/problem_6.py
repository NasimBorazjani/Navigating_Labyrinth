
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 20, None], [None, None, None], [None, None, 33]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   column_sum = 82
   row_sum = 82
   diagonal_sum = 96


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
       # The goal state is when the sum of the specified rows, columns, and diagonal equals the given amounts
       if sum(row) == row_sum and sum(state[0]) == column_sum and sum(diagonal(state)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that is not in the current state
                   for num in range(19, 44):
                       if num not in flatten(state):
                           new_state[row_ind][col_ind] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only cares about the difference between the current state and the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the same in the current and goal states), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               h += abs(state[row_ind][col_ind] - goal_state[row_ind][col_ind])
   return h


def diagonal(state):
   # Function to get the diagonal of the state
   return [state[i][i] for i in range(len(state))]


def flatten(state):
   # Function to flatten the state into a 1d list
   return [num for row in state for num in row if num is not None]


print(a_star())
