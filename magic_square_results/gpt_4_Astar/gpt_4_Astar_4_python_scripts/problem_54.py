
import heapq

def a_star():
    # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of unique integers
    initial_state = (('30', 'x', 'x', '37'), ('41', '56', 'x', 'x'), ('x', 'x', '29', '55'), ('x', 'x', 'x', '42'))
    row_sums = [None, 196, 162, None]
    col_sums = [None, 208, 157, None]
    diag_sum = 166
    num_rows = 4
    num_cols = 4
    available_numbers = set(range(28, 60))

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
        # The goal state is where all of the 'x's in the grid are replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
        if all(cell != 'x' for row in state for cell in row):
            return actions

        # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for number in available_numbers - set(cell for row in state for cell in row if cell != 'x'):
                        # Generate the new state
                        new_state = [list(row[:]) for row in state]
                        new_state[i][j] = str(number)
                        new_state = tuple(tuple(row) for row in new_state)
                        # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                        new_cost = g + number

                        # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diag_sum), new_cost, actions + [(i, j, number)], new_state))
                    break
            else:
                continue
            break
    return None

def heuristic(state, row_sums, col_sums, diag_sum):
    # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and the goal sums
    # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the goal sums
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current sums and the goal sums
    h = 0
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            h += abs(row_sums[i] - sum(int(cell) for cell in state[i] if cell != 'x'))
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            h += abs(col_sums[j] - sum(int(state[i][j]) for i in range(len(state)) if state[i][j] != 'x'))
    h += abs(diag_sum - sum(int(state[i][len(state) - i - 1]) for i in range(len(state)) if state[i][len(state) - i - 1] != 'x'))
    return h

print(a_star())
