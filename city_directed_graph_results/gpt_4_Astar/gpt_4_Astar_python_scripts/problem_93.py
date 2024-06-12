
import heapq

def a_star():
    # Define the adjacency matrix of the graph, the initial state, and the goal state
    adjacency_matrix = [[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]]
    cities = ['C', 'Q', 'T', 'K', 'M', 'B', 'R', 'D', 'J', 'A', 'Y', 'V', 'O', 'N', 'P']
    initial_state = ('M', ['K', 'Y'], [])
    goal_state = ('M', [], ['K', 'Y', 'K', 'Y'])

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        current_city = state[0]
        remaining_destinations = state[1]
        visited_destinations = state[2]

        for i in range(len(cities)):
            if adjacency_matrix[cities.index(current_city)][i] == 1:
                next_city = cities[i]
                if next_city not in visited_destinations or (next_city in remaining_destinations and visited_destinations.count(next_city) < 2):
                    new_remaining_destinations = remaining_destinations[:]
                    new_visited_destinations = visited_destinations[:]
                    if next_city in new_remaining_destinations:
                        new_remaining_destinations.remove(next_city)
                    new_visited_destinations.append(next_city)
                    new_state = (next_city, new_remaining_destinations, new_visited_destinations)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal_state):
    # The heuristic function can be the number of remaining cities to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining city must be visited at least once
    # It's consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a remaining city to visit
    return len(state[1])

print(a_star())
