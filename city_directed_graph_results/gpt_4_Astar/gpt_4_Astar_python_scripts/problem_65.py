
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'F': ['Z', 'I', 'P'],
        'D': ['F', 'E', 'I'],
        'E': ['G', 'S', 'C'],
        'Z': ['E', 'Y', 'X', 'S', 'C'],
        'G': ['F', 'I', 'P'],
        'Y': ['G', 'I'],
        'N': ['Y'],
        'I': ['E', 'Z', 'X'],
        'X': ['E', 'G', 'P', 'S'],
        'P': ['D', 'Z', 'Q'],
        'S': ['F', 'D', 'Z', 'X', 'C'],
        'Q': ['D', 'X'],
        'C': ['E', 'N', 'I', 'X']
    }
    # Define the initial state and the goal state
    initial_state = ('Q', frozenset(), 0)
    goal_state = 2

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
        if state[2] == goal_state and 'F' in state[1] and 'N' in state[1]:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in graph[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it's F or N
            if neighbor not in state[1] or (neighbor in ['F', 'N'] and state[1].count(neighbor) < 2):
                # Generate the new state
                new_state = (neighbor, state[1] | frozenset([neighbor]), state[2] + 1 if neighbor in ['F', 'N'] else state[2])
                # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [neighbor], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities not yet visited
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited destination city must be visited at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city
    return goal - state[2]

print(a_star())
