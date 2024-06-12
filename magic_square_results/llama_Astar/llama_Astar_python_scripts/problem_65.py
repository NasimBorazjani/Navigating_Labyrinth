
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 65, 49, 35], [40, None, 52, None], [None, None, 34, None], [None, None, 55, 61]]
   # Define the goal state, with the sums of the specified rows, columns, and diagonal
   goal_state = (None, 191, 190, None, 192, 173, None, None, 180)
   # Define the range of the unique integers
   unique_integers = list(range(30, 67))
   # Define the number of rows and columns in the grid
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
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique integer
                   for integer in unique_integers:
                       new_state[row_ind][col_ind] = integer
                       # Check if the new state is valid, ie the sums of the specified rows, columns, and diagonal are correct
                       if is_valid(new_state):
                           # The cost so far is the number of unique integers used, as the task is to minimize the number of unique integers used to fill the grid
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                               visited_costs[tuple(map(tuple, new_state))] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, integer)], new_state))
                   # Reset the 'x' in the current state
                   new_state[row_ind][col_ind] = None


def is_valid(state):
   # Check if the sums of the specified rows, columns, and diagonal are correct
   # The sum of the diagonal from the top right to the bottom left corner of the grid
   diagonal_sum = sum(state[i][i] for i in range(len(state)))
   # The sum of the diagonal from the top left to the bottom right corner of the grid
   anti_diagonal_sum = sum(state[i][len(state) - i - 1] for i in range(len(state)))
   # The sum of the numbers in the grid
   total_sum = sum(sum(row) for row in state)
   # The sums of the rows and columns
   row_sums = [sum(row) for row in state]
   col_sums = [sum(state[i][j] for i in range(len(state))) for j in range(len(state[0]))]
   # The goal state sums
   goal_state_sums = (None, 191, 190, None, 192, 173, None, None, 180)
   # Check if the sums of the rows, columns, and diagonal are correct
   return row_sums == goal_state_sums[:len(state)] and col_sums == goal_state_sums[len(state):2 * len(state)] and diagonal_sum == goal_state_sums[2 * len(state)] and anti_diagonal_sum == goal_state_sums[2 * len(state) + 1] and total_sum == goal_state_sums[-1]


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the grid
   # This heuristic relaxes the constraint that the unique integers must be unique, as it only cares about the total sum of the numbers in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each unique integer must be placed at least once
   # It's consistent because moving a unique integer from one position to another reduces the heuristic cost of the successor node by a max of 2 * (the difference between the old and new unique integers), which is equal to the cost of reaching the successor node
   return sum(sum(row) for row in state)


print(a_star())
