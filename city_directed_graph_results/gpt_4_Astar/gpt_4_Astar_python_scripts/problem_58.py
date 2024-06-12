
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'B': ['K', 'P', 'M', 'R', 'J'],
        'K': ['B', 'X', 'P'],
        'S': ['K', 'P'],
        'X': ['K', 'V', 'E'],
        'T': ['K', 'S', 'Q', 'V', 'E'],
        'P': ['B', 'K', 'T', 'G'],
        'Q': ['B', 'P', 'R', 'G', 'V'],
        'M': ['B', 'K', 'T'],
        'R': ['B', 'K', 'X', 'Q', 'G'],
        'G': ['S', 'P', 'Q', 'J', 'V'],
        'J': ['B', 'K', 'T', 'M'],
        'V': ['B', 'X', 'T', 'Q', 'G', 'E'],
        'E': ['B', 'K', 'T', 'P', 'Q', 'R', 'G', 'V']
    }

    # Define the initial state and the goal state
    initial_state = ('S', ['B', 'B', 'V', 'V'], ['B', 'K', 'S', 'X', 'T', 'P', 'Q', 'M', 'R', 'G', 'J', 'V', 'E'])
    goal_state = ('S', [], [])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['S'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path taken to reach the goal state
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in graph[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is a destination city and it has not been visited twice already
            if neighbor in state[2] or (neighbor in state[1] and state[1].count(neighbor) > 1):
                # Generate the new state
                new_state = (neighbor, [city for city in state[1] if city != neighbor or state[1].count(neighbor) > 1], [city for city in state[2] if city != neighbor] if neighbor in state[2] else state[2] + [neighbor])
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [neighbor], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities left to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of destination cities left to visit, if the city is a destination city
    return len(state[1])

print(a_star())
