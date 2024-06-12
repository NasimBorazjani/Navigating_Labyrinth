
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'Q': ['A', 'G', 'L'],
        'A': ['X', 'B', 'O'],
        'E': ['Q', 'B', 'Z'],
        'R': ['Q', 'A', 'W'],
        'D': ['Z'],
        'G': ['A', 'E', 'B', 'Z', 'F', 'O'],
        'X': ['E', 'G', 'K', 'B', 'L'],
        'K': ['E', 'R', 'Z', 'W', 'B', 'L'],
        'B': ['X', 'K', 'Z', 'W', 'F', 'O', 'L'],
        'Z': ['A', 'G', 'B', 'W', 'F', 'O'],
        'W': ['R', 'G', 'Z', 'B', 'F', 'L'],
        'F': ['R', 'G', 'X', 'K', 'B', 'Z', 'W', 'O', 'L'],
        'O': ['A', 'G', 'B', 'Z', 'L'],
        'L': ['Q', 'X', 'K', 'B', 'W', 'F', 'O']
    }

    # Define the initial state and the goal state
    initial_state = ('D', ['K', 'K', 'X', 'X'], [])
    goal_state = ('D', [], ['K', 'K', 'X', 'X'])

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
        current_city, remaining_cities, visited_cities = state
        for next_city in graph[current_city]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is a destination city
            if next_city not in visited_cities or next_city in remaining_cities:
                # Generate the new state
                new_remaining_cities = remaining_cities[:]
                new_visited_cities = visited_cities[:]
                if next_city in new_remaining_cities:
                    new_remaining_cities.remove(next_city)
                new_visited_cities.append(next_city)
                new_state = (next_city, new_remaining_cities, new_visited_cities)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of remaining cities to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining city must be visited at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of remaining cities, if the city is a remaining city
    return len(state[1])

print(a_star())
