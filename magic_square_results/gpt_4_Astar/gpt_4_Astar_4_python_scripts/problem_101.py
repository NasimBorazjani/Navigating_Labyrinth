
import heapq

def a_star():
    # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of unique integers that can be used to fill the grid
    initial_state = (('44', 'x', 'x', 'x'), ('90', '52', 'x', '91'), ('x', '58', 'x', '62'), ('x', '80', 'x', 'x'))
    row_sums = [None, 315, 234, None]
    col_sums = [None, 279, 306, None]
    diag_sum = 264
    num_rows = 4
    num_cols = 4
    available_numbers = set(range(36, 93)) - set(int(cell) for row in initial_state for cell in row if cell != 'x')

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        # The goal state is where all the 'x's in the grid are replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
        if all(cell != 'x' for row in state for cell in row):
            if all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and \
               all(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and \
               sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') == diag_sum:
                return actions

        # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
        if any(cell == 'x' for row in state for cell in row):
            # Find the next 'x' in the grid
            for i in range(num_rows):
                for j in range(num_cols):
                    if state[i][j] == 'x':
                        # Try replacing the 'x' with each of the available numbers
                        for number in available_numbers:
                            # Generate the new state
                            new_state = [list(row) for row in state]
                            new_state[i][j] = str(number)
                            new_state = tuple(tuple(row) for row in new_state)
                            # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                            new_cost = g + number

                            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diag_sum), new_cost, actions + [(i, j, number)], new_state))
                        # Once we have tried all possible numbers for the current 'x', break the loop to avoid replacing other 'x's in the same iteration
                        break
                else:
                    continue
                break
    return None

def heuristic(state, row_sums, col_sums, diag_sum):
    # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums and the goal sums of the rows, columns, and diagonal
    # The heuristic relaxes the constraints that each number in the grid must be unique and that the sum of all of the numbers in the grid is as low as possible; ie It presumes we can add any number to the grid to reach the goal sums
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current sum and the goal sum
    h = 0
    num_rows = len(state)
    num_cols = len(state[0])
    for row, row_sum in zip(state, row_sums):
        if row_sum is not None:
            h += abs(sum(int(cell) for cell in row if cell != 'x') - row_sum)
    for j, col_sum in enumerate(col_sums):
        if col_sum is not None:
            h += abs(sum(int(state[i][j]) for i in range(num_rows) if state[i][j] != 'x') - col_sum)
    h += abs(sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') - diag_sum)
    return h

print(a_star())
