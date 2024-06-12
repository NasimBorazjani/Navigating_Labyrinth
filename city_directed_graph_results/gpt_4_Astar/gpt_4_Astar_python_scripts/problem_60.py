
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the travel time (1 for all cities)
    adjacency_matrix = {'H': {'Q': 1, 'N': 1, 'E': 1},
                        'T': {'L': 1, 'N': 1},
                        'R': {'H': 1, 'L': 1, 'G': 1, 'X': 1},
                        'F': {'T': 1, 'R': 1, 'Q': 1},
                        'L': {'F': 1, 'Y': 1, 'X': 1},
                        'U': {'G': 1, 'Y': 1, 'X': 1},
                        'Q': {'F': 1, 'E': 1, 'Y': 1},
                        'G': {'H': 1, 'T': 1, 'F': 1, 'L': 1, 'E': 1},
                        'N': {'T': 1, 'L': 1, 'U': 1, 'G': 1},
                        'E': {'R': 1, 'F': 1, 'G': 1},
                        'Y': {'R': 1, 'Q': 1, 'G': 1},
                        'I': {'H': 1},
                        'X': {'L': 1, 'U': 1, 'Q': 1, 'I': 1}}
    # Define the initial state as a tuple with the current city, the cities visited so far, the number of times city F has been visited, and the number of times city U has been visited
    initial_state = ('I', ['I'], 0, 0)
    # Define the goal state as a tuple with the current city, the cities visited so far, the number of times city F has been visited, and the number of times city U has been visited
    goal_state = ('I', ['I'], 2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken to reach the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any city that can be reached from the current city
        for city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is city F or U and they have been visited less than 2 times
            if (city not in state[1] or (city == 'F' and state[2] < 2) or (city == 'U' and state[3] < 2)):
                # Generate the new state
                new_state = (city, state[1] + [city], state[2] + (city == 'F'), state[3] + (city == 'U'))
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the number of cities left to visit, which is the number of cities minus the number of cities visited so far
                    h = len(adjacency_matrix) - len(new_state[1])
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [city], new_state))

    return None

print(a_star())
