
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]]

    # Define the city names
    city_names = ['Z', 'N', 'R', 'F', 'O', 'U', 'P', 'L', 'J', 'I', 'S', 'Q', 'G']

    # Define the initial state and goal state
    initial_state = (3, 0, 0)  # (current city, visited N, visited J)
    goal_state = (3, 2, 2)  # (current city, visited N twice, visited J twice)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element.
    queue = [(0, 0, [initial_state[0]])]  # (priority, cost so far, path)

    while queue:
        _, g, path = heapq.heappop(queue)
        state = path[-1]

        # If the current state is the goal state, return the path
        if state == goal_state:
            return [city_names[i] for i in path]

        # Generate all possible actions from the current state
        for next_city in range(len(city_names)):
            # Check if there is a direct road from the current city to the next city
            if adjacency_matrix[state[0]][next_city] == 1:
                # Check if the next city is N or J
                if next_city == 1:  # N
                    if state[1] < 2:  # If N has not been visited twice
                        new_state = (next_city, state[1] + 1, state[2])
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, path + [new_state]))
                elif next_city == 8:  # J
                    if state[2] < 2:  # If J has not been visited twice
                        new_state = (next_city, state[1], state[2] + 1)
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, path + [new_state]))
                else:  # Other cities
                    if next_city not in [i[0] for i in path]:  # If the city has not been visited
                        new_state = (next_city, state[1], state[2])
                        new_cost = g + 1
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, path + [new_state]))

    return None

print(a_star())
