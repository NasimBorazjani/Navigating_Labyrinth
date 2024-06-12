
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[70, None, 50, None], [None, 39, 46, None], [34, 60, None, 51], [None, None, None, 68]]
   # Define the goal state of the grid, with the sums of rows and columns and the diagonal
   goal_state = (None, 260, 216, None, 183, 217, None, 214)
   # Define the range of the integers that can be placed in the grid
   integer_range = range(30, 87)
   # Define the number of rows and columns in the grid
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


       # Generate all possible actions from the current state, which includes placing a unique integer in each 'x' position in the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Place a unique integer in the current 'x' position
                   new_state[row_ind][col_ind] = integer_range.pop(0)
                   # Check if the new state is valid, ie the sums of rows, columns, and diagonal match the goal state
                   if is_valid(new_state):
                       # The cost so far is the number of integers placed in the grid, as the task is to minimize the number of integers placed in the grid
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def is_valid(state):
   # Check if the sums of rows, columns, and diagonal match the goal state
   for row_ind in range(len(state)):
       row_sum = sum(state[row_ind])
       if row_sum is not None and row_sum != goal_state[row_ind]:
           return False
   for col_ind in range(len(state[0])):
       col_sum = sum(state[row_ind][col_ind] for row_ind in range(len(state)))
       if col_sum is not None and col_sum != goal_state[col_ind + len(state)]:
           return False
   diagonal_sum = sum(state[i][i] for i in range(len(state)))
   if diagonal_sum != goal_state[-1]:
       return False
   return True


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the integers in the grid
   # This heuristic relaxes the constraint that the integers must be unique and in the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each integer must be placed at least once
   # It's consistent because moving an integer from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved integer is the same in the new position), which is equal to the cost of reaching the successor node
   return sum(sum(row) for row in state)


print(a_star())
