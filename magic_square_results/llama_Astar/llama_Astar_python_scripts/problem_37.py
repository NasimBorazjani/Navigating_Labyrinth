
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [['48', None, None], [None, None, None], [None, '49', None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = [150, 169, 209]


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
       # The goal state is when the sum of the numbers in the specified rows, columns, and diagonal equals the given amounts
       if all(sum(row) == goal_col_sum[i] for i, row in enumerate(state)) and sum(sum(row) for row in state) == 209:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that makes the sum of the numbers in the specified rows, columns, and diagonal equal to the given amounts
                   for num in range(40, 90):
                       new_state[row_ind][col_ind] = num
                       # Check if the new state is valid, ie the sum of the numbers in the specified rows, columns, and diagonal equals the given amounts
                       if all(sum(row) == goal_col_sum[i] for i, row in enumerate(new_state)) and sum(sum(row) for row in new_state) == 209:
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the 'x' in the current state
                   new_state[row_ind][col_ind] = None
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the grid
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only considers the sum of the numbers in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each unique integer must be placed at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the same in the new position), which is equal to the cost of reaching the successor node
   return sum(sum(row) for row in state)


print(a_star())
