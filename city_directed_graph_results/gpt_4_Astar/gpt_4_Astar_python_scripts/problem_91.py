
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'O': ['F', 'U', 'M'],
        'F': ['O'],
        'U': ['O', 'A', 'Y'],
        'W': ['Y', 'S', 'G'],
        'T': ['O', 'A', 'G', 'Y', 'Q'],
        'Y': ['U', 'T', 'A', 'S', 'H', 'X'],
        'A': ['U', 'T', 'Y', 'Z', 'S'],
        'Z': ['A', 'W', 'G', 'X', 'M', 'Q'],
        'S': ['W', 'T', 'A', 'Y', 'H', 'D', 'M', 'Q'],
        'G': ['T', 'Z', 'S', 'X', 'D', 'M'],
        'X': ['T', 'Z', 'G', 'Y', 'M'],
        'H': ['A', 'Y', 'S', 'D'],
        'D': ['O', 'F', 'U', 'W', 'T', 'G', 'H', 'Q'],
        'M': ['O', 'Z', 'S', 'G', 'X', 'Q'],
        'Q': ['T', 'Z', 'S', 'D', 'M']
    }

    # Define the initial state and the goal state
    initial_state = ('A', 'A', 0, 0)
    goal_state = ('A', 'A', 2, 2)

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
            # Check if the new state would be valid, ie we can only visit each city once, except for 'G' and 'O'
            if (actions.count(neighbor) < 1 or neighbor in ['G', 'O']) and (neighbor != 'G' or state[2] < 2) and (neighbor != 'O' or state[3] < 2):
                # Generate the new state
                new_state = (neighbor, state[0], state[2] + (neighbor == 'G'), state[3] + (neighbor == 'O'))
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, actions + [neighbor], new_state))

    return None

print(a_star())
