
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[30, None, None, 37], [41, 56, None, None], [None, None, 29, 55], [None, None, None, 42]]
   # Define the goal state, with the sums of the rows and columns
   goal_state = (None, 208, 157, None, 196, 162, None, None, 166)
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state_to_goal(state) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that minimizes the sum of the grid, so we choose the smallest integer that has not been used in the grid
                   new_value = min(set(range(28, 60)) - set(sum(state, [])))
                   new_state[row_ind][col_ind] = new_value
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state_to_goal(new_state), goal_state), g + 1, actions + [(row_ind, col_ind, new_value)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only cares about the sum of the differences between the current state and the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a unique integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved integer is the same in the new and old state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               h += abs(state[row_ind][col_ind] - goal[row_ind * num_cols + col_ind])
   return h


def state_to_goal(state):
   # Convert the state to the goal format, with the sums of the rows and columns
   goal = [None] * (num_rows * num_cols + num_rows + num_cols - 2)
   for row_ind in range(num_rows):
       goal[row_ind * num_cols:(row_ind + 1) * num_cols] = state[row_ind]
   goal[num_rows * num_cols:num_rows * num_cols + num_rows] = [sum(state[row_ind]) for row_ind in range(num_rows)]
   goal[num_rows * num_cols + num_rows:num_rows * num_cols + num_rows + num_cols - 1] = [sum(state[col_ind] for col_ind in range(num_cols)) for row_ind in range(num_rows)]
   goal[-1] = sum(state[row_ind][col_ind] for row_ind in range(num_rows) for col_ind in range(num_cols) if row_ind != col_ind)
   return tuple(goal)


print(a_star())
