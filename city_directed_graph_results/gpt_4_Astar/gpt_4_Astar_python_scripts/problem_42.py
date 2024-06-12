
import heapq

def a_star():
    # Define the adjacency matrix of the graph, the initial state, and the goal state
    adjacency_matrix = {
        'J': ['Y', 'M'],
        'U': ['T', 'Y', 'C', 'P'],
        'T': ['J', 'N', 'H'],
        'S': ['J', 'U', 'Y', 'P'],
        'N': ['J', 'S', 'A', 'M'],
        'F': ['A'],
        'Y': ['H'],
        'C': ['T', 'F'],
        'H': ['J', 'U', 'S', 'C'],
        'A': ['J', 'N', 'H', 'M'],
        'M': ['T', 'H', 'P'],
        'P': ['N', 'C', 'H', 'M']
    }
    initial_state = ('F', 0, 0)
    goal_state = (2, 2)

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
        if state[1:] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie we can't visit a city more than once, except for 'H' and 'N' which we must visit twice
            if (actions.count(neighbor) < 1 or neighbor in ['H', 'N']) and (neighbor != 'H' or state[1] < 2) and (neighbor != 'N' or state[2] < 2):
                # Generate the new state
                new_state = (neighbor, state[1] + (neighbor == 'H'), state[2] + (neighbor == 'N'))
                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [neighbor], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the remaining visits to 'H' and 'N'
    # The heuristic relaxes the constraint that we can only move to neighboring cities and presumes we can move directly to 'H' or 'N'
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the remaining visits to 'H' or 'N', if we move to 'H' or 'N', otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining visits to 'H' or 'N' in the goal state.
    return goal[0] - state[1] + goal[1] - state[2]

print(a_star())
