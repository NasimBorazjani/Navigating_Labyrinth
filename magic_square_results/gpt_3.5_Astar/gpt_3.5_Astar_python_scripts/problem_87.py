
import heapq


def a_star():
    # Define the initial grid with the given numbers and 'x's
    grid = [[72, 76, 68, 69],
            [56, 'x', 'x', 'x'],
            [49, 'x', 'x', 43],
            ['x', 'x', 61, 'x']]
    
    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 233, 237, None]
    col_sums = [None, 258, 247, None]
    diagonal_sum = 242
    
    # Define the range of unique integers that can be placed in the grid
    unique_integers = list(range(37, 84))
    
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = []
    heapq.heappush(queue, (0, 0, [], grid))
    
    # While there are unvisited states
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # If the grid is filled and satisfies all constraints, return the actions taken
        if is_valid_solution(state, row_sums, col_sums, diagonal_sum):
            return actions
        
        # Generate all possible actions from the current state, which includes replacing 'x's with unique integers
        for i in range(4):
            for j in range(4):
                if state[i][j] == 'x':
                    for num in unique_integers:
                        new_state = [row[:] for row in state]
                        new_state[i][j] = num
                        new_cost = g + num
                        
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_state))
    
    return None


def is_valid_solution(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid satisfies all constraints
    for i in range(4):
        if row_sums[i] is not None and sum(grid[i]) != row_sums[i]:
            return False
        
        if col_sums[i] is not None and sum(row[i] for row in grid) != col_sums[i]:
            return False
    
    if grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0] != diagonal_sum:
        return False
    
    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences can only decrease as we get closer to the goal
    # It is consistent because the estimated cost of the next node is higher if the sum of a row, column, or diagonal is further from the target sum, or equal or less by at most 1 (equal to the cost of reaching the successor node)
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(grid[i]) - row_sums[i])
        
        if col_sums[i] is not None:
            h += abs(sum(row[i] for row in grid) - col_sums[i])
    
    h += abs(grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0] - diagonal_sum)
    
    return h


print(a_star())
