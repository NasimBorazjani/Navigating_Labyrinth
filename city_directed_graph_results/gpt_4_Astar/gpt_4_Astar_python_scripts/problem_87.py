
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = 'E'
    goal_state = ['A', 'P', 'A', 'P']

    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'A': {'Z': 1, 'O': 1, 'E': 1, 'T': 1, 'G': 1},
        'P': {'A': 1, 'I': 1},
        'Z': {'L': 1, 'X': 1, 'D': 1},
        'O': {'A': 1, 'I': 1, 'G': 1},
        'R': {'P': 1, 'Z': 1, 'X': 1, 'T': 1, 'W': 1},
        'I': {'Q': 1},
        'L': {'A': 1, 'P': 1, 'O': 1, 'R': 1, 'S': 1},
        'X': {'E': 1, 'S': 1},
        'E': {'O': 1, 'L': 1, 'G': 1},
        'T': {'I': 1, 'L': 1, 'E': 1},
        'W': {'Z': 1, 'L': 1, 'E': 1, 'D': 1, 'Q': 1},
        'D': {'A': 1, 'O': 1, 'I': 1, 'L': 1, 'T': 1, 'Q': 1},
        'S': {'A': 1, 'P': 1, 'Z': 1, 'I': 1, 'E': 1, 'D': 1},
        'G': {'P': 1, 'X': 1, 'E': 1, 'W': 1},
        'Q': {'A': 1, 'Z': 1, 'O': 1, 'X': 1, 'T': 1, 'S': 1}
    }

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if actions == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in adjacency_matrix[state]:
            # The new state is the neighboring city
            new_state = neighbor
            # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
            new_cost = g + 1

            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                visited_costs[new_state] = new_cost
                heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of remaining cities to visit
    # The heuristic relaxes the constraint that we can only move to neighboring cities and presumes we can move to any of the remaining cities directly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of remaining cities to visit, if the city is a remaining city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining cities to visit in the goal state.
    return len([city for city in goal if city != state])

print(a_star())
