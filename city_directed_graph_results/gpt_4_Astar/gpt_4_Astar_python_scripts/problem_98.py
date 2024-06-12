
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = 'D'
    goal_state = ['J', 'X', 'J', 'X']
    # Define the adjacency matrix as a dictionary of lists
    adjacency_matrix = {
        'B': ['X', 'F', 'Q', 'V', 'A', 'K'],
        'X': ['V', 'M', 'H', 'K'],
        'F': ['B', 'X', 'J', 'T'],
        'Q': ['B', 'A', 'J', 'M'],
        'V': ['X', 'J', 'N', 'M', 'G', 'H', 'T'],
        'D': ['B', 'M'],
        'A': ['B', 'X', 'Q', 'V', 'T'],
        'J': ['B', 'Q', 'V', 'D', 'H'],
        'N': ['X', 'F', 'A', 'J', 'T'],
        'M': ['X', 'Q', 'V', 'D', 'T'],
        'G': ['B', 'Q', 'V', 'D', 'N', 'M', 'H', 'K', 'T'],
        'H': ['X', 'V', 'D', 'J', 'T'],
        'K': ['B', 'X', 'D', 'A', 'G', 'H', 'S', 'T'],
        'T': ['B', 'F', 'A', 'V', 'N', 'M', 'G', 'K', 'S'],
        'S': ['X', 'Q', 'N', 'G', 'H', 'K', 'T']
    }

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [initial_state], initial_state, goal_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state, remaining_goals = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if not remaining_goals:
            return path

        # Generate all valid actions from the current state, which includes moving to any of the cities connected to the current city
        for next_city in adjacency_matrix[state]:
            # The action is valid if the next city is in the remaining goals or has not been visited yet
            if next_city in remaining_goals or next_city not in path:
                # Generate the new state
                new_state = next_city
                # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
                new_cost = g + 1
                # Update the remaining goals
                new_remaining_goals = remaining_goals[:]
                if next_city in new_remaining_goals:
                    new_remaining_goals.remove(next_city)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, new_remaining_goals), new_cost, path + [new_state], new_state, new_remaining_goals))

    return None

def heuristic(state, remaining_goals):
    # An admissible and consistent heuristic is the number of remaining goals
    # The heuristic relaxes the constraint that we can only move to a city connected to the current city and presumes we can move to any city directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a city is always 1, which is exactly the decrease in the number of remaining goals, if the city is a goal city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining goals in the goal state.
    return len(remaining_goals)

print(a_star())
