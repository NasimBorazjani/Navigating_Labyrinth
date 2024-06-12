
import heapq


def initialize():
    # Define the adjacency matrix of the directed graph
    adj_matrix = [
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
    ]
    # Define the start city 'K' and the destination cities 'P' and 'N'
    start = 'K'
    destinations = ['P', 'N']
    num_cities = len(adj_matrix)
    # Define the goal state as visiting each destination city exactly twice
    goal_state = {city: 2 for city in destinations}
    # Define the heuristic function
    heuristic = lambda city_counts: sum(abs(city_counts[city] - goal_state[city]) for city in goal_state)
    # Initialize the visited_costs dictionary and the priority queue
    visited_costs = {start: 0}
    queue = [(0, 0, [start], start)]
   
    return adj_matrix, num_cities, start, destinations, goal_state, visited_costs, queue
  
def a_star():
   
    adj_matrix, num_cities, start, destinations, goal_state, visited_costs, queue = initialize()

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state meets the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
        for city_index, city in enumerate(state):
            if city in destinations and state[city] < goal_state[city]:
                # Generate the new state
                new_state = {k: v + 1 if k == city else v for k, v in state.items()}
                # The cost of the new state is the travel time to get to the new city in the adjacency matrix
                new_cost = g + adj_matrix[city_index][list(state.keys()).index(city)]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The city must be added to the path
                    heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, path + [city], new_state))

    return None


print(a_star())
