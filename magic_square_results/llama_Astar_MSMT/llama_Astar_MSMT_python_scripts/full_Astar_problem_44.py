
import heapq


def initialize():
   # Define the magic square, encoding the given numbers as integers and the unknown numbers as 'x'
   magic_square = [['x', 'x', 39, 'x'],
                   ['x', 'x', 'x', 43],
                   ['x', 'x', 'x', 47],
                   [46, 49, 'x', 53]]


   # Encoding other variables of the problem
   num_rows = 4
   num_cols = 4
   row_sums = [None, 188, 188, None]
   col_sums = [None, 177, 160, None]
   goal_diagonal_sum = 173


   visited_costs = {}
   visited_costs[magic_square] = 0
  
   # The information we must encode for each state includes the current state of the magic square
   initial_state = magic_square
   # The cost of the initial state is 0, as we have not yet replaced any 'x's with numbers
   queue = [(0, 0, [], initial_state)]
  
   return magic_square, num_rows, num_cols, row_sums, col_sums, goal_diagonal_sum, visited_costs, initial_state, queue
  
def a_star():
  
   magic_square, num_rows, num_cols, row_sums, col_sums, goal_diagonal_sum, visited_costs, initial_state, queue = initialize()
  
   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if the sum of all the numbers in the grid is as low as possible and the sums of the specified rows, columns, and diagonal equal the given amounts
       if all(sum(row) == row_sums[i] for i, row in enumerate(state)) and all(sum(col) == col_sums[j] for j, col in enumerate(zip(*state))) and sum(state[i][i] for i in range(num_rows)) == goal_diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in range(35, 62):
                       if num not in new_state[row_ind] and num not in new_state[col_ind]:
                           new_state[row_ind][col_ind] = num
                           # The cost so far is the sum of the numbers in the grid, as we aim to minimize the sum of all the numbers in the grid
                           new_cost = g + num


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the grid
   # This heuristic relaxes the constraint that the numbers in the grid must be unique, as it only aims to minimize the sum of all the numbers in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each move (adding a number to the grid) will decrease the heuristic cost of the successor node by at least 1
   # It's consistent because moving a number from one position to another in the grid, or removing a number from the grid, decreases the heuristic cost of the successor node by a max of 1, which is equal to the cost of reaching the successor node
   return sum(sum(row) for row in state)


print(a_star())
