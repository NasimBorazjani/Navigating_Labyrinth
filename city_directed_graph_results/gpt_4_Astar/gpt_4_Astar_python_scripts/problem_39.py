
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'O': ['Z', 'M'],
        'Z': ['N', 'Y'],
        'J': ['O', 'M', 'N', 'U'],
        'K': ['O', 'W', 'Q'],
        'E': ['O', 'J', 'T', 'Y'],
        'M': ['Z', 'K'],
        'T': ['Z', 'J', 'E', 'Y'],
        'W': ['J', 'M', 'N', 'T'],
        'N': ['O', 'K', 'E', 'M', 'Y'],
        'Q': ['E', 'W'],
        'U': ['E', 'N', 'Q'],
        'Y': ['O', 'J', 'K', 'M', 'W', 'U']
    }
    # Define the initial state and the goal state
    initial_state = ('O', False, False)
    goal_state = ('O', True, True)

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

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in graph[state[0]]:
            # If the neighbor is a destination city, check if it has been visited twice already
            if neighbor in ['N', 'T']:
                if state[1] and state[2] and neighbor == 'N':
                    continue
                if state[1] and state[2] and neighbor == 'T':
                    continue
                # If the neighbor is a destination city and has not been visited twice, generate the new state
                new_state = (neighbor, state[1] or neighbor == 'N', state[2] or neighbor == 'T')
            else:
                # If the neighbor is not a destination city, it must not have been visited before
                if neighbor in actions:
                    continue
                # If the neighbor is not a destination city and has not been visited, generate the new state
                new_state = (neighbor, state[1], state[2])

            # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
            new_cost = g + 1

            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                visited_costs[new_state] = new_cost
                heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [neighbor], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities not visited twice
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited twice
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city and has not been visited twice
    return 2 - state[1] - state[2]

print(a_star())
