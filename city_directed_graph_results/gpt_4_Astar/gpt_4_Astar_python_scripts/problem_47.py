
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'Z': ['K', 'R'],
        'O': ['C'],
        'F': ['O', 'B', 'U', 'D'],
        'M': ['Z', 'F', 'K', 'D'],
        'C': ['F', 'U', 'R', 'J'],
        'K': ['O', 'D', 'R'],
        'B': ['F', 'C', 'U', 'S'],
        'U': ['Z', 'M', 'D', 'R', 'J'],
        'D': ['O', 'K', 'S', 'J'],
        'R': ['F', 'B', 'S'],
        'S': ['F', 'M', 'C', 'R'],
        'J': ['O', 'B', 'D']
    }

    # Define the initial state and the goal state
    initial_state = ('Z', ['C', 'C', 'D', 'D'], ['Z'])
    goal_state = ('Z', [], ['Z'])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in graph[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it's a destination city
            if neighbor not in state[2] or neighbor in state[1]:
                # Generate the new state
                new_state = (neighbor, [city for city in state[1] if city != neighbor], state[2] + [neighbor])
                # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [neighbor], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities left to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least once
    # It's consistent because moving to a new city reduces the heuristic cost of the successor node by a max of 1 (if the new city is a destination city), which is equal to the cost of reaching the successor node
    return len(state[1])

print(a_star())
