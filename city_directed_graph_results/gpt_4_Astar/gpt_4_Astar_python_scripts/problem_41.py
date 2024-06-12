
import heapq

def a_star():
    # Define the adjacency matrix of the graph, the initial state, and the goal state
    adjacency_matrix = [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
                        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0]]
    cities = ['L', 'Y', 'V', 'E', 'A', 'M', 'C', 'Q', 'F', 'Z', 'G', 'O']
    initial_state = ('E', ['E'], ['A', 'A', 'Y', 'Y'])
    goal_state = ('E', ['E', 'A', 'Y', 'A', 'Y'], [])
    num_cities = len(cities)

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(num_cities):
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                new_city = cities[i]
                # Check if the new state would be valid, ie the city must not have been visited before, unless it is a destination city and it has not been visited twice already
                if (new_city not in state[1] or (new_city in state[2] and state[1].count(new_city) < 2)):
                    # Generate the new state
                    new_state = (new_city, state[1] + [new_city], [city for city in state[2] if city != new_city or state[1].count(city) < 2])
                    # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities left to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least once
    # It's consistent because moving to a new city reduces the heuristic cost of the successor node by a max of 1 (if the new city is a destination city), which is equal to the cost of reaching the successor node
    return len(state[2])

print(a_star())
