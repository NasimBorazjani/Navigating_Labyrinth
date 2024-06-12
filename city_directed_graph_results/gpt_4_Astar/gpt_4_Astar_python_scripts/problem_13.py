
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = 'H'
    goal_state = ['E', 'E', 'X', 'X']

    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the travel time (1 for all cities)
    adjacency_matrix = {
        'G': {'X': 1, 'T': 1},
        'X': {'L': 1, 'Y': 1, 'B': 1},
        'R': {'Y': 1, 'E': 1, 'B': 1},
        'L': {'E': 1},
        'Y': {'X': 1},
        'E': {'Y': 1, 'T': 1, 'B': 1},
        'V': {'R': 1, 'Y': 1, 'E': 1, 'B': 1, 'H': 1},
        'T': {'G': 1, 'X': 1, 'R': 1, 'L': 1, 'E': 1},
        'B': {'Y': 1, 'T': 1, 'H': 1},
        'H': {'Y': 1, 'V': 1}
    }

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[(initial_state, tuple(goal_state))] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], (initial_state, tuple(goal_state)))]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, (current_city, remaining_cities) = heapq.heappop(queue)

        # Check if the current state is the goal state
        if not remaining_cities:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[current_city]:
            # Check if the next city is in the remaining cities to visit
            if next_city in remaining_cities:
                # Generate the new state
                new_remaining_cities = list(remaining_cities)
                new_remaining_cities.remove(next_city)
                new_state = (next_city, tuple(new_remaining_cities))

                # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of remaining cities to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as we need to make at least one move to visit each remaining city
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of remaining cities if we move to a city that we need to visit
    return len(state[1])

print(a_star())
