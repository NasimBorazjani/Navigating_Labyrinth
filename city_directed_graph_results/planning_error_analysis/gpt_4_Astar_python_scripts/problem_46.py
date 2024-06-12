
import heapq

def a_star():
    # Define the adjacency matrix of the graph, the initial state, and the goal state
    adjacency_matrix = {
        'O': ['Y'],
        'T': ['O', 'G', 'M'],
        'F': ['T', 'C'],
        'C': ['F', 'K', 'X', 'Y'],
        'K': ['O', 'F', 'A', 'M'],
        'U': ['G', 'W'],
        'X': ['F', 'U', 'A'],
        'G': ['K', 'U', 'Y'],
        'A': ['T', 'C'],
        'M': ['T', 'U', 'X', 'A'],
        'W': ['O', 'K', 'M'],
        'Y': ['T', 'F', 'W']
    }
    initial_state = ('O', False, False, False, False)
    goal_state = ('O', True, True, True, True)

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
            # Check if the new state would be valid, ie we can't visit a city more than once, except for the destination cities 'M' and 'K'
            if (neighbor not in actions or (neighbor == 'M' and state[1] < 2) or (neighbor == 'K' and state[2] < 2)):
                # Generate the new state
                new_state = list(state)
                new_state[0] = neighbor
                if neighbor == 'M':
                    new_state[1] += 1
                if neighbor == 'K':
                    new_state[2] += 1
                new_state = tuple(new_state)
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [neighbor], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities not yet visited twice
    # The heuristic relaxes the constraint that we can't visit a city more than once and presumes we can move to the destination cities directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city and we haven't visited it twice yet, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as we would have visited all destination cities twice in the goal state.
    return 2 - state[1] + 2 - state[2]

print(a_star())
