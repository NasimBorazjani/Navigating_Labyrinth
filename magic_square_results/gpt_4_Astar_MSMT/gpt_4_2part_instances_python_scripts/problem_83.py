
import heapq

def initialize():
    initial_state = (('x', '51', 'x', '65'), ('x', 'x', 'x', '68'), ('x', 'x', '64', '75'), ('x', 'x', 'x', 'x'))
    goal_sums = {'row1': 255, 'row2': 268, 'col1': 240, 'col2': 226, 'diag': 264}
    num_range = set(range(43, 85))
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, goal_sums, num_range, visited_costs, queue)

def a_star():
    (initial_state, goal_sums, num_range, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (all(((cell != 'x') for row in state for cell in row)) and (sum((int(cell) for cell in state[1])) == goal_sums['row1']) and (sum((int(state[i][1]) for i in range(3))) == goal_sums['col1']) and (sum((int(state[i][(2 - i)]) for i in range(3))) == goal_sums['diag'])):
            return actions
        if any(((cell == 'x') for row in state for cell in row)):
            for i in range(3):
                for j in range(3):
                    if (state[i][j] == 'x'):
                        available_nums = (num_range - set((int(cell) for row in state for cell in row if (cell != 'x'))))
                        for num in available_nums:
                            new_state = [list(row) for row in state]
                            new_state[i][j] = str(num)
                            new_state = tuple((tuple(row) for row in new_state))
                            new_cost = (g + num)
                            if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, ((new_cost + heuristic(new_state, goal_sums)), new_cost, (actions + [(i, j, num)]), new_state))
                        break
                else:
                    continue
                break
    return None

def heuristic(state, goal_sums):
    h = 0
    if any(((cell == 'x') for row in state for cell in row)):
        h += abs((sum((int(cell) for cell in state[1] if (cell != 'x'))) - goal_sums['row1']))
        h += abs((sum((int(state[i][1]) for i in range(3) if (state[i][1] != 'x'))) - goal_sums['col1']))
        h += abs((sum((int(state[i][(2 - i)]) for i in range(3) if (state[i][(2 - i)] != 'x'))) - goal_sums['diag']))
    return h
print(a_star())
