
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (2, 1, 0)  # The third element in the tuple is the number of diagonal jumps made so far
    goal_state = (10, 9, 3)  # The goal state includes making exactly 3 diagonal jumps

    # Define the map of the trampoline park
    park = [[1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1]]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [initial_state], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path to the goal state
        if state == goal_state:
            return [(i, j) for i, j, _ in path]

        # Generate all possible actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the new state would be valid, ie if the new position is within the bounds of the park and the trampoline at the new position is not broken
            if 0 <= new_row < len(park) and 0 <= new_col < len(park[0]) and park[new_row][new_col] == 0:
                # The new state is valid, generate the new state
                new_state = (new_row, new_col, state[2] + int(abs(d_row) == abs(d_col)))
                # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
    # The heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps and presumes Alex can move to the goal position by making only vertical or horizontal jumps
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal position, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

print(a_star())
