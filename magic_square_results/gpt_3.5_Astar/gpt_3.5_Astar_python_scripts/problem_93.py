
import heapq


def a_star():
    # Define the initial grid with some numbers given and others as 'x'
    grid = [['53', '57', 'x', 'x'],
            ['77', '78', 'x', '56'],
            ['51', '62', '88', 'x'],
            ['x', 'x', 'x', 'x']]
    
    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 266, 261, None]
    col_sums = [244, 295, None, None]
    diagonal_sum = 265
    
    # Define the range of unique integers that can be placed in the grid
    unique_integers = list(range(41, 93))
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    
    visited_costs = {}
    visited_costs[str(grid)] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], grid))
    
    while queue:
        _, g, actions, grid = heappop(queue)
        
        # If the grid satisfies all constraints, return the actions taken
        if check_constraints(grid, row_sums, col_sums, diagonal_sum):
            return actions
        
        # Generate all possible actions from the current grid, which includes replacing 'x' with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 'x':
                    for num in unique_integers:
                        new_grid = [row[:] for row in grid]
                        new_grid[i][j] = str(num)
                        new_cost = g + num
                        
                        if str(new_grid) not in visited_costs or new_cost < visited_costs[str(new_grid)]:
                            visited_costs[str(new_grid)] = new_cost
                            heappush(queue, (new_cost + heuristic(new_grid, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_grid))
    
    return None


def check_constraints(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            if sum(int(grid[i][j]) for j in range(len(grid[i])) if grid[i][j] != 'x') != row_sums[i]:
                return False
    
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            if sum(int(grid[i][j]) for i in range(len(grid)) if grid[i][j] != 'x') != col_sums[j]:
                return False
    
    if sum(int(grid[i][i]) for i in range(len(grid)) if grid[i][i] != 'x') != diagonal_sum:
        return False
    
    if sum(int(grid[i][len(grid)-1-i]) for i in range(len(grid)) if grid[i][len(grid)-1-i] != 'x') != diagonal_sum:
        return False
    
    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and presumes we can directly replace 'x' with the unique integers to reach the target sums
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum value that can be placed in a position is the smallest unique integer, which is exactly the decrease in the heuristic estimate
    h = 0
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            h += abs(sum(int(grid[i][j]) for j in range(len(grid[i])) if grid[i][j] != 'x') - row_sums[i])
    
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            h += abs(sum(int(grid[i][j]) for i in range(len(grid)) if grid[i][j] != 'x') - col_sums[j])
    
    h += abs(sum(int(grid[i][i]) for i in range(len(grid)) if grid[i][i] != 'x') - diagonal_sum)
    h += abs(sum(int(grid[i][len(grid)-1-i]) for i in range(len(grid)) if grid[i][len(grid)-1-i] != 'x') - diagonal_sum)
    
    return h


print(a_star())
