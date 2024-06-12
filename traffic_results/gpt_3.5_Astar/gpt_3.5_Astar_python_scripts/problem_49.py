
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (
        ('x', 'x', 13, 9, 'x', 15, 'x', 'x', 2, 13, 9, 11),
        (8, 'x', 4, 5, 13, 'x', 'x', 7, 16, 'x', 15, 13),
        ('x', 'x', 'x', 'x', 3, 'x', 4, 3, 18, 'x', 11, 18),
        (6, 'x', 14, 5, 16, 'x', 11, 'x', 3, 16, 3, 3),
        (15, 12, 'x', 'x', 10, 3, 2, 14, 'x', 18, 'x', 'x'),
        (11, 1, 2, 1, 17, 15, 'x', 2, 'x', 12, 'x', 'x'),
        ('x', 'x', 3, 15, 16, 1, 'x', 'x', 'x', 'x', 'x', 'x'),
        ('x', 10, 'x', 'x', 'x', 6, 1, 8, 19, 13, 7, 'x'),
        ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3),
        (3, 7, 12, 'x', 15, 'x', 19, 13, 17, 14, 'x', 'x'),
        ('x', 'x', 'x', 'x', 4, 4, 18, 'x', 5, 'x', 'x', 10),
        ('x', 'x', 15, 9, 13, 10, 8, 4, 8, 6, 7, 7)
    )
    num_rows = 12
    num_cols = 12
    districts = {
        1: (0, 2),
        2: (3, 5),
        3: (6, 11)
    }
    start = (3, 11)
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
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_district = get_district(new_row, districts)
                if new_row == end[0] and new_col == end[1]:
                    new_district = get_district(end[0], districts)
                if new_district not in [get_district(pos[0], districts) for pos in actions] or new_row == end[0] and new_col == end[1]:
                    if (new_row, new_col) not in visited_costs or new_cost < visited_costs[(new_row, new_col)]:
                        visited_costs[(new_row, new_col)] = new_cost
                        h = heuristic((new_row, new_col), end)
                        heapq.heappush(queue, (g + h, new_cost, actions + [(new_row, new_col)], (new_row, new_col)))

    return None

def get_district(row, districts):
    for district, (start, end) in districts.items():
        if start <= row <= end:
            return district
    return None

def heuristic(current, end):
    # Calculate the Manhattan distance as the heuristic
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
