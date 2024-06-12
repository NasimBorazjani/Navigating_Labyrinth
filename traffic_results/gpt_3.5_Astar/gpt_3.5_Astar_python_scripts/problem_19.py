
import heapq
import math


def a_star():
    # Define the matrix map of the city
    city_map = [[math.inf, 16, 15, 14, 2, 12, 3, math.inf, 7, 7],
                [11, math.inf, math.inf, math.inf, 4, 10, 5, math.inf, math.inf, math.inf],
                [12, math.inf, 3, math.inf, math.inf, 19, math.inf, 13, math.inf, math.inf],
                [16, 15, 13, math.inf, 12, math.inf, math.inf, 1, math.inf, 7],
                [2, 6, math.inf, 5, math.inf, 14, 7, math.inf, 8, 18],
                [19, 17, 2, 11, 8, 17, 12, 8, 9, 14],
                [11, 1, 10, 11, math.inf, math.inf, 19, 6, 2, 18],
                [7, math.inf, 10, 15, math.inf, math.inf, math.inf, math.inf, 18, 17],
                [math.inf, 6, math.inf, math.inf, math.inf, 5, math.inf, 7, 12, 20],
                [math.inf, math.inf, 2, 15, math.inf, 17, math.inf, math.inf, 10, 11]]

    num_rows = 10
    num_cols = 10
    districts = {1: [(0, 3), (1, 3), (2, 3), (3, 3)],
                 2: [(4, 5), (5, 5)],
                 3: [(6, 9), (7, 9), (8, 9), (9, 9)]}

    visited_costs = {}
    visited_costs[(5, 0)] = 0

    queue = [(0, 0, [], (5, 0))]

    while queue:
        _, g, actions, current_pos = heapq.heappop(queue)

        # Check if Ben has reached the destination workshop
        if current_pos == (3, 9):
            return actions

        # Generate all possible actions from the current position, which includes moving north, south, east, or west
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_pos[0] + d_row, current_pos[1] + d_col

            # Check if the new position is within the city map boundaries and not a closed workshop
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != math.inf:
                new_pos = (new_row, new_col)
                new_cost = g + city_map[new_row][new_col]

                # Check if Ben has visited at least one workshop in each district
                for district, workshops in districts.items():
                    if new_pos in workshops and all(workshop in actions for workshop in workshops):
                        break
                else:
                    continue

                if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                    visited_costs[new_pos] = new_cost
                    heapq.heappush(queue, (g + city_map[new_row][new_col], new_cost, actions + [new_pos], new_pos))

    return None


print(a_star())
