
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[53, 57, None, None], [77, 78, None, 56], [51, 62, 88, None], [None, None, None, None]]
   # Define the goal state, with the sums of the rows and columns
   goal_state = (None, 244, 295, None, 266, 261, None, None, 265)
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The new state must maintain the constraint on the sums of the rows and columns
                   for i in range(num_rows):
                       for j in range(num_cols):
                           if new_state[i][j] is None:
                               new_state[i][j] = 41
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the grid with unique integers
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the sums of the rows and columns must be equal to the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is the largest difference), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] is not None:
               h += abs(state[i][j] - goal[i * num_cols + j])
   return h


print(a_star())
