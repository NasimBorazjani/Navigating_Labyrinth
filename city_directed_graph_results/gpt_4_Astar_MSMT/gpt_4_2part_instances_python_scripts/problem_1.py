
import heapq

def initialize():
    initial_state = ('W', ('A', 'A', 'H', 'H'))
    goal_state = []
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 1, 0, 1, 0, 0, 1, 1, 0, 0]]
    cities = ['G', 'D', 'X', 'N', 'Y', 'W', 'A', 'P', 'V', 'H']
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, ['W'], initial_state)]
    return (initial_state, goal_state, adjacency_matrix, cities, visited_costs, queue)

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
