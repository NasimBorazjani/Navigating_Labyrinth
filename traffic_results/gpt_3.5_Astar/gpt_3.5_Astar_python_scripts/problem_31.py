
import heapq
import math

def a_star():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((10, 'x', 19, 11, 'x', 'x', 6, 12, 'x', 'x', 'x'),
                     (2, 9, 10, 'x', 'x', 10, 17, 'x', 'x', 11, 5),
                     ('x', 15, 8, 9, 'x', 7, 17, 20, 'x', 'x', 13),
                     (1, 9, 15, 14, 9, 9, 13, 7, 12, 'x', 10),
                     (9, 'x', 17, 'x', 'x', 7, 'x', 'x', 1, 'x', 14),
                     (16, 18, 11, 'x', 14, 18, 9, 13, 'x', 'x', 'x'),
                     (9, 3, 5, 8, 17, 15, 19, 'x', 3, 'x', 14),
                     (2, 13, 'x', 'x', 17, 13, 14, 18, 9, 'x', 6),
                     (3, 'x', 18, 6, 'x', 14, 'x', 'x', 'x', 8, 19),
                     (2, 4, 'x', 'x', 'x', 'x', 3, 4, 'x', 19, 'x'),
                     ('x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 5, 5))
    num_rows = 11
    num_cols = 11
    districts = {1: (0, 2), 2: (3, 6), 3: (7, 10)}
    start = (3, 7)
    end = (7, 0)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(1 in [1 if districts[i][0] <= path.count(1) <= districts[i][1] else 0 for i in range(1, 4)] for i in range(1, 4)):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row == end[0] and new_col == end[1]:
                    new_cost += initial_state[new_row][new_col]
                if new_path not in visited_costs or new_cost < visited_costs[new_path]:
                    visited_costs[new_path] = new_cost
                    h = heuristic(new_path, districts)
                    heapq.heappush(queue, (g + h, new_cost, new_path, (new_row, new_col)))

    return None

def heuristic(path, districts):
    # The heuristic is the sum of the distances from the current position to the end position in each district
    # This heuristic is admissible because it never overestimates the cost to reach the goal state
    # The heuristic is consistent because the cost of moving from one position to another is always 1, which is exactly the decrease in the heuristic estimate, if the position is moved towards the goal position, otherwise the estimated cost of the successor node is the same or higher
    h = 0
    for i in range(1, 4):
        district_start, district_end = districts[i]
        district_path = [pos for pos in path if district_start <= pos[0] <= district_end]
        if district_path:
            h += abs(district_path[-1][0] - district_end) + abs(district_path[-1][1])
    return h

print(a_star())
