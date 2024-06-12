
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = 'P'
    goal_state = ['N', 'N', 'R', 'R']

    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the cost to reach that city
    adjacency_matrix = {
        'N': {'Y': 1, 'H': 1, 'G': 1, 'T': 1},
        'Y': {'N': 1, 'U': 1, 'T': 1},
        'P': {'Q': 1, 'U': 1, 'T': 1},
        'L': {'N': 1, 'Y': 1, 'Q': 1, 'U': 1, 'T': 1},
        'Q': {'R': 1},
        'H': {'L': 1, 'K': 1, 'B': 1},
        'C': {'N': 1, 'Y': 1, 'P': 1, 'L': 1, 'Q': 1, 'H': 1, 'G': 1, 'R': 1},
        'G': {'Y': 1, 'P': 1, 'L': 1, 'Q': 1},
        'U': {'Q': 1, 'C': 1, 'G': 1},
        'K': {'N': 1, 'Y': 1, 'L': 1, 'R': 1},
        'J': {'N': 1, 'Y': 1, 'P': 1, 'L': 1, 'C': 1, 'R': 1},
        'B': {'N': 1, 'H': 1, 'C': 1, 'G': 1, 'K': 1, 'T': 1},
        'R': {'Y': 1, 'P': 1, 'L': 1, 'Q': 1, 'U': 1, 'J': 1, 'B': 1},
        'T': {'Y': 1, 'Q': 1, 'C': 1, 'K': 1, 'B': 1}
    }

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state, goal_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, remaining_goals = heapq.heappop(queue)

        # Check if the current state is the goal state
        if not remaining_goals:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city, cost in adjacency_matrix[state].items():
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is a goal city
            if next_city in remaining_goals or next_city not in actions:
                # Generate the new state
                new_state = next_city
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + cost
                # Update the remaining goal cities
                new_remaining_goals = remaining_goals[:]
                if next_city in new_remaining_goals:
                    new_remaining_goals.remove(next_city)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, new_remaining_goals), new_cost, actions + [new_state], new_state, new_remaining_goals))

    return None

def heuristic(state, remaining_goals):
    # An admissible and consistent heuristic is the number of remaining goal cities
    # The heuristic relaxes the constraint that a city can only be visited once and presumes we can move to the goal cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of remaining goal cities, if the city is moved toward is a goal city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining goal cities in the goal state.
    return len(remaining_goals)

print(a_star())
