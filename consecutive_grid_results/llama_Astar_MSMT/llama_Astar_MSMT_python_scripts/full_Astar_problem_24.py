
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[66, None, None], [65, 68, None], [None, None, 79]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid and dimensions of the grid)
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if the grid is filled with unique integers and the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner is minimized
       if all(state[i][j] is not None for i in range(num_rows) for j in range(num_cols)) and is_grid_valid(state):
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The number to replace the 'x' with is the next unique integer in the given range
                   number_to_replace_x = get_next_unique_number(new_state)
                   new_state[i][j] = number_to_replace_x
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to fill the grid
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number_to_replace_x)], new_state))
                      
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the same in the new position), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = sum(state[0]) + sum(state[i][-1] for i in range(len(state))) + state[0][0]
   for i in range(len(state)):
       h += state[i][i]
   return h


def is_grid_valid(grid):
   # Check if the grid is filled with unique integers and the numbers in each row and column are strictly increasing or decreasing
   for row in grid:
       if row != sorted(row) and row != sorted(row, reverse=True):
           return False
   for col in range(len(grid)):
       if [row[col] for row in grid] != sorted(grid[i][col] for i in range(len(grid))) and [row[col] for row in grid] != sorted(grid[i][col] for i in range(len(grid)), reverse=True):
           return False
   return True


def get_next_unique_number(grid):
   # Get the unique numbers from the given range
   unique_numbers = list(range(50, 94))
   # Remove the numbers that are already in the grid
   for row in grid:
       for num in row:
           if num in unique_numbers:
               unique_numbers.remove(num)
   # Return the next unique number
   return unique_numbers[0]


print(a_star())
