
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle, represented as tuples
    initial_state = (0, 13)
    goal_state = (8, 1)

    # Define the map of the trampoline park
    park_map = [
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1]
    ]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, 0)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, diagonal_jumps = heapq.heappop(queue)

        # If the current state is the goal state and the number of diagonal jumps is exactly 4, return the actions taken
        if state == goal_state and diagonal_jumps == 4:
            return actions

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state is valid, ie within the bounds of the park and the trampoline is not broken
            if 0 <= new_row < 14 and 0 <= new_col < 14 and park_map[new_row][new_col] == 0:
                # The new state is valid, generate the new state
                new_state = (new_row, new_col)
                # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
                new_cost = g + 1
                # If the jump was diagonal, increment the count of diagonal jumps
                new_diagonal_jumps = diagonal_jumps + 1 if d_row != 0 and d_col != 0 else diagonal_jumps

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_diagonal_jumps))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current position to the goal position
    # The heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps and presumes Alex can move to the goal position by jumping to any of the eight adjacent trampolines
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance from the goal position to itself is 0.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

print(a_star())
