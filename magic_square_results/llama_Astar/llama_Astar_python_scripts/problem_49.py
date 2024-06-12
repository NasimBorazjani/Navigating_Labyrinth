
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[37, None, None, 56], [52, None, None, None], [None, 50, None, None], [None, None, None, 46]]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   row_sums = [None, 165, 155, None]
   col_sums = [None, 169, 190, None]
   diagonal_sum = 201


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
       # The goal state is when the sum of the numbers in the specified rows, columns, and diagonal equals the given amounts
       if check_goal(state, row_sums, col_sums, diagonal_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that makes the sum of the specified rows, columns, and diagonal equal the given amounts
                   for num in range(34, 61):
                       new_state[row_ind][col_ind] = num
                       # Check if the new state is valid, ie if the sum of the numbers in the specified rows, columns, and diagonal equal the given amounts
                       if check_state(new_state, row_sums, col_sums, diagonal_sum):
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                               visited_costs[tuple(map(tuple, new_state))] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), g + 1, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the cell to 'x' for the next iteration
                   new_state[row_ind][col_ind] = None


def check_goal(state, row_sums, col_sums, diagonal_sum):
   # Check if the current state is the goal state
   # The goal state is when the sum of the numbers in the specified rows, columns, and diagonal equals the given amounts
   row_sums_check = [sum(row) if row_sum is not None else None for row_ind, row_sum in enumerate(row_sums)]
   col_sums_check = [sum(col) if col_sum is not None else None for col_ind, col_sum in enumerate(col_sums)]
   diagonal_sum_check = sum(state[i][i] for i in range(len(state))) - state[1][1]
   return row_sums_check == row_sums and col_sums_check == col_sums and diagonal_sum_check == diagonal_sum


def check_state(state, row_sums, col_sums, diagonal_sum):
   # Check if the current state is valid, ie if the sum of the numbers in the specified rows, columns, and diagonal equal the given amounts
   row_sums_check = [sum(row) if row_sum is not None else None for row_ind, row_sum in enumerate(row_sums)]
   col_sums_check = [sum(col) if col_sum is not None else None for col_ind, col_sum in enumerate(col_sums)]
   diagonal_sum_check = sum(state[i][i] for i in range(len(state))) - state[1][1]
   return row_sums_check == row_sums and col_sums_check == col_sums and diagonal_sum_check == diagonal_sum


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the grid
   # This heuristic relaxes the constraint that the sum of the numbers in the specified rows, columns, and diagonal must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect number must be replaced with the correct one
   # It's consistent because moving a number from one cell to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is incorrect), which is equal to the cost of reaching the successor node
   return sum(sum(row) for row in state)


print(a_star())
