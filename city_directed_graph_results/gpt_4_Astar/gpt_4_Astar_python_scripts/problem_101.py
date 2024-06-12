
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                        [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0]]
    # Define the cities
    cities = ['S', 'Z', 'I', 'R', 'P', 'T', 'X', 'B', 'F', 'A', 'L', 'M', 'G', 'N', 'E']
    # Define the initial state and the goal state
    initial_state = ('P', ['I', 'N'], ['I', 'N'], ['P'])
    goal_state = ('P', [], [], ['P', 'I', 'N', 'I', 'N'])
    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Define the queue
    queue = [(0, 0, [], initial_state)]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions
        if state == goal_state:
            return actions
        # Generate all possible actions from the current state
        for i in range(len(cities)):
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                new_city = cities[i]
                # Check if the new city is a destination city
                if new_city in state[1]:
                    new_destinations = list(state[1])
                    new_destinations.remove(new_city)
                    new_path = list(state[3])
                    new_path.append(new_city)
                    new_state = (new_city, new_destinations, state[2], new_path)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [new_city], new_state))
                # Check if the new city is a city that we have already visited
                elif new_city in state[2]:
                    continue
                # If the new city is not a destination city and we have not visited it before
                else:
                    new_visited = list(state[2])
                    new_visited.append(new_city)
                    new_path = list(state[3])
                    new_path.append(new_city)
                    new_state = (new_city, state[1], new_visited, new_path)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [new_city], new_state))
    return None

print(a_star())
