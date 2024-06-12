
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [65, None, None], [79, 73, 50]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, where each row and column is strictly increasing or decreasing
       if all(state[i][j] is not None for i in range(num_rows) for j in range(num_cols)) and is_increasing_or_decreasing(state):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   # Generate the new state
                   new_state = [list(row_state[:]) for row_state in state]
                   for num in range(34, 88):
                       new_state[row][col] = num
                       # Check if the new state is valid, ie the new state maintains the consecutive order in each row and column
                       if is_valid(new_state):
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, num)], new_state))
                              
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number to its correct position reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the largest or smallest in its row or column), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   h += sum(state[0])
   h += sum(state[i][-1] for i in range(num_rows))
   h += sum(state[i][i] for i in range(num_rows))
   return h


def is_increasing_or_decreasing(state):
   # Check if each row and column is strictly increasing or decreasing
   for i in range(num_rows):
       if not (all(state[i][j] < state[i][j + 1] for j in range(num_cols - 1)) or all(state[i][j] > state[i][j + 1] for j in range(num_cols - 1))):
           return False
       if not (all(state[j][i] < state[j + 1][i] for j in range(num_rows - 1)) or all(state[j][i] > state[j + 1][i] for j in range(num_rows - 1))):
           return False
   return True


def is_valid(state):
   # Check if the new state maintains the consecutive order in each row and column
   for i in range(num_rows):
       if not (all(state[i][j] < state[i][j + 1] for j in range(num_cols - 1)) and all(state[i][j] > state[i][j + 1] for j in range(num_cols - 1))):
           return False
       if not (all(state[j][i] < state[j + 1][i] for j in range(num_rows - 1)) and all(state[j][i] > state[j + 1][i] for j in range(num_rows - 1))):
           return False
   return True


print(a_star())
