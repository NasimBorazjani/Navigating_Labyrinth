
import heapq
import math


def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((15, 'x', 8, 'x', 6, 9, 'x', 'x', 'x'),
                     (14, 'x', 8, 'x', 14, 'x', 5, 11, 'x', 9),
                     ('x', 17, 8, 'x', 17, 15, 12, 'x', 'x', 13),
                     ('x', 13, 'x', 'x', 2, 'x', 17, 17, 1, 'x'),
                     (6, 'x', 1, 5, 17, 'x', 2, 18, 11, 7),
                     (12, 8, 17, 10, 'x', 'x', 'x', 15, 'x', 16),
                     (12, 12, 'x', 4, 'x', 13, 'x', 10, 'x', 16),
                     ('x', 'x', 10, 'x', 6, 'x', 'x', 'x', 8, 5),
                     ('x', 2, 11, 18, 15, 'x', 11, 'x', 'x', 12),
                     ('x', 'x', 14, 'x', 'x', 7, 14, 15, 18, 9))
    num_rows = 10
    num_cols = 10
    districts = {1: (0, 3), 2: (4, 4), 3: (5, 9)}
    start = (5, 0)
    end = (3, 8)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(visited_costs.get((x, y)) for x, y in path):
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = current[0] + dx, current[1] + dy
            if 0 <= new_x < num_rows and 0 <= new_y < num_cols and initial_state[new_x][new_y] != 'x':
                new_cost = g + initial_state[new_x][new_y]
                new_path = path + [(new_x, new_y)]
                if districts.get(new_x) and not any(districts.get(d) and all(cell == 'x' for cell in [initial_state[x][y] for x, y in districts[d]]) for d in range(1, 4)):
                    new_cost += 1
                if new_cost < visited_costs.get((new_x, new_y), math.inf):
                    visited_costs[(new_x, new_y)] = new_cost
                    heapq.heappush(queue, (g + 1 + abs(new_x - end[0]) + abs(new_y - end[1]), new_cost, new_path, (new_x, new_y)))

    return None


print(a_star())
