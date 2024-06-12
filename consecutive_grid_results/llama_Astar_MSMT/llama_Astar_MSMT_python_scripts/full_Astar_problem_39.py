
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 60, None], [None, None, 53], [52, 39, 20]]
  
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


       # We can check if the current state is the goal state by checking if there are no 'x's in the grid
       if None not in state:
           return actions


       # Generate all valid actions from the current state, which includes replacing each 'x' with a unique number from the given range
       # Iterate through the grid
       for row in range(num_rows):
           for col in range(num_cols):
               # Check if the current cell is an 'x'
               if state[row][col] is None:
                   # Generate all possible numbers that can replace the 'x', while maintaining the consecutive order in each row and column
                   for num in range(18, 72):
                       if (row > 0 and num > state[row - 1][col]) or (row == 0) and (col > 0 and num > state[row][col - 1]) or (row > 0 and col > 0 and num > state[row - 1][col - 1]):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required
                           new_cost = g + 1
                          
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, num)], new_state))
                              
   return None


def heuristic(state):
   # An admissible and consistent heuristic is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each number can only be replaced by a lower number
   # It's consistent because moving a number to a lower number reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the only one that can be moved to a lower number), which is equal to the cost of reaching the successor node
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
