
import heapq
import numpy as np

def initialize():
    initial_state = (('37', 'x', 'x'), ('x', 'x', 'x'), ('44', 'x', '61'))
    num_rows = 3
    num_cols = 3
    numbers = set(range(28, 66))
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_rows, num_cols, numbers, visited_costs, queue)

def a_star():
    (initial_state, num_rows, num_cols, numbers, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        x_coords = [(i, j) for (i, row) in enumerate(state) for (j, element) in enumerate(row) if (element == 'x')]
        if (not x_coords):
            state_array = np.array([[int(element) for element in row] for row in state])
            if (all(((all(((state_array[(i, j)] < state_array[(i, (j + 1))]) for j in range((num_cols - 1)))) or all(((state_array[(i, j)] > state_array[(i, (j + 1))]) for j in range((num_cols - 1))))) for i in range(num_rows))) and all(((all(((state_array[(i, j)] < state_array[((i + 1), j)]) for i in range((num_rows - 1)))) or all(((state_array[(i, j)] > state_array[((i + 1), j)]) for i in range((num_rows - 1))))) for j in range(num_cols)))):
                return actions
        else:
            first_x_coord = x_coords[0]
            used_numbers = set((int(cell) for row in state for cell in row if (cell != 'x')))
            for number in numbers:
                if (number not in used_numbers):
                    new_state = [list(row[:]) for row in state]
                    new_state[first_x_coord[0]][first_x_coord[1]] = str(number)
                    new_state = tuple((tuple(row) for row in new_state))
                    new_cost = (g + number)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, numbers)
                        heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [(first_x_coord[0], first_x_coord[1], number)]), new_state))
    return None

def heuristic(state, numbers):
    used_numbers = set((int(cell) for row in state for cell in row if (cell != 'x')))
    available_numbers = sorted(list((numbers - used_numbers)))
    h = 0
    for i in range(len(state)):
        for cell in state[i]:
            if ((cell == 'x') and available_numbers):
                h += available_numbers.pop(0)
    return h
print(a_star())
