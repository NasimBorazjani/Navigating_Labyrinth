
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                        [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
                        [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]]
    # Define the cities
    cities = ['O', 'C', 'F', 'W', 'I', 'P', 'U', 'B', 'H', 'Q', 'G', 'S']
    # Define the initial state and the goal state
    initial_state = ('G', ['F', 'F', 'U', 'U'], ['G'])
    goal_state = ('G', [], ['G', 'F', 'U', 'F', 'U'])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        current_city = state[0]
        remaining_cities = state[1]
        visited_cities = state[2]
        for i in range(len(cities)):
            # Check if the city is connected to the current city
            if adjacency_matrix[cities.index(current_city)][i] == 1:
                next_city = cities[i]
                # Check if the city is one of the destination cities
                if next_city in remaining_cities:
                    new_remaining_cities = remaining_cities[:]
                    new_remaining_cities.remove(next_city)
                    new_visited_cities = visited_cities + [next_city]
                    new_state = (next_city, new_remaining_cities, new_visited_cities)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
                # Check if the city is not one of the destination cities and has not been visited before
                elif next_city not in visited_cities:
                    new_visited_cities = visited_cities + [next_city]
                    new_state = (next_city, remaining_cities, new_visited_cities)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal_state):
    # The heuristic function can be the number of remaining cities to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining city must be visited at least once
    # It's consistent because the cost of moving to a city is always 1, which is exactly the decrease in the number of remaining cities, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining cities to visit in the goal state.
    return len(state[1])

print(a_star())
