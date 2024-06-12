
import heapq


def initialize():
    # Define the initial state of the grid, with 'x' represented as None
    initial_state = [[12, None, None], [18, None, 52], [22, None, 31]]
    # Define the goal state, with all 'x' replaced with unique integers
    goal_state = [[12, 15, 16], [18, 20, 52], [22, 24, 31]]
    # Define the constraints of the grid
    num_rows = 3
    num_cols = 3

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    return initial_state, goal_state, num_rows, num_cols, visited_costs, queue


def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal grids and dimensions of the grid)
    initial_state, goal_state, num_rows, num_cols, visited_costs, queue = initialize()

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
        for row in range(num_rows):
            for col in range(num_cols):
                if state[row][col] is None:
                    # Generate the new state
                    new_state = [list(row[:]) for row in state]
                    # Replace the 'x' with a unique integer from the given range
                    new_state[row][col] = get_unique_integer(state)
                    new_state = [tuple(row) for row in new_state]
                    # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row, col, new_state[row][col])], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the values of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
    h = sum(state[0]) + sum(row[-1] for row in state) + sum(state[i][i] for i in range(len(state)))
    return h


def get_unique_integer(state):
    # Get the unique integers from the given range
    unique_integers = list(range(13, 61))
    # Remove the integers that already exist in the state
    for row in state:
        for cell in row:
            if cell is not None:
                unique_integers.remove(cell)
    # Return the first unique integer
    return unique_integers[0]


print(a_star())
