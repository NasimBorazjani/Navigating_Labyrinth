
import heapq

def initialize():
    city_graph = [[0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1, 0, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 1, 1, 0]]
    city_names = ['R', 'T', 'C', 'F', 'S', 'X', 'Y', 'E', 'A', 'W']
    initial_state = ('C', ('F', 'F', 'W', 'W'), ('C',))
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, ['C'], initial_state)]
    return (city_graph, city_names, initial_state, visited_costs, queue)

def a_star():
    (city_graph, city_names, initial_state, visited_costs, queue) = initialize()
    while queue:
        (_, g, path, state) = heapq.heappop(queue)
        (current_city, cities_to_visit, cities_visited) = state
        if (not cities_to_visit):
            return path
        for i in range(len(city_graph)):
            if (city_graph[city_names.index(current_city)][i] == 1):
                next_city = city_names[i]
                if ((next_city in cities_to_visit) or (next_city not in cities_visited)):
                    new_cities_to_visit = list(cities_to_visit)
                    if (next_city in new_cities_to_visit):
                        new_cities_to_visit.remove(next_city)
                    new_cities_visited = (list(cities_visited) + [next_city])
                    new_state = (next_city, tuple(new_cities_to_visit), tuple(new_cities_visited))
                    new_cost = (g + 1)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, (path + [next_city]), new_state))
    return None
print(a_star())
