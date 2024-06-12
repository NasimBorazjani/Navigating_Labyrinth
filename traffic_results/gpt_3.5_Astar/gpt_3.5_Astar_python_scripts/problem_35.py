
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (('x', 18, 'x', 5, 'x', 6, 5, 'x', 6, 17, 'x'),
                     ('x', 'x', 1, 5, 9, 13, 'x', 2, 'x', 'x', 2),
                     ('x', 17, 12, 'x', 'x', 'x', 5, 'x', 'x', 17, 'x'),
                     (9, 3, 13, 8, 'x', 7, 'x', 'x', 4, 2, 'x'),
                     (11, 17, 'x', 10, 'x', 'x', 'x', 'x', 17, 15, 11),
                     ('x', 10, 10, 14, 9, 7, 1, 5, 'x', 'x', 7),
                     ('x', 5, 6, 12, 8, 9, 4, 'x', 'x', 4, 9),
                     (11, 'x', 4, 13, 14, 'x', 12, 17, 13, 'x', 'x'),
                     ('x', 8, 'x', 19, 11, 7, 7, 19, 15, 14, 7),
                     (11, 8, 'x', 11, 10, 16, 'x', 'x', 9, 'x', 5),
                     (9, 4, 'x', 'x', 1, 11, 14, 'x', 'x', 'x', 10))
    num_rows = 11
    num_cols = 11
    districts = {1: (0, 2), 2: (3, 7), 3: (8, 10)}
    start = (7, 8)
    end = (2, 1)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [], start)]

    while queue:
        _, g, actions, current = heapq.heappop(queue)

        if current == end and all(visited_costs.get((i, j)) for i, j in [(0, 0), (0, 2), (3, 0), (8, 0)]):
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_district = get_district(new_row, districts)
                if new_district and not visited_costs.get((new_row, new_col)) and new_cost < 1000:
                    visited_costs[(new_row, new_col)] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_row, new_col, end, districts), new_cost, actions + [(new_row, new_col)], (new_row, new_col)))

    return None


def heuristic(row, col, end, districts):
    # A heuristic function that calculates the Manhattan distance from the current position to the end position
    # The heuristic is admissible as it never overestimates the cost to reach the goal
    # The heuristic is consistent as the cost of moving from one position to a neighboring position is always 1
    # The cost of the goal state is 0, as it is the destination
    end_district = get_district(end[0], districts)
    current_district = get_district(row, districts)
    return abs(row - end[0]) + abs(col - end[1]) + abs(current_district - end_district)


def get_district(row, districts):
    # Helper function to determine the district number based on the row index
    for district, (start, end) in districts.items():
        if start <= row <= end:
            return district
    return None


print(a_star())
