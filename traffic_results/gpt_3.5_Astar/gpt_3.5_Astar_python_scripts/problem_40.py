
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (
        ('x', 10, 'x', 8, 13, 8, 4, 3, 15, 'x', 17),
        (9, 'x', 6, 4, 17, 'x', 16, 3, 19, 'x', 'x'),
        (8, 3, 18, 'x', 'x', 3, 'x', 7, 12, 16, 17),
        (8, 'x', 'x', 13, 'x', 7, 'x', 8, 'x', 12, 9),
        (2, 9, 'x', 'x', 9, 4, 18, 'x', 'x', 11, 'x'),
        (14, 20, 'x', 'x', 'x', 'x', 10, 'x', 'x', 7, 'x'),
        ('x', 'x', 18, 16, 12, 10, 'x', 'x', 10, 'x', 'x'),
        ('x', 'x', 16, 'x', 'x', 10, 'x', 'x', 3, 18, 18),
        ('x', 'x', 'x', 'x', 'x', 'x', 13, 3, 'x', 'x', 'x'),
        (5, 13, 1, 'x', 'x', 8, 'x', 19, 'x', 'x', 'x'),
        ('x', 'x', 16, 'x', 'x', 7, 18, 4, 11, 'x', 16)
    )
    num_rows = 11
    num_cols = 11
    districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (4, 10)], 3: [(5, 0), (10, 10)]}
    start = (3, 10)
    end = (5, 1)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end:
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_district = get_district(new_row, new_col, districts)
                if new_row == end[0] and new_col == end[1]:
                    new_district = 0
                if new_district != 0 and new_district not in [get_district(action[0], action[1], districts) for action in actions]:
                    new_cost += 100
                if new_cost < visited_costs.get((new_row, new_col), math.inf):
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (g + 1, new_cost, actions + [(new_row, new_col)], (new_row, new_col)))

    return None

def get_district(row, col, districts):
    for district, coords in districts.items():
        if coords[0][0] <= row <= coords[1][0] and coords[0][1] <= col <= coords[1][1]:
            return district
    return 0

print(a_star())
