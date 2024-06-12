
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the cost to reach that city (1 for all cities as the travel time between any two directly connected cities is the same)
    adjacency_matrix = {'V': {'C': 1, 'Y': 1, 'W': 1},
                        'C': {'Y': 1, 'J': 1},
                        'I': {'V': 1, 'C': 1, 'Y': 1, 'Q': 1},
                        'Y': {'Z': 1, 'J': 1, 'F': 1},
                        'W': {'C': 1, 'Q': 1, 'X': 1},
                        'Q': {'C': 1, 'K': 1, 'F': 1},
                        'X': {'V': 1, 'I': 1, 'U': 1, 'F': 1},
                        'K': {'V': 1, 'W': 1, 'X': 1},
                        'Z': {'V': 1, 'C': 1, 'Y': 1, 'Q': 1, 'X': 1, 'K': 1},
                        'T': {'C': 1, 'W': 1, 'X': 1, 'K': 1, 'F': 1},
                        'J': {'C': 1, 'I': 1, 'Q': 1, 'X': 1, 'K': 1, 'T': 1},
                        'U': {'V': 1, 'I': 1, 'Z': 1, 'T': 1, 'J': 1},
                        'F': {'Q': 1, 'J': 1}}
    # Define the initial state as a tuple with the current city, the set of visited cities, and the number of times the destination cities have been visited
    initial_state = ('T', frozenset(['T']), {'I': 0, 'V': 0})
    # Define the goal state as visiting the destination cities twice
    goal_state = {'I': 2, 'V': 2}
    # Define the set of all cities
    cities = set(adjacency_matrix.keys())

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

        # Check if the current state is the goal state
        if state[2] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is one of the destination cities and it has not been visited twice yet
            if (city not in state[1] or (city in goal_state and state[2][city] < 2)):
                # Generate the new state
                new_state = (city, state[1].union([city]), state[2].copy())
                # Increment the visit count of the destination cities
                if city in goal_state:
                    new_state[2][city] += 1
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state, cities)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [city], new_state))
    return None

def heuristic(state, goal_state, cities):
    # An admissible and consistent heuristic for this problem is the number of destination cities that have not been visited twice yet plus the number of cities that have not been visited yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once and each destination city must be visited at least twice
    # It's consistent because the cost of moving to a new city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city that has not been visited twice yet or a city that has not been visited yet
    h = sum(2 - state[2][city] for city in goal_state) + len(cities - state[1])
    return h

print(a_star())
