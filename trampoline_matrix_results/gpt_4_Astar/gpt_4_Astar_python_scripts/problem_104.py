
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as 2D tuples
    initial_state = (14, 1)
    goal_state = (2, 10)
    # Define the map of the park
    park_map = [[0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
                [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
                [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
                [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]]
    # Define the size of the park
    park_size = 15
    # Define the number of diagonal jumps
    num_diagonal_jumps = 5

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[(initial_state, num_diagonal_jumps)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], (initial_state, num_diagonal_jumps))]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, (state, diagonal_jumps) = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state and diagonal_jumps == 0:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the jump is valid, ie if the coordinate of the trampoline to jump to is a valid coordinate within the bounds of the park and the trampoline is not broken
            if 0 <= new_row < park_size and 0 <= new_col < park_size and park_map[new_row][new_col] == 0:
                # The jump is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
                new_cost = g + 1
                # If the jump is diagonal, decrement the number of diagonal jumps left
                new_diagonal_jumps = diagonal_jumps - 1 if d_row != 0 and d_col != 0 else diagonal_jumps

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_state, new_diagonal_jumps) not in visited_costs or new_cost < visited_costs[(new_state, new_diagonal_jumps)]:
                    visited_costs[(new_state, new_diagonal_jumps)] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], (new_state, new_diagonal_jumps)))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
    # The heuristic relaxes the constraint that Alex can only jump to an adjacent trampoline and presumes Alex can jump directly to the goal position
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

print(a_star())
