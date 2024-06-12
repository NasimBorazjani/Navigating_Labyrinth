
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the cost to reach that city
    adjacency_matrix = {'S': {'X': 1, 'V': 1, 'F': 1, 'C': 1},
                        'X': {'S': 1, 'O': 1, 'D': 1},
                        'Y': {'S': 1, 'X': 1, 'R': 1, 'F': 1},
                        'Q': {'X': 1, 'D': 1},
                        'O': {'X': 1, 'V': 1, 'H': 1},
                        'R': {'X': 1, 'V': 1, 'C': 1},
                        'D': {'S': 1, 'Y': 1, 'H': 1},
                        'V': {'Y': 1, 'R': 1, 'D': 1, 'C': 1},
                        'H': {'S': 1, 'Y': 1, 'Q': 1, 'V': 1, 'C': 1},
                        'J': {'X': 1, 'Y': 1, 'R': 1, 'H': 1},
                        'F': {'Y': 1, 'D': 1, 'V': 1, 'J': 1},
                        'C': {'S': 1, 'X': 1, 'V': 1, 'J': 1, 'F': 1}}

    # Define the initial state and the goal state
    initial_state = ('Q', frozenset(), 0)
    goal_state = ('Q', frozenset(['F', 'V']), 2)

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

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is one of the destination cities and it has not been visited twice already
            if (next_city not in state[1] or (next_city in ['F', 'V'] and state[2] < 2)):
                # Generate the new state
                visited_cities = set(state[1])
                visited_cities.add(next_city)
                num_destinations_visited = state[2]
                if next_city in ['F', 'V']:
                    num_destinations_visited += 1
                new_state = (next_city, frozenset(visited_cities), num_destinations_visited)

                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities not yet visited twice
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least twice
    # The heuristic is consistent because the cost of moving to a new city is always 1, which is exactly the decrease in the heuristic cost, if the new city is a destination city and it has not been visited twice already
    return 2 - state[2]

print(a_star())
