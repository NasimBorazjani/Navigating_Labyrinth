
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = {
        'R': ['E', 'D', 'J'],
        'S': ['W', 'G', 'N', 'J'],
        'W': ['R'],
        'B': ['P', 'J'],
        'P': ['S', 'D'],
        'G': ['B'],
        'Q': ['W', 'B', 'P', 'N', 'D'],
        'E': ['R', 'S', 'P', 'G', 'Q'],
        'N': ['P', 'G', 'D'],
        'D': ['W', 'E'],
        'J': ['S', 'P', 'Q']
    }

    # Define the initial state and the goal state
    initial_state = ('G', False, False)
    goal_state = ('G', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['G'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in adjacency_matrix[state[0]]:
            # Check if the new state is valid, ie if the city has not been visited before, or if it is one of the destination cities
            if neighbor not in path or neighbor in ['E', 'S']:
                # Generate the new state
                new_state = list(state)
                new_state[0] = neighbor
                # If the new city is one of the destination cities, update the visited status of the city
                if neighbor == 'E':
                    new_state[1] = True
                elif neighbor == 'S':
                    new_state[2] = True
                new_state = tuple(new_state)
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic relaxes the constraint that we can only move to neighboring cities and presumes we can move directly to the destination cities
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all destination cities would have been visited in the goal state.
    return 2 - sum(state[1:])

print(a_star())
