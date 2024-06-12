
import heapq


def initialize():
   # Define the initial state of the magic square, as a 3x3 list of lists
   initial_state = [['x', '16', 'x'],
                    ['x', 'x', 'x'],
                    ['45', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   diagonal = [0, 4, 8]
   row_sums = [60, 'x', 'x']
   col_sums = ['x', 67, 'x']
   total_sum = 212


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, diagonal, row_sums, col_sums, total_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, diagonal, row_sums, col_sums, total_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the sum of all the numbers in the grid is equal to the given total sum, return the actions taken
       if sum(sum(row) for row in state) == total_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   for num in range(9, 49):
                       # Check if the new state would be valid, ie the number is unique and the sums of the specified rows, columns, and diagonal remain equal to the given amounts
                       if num not in state[row_ind] and num not in state[col_ind]:
                           new_state = [row[:] for row in state]
                           new_state[row_ind][col_ind] = num
                           if check_valid(new_state, diagonal, row_sums, col_sums, total_sum):
                               new_cost = g + 1


                               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                   visited_costs[new_state] = new_cost
                                   h = heuristic(new_state, total_sum)
                                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def check_valid(state, diagonal, row_sums, col_sums, total_sum):
   # Check if the new state is valid, ie if the sum of all the numbers in the grid is equal to the given total sum, and the sum of the specified rows, columns, and diagonal remain equal to the given amounts
   if sum(sum(row) for row in state) != total_sum:
       return False
   for row_ind in range(len(state)):
       if row_sums[row_ind] != 'x' and sum(state[row_ind]) != row_sums[row_ind]:
           return False
   for col_ind in range(len(state[0])):
       if col_sums[col_ind] != 'x' and sum(state[row_ind][col_ind] for row_ind in range(len(state))) != col_sums[col_ind]:
           return False
   if sum(state[row_ind][col_ind] for row_ind, col_ind in enumerate(diagonal)) != 89:
       return False
   return True


def heuristic(state, total_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the given total sum
   # This heuristic relaxes the constraint that the sum of all the numbers in the grid must be equal to the given total sum
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is equal to the current total sum), which is equal to the cost of reaching the successor node
   return abs(sum(sum(row) for row in state) - total_sum)


print(a_star())
