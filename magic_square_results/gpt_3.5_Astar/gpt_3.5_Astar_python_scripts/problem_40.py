
import heapq


def a_star():
    # Define the initial grid with the given numbers and 'x's
    initial_grid = [['38', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x'],
                    ['x', '39', '40', '27'],
                    ['32', '46', 'x', '25']]
    
    # Define the constraints for the rows, columns, and diagonal
    row_sums = [None, 135, 130, None]
    col_sums = [None, 149, 178, None]
    diagonal_sum = 151
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    num_unique_integers = 27
    
    visited_costs = {}
    visited_costs[str(initial_grid)] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_grid))
    
    while queue:
        _, g, actions, grid = heappop(queue)
        
        # If the grid satisfies all constraints, return the actions taken
        if check_constraints(grid, row_sums, col_sums, diagonal_sum):
            return actions
        
        # Generate all possible actions from the current grid, which includes replacing 'x's with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in range(24, 51):
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num
                        new_grid_str = str(new_grid)
                        
                        if new_grid_str not in visited_costs or new_cost < visited_costs[new_grid_str]:
                            visited_costs[new_grid_str] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))
    
    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
    for i in range(1, 3):
        if row_sums[i] is not None and sum(int(grid[i][j]) for j in range(4)) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(int(grid[j][i]) for j in range(4)) != col_sums[i]:
            return False
    if sum(int(grid[i][i]) for i in range(4)) != diagonal_sum:
        return False
    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences can only decrease as we replace 'x's with numbers
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum increase in the sum of a row, column, or diagonal is 1
    h = 0
    for i in range(1, 3):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(4)) - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_sums[i])
    h += abs(sum(int(grid[i][i]) for i in range(4)) - diagonal_sum)
    return h


print(a_star())
