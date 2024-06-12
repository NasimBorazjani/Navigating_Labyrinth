
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]]
    # Define the cities
    cities = ['T', 'W', 'Y', 'B', 'I', 'J', 'R', 'O', 'P', 'A', 'V', 'X', 'M', 'K', 'F']
    # Define the initial state and the goal state
    initial_state = ('A', ['J', 'M'], ['J', 'M'], ['T', 'W', 'Y', 'B', 'I', 'R', 'O', 'P', 'V', 'X', 'K', 'F'])
    goal_state = ('A', [], [], [])
    # Define the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited
    queue = [(0, 0, [], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions
        # Generate all possible actions from the current state
        current_city, to_visit, to_visit_twice, unvisited = state
        for i in range(len(cities)):
            # If there is a road from the current city to the city at index i
            if adjacency_matrix[cities.index(current_city)][i] == 1:
                next_city = cities[i]
                # If the next city is one of the cities to visit twice
                if next_city in to_visit_twice:
                    new_to_visit_twice = list(to_visit_twice)
                    new_to_visit_twice.remove(next_city)
                    new_state = (next_city, to_visit, new_to_visit_twice, unvisited)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], new_state))
                # If the next city is one of the cities to visit
                elif next_city in to_visit:
                    new_to_visit = list(to_visit)
                    new_to_visit.remove(next_city)
                    new_state = (next_city, new_to_visit, to_visit_twice, unvisited)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], new_state))
                # If the next city is one of the unvisited cities
                elif next_city in unvisited:
                    new_unvisited = list(unvisited)
                    new_unvisited.remove(next_city)
                    new_state = (next_city, to_visit, to_visit_twice, new_unvisited)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], new_state))
    return None

print(a_star())
