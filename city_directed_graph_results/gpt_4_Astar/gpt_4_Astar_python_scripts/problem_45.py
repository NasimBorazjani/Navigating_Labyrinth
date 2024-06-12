
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'Z': ['P', 'B', 'Y', 'C'],
        'H': ['Z', 'P', 'L', 'Q', 'Y', 'V', 'C'],
        'M': ['H', 'Y', 'V'],
        'P': ['B', 'E', 'C'],
        'B': ['H', 'I'],
        'I': ['H', 'B', 'E', 'Q', 'C'],
        'E': ['Z', 'H', 'M'],
        'L': ['Z', 'H', 'M', 'B', 'I', 'E', 'Q'],
        'Q': ['Z', 'M', 'P', 'B', 'E', 'L'],
        'Y': ['L', 'C'],
        'V': ['M'],
        'C': ['B', 'Y']
    }

    # Define the initial state and the goal state
    initial_state = ('C', frozenset(['M', 'Q']), 2, 2)
    goal_state = ('C', frozenset(), 0, 0)

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
        current_city, remaining_cities, remaining_visits_M, remaining_visits_Q = state
        for next_city in graph[current_city]:
            # Check if the new state would be valid, ie the city must not have been visited before or it must be one of the destination cities
            if next_city in remaining_cities or next_city == 'M' or next_city == 'Q':
                # Generate the new state
                new_remaining_cities = remaining_cities - {next_city} if next_city in remaining_cities else remaining_cities
                new_remaining_visits_M = remaining_visits_M - 1 if next_city == 'M' else remaining_visits_M
                new_remaining_visits_Q = remaining_visits_Q - 1 if next_city == 'Q' else remaining_visits_Q
                new_state = (next_city, new_remaining_cities, new_remaining_visits_M, new_remaining_visits_Q)

                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of remaining visits to the destination cities
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining visit must be made at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of remaining visits, if the city is a destination city
    _, _, remaining_visits_M, remaining_visits_Q = state
    return remaining_visits_M + remaining_visits_Q

print(a_star())
