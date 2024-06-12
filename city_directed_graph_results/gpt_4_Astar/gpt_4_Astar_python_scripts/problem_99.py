
import heapq

def a_star():
    # Define the adjacency matrix of the graph, the initial state, and the goal state
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    cities = ['R', 'P', 'Z', 'U', 'H', 'T', 'E', 'W', 'F', 'M', 'D', 'L', 'Y', 'C', 'G']
    initial_state = ('L', ['P', 'W'], [])
    goal_state = ('L', [], ['P', 'W', 'P', 'W'])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
        current_city_index = cities.index(state[0])
        for i in range(len(cities)):
            if adjacency_matrix[current_city_index][i] == 1:
                new_city = cities[i]
                # Check if the new state would be valid, ie the new city must not have been visited before, unless it is one of the destination cities
                if new_city not in state[2] or new_city in state[1]:
                    # Generate the new state
                    new_state = (new_city, state[1][:], state[2][:])
                    # If the new city is a destination city, remove it from the list of destination cities to visit
                    if new_city in new_state[1]:
                        new_state[1].remove(new_city)
                    # Add the new city to the list of visited cities
                    new_state[2].append(new_city)
                    # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities left to visit
    # The heuristic relaxes the constraint that we can only move to cities directly connected to the current city and presumes we can move to any of the destination cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of destination cities left to visit, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no destination cities left to visit in the goal state.
    return len(state[1])

print(a_star())
