
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]]
    # Define the cities
    cities = ['T', 'J', 'X', 'U', 'L', 'S', 'C', 'H', 'Z', 'O', 'D', 'Q', 'G', 'W']
    # Define the initial state and the goal state
    initial_state = ('U', ['H', 'H', 'L', 'L'], ['U'])
    goal_state = ('U', [], ['U', 'H', 'L', 'H', 'L'])
    # Define the visited costs
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Define the queue
    queue = [(0, 0, [], initial_state)]
    # While there are unvisited states
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions
        if state == goal_state:
            return actions
        # Generate all possible actions from the current state
        current_city = state[0]
        remaining_cities = state[1]
        visited_cities = state[2]
        for i in range(len(cities)):
            if adjacency_matrix[cities.index(current_city)][i] == 1:
                next_city = cities[i]
                if next_city in remaining_cities:
                    new_remaining_cities = remaining_cities[:]
                    new_remaining_cities.remove(next_city)
                    new_visited_cities = visited_cities + [next_city]
                    new_state = (next_city, new_remaining_cities, new_visited_cities)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], new_state))
                elif next_city not in visited_cities and next_city != 'H' and next_city != 'L':
                    new_visited_cities = visited_cities + [next_city]
                    new_state = (next_city, remaining_cities, new_visited_cities)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], new_state))
    return None

print(a_star())
