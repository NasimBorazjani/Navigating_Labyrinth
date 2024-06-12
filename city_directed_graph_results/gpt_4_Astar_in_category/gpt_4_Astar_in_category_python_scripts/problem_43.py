
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = {
        'Y': ['J'],
        'E': ['P', 'B'],
        'L': ['E', 'M', 'C', 'T'],
        'P': ['L'],
        'M': ['P', 'T'],
        'C': ['P', 'M', 'B'],
        'B': ['E', 'P', 'V'],
        'I': ['Y', 'E', 'M', 'B', 'G'],
        'G': ['Y', 'E'],
        'V': ['M'],
        'J': ['P', 'B', 'I', 'G', 'T'],
        'T': ['C', 'I', 'G']
    }

    # Define the initial state and the goal state
    initial_state = ('Y', False, False, ['Y'])
    goal_state = ('Y', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, initial_state)]

    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state[:3] == goal_state:
            return state[3]

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in adjacency_matrix[state[0]]:
            # Check if the new state is valid, ie if the city has not been visited before, or if it is one of the destination cities
            if neighbor not in state[3] or neighbor in ['E', 'M']:
                # Generate the new state
                new_state = list(state)
                new_state[0] = neighbor
                new_state[3] = new_state[3] + [neighbor]
                # Update the visited status of the destination cities
                if neighbor == 'E':
                    new_state[1] = True
                elif neighbor == 'M':
                    new_state[2] = True
                new_state = tuple(new_state)
                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited destination city must be visited at least once
    # The heuristic is consistent because the cost of moving from one city to an adjacent city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city
    return sum(1 for i in range(1, 3) if state[i] != goal[i])

print(a_star())
