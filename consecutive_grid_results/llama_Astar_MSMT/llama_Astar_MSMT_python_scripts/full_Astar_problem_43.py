
import heapq


def initialize():
   # Define the initial state of the grid, with the 'x's replaced by '_' for easier processing
   initial_state = [['13', '_', '_'], ['_', '_', '27'], ['_', '26', '_']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 7
   range_end = 60


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue
  
def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, the range of numbers, and dimensions of the grid)
   initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, replacements, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if the grid is filled with unique integers and each row and column is strictly increasing or decreasing
       if is_goal_state(state):
           return replacements


       # Generate all possible actions from the current state, which includes replacing an 'x' with any unique integer from the range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == '_':
                   # Generate all possible unique integers that can replace the 'x'
                   for num in range(range_start, range_end + 1):
                       if num not in state:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, new_state), new_cost, replacements + [(row, col, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in the grid are unique and must be in strictly increasing or decreasing order in each row and column
   # It is admissible because it never overestimates the cost to reach the goal, as each number can only be replaced by a number with a smaller value
   # It's consistent because moving a number to a lower value in the grid results in a lower heuristic cost of the successor node, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in range(len(state)):
       h += sum(int(num) for num in state[row])
   for col in range(len(state[0])):
       h += state[col][col]
   h += state[0][0] + state[len(state)-1][len(state[0])-1]
   return h


def is_goal_state(state):
   # A state is the goal state if the grid is filled with unique integers and each row and column is strictly increasing or decreasing
   if len(set(num for row in state for num in row)) != len(state) * len(state[0]):
       return False
   for row in state:
       if not is_increasing(row) and not is_decreasing(row):
           return False
   for col in range(len(state[0])):
       if not is_increasing([row[col] for row in state]) and not is_decreasing([row[col] for row in state]):
           return False
   return True


def is_increasing(numbers):
   return all(int(numbers[i]) < int(numbers[i + 1]) for i in range(len(numbers) - 1))


def is_decreasing(numbers):
   return all(int(numbers[i]) > int(numbers[i + 1]) for i in range(len(numbers) - 1))


print(a_star())
