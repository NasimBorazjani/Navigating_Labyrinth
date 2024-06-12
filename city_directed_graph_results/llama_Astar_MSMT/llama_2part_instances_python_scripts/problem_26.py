
import heapq
import heapq

def a_star():
    (adjacency_matrix, cities, start, destinations, num_cities, visited_costs, queue) = initialize()
    while queue:
        (_, g, path, state) = heapq.heappop(queue)
        (current_city, d_visits, t_visits) = state
        if ((d_visits == 2) and (t_visits == 2)):
            return path
        city_index = list(cities.values()).index(current_city)
        for i in range(num_cities):
            if (adjacency_matrix[city_index][i] == 1):
                next_city = cities[i]
                (d_visits_new, t_visits_new) = (d_visits, t_visits)
                if (next_city == 'D'):
                    d_visits_new += 1
                elif (next_city == 'T'):
                    t_visits_new += 1
                new_state = (next_city, d_visits_new, t_visits_new)
                new_cost = (g + 1)
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, ((new_cost + heuristic(new_state, destinations)), new_cost, (path + [next_city]), new_state))
    return None

def heuristic(state, destinations):
    (current_city, d_visits, t_visits) = state
    h = 0
    if ('D' not in destinations):
        d_visits = 2
    if ('T' not in destinations):
        t_visits = 2
    h = min(d_visits, t_visits)
    return h
print(a_star())
