
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[29, 45, None], [None, None, None], [None, 43, 34]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the sum of the numbers in the topmost row, rightmost column, and the diagonal
   initial_state_info = (initial_state, 74, 117, 63)
   # Since the initial state is valid, we must add it to the visited_costs
   visited_costs[initial_state_info] = 0
   # The priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if all(row[i] is not None for row in state[0] for i in range(num_cols)) and all(state[0][i][i] is not None for i in range(num_rows)):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[0][row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state[0]]
                   for num in range(21, 59):
                       if num not in new_state[row_ind] and num not in [row[col_ind] for row in new_state]:
                           new_state[row_ind][col_ind] = num
                           # Calculate the sum of the numbers in the topmost row, rightmost column, and the diagonal
                           new_state_info = (new_state, sum(new_state[0]), sum([row[-1] for row in new_state]), sum(new_state[i][i] for i in range(num_rows)))
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the grid with unique integers
                           new_cost = g + 1


                           if new_state_info not in visited_costs or new_cost < visited_costs[new_state_info]:
                               visited_costs[new_state_info] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, new_state_info), new_cost, actions + [(row_ind, col_ind, num)], new_state_info))
   return None


def heuristic(state, new_state_info):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and the diagonal
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the same in the new state), which is equal to the cost of reaching the successor node
   return abs(state[1] - new_state_info[1]) + abs(state[2] - new_state_info[2]) + abs(state[3] - new_state_info[3])


print(a_star())
