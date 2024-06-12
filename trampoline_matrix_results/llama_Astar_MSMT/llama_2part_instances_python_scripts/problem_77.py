
import heapq

def initialize():
    initial_state = ((0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0), (0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0), (1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0), (1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0), (0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0), (0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0), (1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0), (1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0), (1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1), (1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0), (0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1), (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0), (1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1))
    num_rows = 14
    num_cols = 14
    start_pos = (0, 13)
    goal_pos = (8, 1)
    visited_costs = {}
    visited_costs[start_pos] = 0
    queue = [(0, 0, [], start_pos)]
    return (initial_state, num_rows, num_cols, start_pos, goal_pos, visited_costs, queue)

def a_star():
    (initial_state, num_rows, num_cols, start_pos, goal_pos, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (state == goal_pos):
            return actions
        for (row_delta, col_delta) in [((- 1), (- 1)), ((- 1), 0), ((- 1), 1), (0, (- 1)), (0, 1), (1, (- 1)), (1, 0), (1, 1)]:
            new_state = ((state[0] + row_delta), (state[1] + col_delta))
            if ((0 <= new_state[0] < num_rows) and (0 <= new_state[1] < num_cols) and (initial_state[new_state[0]][new_state[1]] != 1)):
                new_cost = (g + 1)
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_pos)
                    heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [new_state]), new_state))
    return None

def heuristic(state, goal):
    h = (abs((state[0] - goal[0])) + abs((state[1] - goal[1])))
    return h
print(a_star())
