
import heapq

def initialize():
    adjacency_matrix = [[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1], [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]]
    cities = ['C', 'Q', 'T', 'K', 'M', 'B', 'R', 'D', 'J', 'A', 'Y', 'V', 'O', 'N', 'P']
    start_city = 'M'
    target_cities = ['Y', 'K']
    num_cities = len(cities)
    visited_costs = {}
    visited_costs[start_city] = 0
    queue = [(0, 0, [], start_city)]
    return (adjacency_matrix, cities, start_city, target_cities, num_cities, visited_costs, queue)

def a_star():
    (adjacency_matrix, cities, start_city, target_cities, num_cities, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, current_city) = heapq.heappop(queue)
        if all(((actions.count(city) == 2) for city in target_cities)):
            return (actions + [current_city])
        current_city_index = cities.index(current_city)
        for i in range(num_cities):
            if ((adjacency_matrix[current_city_index][i] == 1) and (cities[i] not in actions)):
                new_cost = (g + 1)
                new_actions = (actions + [current_city])
                if (cities[i] in target_cities):
                    new_actions.append(cities[i])
                heapq.heappush(queue, (new_cost, new_cost, new_actions, cities[i]))
    return None
print(a_star())
