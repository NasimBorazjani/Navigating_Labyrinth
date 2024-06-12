
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 0, 1, 1, 1, 1, 1, 0, 0),
                     (0, 1, 1, 1, 1, 1, 1, 0, 0),
                     (1, 1, 1, 1, 0, 0, 0, 1, 0),
                     (1, 1, 1, 0, 0, 1, 1, 0, 0),
                     (0, 0, 1, 0, 0, 1, 1, 0, 0),
                     (1, 1, 0, 0, 1, 0, 1, 0, 0),
                     (0, 1, 1, 1, 1, 1, 1, 1, 0),
                     (1, 0, 0, 0, 0, 1, 1, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0))
    num_rows = 9
    num_cols = 9
    start = (8, 2)
    goal = (0, 7)
    # Define the possible moves Alex can make, including diagonal jumps
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    # Define the number of diagonal jumps Alex must make
    num_diagonal_jumps = 3

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current_pos = heapq.heappop(queue)

        # If Alex reaches the goal position, return the sequence of trampolines he jumped on
        if current_pos == goal:
            return actions

        # Generate all possible actions from the current position, which includes moving to any of the eight adjacent trampolines
        for move in moves:
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            # Check if the new position is within the bounds of the grid and not a broken trampoline
            if 0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] == 0:
                # Calculate the number of diagonal jumps made so far
                num_diagonal_jumps_made = sum([1 for action in actions if abs(action[0] - current_pos[0]) == 1 and abs(action[1] - current_pos[1]) == 1])
                # Check if the number of diagonal jumps made does not exceed the limit
                if num_diagonal_jumps_made < num_diagonal_jumps:
                    new_cost = g + 1
                    if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                        visited_costs[new_pos] = new_cost
                        # Calculate the heuristic cost based on the Euclidean distance to the goal position
                        h = math.sqrt((new_pos[0] - goal[0]) ** 2 + (new_pos[1] - goal[1]) ** 2)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_pos], new_pos))
    return None


print(a_star())
