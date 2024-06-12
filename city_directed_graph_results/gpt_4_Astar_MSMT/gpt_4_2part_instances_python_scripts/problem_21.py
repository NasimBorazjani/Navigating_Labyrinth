
import heapq

def initialize():
    initial_state = (('47', 'x', 'x', '32'), ('x', 'x', 'x', '49'), ('x', '31', '50', 'x'), ('x', 'x', '52', '30'))
    num_rows = 4
    num_cols = 4
    row_sums = [None, 187, 149, None]
    col_sums = [None, 148, 196, None]
    diagonal_sum = 166
    numbers = set(range(29, 54))
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_rows, num_cols, row_sums, col_sums, diagonal_sum, numbers, visited_costs, queue)

def a_star():
    (initial_state, goal_state, adjacency_matrix, cities, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (current_city, remaining_cities) = state
        if (not remaining_cities):
            return actions
        for i in range(len(cities)):
            if (adjacency_matrix[cities.index(current_city)][i] == 1):
                next_city = cities[i]
                if (next_city in remaining_cities):
                    new_remaining_cities = list(remaining_cities)
                    new_remaining_cities.remove(next_city)
                    new_state = (next_city, tuple(new_remaining_cities))
                    new_cost = (g + 1)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((new_cost + heuristic(new_state, goal_state)), new_cost, (actions + [next_city]), new_state))
                elif (next_city not in actions):
                    new_state = (next_city, remaining_cities)
                    new_cost = (g + 1)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((new_cost + heuristic(new_state, goal_state)), new_cost, (actions + [next_city]), new_state))
    return None

def heuristic(state, goal_state):
    return len(state[1])
print(a_star())
