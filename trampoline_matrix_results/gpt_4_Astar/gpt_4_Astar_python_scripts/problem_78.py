
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2D tuples
    initial_state = (10, 12)
    goal_state = (1, 1)
    # Define the grid of the trampoline park
    grid = [[1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]]
    # Define the size of the grid
    num_rows = len(grid)
    num_cols = len(grid[0])
    # Define the directions of movement
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Define the cost of diagonal and non-diagonal movements
    diagonal_cost = 1.5
    non_diagonal_cost = 1

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, num_diagonal_jumps, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the 8 neighboring trampolines
        for direction in directions:
            new_state = (state[0] + direction[0], state[1] + direction[1])
            # Check if the new state is valid, ie if the new state is within the bounds of the grid and the trampoline is not broken
            if 0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and grid[new_state[0]][new_state[1]] == 0:
                # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
                # The cost of a diagonal jump is 1.5 and the cost of a non-diagonal jump is 1
                if direction in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    new_cost = g + diagonal_cost
                    new_num_diagonal_jumps = num_diagonal_jumps + 1
                else:
                    new_cost = g + non_diagonal_cost
                    new_num_diagonal_jumps = num_diagonal_jumps

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                # Also, the number of diagonal jumps must not exceed 4
                if new_num_diagonal_jumps <= 4 and (new_state not in visited_costs or new_cost < visited_costs[new_state]):
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_num_diagonal_jumps, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Alex can only move to neighboring trampolines and presumes Alex can move directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring trampoline is always 1 or 1.5, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance from the goal state to itself is 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

print(a_star())
