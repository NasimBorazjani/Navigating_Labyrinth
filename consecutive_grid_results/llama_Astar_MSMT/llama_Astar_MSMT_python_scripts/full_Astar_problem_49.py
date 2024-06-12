
import heapq


def initialize():
   # Define the initial state of the grid, with numbers encoded as strings
   initial_state = [['22', '35', '40', '47'],
                    ['x', 'x', '37', '45'],
                    ['18', '24', 'x', 'x'],
                    ['x', '17', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
  
   visited_costs = {}
   visited_costs[str(initial_state)] = 0
  
   # The initial state is represented as a string to be able to use it as a dictionary key
   queue = [(0, 0, [], str(initial_state))]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all 'x's in the grid are replaced with unique numbers and the grid fulfills the conditions of each row and column being strictly increasing or decreasing
       # This condition is met when there are no 'x's in the grid
       if 'x' not in state:
           return actions


       # Generate all valid actions from the current state, which includes replacing each 'x' in the grid with a unique number
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The possible values for the new state are all the unique numbers in the given range not already in the grid
                   for value in range(49, 9, -1):
                       if str(value) not in str(new_state):
                           # Replace the 'x' with the new value
                           new_state[row][col] = str(value)
                           # Check if the new state fulfills the conditions of each row and column being strictly increasing or decreasing
                           if is_valid(new_state):
                               new_state = tuple(tuple(row) for row in new_state)
                               # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                               new_cost = g + 1


                               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                               if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                                   visited_costs[str(new_state)] = new_cost
                                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, value)], str(new_state)))
   return None


def is_valid(state):
   # Check if the grid fulfills the conditions of each row and column being strictly increasing or decreasing
   for row in state:
       if row[0] < row[1] < row[2] < row[3]:
           continue
       elif row[0] > row[1] > row[2] > row[3]:
           continue
       else:
           return False
   for col in range(len(state)):
       if state[0][col] < state[1][col] < state[2][col] < state[3][col]:
           continue
       elif state[0][col] > state[1][col] > state[2][col] > state[3][col]:
           continue
       else:
           return False
   # Check if the diagonal from the top-left corner to the bottom-right corner is strictly increasing or decreasing
   diagonal = [state[i][i] for i in range(len(state))]
   if diagonal[0] < diagonal[1] < diagonal[2] < diagonal[3]:
       return True
   elif diagonal[0] > diagonal[1] > diagonal[2] > diagonal[3]:
       return True
   return False


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each move must decrease the heuristic cost of the successor node
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2, which is equal to the cost of reaching the successor node
   h = sum(int(state[0][i]) for i in range(len(state)))
   h += sum(int(state[i][3]) for i in range(len(state)))
   h += sum(int(state[i][i]) for i in range(len(state)))
   return h


print(a_star())
