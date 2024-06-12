
import heapq
import numpy as np

def initialize():
    initial_state = (('42', '56', '64', 'x'), ('x', 'x', '55', 'x'), ('30', 'x', 'x', 'x'), ('24', 'x', '45', 'x'))
    num_rows = 4
    num_cols = 4
    numbers = set(range(17, 67))
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_rows, num_cols, numbers, visited_costs, queue)

def a_star():
    (initial_state, num_rows, num_cols, numbers, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if all(((cell != 'x') for row in state for cell in row)):
            return actions
        for i in range(num_rows):
            for j in range(num_cols):
                if (state[i][j] == 'x'):
                    used_numbers = set((int(cell) for row in state for cell in row if (cell != 'x')))
                    available_numbers = (numbers - used_numbers)
                    for number in available_numbers:
                        new_state = [list(row[:]) for row in state]
                        new_state[i][j] = str(number)
                        new_state = tuple((tuple(row) for row in new_state))
                        if (all((is_consecutive([cell for cell in row if (cell != 'x')]) for row in new_state)) and all((is_consecutive([new_state[row][col] for row in range(num_rows) if (new_state[row][col] != 'x')]) for col in range(num_cols)))):
                            new_cost = ((sum((int(cell) for cell in new_state[0] if (cell != 'x'))) + sum((int(new_state[row][(num_cols - 1)]) for row in range(num_rows) if (new_state[row][(num_cols - 1)] != 'x')))) + sum((int(new_state[i][i]) for i in range(num_rows) if (new_state[i][i] != 'x'))))
                            if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, ((new_cost + heuristic(new_state)), new_cost, (actions + [(i, j, number)]), new_state))
                    break
            else:
                continue
            break
    return None

def is_consecutive(lst):
    return (all(((int(lst[i]) <= int(lst[(i + 1)])) for i in range((len(lst) - 1)))) or all(((int(lst[i]) >= int(lst[(i + 1)])) for i in range((len(lst) - 1)))))

def heuristic(state):
    return sum(((cell == 'x') for row in state for cell in row))
print(a_star())
