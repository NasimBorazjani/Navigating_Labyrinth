
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'Q': ['Z'],
        'T': ['Q', 'A', 'X'],
        'A': ['M'],
        'X': ['M', 'Z', 'B', 'S'],
        'M': ['Q', 'B', 'E'],
        'Y': ['T', 'A', 'X'],
        'Z': ['M', 'Y', 'B'],
        'B': ['Q', 'T', 'A'],
        'S': ['T', 'Y', 'E'],
        'E': ['A', 'X', 'M', 'B', 'S']
    }

    # Define the initial state and the goal state
    initial_state = ('Q', frozenset(), 0)
    goal_state = ('Q', frozenset(['T', 'T', 'E', 'E']), 0)

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
            # If the neighbor is a destination city and we have not visited it twice yet, or the neighbor is not a destination city and we have not visited it yet
            if (neighbor in ['T', 'E'] and state[1].count(neighbor) < 2) or (neighbor not in ['T', 'E'] and neighbor not in state[1]):
                # Generate the new state
                new_state = (neighbor, frozenset(list(state[1]) + [neighbor]), 0)
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [neighbor], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of destination cities not yet visited twice
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as each destination city must be visited twice
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city and we have not visited it twice yet
    return goal[1].count('T') + goal[1].count('E') - state[1].count('T') - state[1].count('E')

print(a_star())
