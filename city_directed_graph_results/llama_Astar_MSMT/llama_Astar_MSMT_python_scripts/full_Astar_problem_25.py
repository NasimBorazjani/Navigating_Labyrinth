
import heapq


def initialize():
    # Define the adjacency matrix of the directed graph
    adj_matrix = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    ]
    # Define the start city, the destination cities, and the total number of cities
    start_city = 'M'
    dest_cities = ['X', 'Y']
    num_cities = len(adj_matrix)

    # Initialize the visited_costs dictionary and the priority queue
    visited_costs = {}
    visited_costs[(start_city, 0, 0)] = 0
    queue = [(0, 0, [], (start_city, 0, 0))]

    return adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue


def a_star():
    adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If we have visited all destination cities twice, return the path
        if state[1] == 2 and state[2] == 2:
            return actions

        # Generate all possible actions from the current state
        for i in range(num_cities):
            # Check if we can move to the next city
            if adj_matrix[state[0].upper() - 'A'][i] == 1:
                next_city = chr(i + ord('A'))
                # Update the destination city counts
                dest_city_counts = list(state[1:])
                if next_city in dest_cities:
                    dest_city_counts[dest_cities.index(next_city)] += 1
                # Generate the new state
                new_state = (next_city, *dest_city_counts)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic for the new state
                    h = heuristic(new_state, dest_cities)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))

    return None


def heuristic(state, dest_cities):
    # Calculate the heuristic as the sum of the remaining distances to the destination cities
    h = 0
    for i, dest_city in enumerate(dest_cities):
        if state[i + 1] < 2:
            h += 2 - state[i + 1]
    return h


print(a_star())
