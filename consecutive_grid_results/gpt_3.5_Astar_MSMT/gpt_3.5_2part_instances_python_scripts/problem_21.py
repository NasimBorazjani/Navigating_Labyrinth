
import heapq
import numpy as np

def initialize():
    grid = np.array([[30, 'x', 'x'], [28, 33, 43], ['x', 'x', 51]])
    numbers_range = set(range(15, 58))
    num_rows = 3
    num_cols = 3
    visited_costs = {}
    visited_costs[tuple(map(tuple, grid))] = 0
    queue = [(0, 0, [], grid, numbers_range)]
    return (grid, num_rows, num_cols, visited_costs, queue)

def a_star():
    (grid, num_rows, num_cols, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state, numbers_range) = heapq.heappop(queue)
        state = np.array(state)
        if ('x' not in state):
            return actions
        for row in range(num_rows):
            for col in range(num_cols):
                if (state[row][col] == 'x'):
                    for num in numbers_range:
                        new_state = state.copy()
                        new_state[row][col] = num
                        new_numbers_range = numbers_range.copy()
                        new_numbers_range.remove(num)
                        new_cost = (g + num)
                        if ((tuple(map(tuple, new_state)) not in visited_costs) or (new_cost < visited_costs[tuple(map(tuple, new_state))])):
                            visited_costs[tuple(map(tuple, new_state))] = new_cost
                            heapq.heappush(queue, ((new_cost + heuristic(new_state, new_numbers_range)), new_cost, (actions + [(row, col, num)]), new_state, new_numbers_range))
    return None

def heuristic(state, numbers_range):
    h = sum(numbers_range)
    return h
print(a_star())
