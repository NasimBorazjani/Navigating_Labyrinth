
import heapq

def initialize():
    # Define the initial state of the city map as a 2d tuple
    initial_state = ((13, 'x', 'x', 3, 10, 20, 3, 'x', 5),
                     ('x', 'x', 'x', 'x', 20, 16, 'x', 'x', 17),
                     (3, 14, 18, 8, 1, 20, 14, 'x', 7),
                     (13, 3, 6, 10, 7, 4, 6, 6, 1),
                     (10, 12, 2, 'x', 11, 'x', 10, 8, 11),
                     ('x', 'x', 'x', 11, 6, 18, 13, 20, 17),
                     ('x', 'x', 16, 'x', 4, 17, 7, 10, 15),
                     ('x', 7, 16, 6, 19, 4, 7, 'x', 'x'),
                     ('x', 11, 18, 'x', 'x', 'x', 3, 8, 'x'))
    num_rows = 9
    num_cols = 9
    start_workshop = (5, 7)
    end_workshop = (2, 1)
    districts = {1: [(0, 2), (0, 1), (0, 0)], 2: [(3, 4), (3, 3)], 3: [(5, 8), (5, 7), (5, 6)]}

    visited_costs = {}
    visited_costs[start_workshop] = 0

    queue = [(0, 0, [], start_workshop)]

    return initial_state, num_rows, num_cols, start_workshop, end_workshop, districts, visited_costs, queue


def a_star():
    initial_state, num_rows, num_cols, start_workshop, end_workshop, districts, visited_costs, queue = initialize()

    while queue:
        _, g, actions, current_workshop = heapq.heappop(queue)

        if current_workshop == end_workshop and all(len(set(districts[i]) & set(actions)) > 0 for i in districts):
            return actions

        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current_workshop[0] + d_row, current_workshop[1] + d_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
                new_workshop = (new_row, new_col)
                new_cost = g + initial_state[new_row][new_col]

                if new_workshop not in visited_costs or new_cost < visited_costs[new_workshop]:
                    visited_costs[new_workshop] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, actions + [new_workshop], new_workshop))

    return None


print(a_star())
