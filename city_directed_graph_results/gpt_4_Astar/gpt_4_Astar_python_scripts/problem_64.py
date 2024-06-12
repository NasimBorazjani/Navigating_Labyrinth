
import heapq

def a_star():
    # Define the adjacency matrix of the graph, with the cities as the nodes and the roads as the edges
    # The adjacency matrix is represented as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries that represent the cities that can be reached from the key city, with the travel time as the value
    graph = {
        'Z': {'H': 1, 'R': 1, 'I': 1},
        'J': {'V': 1, 'H': 1, 'R': 1},
        'T': {'Z': 1, 'D': 1},
        'D': {'Z': 1, 'T': 1, 'L': 1, 'P': 1, 'H': 1, 'A': 1},
        'W': {'Z': 1, 'J': 1, 'T': 1, 'H': 1, 'A': 1},
        'L': {'J': 1, 'T': 1, 'W': 1, 'V': 1, 'H': 1, 'R': 1, 'A': 1},
        'P': {'Z': 1, 'J': 1, 'T': 1, 'W': 1, 'L': 1, 'V': 1},
        'Y': {'T': 1, 'H': 1},
        'V': {'T': 1, 'D': 1, 'L': 1, 'P': 1, 'R': 1, 'A': 1},
        'H': {'T': 1, 'I': 1},
        'R': {'Z': 1, 'T': 1, 'L': 1, 'H': 1},
        'I': {'T': 1, 'D': 1, 'R': 1},
        'A': {'J': 1, 'D': 1, 'W': 1, 'P': 1, 'Y': 1, 'H': 1, 'R': 1}
    }

    # Define the initial state and the goal state of the problem
    # The initial state is a tuple of the current city, the set of visited cities, and the number of times the destination cities have been visited
    initial_state = ('Y', frozenset(['Y']), {'D': 0, 'R': 0})
    # The goal state is when the destination cities have been visited twice
    goal_state = {'D': 2, 'R': 2}

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
        for city in graph[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is a destination city and it has not been visited twice yet
            if (city not in state[1] or (city in goal_state and state[2][city] < 2)):
                # Generate the new state
                new_state = (city, state[1].union([city]), state[2].copy())
                # Increment the visit count of the destination cities
                if city in goal_state:
                    new_state[2][city] += 1
                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the number of destination cities that have not been visited twice yet
                    h = sum(2 - new_state[2][city] for city in goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [city], new_state))

    return None

print(a_star())
