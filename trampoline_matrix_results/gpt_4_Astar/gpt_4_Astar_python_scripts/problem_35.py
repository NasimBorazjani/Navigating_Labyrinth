
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (1, 9, 0)  # The third element of the tuple is the number of diagonal jumps made so far
    goal_state = (8, 0)

    # Define the map of the trampoline park
    park_map = [[1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
                [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
                [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
                [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
                [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1]]

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [initial_state])]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path = heapq.heappop(queue)
        state = path[-1]

        # If the current state is the goal state, return the path
        if state[:2] == goal_state and state[2] == 3:
            return [(i, j) for i, j, _ in path]

        # Generate all valid actions from the current state, which includes jumping to any of the eight adjacent trampolines
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = state[0] + d_row, state[1] + d_col
            # Check if the jump is valid, ie if the new position is a valid coordinate within the bounds of the park and the trampoline is not broken
            if 0 <= new_row < 11 and 0 <= new_col < 11 and park_map[new_row][new_col] == 0:
                # The new state
                new_state = (new_row, new_col, state[2] + (d_row != 0 and d_col != 0))
                # The cost so far is the number of jumps made
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the Manhattan distance to the goal state
                    h = abs(new_row - goal_state[0]) + abs(new_col - goal_state[1])
                    heapq.heappush(queue, (new_cost + h, new_cost, path + [new_state]))

    return None

print(a_star())
