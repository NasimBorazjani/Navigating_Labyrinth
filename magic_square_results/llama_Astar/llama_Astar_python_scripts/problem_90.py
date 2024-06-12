
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 32, None], [37, 61, None, 54], [None, None, None, 62], [None, 30, None, 44]]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   row_sums = [None, 211, None, None]
   col_sums = [None, 143, 170, None]
   diagonal_sum = 146


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
       # The goal state is when the sum of the numbers in the grid is as low as possible, and the sums of the specified rows, columns, and diagonal equal the given amounts
       if check_goal(state, row_sums, col_sums, diagonal_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to replace 'x' is the one that does not violate the constraints of the sums of the rows, columns, and diagonal
                   for num in range(22, 69):
                       new_state[row_ind][col_ind] = num
                       if check_state(new_state, row_sums, col_sums, diagonal_sum):
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                               visited_costs[tuple(map(tuple, new_state))] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), g + 1, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the cell to 'x' for the next iteration
                   new_state[row_ind][col_ind] = None
   return None


def check_state(state, row_sums, col_sums, diagonal_sum):
   # Check if the state satisfies the constraints of the sums of the rows, columns, and diagonal
   row_sums_check = [sum(row) for row in state]
   col_sums_check = [sum(col) for col in zip(*state)]
   diagonal_sum_check = sum(state[i][i] for i in range(len(state))) - state[1][1]
   return row_sums_check == row_sums and col_sums_check == col_sums and diagonal_sum_check == diagonal_sum


def check_goal(state, row_sums, col_sums, diagonal_sum):
   # The goal state is when the sum of the numbers in the grid is as low as possible, and the sums of the specified rows, columns, and diagonal equal the given amounts
   return check_state(state, row_sums, col_sums, diagonal_sum) and sum(sum(row) for row in state) == 214


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the grid
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each increase in the sum of the numbers in the grid must be accompanied by a decrease in the heuristic cost of the successor node
   # It's consistent because moving a number from one cell to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the largest in the grid), which is equal to the cost of reaching the successor node
   return sum(sum(row) for row in state)


print(a_star())
