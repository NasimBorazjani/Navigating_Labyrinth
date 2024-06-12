
import heapq


def a_star():
    # Define the initial grid with some numbers given and others as 'x'
    grid = [['68', 'x', 'x', '76'],
            ['74', 'x', 'x', 'x'],
            ['x', 'x', '82', 'x'],
            ['66', 'x', '35', 'x']]

    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 229, 249, None]
    col_sums = [None, 189, 204, None]
    diagonal_sum = 219

    # Define the range of unique integers that can be placed in the grid
    unique_integers = list(range(33, 85))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], grid)]

    # While there are un-visited states
    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the grid is filled with unique integers and satisfies the constraints, return the actions taken
        if is_valid_solution(state, row_sums, col_sums, diagonal_sum):
            return actions

        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers
        for i in range(4):
            for j in range(4):
                if state[i][j] == 'x':
                    for num in unique_integers:
                        new_state = [row[:] for row in state]
                        new_state[i][j] = str(num)
                        new_cost = g + num

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_state))

    return None


def is_valid_solution(grid, row_sums, col_sums, diagonal_sum):
    # Check if the grid is filled with unique integers
    unique_numbers = set()
    for row in grid:
        for num in row:
            if num != 'x':
                unique_numbers.add(int(num))
    if len(unique_numbers) != 16:
        return False

    # Check if the sums of rows, columns, and diagonal match the constraints
    for i in range(4):
        if row_sums[i] is not None and sum(int(num) for num in grid[i]) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(int(grid[j][i]) for j in range(4)) != col_sums[i]:
            return False
    if (int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0])) != diagonal_sum:
        return False

    return True


def heuristic(grid, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and that the sums must match the constraints
    # It is admissible because it never overestimates the cost to reach the goal, as the sum of the differences is always less than or equal to the actual cost to reach the goal
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum increase in the sum is 1
    h = 0
    for i in range(4):
        if row_sums[i] is not None:
            h += abs(sum(int(num) for num in grid[i]) - row_sums[i])
        if col_sums[i] is not None:
            h += abs(sum(int(grid[j][i]) for j in range(4)) - col_sums[i])
    h += abs(int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0]) - diagonal_sum)
    return h


print(a_star())
