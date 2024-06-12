
import heapq
import numpy as np

def initialize():
    initial_state = (('x', 'x', '42'), ('x', '46', 'x'), ('x', 'x', '55'))
    num_range = set(range(25, 58))
    num_rows = 3
    num_cols = 3
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_range, num_rows, num_cols, visited_costs, queue)

def a_star():
    (initial_state, num_range, num_rows, num_cols, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (all((all(((cell != 'x') for cell in row)) for row in state)) and all(((all(((int(row[i]) < int(row[(i + 1)])) for i in range((len(row) - 1)))) or all(((int(row[i]) > int(row[(i + 1)])) for i in range((len(row) - 1))))) for row in state)) and all(((all(((int(state[i][col]) < int(state[(i + 1)][col])) for i in range((len(state) - 1)))) or all(((int(state[i][col]) > int(state[(i + 1)][col])) for i in range((len(state) - 1))))) for col in range(len(state[0]))))):
            return actions
        if any((('x' in row) for row in state)):
            for row_ind in range(num_rows):
                for col_ind in range(num_cols):
                    if (state[row_ind][col_ind] == 'x'):
                        for num in (num_range - set((cell for row in state for cell in row if (cell != 'x')))):
                            new_state = [list(row[:]) for row in state]
                            new_state[row_ind][col_ind] = num
                            new_state = tuple((tuple(row) for row in new_state))
                            new_cost = ((sum((int(cell) for cell in new_state[0] if (cell != 'x'))) + sum((int(new_state[i][(- 1)]) for i in range(num_rows) if (new_state[i][(- 1)] != 'x')))) + sum((int(new_state[i][i]) for i in range(num_rows) if (new_state[i][i] != 'x'))))
                            if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, ((new_cost + heuristic(new_state)), new_cost, (actions + [(row_ind, col_ind, num)]), new_state))
                        break
                else:
                    continue
                break
    return None

def heuristic(state):
    return sum(sorted((set(range(21, 59)) - set((int(cell) for row in state for cell in row if (cell != 'x')))))[:sum(((cell == 'x') for row in state for cell in row))])
print(a_star())
