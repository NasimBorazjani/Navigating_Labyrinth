
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = (
        ('x', 'x', 10, 'x', 'x', 'x', 3, 'x', 'x', 'x', 'x', 'x', 'x'),
        (6, 19, 'x', 'x', 'x', 12, 'x', 'x', 3, 'x', 'x', 'x', 'x'),
        (5, 3, 7, 7, 'x', 7, 9, 'x', 18, 'x', 'x', 'x', 'x'),
        (1, 4, 19, 19, 16, 6, 'x', 2, 10, 'x', 1, 7, 'x'),
        (14, 10, 'x', 'x', 2, 3, 5, 3, 13, 7, 'x', 8, 'x'),
        ('x', 8, 11, 14, 18, 'x', 'x', 16, 15, 8, 'x', 10, 'x'),
        ('x', 17, 'x', 'x', 15, 'x', 'x', 1, 17, 9, 7, 'x', 10),
        (18, 6, 14, 4, 12, 12, 'x', 12, 5, 'x', 'x', 5, 18),
        ('x', 'x', 'x', 'x', 'x', 'x', 'x', 7, 17, 4, 16, 'x', 'x'),
        ('x', 6, 17, 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 12, 'x'),
        (14, 'x', 'x', 12, 3, 11, 'x', 'x', 'x', 'x', 'x', 17),
        ('x', 16, 'x', 'x', 'x', 3, 5, 19, 'x', 16, 14, 'x', 19),
        (13, 'x', 11, 'x', 3, 16, 'x', 1, 'x', 'x', 1, 'x', 'x')
    )
    num_rows = 13
    num_cols = 13
    districts = [(0, 2), (3, 7), (8, 12)]
    start = (2, 3)
    end = (8, 10)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end:
            return path

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + i, current[1] + j
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row in range(districts[0][0], districts[0][1] + 1) and len(set([p for p, _ in new_path if p in range(districts[0][0], districts[0][1] + 1)])) >= 2:
                    new_cost += 10
                if new_row in range(districts[1][0], districts[1][1] + 1) and len(set([p for p, _ in new_path if p in range(districts[1][0], districts[1][1] + 1)])) >= 2:
                    new_cost += 10
                if new_row in range(districts[2][0], districts[2][1] + 1) and len(set([p for p, _ in new_path if p in range(districts[2][0], districts[2][1] + 1)])) >= 2:
                    new_cost += 10

                if new not in visited_costs or new_cost < visited_costs[new]:
                    visited_costs[new] = new_cost
                    heapq.heappush(queue, (g + math.sqrt((new_row - end[0])**2 + (new_col - end[1])**2) + new_cost, new_cost, new_path, new))

    return None

print(a_star())
