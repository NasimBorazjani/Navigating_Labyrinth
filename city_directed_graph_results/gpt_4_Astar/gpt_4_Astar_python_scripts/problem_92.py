
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = 'F'
    goal_state = ['R', 'R', 'S', 'S']

    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'I': {'E': 1, 'J': 1, 'L': 1},
        'H': {'I': 1, 'G': 1, 'S': 1, 'W': 1},
        'R': {'H': 1, 'E': 1, 'G': 1, 'W': 1, 'B': 1, 'V': 1, 'L': 1},
        'E': {'H': 1, 'Q': 1, 'C': 1},
        'G': {'I': 1},
        'S': {'I': 1, 'W': 1, 'Q': 1, 'J': 1, 'L': 1},
        'W': {'I': 1, 'R': 1},
        'Q': {'I': 1, 'S': 1, 'C': 1, 'A': 1, 'B': 1, 'J': 1},
        'C': {'I': 1, 'H': 1, 'R': 1, 'G': 1, 'W': 1, 'A': 1, 'F': 1, 'J': 1, 'V': 1},
        'A': {'I': 1, 'H': 1, 'W': 1},
        'B': {'E': 1, 'S': 1, 'W': 1, 'A': 1, 'L': 1},
        'F': {'I': 1, 'H': 1, 'L': 1},
        'J': {'E': 1, 'S': 1, 'W': 1, 'B': 1},
        'V': {'E': 1, 'G': 1, 'Q': 1, 'A': 1, 'B': 1},
        'L': {'E': 1, 'G': 1, 'Q': 1}
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

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if not remaining_cities:
            return actions

        # Generate all valid actions from the current state, which includes moving to any of the cities directly connected to the current city
        for next_city in adjacency_matrix[current_city]:
            if next_city in remaining_cities:
                new_remaining_cities = list(remaining_cities)
                new_remaining_cities.remove(next_city)
                new_state = (next_city, tuple(new_remaining_cities))

                # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state):
    # An admissible and consistent heuristic is the number of remaining cities to visit
    # The heuristic relaxes the constraint that we can only move to cities directly connected to the current city and presumes we can move to any of the remaining cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a city is always 1, which is exactly the decrease in the number of remaining cities to visit, if the city is one of the remaining cities, otherwise the estimated cost of the successor node is the same, and the heuristic estimate for the goal state is 0, as there are no remaining cities to visit in the goal state.
    return len(state[1])

print(a_star())
