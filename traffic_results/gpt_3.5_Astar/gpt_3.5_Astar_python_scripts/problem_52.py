
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (
        ('x', 3, 11, 7, 'x', 'x', 1, 3, 'x', 'x', 'x', 3),
        ('x', 10, 'x', 'x', 3, 9, 7, 8, 'x', 2, 'x', 17),
        (6, 16, 'x', 18, 10, 5, 'x', 6, 'x', 'x', 7, 'x'),
        ('x', 10, 'x', 8, 13, 10, 'x', 'x', 'x', 'x', 6, 13),
        (6, 11, 3, 16, 8, 15, 'x', 'x', 'x', 13, 12, 20),
        (15, 'x', 16, 'x', 17, 13, 'x', 'x', 8, 6, 19, 9),
        (14, 10, 16, 14, 'x', 'x', 10, 11, 19, 15, 17, 'x'),
        ('x', 'x', 'x', 'x', 18, 13, 14, 19, 12, 1, 3, 'x'),
        (15, 1, 3, 17, 4, 18, 'x', 18, 2, 7, 12, 'x'),
        (19, 'x', 13, 17, 2, 14, 8, 'x', 'x', 8, 16, 'x'),
        ('x', 19, 'x', 15, 'x', 18, 'x', 13, 'x', 13, 'x', 'x'),
        (7, 14, 2, 'x', 10, 3, 'x', 'x', 2, 5, 10, 'x')
    )
    num_rows = 12
    num_cols = 12
    districts = {1: (0, 4), 2: (5, 8), 3: (9, 11)}
    start = (8, 1)
    end = (5, 11)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end:
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row >= districts[1][0] and new_row <= districts[1][1] and len(set([p for p in new_path if p[0] >= districts[1][0] and p[0] <= districts[1][1]])) >= 2:
                    if new_row >= districts[2][0] and new_row <= districts[2][1] and len(set([p for p in new_path if p[0] >= districts[2][0] and p[0] <= districts[2][1]])) >= 2:
                        if new_row >= districts[3][0] and new_row <= districts[3][1] and len(set([p for p in new_path if p[0] >= districts[3][0] and p[0] <= districts[3][1]])) >= 2:
                            if new_cost < visited_costs.get((new_row, new_col), math.inf):
                                visited_costs[(new_row, new_col)] = new_cost
                                heapq.heappush(queue, (g + abs(new_row - end[0]) + abs(new_col - end[1]), new_cost, new_path, (new_row, new_col)))

    return None

print(a_star())
