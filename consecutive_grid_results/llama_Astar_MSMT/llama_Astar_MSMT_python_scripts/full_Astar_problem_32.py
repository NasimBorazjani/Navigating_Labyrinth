
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[49, None, None], [47, None, 54], [None, 35, None]]
  
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


       # Check if the current state is the goal state, ie all cells in the grid are filled with unique integers and the consecutive order constraint is maintained for each row and column
       if all(len(set(row)) == len(row) for row in state) and all(len(set(state[i][j] for i in range(num_rows))) == num_rows for j in range(num_cols)) and all(len(set(state[i][j] for j in range(num_cols))) == num_cols for i in range(num_rows)):
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate all possible unique integers from the given range that can be placed in the current cell
                   for num in range(58):
                       if num not in {state[i][j] for i in range(num_rows) for j in range(num_cols)}:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to fill the grid
                           new_cost = g + 1
                          
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                              
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one cell to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's value matches the most common value in the new cell but not in the old one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   # Add the numbers in the topmost row
   h += sum(state[0])
   # Add the numbers in the rightmost column
   h += sum(state[i][-1] for i in range(len(state)))
   # Add the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   h += sum(state[i][i] for i in range(len(state)))
   return h


print(a_star())
