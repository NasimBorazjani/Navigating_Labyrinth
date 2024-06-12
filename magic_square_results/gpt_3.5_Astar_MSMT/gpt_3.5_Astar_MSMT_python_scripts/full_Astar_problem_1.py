
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing unknown numbers
   initial_state = [['35', 'x', '46'],
                    ['x', 'x', 'x'],
                    ['x', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   row_sum = [103, None, None]
   col_sum = [107, None, None]
   diagonal_sum = 124
   available_numbers = set(range(29, 49))


   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_state, available_numbers))
  
   return initial_state, num_rows, num_cols, row_sum, col_sum, diagonal_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, row_sum, col_sum, diagonal_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # If there are no remaining unknown numbers in the grid, check if the sums of rows, columns, and diagonal match the specified values
       if all(sum(int(cell) if cell != 'x' else 0 for cell in row) == sum_val if sum_val is not None else True for row, sum_val in zip(state, row_sum)) and \
          all(sum(int(row[i]) if row[i] != 'x' else 0 for row in state) == sum_val if sum_val is not None else True for i, sum_val in enumerate(col_sum)) and \
          sum(int(state[i][i]) if state[i][i] != 'x' else 0 for i in range(num_rows)) == diagonal_sum:
           return actions


       # If the state has at least 1 remaining unknown number, generate all possible actions from the current state
       if any('x' in row for row in state):
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       for num in available_numbers:
                           new_state = [list(row) for row in state]
                           new_state[i][j] = str(num)
                           new_state = [tuple(row) for row in new_state]
                           new_available_numbers = available_numbers.copy()
                           new_available_numbers.remove(num)
                           new_cost = g + num
                           new_state_tuple = tuple(new_state)
                           if new_state_tuple not in visited_costs or new_cost < visited_costs[new_state_tuple]:
                               visited_costs[new_state_tuple] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, row_sum, col_sum, diagonal_sum), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))
   return None




def heuristic(state, row_sum, col_sum, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the remaining unique numbers that can be added to the grid
   # The heuristic relaxes the constraint that the numbers in the grid must be unique, as it presumes we can add any of the remaining unique numbers to the grid
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most the value of the number added, which is exactly the cost of reaching the successor node
   return sum(available_numbers)


print(a_star())
