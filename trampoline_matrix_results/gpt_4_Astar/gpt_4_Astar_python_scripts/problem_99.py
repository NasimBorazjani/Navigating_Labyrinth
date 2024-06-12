
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2D tuples
    initial_state = (11, 1)
    goal_state = (2, 12)
    # Define the grid of the trampoline park
    grid = [[0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]]
    num_rows = len(grid)
    num_cols = len(grid[0])
    # Define the possible moves from a trampoline
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, 0)]
    while queue:
        _, g, actions, state, num_diagonal_jumps = heapq.heappop(queue)
        # If the current state is the goal state and the number of diagonal jumps is exactly 5, return the actions taken
        if state == goal_state and num_diagonal_jumps == 5:
            return actions
        # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
        for move in moves:
            new_state = (state[0] + move[0], state[1] + move[1])
            # Check if the new state is valid, ie within the bounds of the grid and the trampoline is not broken
            if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and grid[new_state[0]][new_state[1]] == 0):
                # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
                new_cost = g + 1
                # If the move is diagonal, increment the number of diagonal jumps
                new_num_diagonal_jumps = num_diagonal_jumps + 1 if move in [(1, 1), (-1, -1), (1, -1), (-1, 1)] else num_diagonal_jumps
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_num_diagonal_jumps))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
    # The heuristic relaxes the constraint that Alex can only jump to an adjacent trampoline and presumes Alex can jump directly to the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal state, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance from the goal state to itself is 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

print(a_star())
