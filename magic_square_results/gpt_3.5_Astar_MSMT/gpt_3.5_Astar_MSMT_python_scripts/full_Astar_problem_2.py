
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing unknown numbers
   initial_state = [['x', 'x', 'x'],
                    ['30', 'x', 'x'],
                    ['x', 'x', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   row_sum = [0, 87, 0]
   col_sum = [82, 0, 0]
   diagonal_sum = 94
   available_numbers = set(range(20, 40))


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_rows, num_cols, row_sum, col_sum, diagonal_sum, available_numbers, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, row_sum, col_sum, diagonal_sum, available_numbers, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If there are no remaining unknown numbers in the grid, and the sums of rows, columns, and diagonal match the specified values, return the actions taken
       if all(sum(int(cell) if cell != 'x' else 0 for cell in row) == row_sum[i] for i, row in enumerate(state)) and \
          all(sum(int(row[j]) if row[j] != 'x' else 0 for row in state) == col_sum[j] for j in range(num_cols)) and \
          sum(int(state[i][i]) if state[i][i] != 'x' else 0 for i in range(num_rows)) == diagonal_sum:
           return actions


       # If the state has at least 1 remaining unknown number, generate all possible actions from the current state
       if any(cell == 'x' for row in state for cell in row):
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
                           new_state_str = str(new_state)


                           if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                               visited_costs[new_state_str] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, row_sum, col_sum, diagonal_sum, new_available_numbers), new_cost, actions + [(i, j, num)], new_state))
   return None




def heuristic(state, row_sum, col_sum, diagonal_sum, available_numbers):
   # An admissible and consistent heuristic for this problem is the sum of the remaining unique numbers that can be added to the grid
   # The heuristic relaxes the constraint that the numbers in the grid must be unique, as it presumes we can add any of the remaining unique numbers to the grid
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number that can be added to the grid is the smallest number in the remaining unique numbers, which is exactly the number added to the grid in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   return sum(available_numbers)


print(a_star())
