
import heapq
import math


def a_star():
    # Define the matrix map of the city
    city_map = [[0, 0, 13, 0, 0, 7, 0, 13, 3, 0, 13],
                [10, 4, 0, 4, 12, 2, 0, 3, 4, 0, 15],
                [0, 3, 0, 0, 15, 9, 0, 0, 18, 17, 14],
                [5, 0, 0, 0, 3, 0, 11, 0, 17, 9, 17],
                [8, 3, 13, 0, 5, 7, 8, 17, 7, 0, 0],
                [0, 0, 13, 2, 2, 11, 6, 8, 0, 0, 0],
                [0, 1, 9, 6, 5, 13, 16, 1, 7, 5, 0],
                [4, 0, 13, 0, 10, 18, 3, 0, 0, 19, 19],
                [0, 0, 0, 2, 5, 9, 13, 0, 7, 1, 0],
                [0, 0, 7, 0, 0, 5, 19, 0, 0, 0, 1],
                [0, 0, 0, 6, 0, 19, 0, 0, 0, 0, 1]]

    num_rows = 11
    num_cols = 11
    districts = {1: [(0, 2), (1, 2), (2, 2)],
                 2: [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
                 3: [(5, 0), (6, 1), (7, 2), (8, 3), (9, 4), (10, 5)]}

    visited_costs = {}
    visited_costs[(5, 2)] = 0

    queue = [(0, 0, [], (5, 2))]

    while queue:
        _, g, actions, current_pos = heapq.heappop(queue)

        # Check if Ben has reached the destination workshop
        if current_pos == (2, 10):
            return actions

        # Generate all possible actions from the current position, moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_pos[0] + d_row, current_pos[1] + d_col

            # Check if the new position is within the city map boundaries and not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 0:
                new_pos = (new_row, new_col)
                new_cost = g + city_map[new_row][new_col]

                # Check if Ben has visited at least one workshop in each district
                for district, workshops in districts.items():
                    if new_pos in workshops and not any(workshop in actions for workshop in workshops):
                        break
                else:
                    # If Ben has visited at least one workshop in each district, add the new position to the queue
                    if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                        visited_costs[new_pos] = new_cost
                        h = heuristic(new_pos, (2, 10))
                        heapq.heappush(queue, (g + h, new_cost, actions + [new_pos], new_pos))

    return None


def heuristic(current_pos, destination):
    # A heuristic function that calculates the Manhattan distance between the current position and the destination
    return abs(current_pos[0] - destination[0]) + abs(current_pos[1] - destination[1])


print(a_star())
