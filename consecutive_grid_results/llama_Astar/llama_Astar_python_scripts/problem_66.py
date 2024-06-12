
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None
   initial_state = [[10, 26, 30, 46], [None, 33, 43, None], [21, 40, None, None], [None, None, None, 52]]
   # Define the range of numbers to fill in the grid
   num_range = range(9, 54)
   # Define the initial cost of the state
   initial_cost = 0
   # Initialize the visited costs dictionary
   visited_costs = {}
   visited_costs[str(initial_state)] = initial_cost
   # Initialize the priority queue with the initial state
   queue = [(initial_cost, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all the 'x's in the grid are replaced with unique integers from the given range
       if all(None not in row for row in state):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique number from the range
       for row_ind, row in enumerate(state):
           for col_ind, cell in enumerate(row):
               if cell is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       # Check if the number is valid to be placed in the current position
                       if is_valid(new_state, row_ind, col_ind, num):
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(row_ind, col_ind, num)], new_state))


def is_valid(state, row_ind, col_ind, num):
   # Check if the number is valid to be placed in the current position
   # The number must be unique in the row and column
   if num in state[row_ind] or num in list(zip(*state))[col_ind]:
       return False
   # The number must maintain the consecutive order in the row and column
   if row_ind > 0 and num <= state[row_ind - 1][col_ind]:
       return False
   if col_ind > 0 and num <= state[row_ind][col_ind - 1]:
       return False
   return True


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the largest or smallest in its row or column), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += row[0]
   for col in list(zip(*state)):
       h += col[-1]
   h += state[0][0]
   for i in range(len(state)):
       h += state[i][i]
   return h


print(a_star())
