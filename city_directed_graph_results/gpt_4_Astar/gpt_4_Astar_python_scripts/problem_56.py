
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]]
    # Define the cities
    cities = ['K', 'M', 'B', 'X', 'N', 'D', 'V', 'C', 'I', 'R', 'F', 'W', 'L']
    # Define the initial state and the goal state
    initial_state = ('C', ['B', 'L'], ['B', 'L'], ['K', 'M', 'X', 'N', 'D', 'V', 'I', 'R', 'F', 'W'])
    goal_state = ('C', [], [], [])

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
        current_city_index = cities.index(current_city)
        for i in range(len(cities)):
            # Check if there is a road from the current city to the city at index i
            if adjacency_matrix[current_city_index][i] == 1:
                next_city = cities[i]
                # Check if the next city is a destination city
                if next_city in state[1]:
                    # Remove the city from the list of destination cities
                    new_destinations = state[1][:]
                    new_destinations.remove(next_city)
                    # Add the city to the list of visited cities
                    new_visited = state[2][:]
                    new_visited.append(next_city)
                    # Generate the new state
                    new_state = (next_city, new_destinations, new_visited, state[3])
                    # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
                # If the next city is not a destination city and has not been visited before
                elif next_city in state[3]:
                    # Add the city to the list of visited cities
                    new_visited = state[2][:]
                    new_visited.append(next_city)
                    # Remove the city from the list of unvisited cities
                    new_unvisited = state[3][:]
                    new_unvisited.remove(next_city)
                    # Generate the new state
                    new_state = (next_city, state[1], new_visited, new_unvisited)
                    # The cost so far is the number of cities visited
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal_state):
    # An admissible and consistent heuristic for this problem is the number of destination cities that have not been visited yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited destination city must be visited at least once
    # It's consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all destination cities have been visited in the goal state.
    return len(state[1])

print(a_star())
