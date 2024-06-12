
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'R': ['B', 'F', 'N'],
        'B': ['F', 'A'],
        'F': ['Z', 'N', 'M'],
        'Z': ['A', 'J'],
        'N': ['B'],
        'H': ['N', 'J'],
        'A': ['R', 'N', 'P', 'M'],
        'P': ['F', 'Z', 'H', 'M'],
        'M': ['R', 'H', 'A'],
        'J': ['R', 'Z', 'A']
    }

    # Define the initial state and the goal state
    initial_state = ('Z', frozenset(), 0)
    goal_state = ('Z', frozenset(['B', 'B', 'H', 'H']), 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken to reach the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in graph[state[0]]:
            # If the neighbor is a destination city, we can visit it twice
            if neighbor in ['B', 'H'] and state[2] < 2:
                new_state = (neighbor, state[1] | frozenset([neighbor]), state[2] + 1)
            # If the neighbor is not a destination city, we can only visit it once
            elif neighbor not in state[1] and neighbor not in ['B', 'H']:
                new_state = (neighbor, state[1] | frozenset([neighbor]), state[2])

            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
            if new_state not in visited_costs or g + 1 < visited_costs[new_state]:
                visited_costs[new_state] = g + 1
                heapq.heappush(queue, (g + 1 + heuristic(new_state, goal_state), g + 1, actions + [neighbor], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities not yet visited
    # This heuristic is admissible because it never overestimates the cost to reach the goal state, as we need to visit each destination city at least once
    # This heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic value, if the city is a destination city
    return len(goal[1] - state[1])

print(a_star())
