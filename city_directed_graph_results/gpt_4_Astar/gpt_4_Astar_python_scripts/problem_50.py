
import heapq

def a_star():
    # Define the adjacency matrix of the graph, the initial state, and the goal state
    adjacency_matrix = {
        'I': ['A'],
        'E': ['I', 'V'],
        'A': ['I', 'E', 'K', 'B', 'O'],
        'G': ['K', 'N'],
        'V': ['E', 'A', 'N', 'W'],
        'K': ['I', 'G', 'B'],
        'B': ['I', 'A', 'F'],
        'N': ['I', 'A', 'V', 'O'],
        'F': ['G', 'K', 'N'],
        'W': ['I', 'E', 'V', 'O'],
        'J': ['G', 'K', 'O'],
        'O': ['I', 'A', 'K', 'N', 'F', 'W', 'J']
    }
    initial_state = 'E'
    goal_state = ['N', 'N', 'O', 'O']

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

        # Check if the current state is the goal state
        # The goal state is where we have visited the cities 'N' and 'O' twice
        if sorted(actions) == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city by a direct road
        for next_city in adjacency_matrix[state]:
            # The action is valid if we have not visited the city before, or the city is 'N' or 'O' and we have visited it less than 2 times before
            if actions.count(next_city) < 2:
                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                    visited_costs[next_city] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(next_city, goal_state), new_cost, actions + [next_city], next_city))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of cities in the goal state that we have not visited yet
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as we must visit each city in the goal state at least once
    # The heuristic is consistent because the cost of moving to a new city is always 1, which is exactly the decrease in the heuristic cost, if the new city is in the goal state
    return len([city for city in goal if city != state])

print(a_star())
