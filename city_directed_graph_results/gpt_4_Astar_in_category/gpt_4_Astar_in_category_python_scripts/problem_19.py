
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]]
    # Define the names of the cities
    cities = ['J', 'X', 'U', 'I', 'R', 'T', 'Y', 'B', 'M', 'D', 'E']
    # Define the initial state and the goal state
    initial_state = ('E', False, False, False, False)
    goal_state = ('E', True, True, True, True)
    # Define the indices of the destination cities
    destination_cities = ['T', 'Y']
    destination_indices = [cities.index(city) for city in destination_cities]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [initial_state[0]], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        if state == goal_state:
            return path

        current_city, visited_T_once, visited_Y_once, visited_T_twice, visited_Y_twice = state
        current_city_index = cities.index(current_city)

        for next_city_index, road_exists in enumerate(adjacency_matrix[current_city_index]):
            if road_exists:
                next_city = cities[next_city_index]
                # Check if the next city is a destination city
                if next_city_index in destination_indices:
                    # If the next city is 'T'
                    if next_city_index == destination_indices[0]:
                        # If 'T' has not been visited yet
                        if not visited_T_once:
                            new_state = (next_city, True, visited_Y_once, visited_T_twice, visited_Y_twice)
                        # If 'T' has been visited once
                        elif visited_T_once and not visited_T_twice:
                            new_state = (next_city, visited_T_once, visited_Y_once, True, visited_Y_twice)
                        else:
                            continue
                    # If the next city is 'Y'
                    else:
                        # If 'Y' has not been visited yet
                        if not visited_Y_once:
                            new_state = (next_city, visited_T_once, True, visited_T_twice, visited_Y_twice)
                        # If 'Y' has been visited once
                        elif visited_Y_once and not visited_Y_twice:
                            new_state = (next_city, visited_T_once, visited_Y_once, visited_T_twice, True)
                        else:
                            continue
                # If the next city is not a destination city and has not been visited yet
                elif next_city not in path:
                    new_state = (next_city, visited_T_once, visited_Y_once, visited_T_twice, visited_Y_twice)
                else:
                    continue

                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))

    return None

def heuristic(state, goal_state):
    # The heuristic function can be the number of destination cities not visited twice yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal state
    # It is consistent because the cost of moving from one city to another is always 1, which is equal to the decrease in the heuristic cost if a destination city is visited
    return sum(state[i] != goal_state[i] for i in range(1, len(state)))

print(a_star())
