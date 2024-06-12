
import heapq


def initialize():
   # Define the initial state of the grid, with the 'x's represented as None
   initial_state = [[None, None, None], [39, None, 52], [60, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the grid and the sum of the numbers in the topmost row, rightmost column, and diagonal
   initial_state_info = (initial_state, 39 + 52 + 60)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the grid is valid, return the actions taken
       if all(all(row[i] >= row[i - 1] for i in range(1, len(row))) for row in state[0]) and all(all(row[i] >= row[i + 1] for i in range(len(row) - 1)) for row in state[0]) and all(all(state[0][i][j] >= state[0][i + 1][j] for i in range(len(state[0]) - 1)) for j in range(len(state[0][0]))) and all(all(state[0][i][j] >= state[0][i][j + 1] for j in range(len(state[0][0]) - 1)) for i in range(len(state[0]) - 1)):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[0][row_ind][col_ind] is None:
                   for num in range(29, 73):
                       # Check if the new state would be valid, ie the number is not already in the grid
                       if num not in state[0]:
                           # Generate the new state
                           new_state = [row[:] for row in state[0]]
                           new_state[row_ind][col_ind] = num
                           new_state_info = (new_state, state[1] + num - (state[0][row_ind][col_ind] if state[0][row_ind][col_ind] is not None else 0))
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           if new_state_info not in visited_costs or new_cost < visited_costs[new_state_info]:
                               visited_costs[new_state_info] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state_info, state[1]), new_cost, actions + [(row_ind, col_ind, num)], new_state_info))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and diagonal
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must be at least as costly as the current heuristic cost of the successor node
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 * the difference between the new and old numbers, which is equal to the cost of reaching the successor node
   return state[1]


print(a_star())
