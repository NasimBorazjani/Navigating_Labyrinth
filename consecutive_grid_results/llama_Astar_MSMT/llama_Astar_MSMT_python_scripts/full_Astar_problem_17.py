
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 42, 38], [None, None, None], [None, 63, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid, the sum of the top row, rightmost column, and diagonal
   initial_state_info = (initial_state, 42 + 38, 63, 38)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == ([[38, 42, 63], [39, 40, 41], [43, 44, 45]]):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[0][row][col] is None:
                   for num in range(38, 77):
                       # Check if the new state would be valid, ie the number must be unique in its row and column and must maintain the consecutive order
                       if (num > state[0][row][col - 1] if col > 0 else True) and (num < state[0][row][col + 1] if col < num_cols - 1 else True) and (num > state[0][row - 1][col] if row > 0 else True) and (num < state[0][row + 1][col] if row < num_rows - 1 else True):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state[0]]
                           new_state[row][col] = num
                           new_state = (tuple(tuple(row) for row in new_state), state[1] + num, state[2] + num, state[3] + num)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, new_state), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(current_state, goal_state):
   # An admissible and consistent heuristic for this problem is the difference between the sum of the top row, rightmost column, and diagonal in the current state and the goal state
   # This heuristic relaxes the constraint that the numbers in the grid must be unique and must maintain the consecutive order in each row and column
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must decrease the heuristic cost of the successor node by at least 1
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is the largest or smallest in its row or column), which is equal to the cost of reaching the successor node
   return abs(current_state[1] + current_state[2] + current_state[3] - goal_state[1] - goal_state[2] - goal_state[3])


print(a_star())
