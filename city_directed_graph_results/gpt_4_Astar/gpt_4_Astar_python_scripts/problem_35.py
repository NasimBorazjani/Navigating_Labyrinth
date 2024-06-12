
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'A': ['V', 'S', 'M', 'W'],
        'V': ['N', 'H'],
        'N': ['P', 'E', 'L'],
        'Q': ['A', 'V', 'P', 'L'],
        'P': ['V', 'E', 'H'],
        'S': ['Q', 'P'],
        'M': ['V', 'N', 'P', 'S', 'E', 'H', 'W', 'G'],
        'E': ['Q', 'P'],
        'L': ['V', 'E', 'H', 'W', 'G'],
        'H': ['S', 'L'],
        'W': ['A', 'V', 'N', 'P', 'S', 'E', 'G'],
        'G': ['A', 'V', 'M']
    }

    # Define the initial state and the goal state
    initial_state = ('G', ['L', 'L', 'P', 'P'], ['A', 'V', 'N', 'Q', 'S', 'M', 'E', 'H', 'W'])
    goal_state = ('G', [], [])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken to reach it
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        current_city, destinations, other_cities = state
        for next_city in graph[current_city]:
            # If the next city is a destination, remove it from the destinations list
            if next_city in destinations:
                new_destinations = destinations[:]
                new_destinations.remove(next_city)
                new_state = (next_city, new_destinations, other_cities)
                new_cost = g + 1
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
            # If the next city is not a destination and has not been visited yet, remove it from the other cities list
            elif next_city in other_cities:
                new_other_cities = other_cities[:]
                new_other_cities.remove(next_city)
                new_state = (next_city, destinations, new_other_cities)
                new_cost = g + 1
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal):
    # The heuristic function can be the number of remaining destinations plus the number of remaining other cities
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining city must be visited at least once
    # It's consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a remaining city
    return len(state[1]) + len(state[2])

print(a_star())
