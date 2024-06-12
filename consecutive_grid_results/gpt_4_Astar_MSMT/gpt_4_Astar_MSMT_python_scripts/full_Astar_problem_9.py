
import heapq
import numpy as np

def initialize():
    # Define the initial state of the grid, as a 2d tuple
    initial_state = (('x', 'x', 'x'), ('x', '51', 'x'), ('x', '61', '64'))
    # Define the range of numbers that can be used to replace 'x'
    num_range = set(range(34, 67))
    # Define the size of the grid
    num_rows = 3
    num_cols = 3
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
    queue = [(0, 0, [], initial_state)]
    return initial_state, num_range, num_rows, num_cols, visited_costs, queue

def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, the range of numbers, and the dimensions of the grid)
    initial_state, num_range, num_rows, num_cols, visited_costs, queue = initialize()
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, replacements, state = heapq.heappop(queue)
        # Check if the current state is the goal state
        # The goal state is where all 'x's have been replaced with unique integers and the numbers in each row and column are consecutive
        if all(cell != 'x' for row in state for cell in row) and all(all(int(row[i]) < int(row[i + 1]) for i in range(len(row) - 1)) or all(int(row[i]) > int(row[i + 1]) for i in range(len(row) - 1)) for row in state) and all(all(int(state[i][j]) < int(state[i + 1][j]) for i in range(len(state) - 1)) or all(int(state[i][j]) > int(state[i + 1][j]) for i in range(len(state) - 1)) for j in range(len(state[0]))):
            return replacements
        # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
        for row_ind, row in enumerate(state):
            for col_ind, cell in enumerate(row):
                if cell == 'x':
                    # Get the set of numbers that are already in the grid
                    present_nums = set(int(num) for r in state for num in r if num != 'x')
                    # The available numbers are the numbers in the range that are not already in the grid
                    available_nums = num_range - present_nums
                    for num in available_nums:
                        # Generate the new state
                        new_state = [list(r[:]) for r in state]
                        new_state[row_ind][col_ind] = str(num)
                        new_state = tuple(tuple(r) for r in new_state)
                        # The cost so far is the sum of the numbers in the top row, right column, and main diagonal
                        new_cost = sum(int(num) for num in new_state[0]) + sum(int(new_state[i][-1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))
                        # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, replacements + [(row_ind, col_ind, num)], new_state))
                    break
            else:
                continue
            break
    return None

def heuristic(state):
    # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each 'x' in the grid
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as we always choose the minimum available number to replace 'x'
    # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing 'x' with a number is the number itself, which is always greater than or equal to the minimum available number
    h = 0
    present_nums = set(int(num) for row in state for num in row if num != 'x')
    available_nums = sorted(list(num_range - present_nums))
    for row in state:
        for cell in row:
            if cell == 'x':
                h += available_nums.pop(0)
    return h

print(a_star())
