
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                        [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
                        [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                        [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
                        [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
                        [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0]]
    # Define the cities
    cities = ['J', 'H', 'X', 'L', 'F', 'A', 'P', 'M', 'D', 'R', 'T', 'Z', 'N', 'K']
    # Define the initial state and the goal state
    initial_state = ('X', ['N', 'N', 'K', 'K'], ['X'])
    goal_state = ('X', [], ['X', 'N', 'K', 'N', 'K'])
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
            # If there is a road from the current city to the city i
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                # If the city i is not visited yet or it is a destination city
                if cities[i] not in state[2] or cities[i] in state[1]:
                    # Generate the new state
                    new_state = (cities[i], [city for city in state[1] if city != cities[i]], state[2] + [cities[i]])
                    # The cost so far is the number of actions taken
                    new_cost = g + 1
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # The heuristic is the number of destination cities not visited yet
                        h = len(new_state[1])
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [cities[i]], new_state))
    return None

print(a_star())
