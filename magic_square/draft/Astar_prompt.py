import heapq
import math
import numpy as np


def a_star():
    # Define the initial state of the grid
    initial_state = (('47', 'x', 'x', '32'),
                    ('x', 'x', 'x', '49'),
                    ('x', '31', '50', 'x'),
                    ('x', 'x', '52', '30'))
    num_rows = num_cols = 4
    row_sums = [None, 187, 149, None]
    col_sums = [None, 148, 196, None]
    diagonal_sum = 166
    numbers = set(range(29, 54))
    first_x_coord_to_fill = (0, 1)


    visited_costs = {}
    visited_costs[initial_state] = 0


    # Initialize a priority queue with the initial cost + heuristic, cost, the first grid coord to fill, an empty list of actions, and initial state
    queue = [(0, 0, first_x_coord_to_fill, [], initial_state)]
    num_states_generated = 1

    while queue:
       _, g, x_coord, actions, state = heapq.heappop(queue)
       # Create a list version of the state to check the sum of rows, columns, and the diagonal, and determine if an integer is unique in the grid
       list_state = np.array([[int(x) if x != 'x' else 0 for x in row] for row in state])
      
       # The goal state must not have any unknown numbers
       if not x_coord:
           if (np.all([i == j for i, j in zip(np.sum(list_state, axis=0), col_sums) if j]) and
               np.all([i == j for i, j in zip(np.sum(list_state, axis=1), row_sums) if j]) and
               np.trace(list_state) == diagonal_sum):
               return actions, num_states_generated


       # If the state has at least 1 x, generate all possible actions from the current state, which includes replacing the next x in the grid with any of unique integers in the range 
       if x_coord:
           for number in numbers:
               sum_x_row_new_state = sum(int(cell) for cell in state[x_coord[0]] if cell != 'x') + number
               sum_x_col_new_state = sum(int(state[k][x_coord[1]]) for k in range(num_rows) if state[k][x_coord[1]] != 'x') + number
               sum_diag_new_state = sum(int(state[k][k]) for k in range(num_rows) if state[k][k] != 'x') + number
               # Check if the new state would be valid
               #The number must be unique and not be present in any other cells of the grid
               if (number not in set(list_state.flatten()) and
                   # If the x is in one of the rows with a given sum, then the sum of the new row, with addition of the number, must not exceed the target sum
                   (row_sums[x_coord[0]] is None or sum_x_row_new_state <= row_sums[x_coord[0]]) and
                   # Similarly, if the x position is in a column or the diagonal with a goal sum
                   (col_sums[x_coord[1]] is None or sum_x_col_new_state <= col_sums[x_coord[1]]) and
                   (x_coord[0] != x_coord[1] or sum_diag_new_state <= diagonal_sum)):
              
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[x_coord[0]][x_coord[1]] = str(number)
                   new_state = tuple(tuple(row) for row in new_state)
                   new_cost = g + number
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Record the next x to fill
                       next_x_coord = find_next_x(new_state, x_coord)
                       h = heuristic(new_state, row_sums, numbers)
                       heapq.heappush(queue, (g + h, new_cost, next_x_coord, actions + [(x_coord[0], x_coord[1], number)], new_state))
                       num_states_generated += 1
    return None, num_states_generated


def find_next_x(state, start_index):
   # Flatten the grid state to a 1D array
   flat_state = np.array([x for row in state for x in row])
  
   # Convert the 2D start index to a 1D index
   start_index_1d = start_index[0] * len(state[0]) + start_index[1]
  
   # Find the next x in the flattened grid starting from after the start_index
   for i in range(start_index_1d + 1, len(flat_state)):
       if flat_state[i] == 'x':
           return np.unravel_index(i, (len(state), len(state[0])))
  
   # If no x is found, return None
   return None


def heuristic(state, row_sums, numbers):
   # Relaxing the constraints on the columns sums and the diagonal sum
   num_rows = len(state)
   used_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
   available_numbers = sorted(list(numbers - used_numbers))


   h = 0
   for i in range(num_rows):
       if row_sums[i] is not None:
           row_full = True
           sum_row = sum(int(cell) for cell in state[i] if cell != 'x')
           # Check to see if the row with a target some has any more xs
           for cell in state[i]:
               if cell == 'x':
                   row_full = False
          
           # If there exists an x in the row, add the difference between the current sum and target sum to the heuristic         
           if not row_full:   
               h += row_sums[i] - sum_row
           # Otherwise the sum of a row must equal the target sum or there's no path to reach the goal state from this state. Return math.inf
           else:
               if sum_row != row_sums[i]:
                   return math.inf
       # For other rows, greedily fill the x positions with the smallest unique number in the range
       else:
           for cell in state[i]:
               if cell == 'x' and available_numbers:
                   h += available_numbers.pop(0)
   return h


print(a_star())