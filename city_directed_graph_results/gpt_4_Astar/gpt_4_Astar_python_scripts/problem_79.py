
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0]]
    # Define the cities
    cities = ['Z', 'G', 'K', 'N', 'S', 'X', 'I', 'F', 'E', 'C', 'R', 'V', 'L', 'W']
    # Define the initial state and the goal state
    initial_state = ('I', ['S', 'S', 'W', 'W'], ['I'])
    goal_state = ('I', [], ['I', 'S', 'W', 'S', 'W'])
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
        for i in range(len(cities)):
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                new_city = cities[i]
                new_destinations = state[1][:]
                new_path = state[2][:]
                if new_city in new_destinations:
                    new_destinations.remove(new_city)
                new_path.append(new_city)
                new_state = (new_city, new_destinations, new_path)
                new_cost = g + 1
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_state))
    return None

def heuristic(state, goal):
    # The heuristic function can be the number of destination cities not yet visited
    return len(state[1])

print(a_star())
