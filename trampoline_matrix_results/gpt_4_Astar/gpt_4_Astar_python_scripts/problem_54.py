
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2D tuples
    initial_state = ((1, 7), 0)
    goal_state = (10, 0)
    # Define the grid of the trampoline park
    grid = [[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0]]
    # Define the directions of movement
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Define the size of the grid
    size = len(grid)

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

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the eight adjacent trampolines
        for direction in directions:
            new_state = (state[0][0] + direction[0], state[0][1] + direction[1])
            # Check if the new state is valid, ie if the new state is within the bounds of the grid and the trampoline is not broken
            if 0 <= new_state[0] < size and 0 <= new_state[1] < size and grid[new_state[0]][new_state[1]] == 0:
                # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
                new_cost = g + 1
                # Count the number of diagonal moves
                diagonal_moves = state[1]
                if direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    diagonal_moves += 1
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_state, diagonal_moves) not in visited_costs or new_cost < visited_costs[(new_state, diagonal_moves)]:
                    visited_costs[(new_state, diagonal_moves)] = new_cost
                    # The heuristic is the Manhattan distance to the goal state
                    h = abs(new_state[0] - goal_state[0]) + abs(new_state[1] - goal_state[1])
                    # Add a penalty if the number of diagonal moves is not 4
                    if diagonal_moves != 4:
                        h += 10
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], (new_state, diagonal_moves)))

    return None

print(a_star())
