
import heapq

def a_star():
    # Define the adjacency matrix of the graph, the initial state, and the goal state
    adjacency_matrix = {
        'H': ['T'],
        'F': ['R', 'L', 'D'],
        'C': ['L'],
        'E': ['C', 'V'],
        'T': ['H', 'M', 'Z', 'D'],
        'V': ['F', 'C', 'I'],
        'R': ['I', 'M', 'D'],
        'I': ['F', 'C', 'E', 'M'],
        'M': ['H', 'C'],
        'Z': ['H', 'R', 'M'],
        'L': ['C', 'T', 'R', 'M'],
        'D': ['H', 'F', 'C', 'V', 'I', 'M', 'Z']
    }
    initial_state = ('E', 0, 0)
    goal_state = ('E', 2, 2)

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
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in adjacency_matrix[state[0]]:
            # The new state is the neighbor city, and the counts of visits to cities 'D' and 'T' are incremented if the neighbor city is 'D' or 'T'
            new_state = (neighbor, state[1] + (neighbor == 'D'), state[2] + (neighbor == 'T'))

            # Check if the new state is valid, ie we have not visited 'D' or 'T' more than twice and we have not visited any other city more than once
            if (new_state[1] <= 2 and new_state[2] <= 2 and (new_state[0] not in actions or new_state[0] in ['D', 'T'])):
                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [neighbor], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the remaining visits to 'D' and 'T'
    # The heuristic relaxes the constraint that we can only move to neighboring cities and presumes we can move directly to 'D' or 'T'
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the remaining visits to 'D' or 'T', if we move to 'D' or 'T', otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the remaining visits to 'D' and 'T' would be 0 in the goal state.
    return goal[1] - state[1] + goal[2] - state[2]

print(a_star())
