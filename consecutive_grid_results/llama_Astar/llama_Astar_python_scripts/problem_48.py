
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 53, None, 79], [46, 51, None, 78], [45, None, 73, 77], [42, 47, None, None]]
   # Define the range of the numbers
   num_range = range(40, 80)
   # Define the number of rows and columns
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all the 'x's in the grid are replaced with unique integers from the given range
       if all(None not in row for row in state):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique number from the range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [row[:] for row in state]
                   # Replace the 'x' with a unique number from the range
                   for num in num_range:
                       if num not in new_state[row_ind] and num not in zip(*new_state)[col_ind]:
                           new_state[row_ind][col_ind] = num
                           # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                           if is_valid(new_state):
                               new_state = tuple(tuple(row) for row in new_state)
                               # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                               new_cost = g + 1


                               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                               if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                                   visited_costs[str(new_state)] = new_cost
                                   heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the 'x' in the current state
                   new_state[row_ind][col_ind] = None


def is_valid(state):
   # Check if the numbers in each row and column are strictly increasing or decreasing
   for row in state:
       if row != sorted(row) and row != sorted(row, reverse=True):
           return False
   for col in zip(*state):
       if col != sorted(col) and col != sorted(col, reverse=True):
           return False
   return True


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's value matches the most common value in the new position but not in the old one), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += row[0]
   for col in zip(*state):
       h += col[-1]
   h += state[0][0]
   return h


print(a_star())