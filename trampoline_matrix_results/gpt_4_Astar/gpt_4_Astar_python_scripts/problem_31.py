
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (1, 10)
    goal_state = (9, 3)
    # Define the grid of the trampoline park
    grid = [[1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1]]
    # Define the size of the grid
    num_rows = len(grid)
    num_cols = len(grid[0])
    # Define the directions of movement
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Define the number of diagonal jumps
    num_diagonal_jumps = 3

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[(initial_state, num_diagonal_jumps)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state, num_diagonal_jumps)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, diagonal_jumps = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state == goal_state and diagonal_jumps == 0:
            return actions

        # Generate all possible actions from the current state
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid
            if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
                grid[new_state[0]][new_state[1]] == 0):
                # Check if the move is diagonal
                if direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    # If the move is diagonal, decrease the number of diagonal jumps
                    new_diagonal_jumps = diagonal_jumps - 1
                else:
                    new_diagonal_jumps = diagonal_jumps
                # If the number of diagonal jumps is not negative, continue
                if new_diagonal_jumps >= 0:
                    # The cost so far is the number of jumps made
                    new_cost = g + 1
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if (new_state, new_diagonal_jumps) not in visited_costs or new_cost < visited_costs[(new_state, new_diagonal_jumps)]:
                        visited_costs[(new_state, new_diagonal_jumps)] = new_cost
                        # The heuristic is the Manhattan distance to the goal state
                        h = abs(new_state[0] - goal_state[0]) + abs(new_state[1] - goal_state[1])
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_diagonal_jumps))
    return None

print(a_star())
