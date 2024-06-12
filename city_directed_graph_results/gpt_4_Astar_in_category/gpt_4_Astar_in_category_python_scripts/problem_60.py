
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = {
        'H': ['Q', 'N', 'E'],
        'T': ['L', 'N'],
        'R': ['H', 'L', 'G', 'X'],
        'F': ['T', 'R', 'Q'],
        'L': ['F', 'Y', 'X'],
        'U': ['G', 'Y', 'X'],
        'Q': ['F', 'E', 'Y'],
        'G': ['H', 'T', 'F', 'L', 'E'],
        'N': ['T', 'L', 'U', 'G'],
        'E': ['R', 'F', 'G'],
        'Y': ['R', 'Q', 'G'],
        'I': ['H'],
        'X': ['L', 'U', 'Q', 'I']
    }

    # Define the initial state and the goal state
    initial_state = ('I', False, False, False, False)
    goal_state = ('I', True, True, True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [initial_state[0]], initial_state)]

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in adjacency_matrix[state[0]]:
            # Check if the new state is valid, ie if the city has not been visited before or if it is one of the destination cities
            if (state[1] and neighbor == 'F') or (state[2] and neighbor == 'U') or (not state[1] and neighbor != 'F') or (not state[2] and neighbor != 'U'):
                # Generate the new state
                new_state = (neighbor, state[1] or neighbor == 'F', state[2] or neighbor == 'U', state[3] or neighbor == 'F', state[4] or neighbor == 'U')
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as each unvisited destination city must be visited at least once
    # The heuristic is consistent because the cost of moving from one city to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city
    return sum(1 for s, g in zip(state[1:], goal[1:]) if s != g)

print(a_star())
