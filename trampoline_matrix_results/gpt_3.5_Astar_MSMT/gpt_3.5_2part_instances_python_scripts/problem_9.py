
import heapq

def initialize():
    initial_state = ((1, 0, 1, 1, 1, 0, 1, 1, 1), (0, 1, 0, 0, 1, 1, 1, 0, 0), (1, 0, 1, 0, 1, 1, 1, 0, 0), (1, 1, 1, 0, 0, 0, 1, 1, 0), (1, 1, 0, 1, 0, 1, 0, 1, 1), (1, 0, 1, 1, 0, 1, 1, 1, 0), (0, 1, 0, 0, 0, 1, 1, 0, 0), (0, 1, 0, 0, 0, 1, 0, 1, 1), (1, 1, 0, 0, 0, 0, 0, 0, 0))
    num_rows = 9
    num_cols = 9
    start_position = (1, 2)
    end_position = (8, 8)
    visited_costs = {}
    visited_costs[start_position] = 0
    queue = [(0, 0, [], start_position)]
    return (initial_state, num_rows, num_cols, start_position, end_position, visited_costs, queue)

def a_star():
    (initial_state, num_rows, num_cols, start_position, end_position, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, position) = heapq.heappop(queue)
        if (position == end_position):
            return actions
        for d_row in [(- 1), 0, 1]:
            for d_col in [(- 1), 0, 1]:
                (new_row, new_col) = ((position[0] + d_row), (position[1] + d_col))
                if ((0 <= new_row < num_rows) and (0 <= new_col < num_cols) and (initial_state[new_row][new_col] == 0)):
                    if ((abs(d_row) == 1) and (abs(d_col) == 1)):
                        new_diagonal_moves = (actions.count('diagonal') + 1)
                    else:
                        new_diagonal_moves = actions.count('diagonal')
                    if (new_diagonal_moves == 3):
                        new_position = (new_row, new_col)
                        new_cost = (g + 1)
                        if ((new_position not in visited_costs) or (new_cost < visited_costs[new_position])):
                            visited_costs[new_position] = new_cost
                            heapq.heappush(queue, ((new_cost + heuristic(new_position, end_position)), new_cost, (actions + [(new_row, new_col)]), new_position))
                    elif (new_diagonal_moves < 3):
                        new_position = (new_row, new_col)
                        new_cost = (g + 1)
                        if ((new_position not in visited_costs) or (new_cost < visited_costs[new_position])):
                            visited_costs[new_position] = new_cost
                            heapq.heappush(queue, ((new_cost + heuristic(new_position, end_position)), new_cost, (actions + [(new_row, new_col)]), new_position))
    return None

def heuristic(position, end_position):
    return (abs((position[0] - end_position[0])) + abs((position[1] - end_position[1])))
print(a_star())
