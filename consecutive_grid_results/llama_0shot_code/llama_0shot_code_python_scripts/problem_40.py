
from itertools import permutations

def solve_grid(grid, possible_numbers, current_row=0, current_col=0, current_sum=0, current_combo=None):
    if current_combo is None:
        current_combo = []
    if current_row == len(grid):
        # We've filled all the cells.
        # Calculate the sum of the numbers in the topmost row, the rightmost column, and the diagonal.
        top_row_sum = sum(grid[0])
        right_col_sum = sum(grid[i][-1] for i in range(len(grid)))
        diagonal_sum = grid[0][0] + grid[1][1] + grid[2][2]
        total_sum = current_sum + top_row_sum + right_col_sum + diagonal_sum
        # If this combination gives a smaller sum, update the solution.
        if not solution or total_sum < solution[0]:
            solution[0] = total_sum
            solution[1] = current_combo[:]
    else:
        for num in possible_numbers:
            # Check if the number can be placed in the current cell.
            if current_col > 0 and num <= grid[current_row][current_col - 1]:
                continue
            if current_row > 0 and num <= grid[current_row - 1][current_col]:
                continue
            # Place the number in the current cell and update the current sum.
            grid[current_row][current_col] = num
            current_sum += num
            current_combo.append((current_row, current_col, num))
            # Move to the next cell.
            if current_col == len(grid) - 1:
                current_row += 1
                current_col = 0
            else:
                current_col += 1
            # Recurse to fill the rest of the cells.
            solve_grid(grid, possible_numbers, current_row, current_col, current_sum, current_combo)
            # Backtrack: remove the number from the current cell and subtract its value from the current sum.
            current_sum -= num
            grid[current_row][current_col] = 'x'
            current_combo.pop()
            if current_col == 0:
                current_row -= 1
                current_col = len(grid) - 1
            else:
                current_col -= 1

possible_numbers = list(range(34, 87))
grid = [['x', 'x', 'x'], ['65', 'x', 'x'], ['79', '73', '50']]
solution = [float('inf'), []]
solve_grid(grid, possible_numbers)
print(solution[1])
