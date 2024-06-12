
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[41, None, 21], [None, None, None], [12, None, 42]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the sum of the numbers in the topmost row, the rightmost column, and the diagonal
   initial_state_info = (initial_state, 41 + 21 + 12)
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_info = heapq.heappop(queue)


       # Unpack the information encoded in each state
       state, state_sum = state_info


       # If the current state of the grid is the goal state, return the actions taken
       if all(row[i] is not None for i in range(num_cols) for row in state) and all(col[i] is not None for i in range(num_rows) for col in zip(*state)) and state[0][0] == state[1][1] == state[2][2]:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   for num in range(11, 49):
                       # Check if the new state would be valid, ie the number is not already in the row, column, or diagonal
                       if num not in state[row_ind] and num not in zip(*state)[col_ind] and num != state[0][0] == state[1][1] == state[2][2]:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_info, state_sum), new_cost, actions + [(row_ind, col_ind, num)], (new_state, state_sum - num + new_cost)))
   return None


def heuristic(state_info, state_sum):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the rightmost column, and the diagonal minus the current sum of the numbers in the grid
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's position matches the most common position in the new state but not in the old one), which is equal to the cost of reaching the successor node
   return state_sum - sum(state_info[0]) - sum(zip(*state_info)[-1]) - state_info[0][0]


print(a_star())
