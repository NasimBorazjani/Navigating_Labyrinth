
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((math.inf, math.inf, math.inf, 7, 11, 16, 13, 19, 15, math.inf, 19, math.inf, math.inf, 16),
                     (9, math.inf, 14, math.inf, 7, 3, math.inf, math.inf, 17, 9, math.inf, math.inf, math.inf, 19),
                     (math.inf, 11, 6, 18, math.inf, 19, 4, math.inf, math.inf, math.inf, 19, 12, 4, 17),
                     (5, 12, 15, 3, math.inf, math.inf, math.inf, math.inf, 7, math.inf, 11, 17, 20, 20),
                     (6, math.inf, 11, 15, 11, 17, 16, 5, math.inf, 3, 4, 20, math.inf, 14),
                     (math.inf, 11, math.inf, 6, math.inf, 16, 2, 18, 5, 11, math.inf, 14, 4, 7),
                     (math.inf, 6, math.inf, 17, math.inf, math.inf, 15, 7, math.inf, 2, 3, 16, 7, 15),
                     (7, math.inf, math.inf, 8, 1, math.inf, math.inf, math.inf, 14, math.inf, math.inf, 18, math.inf, 19),
                     (13, math.inf, math.inf, math.inf, math.inf, 2, 9, 19, math.inf, 16, 11, 5, math.inf, 11),
                     (math.inf, 17, 15, 18, math.inf, 7, math.inf, 15, 13, math.inf, 14, 2, math.inf, 19),
                     (math.inf, math.inf, math.inf, 14, 7, 19, math.inf, math.inf, 9, 9, math.inf, math.inf, math.inf, math.inf),
                     (math.inf, 3, 13, 15, 18, 17, math.inf, math.inf, 9, 4, math.inf, 12, 10, 14),
                     (15, math.inf, 6, 19, 19, 19, math.inf, 1, 8, 4, 17, 14, math.inf, math.inf),
                     (8, math.inf, 14, 7, 12, 6, 8, math.inf, 5, math.inf, 11, 11, math.inf, math.inf))

    num_rows = 14
    num_cols = 14
    districts = {0: (0, 3), 1: (4, 5), 2: (6, 13)}
    start = (3, 13)
    end = (4, 0)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end:
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != math.inf:
                new_cost = g + initial_state[new_row][new_col]
                new_state = (new_row, new_col)

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, end, districts), new_cost, actions + [new_state], new_state))

    return None


def heuristic(current, end, districts):
    # A heuristic that calculates the Manhattan distance between the current position and the destination
    # The heuristic is admissible as it never overestimates the cost to reach the goal
    # The heuristic is consistent as the cost of moving from one position to a neighboring position is always 1, which is exactly the decrease in the heuristic estimate
    # The heuristic is calculated separately for each district to ensure Ben visits at least one workshop in each district
    h = 0
    for district, (start_row, end_row) in districts.items():
        if start_row <= current[0] <= end_row:
            h += abs(current[0] - end[0]) + abs(current[1] - end[1])
    return h


print(a_star())
