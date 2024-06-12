
import heapq


def initialize():
   # Define the initial state of the grid, with the 'x's replaced by '_' for easier processing
   initial_state = [['30', '_', '_'], ['28', '33', '43'], ['_', '_', '51']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 15
   range_end = 58


   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # The information we must encode for each state includes the current state of the grid and the cost to reach this state
   # The initial state is the initial_state, with the cost to reach it being 0
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue


def a_star():
  
   initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue = initialize()


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all the 'x's in the grid are replaced with unique integers from the given range, and the sum of the numbers in the topmost row, the rightmost column, and the diagonal is minimized
       if all(isinstance(cell, int) for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == '_':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in range(range_start, range_end + 1):
                       # Check if the new state would be valid, ie the new number must be unique in its row and column
                       if num not in new_state[row_ind] and num not in [row[col_ind] for row in new_state]:
                           # Replace the 'x' with the new number
                           new_state[row_ind][col_ind] = num
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if tuple(tuple(row) for row in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(row) for row in new_state)]:
                               visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                              
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the rightmost column, and the diagonal
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must be made at least once
   # It's consistent because moving a number to a new position in the grid can only decrease the heuristic cost of the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   h += sum(state[0])
   h += sum([row[-1] for row in state])
   h += state[0][0] + state[1][1] + state[2][2]
   return h


print(a_star())
