import heapq
import math
import numpy as np
import sys

def a_star(initial_state, min_number, max_number, 
            col_sums, row_sums, diagonal_sum):
    num_rows = len(initial_state)
    num_cols = len(initial_state[0])
    initial_state =  [[int(i) if i != "" else 'x' for i in row] for row in initial_state]
    initial_state = tuple(tuple(row) for row in initial_state)

    numbers = set(range(min_number, max_number))


    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # The goal state must not have any unlnonw numbers, thus we need to get (the coordinates of) the unknown numbers to check wether the current state is the goal state 
        x_coords = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == 'x']
        if not x_coords:
            # Convert the cells of the state to ints to calulate and compare the sum of the specifiec positions in the current state with the given goal sums
            state_array = np.array([[int(element) for element in row] for row in state])
            if (np.all([i == j for i, j in zip(np.sum(state_array, axis=0), col_sums) if j]) and
                np.all([i == j for i, j in zip(np.sum(state_array, axis=1), row_sums) if j]) and
                np.trace(np.fliplr(state_array)) == diagonal_sum):
                return actions

        # If the state has at least 1 remaining unknown number, generate all possible actions from the current state, which includes replacing the next x in the grid with any of unique integers in the range 
        else:
            first_x_coord = x_coords[0]
            # The number must be unique and not be present in any other cells of the grid
            used_numbers  = set(int(cell) for row in state for cell in row if cell != 'x')
            available_numbers = sorted(list(numbers - used_numbers))
            for number in available_numbers:
                # Check if the new state, containing the new number, would be valid; ie the number must be unique and the sum of specified positions must not exceed the goal sums with the addition of the new number 
                sum_x_row_new_state = sum(int(cell) for cell in state[first_x_coord[0]] if cell != 'x') + number
                sum_x_col_new_state = sum(int(state[k][first_x_coord[1]]) for k in range(num_rows) if state[k][first_x_coord[1]] != 'x') + number
                sum_diag_new_state = sum(int(state[k][num_cols - 1 - k]) for k in range(num_rows) if state[k][num_cols - 1 - k] != 'x') + number
                
                new_state = [list(row[:]) for row in state]
                new_state[first_x_coord[0]][first_x_coord[1]] = str(number)
                
                new_col = [new_state[k][first_x_coord[1]] for k in range(num_rows)]
                new_diag = [new_state[k][num_cols - 1 - k] for k in range(num_rows)]
                
                # If the x is in one of the rows with a given sum, then the sum of the new row, with addition of the number, must not exceed the target sum
                if ((row_sums[first_x_coord[0]] is None or (sum_x_row_new_state < row_sums[first_x_coord[0]] and 'x' in new_state[first_x_coord[0]]) or (sum_x_row_new_state == row_sums[first_x_coord[0]] and not 'x' in new_state[first_x_coord[0]])) and
                    # Similarly, if the x position is in a column or the diagonal with a goal sum
                    (col_sums[first_x_coord[1]] is None or (sum_x_col_new_state < col_sums[first_x_coord[1]] and 'x' in new_col) or (sum_x_col_new_state == col_sums[first_x_coord[1]] and not 'x' in new_col)) and
                    (first_x_coord[0] != num_cols - 1 - first_x_coord[1] or (sum_diag_new_state <= diagonal_sum and 'x' in new_diag) or (sum_diag_new_state == diagonal_sum and 'x' not in new_diag))):
                
                    # Generate the new state
                    
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

import time
def main():
    # Read the initial state from the command line
    
    initial_state = eval(sys.argv[1])
    min_number = eval(sys.argv[2])
    max_number = eval(sys.argv[3])
    col_sums =  eval(sys.argv[4])
    row_sums = eval(sys.argv[5])
    diagonal_sum = eval(sys.argv[6])
    
    s = time.time()
    print(a_star(initial_state, min_number, max_number, 
                col_sums, row_sums, diagonal_sum))
    e = time.time()
    #print(e-s)

if __name__ == "__main__":
    main()
    
