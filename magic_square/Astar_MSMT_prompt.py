import heapq
import math
import numpy as np

def initialize():
    # Define the initial state of the grid as a 2d tuple
    initial_state = (('47', 'x', 'x', '32'),
                    ('x', 'x', 'x', '49'),
                    ('x', '31', '50', 'x'),
                    ('x', 'x', '52', '30'))
    num_rows = 4
    num_cols = 4
    row_sums = [None, 187, 149, None]
    col_sums = [None, 148, 196, None]
    diagonal_sum = 166
    # Create the set of the valid numbers that could be in the grid 
    numbers = set(range(29, 54))

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]
    
    return initial_state, num_rows, num_cols, row_sums, col_sums, diagonal_sum, numbers, visited_costs, queue
    
def a_star():
    
    initial_state, num_rows, num_cols, row_sums, col_sums, diagonal_sum, numbers, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # The goal state must not have any unlnonw numbers, thus we need to get (the coordinates of) the unknown numbers to check wether the current state is the goal state 
        x_coords = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == 'x']
        if not x_coords:
            # Convert the cells of the state to ints to calulate and compare the sum of the specifiec positions in the current state with the given goal sums
            state_array = np.array([[int(element) for element in row] for row in state])
            if (np.all([i == j for i, j in zip(np.sum(state_array, axis=0), col_sums) if j]) and
                np.all([i == j for i, j in zip(np.sum(state_array, axis=1), row_sums) if j]) and
                np.trace(state_array) == diagonal_sum):
                return actions

        # If the state has at least 1 remaining unknown number, generate all possible actions from the current state, which includes replacing the next x in the grid with any of unique integers in the range 
        else:
            first_x_coord = x_coords[0]
            # The number must be unique and not be present in any other cells of the grid
            used_numbers  = set(int(cell) for row in state for cell in row if cell != 'x')
            for number in numbers:
                # Check if the new state, containing the new number, would be valid; ie the number must be unique and the sum of specified positions must not exceed the goal sums with the addition of the new number 
                sum_x_row_new_state = sum(int(cell) for cell in state[first_x_coord[0]] if cell != 'x') + number
                sum_x_col_new_state = sum(int(state[k][first_x_coord[1]]) for k in range(num_rows) if state[k][first_x_coord[1]] != 'x') + number
                sum_diag_new_state = sum(int(state[k][k]) for k in range(num_rows) if state[k][k] != 'x') + number
                if (number not in used_numbers and
                    # If the x is in one of the rows with a given sum, then the sum of the new row, with addition of the number, must not exceed the target sum
                    (row_sums[first_x_coord[0]] is None or sum_x_row_new_state <= row_sums[first_x_coord[0]]) and
                    # Similarly, if the x position is in a column or the diagonal with a goal sum
                    (col_sums[first_x_coord[1]] is None or sum_x_col_new_state <= col_sums[first_x_coord[1]]) and
                    (first_x_coord[0] != first_x_coord[1] or sum_diag_new_state <= diagonal_sum)):
                
                    # Generate the new state
                    new_state = [list(row[:]) for row in state]
                    new_state[first_x_coord[0]][first_x_coord[1]] = str(number)
                    new_state = tuple(tuple(row) for row in new_state)
                    # The additional cost of this state is the value of the number replaced with x as we are trying to minimize the sum of the numbers in the grid
                    new_cost = g + number
                    
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                        h = heuristic(new_state, row_sums, numbers)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_x_coord[0], first_x_coord[1], number)], new_state))
    return None


def heuristic(state, row_sums, numbers):
    # Relax the columns and diagonal sum constraints to compute an admissible and consistent heuristic
    # This heuristic considers the sum of differences between the given and current row sums, for rows with a specified sum value that have at least one unknown number, filling other x with the smallest unique number
    
    # The heuristic assumes xs can be filled with the smallest unique number satisfying row sum constraints, even if column or diagonal constraints are violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-increasing along the path to the goal state, because the cost of replacing an x in the grid with a number is the number itself, which is always greater than or equal to the number used to fill that position in the heuristic

    # Get numbers not used int he state currently
    used_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
    available_numbers = sorted(list(numbers - used_numbers))
    h = 0
    for i in range(len(state)):
        if row_sums[i] is not None:
            row_full = True
            sum_row = sum(int(cell) for cell in state[i] if cell != 'x')
            # Check to see if the row with a target some has any more xs
            for cell in state[i]:
                if cell == 'x':
                    row_full = False
            
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