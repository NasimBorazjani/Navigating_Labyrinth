
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None], [None, 51, None], [None, 61, 64]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the sum of the numbers in the topmost row, the rightmost column, and the diagonal
   initial_state_info = (initial_state, 51 + 61 + 64)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if all(row[0] is not None for row in state[0]) and all(row[i] is not None for row in state[0] for i in range(1, len(row))):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[0][row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state[0]]
                   # The new state must maintain the consecutive order in each row and column
                   for i in range(num_rows):
                       if new_state[i][col_ind] is None:
                           new_state[i][col_ind] = min(set(range(34, 68)) - set(new_state[i]))
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the rightmost column, and the diagonal
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the same in the new position), which is equal to the cost of reaching the successor node
   return sum(state[0][0][i] for i in range(len(state[0][0]))) + state[0][1][-1] + state[0][2][2]


print(a_star())
