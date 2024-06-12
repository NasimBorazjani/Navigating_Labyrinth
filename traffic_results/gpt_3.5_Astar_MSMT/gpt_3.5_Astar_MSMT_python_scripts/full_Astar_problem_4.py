
import heapq

def initialize():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((18, 9, 2, 'x', 9, 14, 'x', 1, 'x'),
                     (3, 14, 18, 7, 'x', 3, 'x', 2, 19),
                     (6, 18, 20, 3, 13, 'x', 6, 10, 'x'),
                     (20, 'x', 12, 4, 14, 6, 'x', 'x', 'x'),
                     (7, 18, 8, 5, 19, 3, 'x', 'x', 7),
                     (15, 9, 14, 16, 5, 14, 6, 'x', 'x'),
                     ('x', 5, 13, 'x', 'x', 19, 'x', 'x', 2),
                     ('x', 'x', 8, 'x', 'x', 'x', 'x', 17, 12),
                     ('x', 1, 'x', 'x', 3, 19, 'x', 2, 18))
    num_rows = 9
    num_cols = 9
    start = (2, 0)
    end = (5, 6)
    districts = {1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                 2: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)],
                 3: [(5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
                }

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]
  
    return initial_state, num_rows, num_cols, start, end, districts, visited_costs, queue
  
def a_star():
  
    initial_state, num_rows, num_cols, start, end, districts, visited_costs, queue = initialize()

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == end and all(len(set(districts[i]) & set(path)) > 0 for i in districts):
            return path

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + d_row, current[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_cost = g + initial_state[new_row][new_col]
                new_path = path + [(new_row, new_col)]
                if new_row != current[0] or new_col != current[1]:
                    heapq.heappush(queue, (new_cost, new_cost, new_path, (new_row, new_col)))
    return None

print(a_star())
