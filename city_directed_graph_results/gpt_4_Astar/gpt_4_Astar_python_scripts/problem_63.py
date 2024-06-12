
import heapq

def a_star():
    # Define the adjacency matrix of the graph
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
    # Define the cities
    cities = ['Z', 'N', 'R', 'F', 'O', 'U', 'P', 'L', 'J', 'I', 'S', 'Q', 'G']
    # Define the initial state and the goal state
    initial_state = ('F', ['N', 'J'], ['N', 'J'], ['Z', 'R', 'O', 'U', 'P', 'L', 'I', 'S', 'Q', 'G'])
    goal_state = ('F', [], [], [])
    # Define the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited
    queue = [(0, 0, [], initial_state)]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions
        # Generate all possible actions from the current state
        current_city = state[0]
        remaining_destinations = state[1]
        visited_destinations = state[2]
        remaining_cities = state[3]
        for i in range(len(cities)):
            if adjacency_matrix[cities.index(current_city)][i] == 1:
                next_city = cities[i]
                if next_city in remaining_destinations:
                    new_remaining_destinations = remaining_destinations[:]
                    new_remaining_destinations.remove(next_city)
                    new_visited_destinations = visited_destinations + [next_city]
                    new_remaining_cities = remaining_cities[:]
                    new_state = (next_city, new_remaining_destinations, new_visited_destinations, new_remaining_cities)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], new_state))
                elif next_city in visited_destinations:
                    new_visited_destinations = visited_destinations[:]
                    new_visited_destinations.remove(next_city)
                    new_remaining_destinations = remaining_destinations + [next_city]
                    new_remaining_cities = remaining_cities[:]
                    new_state = (next_city, new_remaining_destinations, new_visited_destinations, new_remaining_cities)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], new_state))
                elif next_city in remaining_cities:
                    new_remaining_cities = remaining_cities[:]
                    new_remaining_cities.remove(next_city)
                    new_state = (next_city, remaining_destinations, visited_destinations, new_remaining_cities)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], new_state))
    return None

print(a_star())
