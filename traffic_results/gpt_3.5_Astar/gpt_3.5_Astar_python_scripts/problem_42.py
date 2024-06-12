
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((14, 'x', 11, 'x', 'x', 8, 15, 17, 18, 'x', 11),
                     (13, 9, 2, 7, 9, 12, 7, 'x', 'x', 'x', 12),
                     ('x', 2, 8, 13, 5, 'x', 'x', 7, 18, 'x', 'x'),
                     (19, 6, 1, 6, 19, 13, 14, 'x', 'x', 17, 'x'),
                     ('x', 9, 6, 'x', 'x', 14, 10, 'x', 'x', 5, 'x'),
                     (12, 'x', 'x', 'x', 7, 17, 11, 'x', 'x', 1, 'x'),
                     ('x', 16, 'x', 2, 11, 15, 6, 'x', 14, 14, 4),
                     ('x', 15, 14, 11, 'x', 17, 20, 18, 4, 16, 8),
                     ('x', 3, 6, 4, 1, 5, 'x', 'x', 3, 7, 9),
                     (18, 14, 3, 4, 'x', 'x', 'x', 12, 15, 10, 'x'),
                     ('x', 8, 'x', 1, 18, 'x', 'x', 'x', 'x', 'x', 'x'))
    num_rows = 11
    num_cols = 11
    districts = {1: (0, 3), 2: (4, 5), 3: (6, 10)}
    start = (6, 10)
    end = (3, 2)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        # If Ben reaches the destination workshop, return the path taken
        if current == end:
            return actions

        # Generate all possible actions from the current workshop, moving north, south, east, or west
        for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            # Check if the new position is within the city map and not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_position = (new_row, new_col)
                new_cost = g + initial_state[new_row][new_col]

                # Check if Ben has visited at least one workshop in each district on the path
                district_visited = {1: False, 2: False, 3: False}
                for action in actions:
                    if districts[1][0] <= action[0] <= districts[1][1]:
                        district_visited[1] = True
                    elif districts[2][0] <= action[0] <= districts[2][1]:
                        district_visited[2] = True
                    elif districts[3][0] <= action[0] <= districts[3][1]:
                        district_visited[3] = True

                if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                    visited_costs[new_position] = new_cost
                    h = heuristic(new_position, end, district_visited)
                    heapq.heappush(queue, (g + h, new_cost, actions + [new_position], new_position))

    return None


def heuristic(current, end, district_visited):
    # The heuristic function calculates the Manhattan distance between the current position and the destination
    # It also considers the number of districts Ben has visited to ensure he visits at least one workshop in each district
    h = abs(current[0] - end[0]) + abs(current[1] - end[1])

    # If Ben has not visited at least one workshop in each district, add a large value to the heuristic
    if not all(district_visited.values()):
        h += 1000

    return h


print(a_star())
