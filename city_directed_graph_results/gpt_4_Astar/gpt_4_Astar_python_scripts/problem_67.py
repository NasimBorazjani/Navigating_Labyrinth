
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'A': ['Q', 'N'],
        'K': ['D', 'X'],
        'G': ['K', 'Z'],
        'U': ['R'],
        'Q': ['Y', 'R'],
        'D': ['A', 'K', 'Q', 'V', 'Y'],
        'N': ['G', 'Q', 'Y', 'R'],
        'X': ['A', 'U', 'N'],
        'S': ['A', 'K', 'Q', 'X', 'Y'],
        'V': ['G', 'N', 'X', 'S'],
        'Y': ['A', 'Q', 'D', 'R', 'Z'],
        'R': ['K', 'N', 'X', 'Y'],
        'Z': ['A', 'K', 'U', 'X', 'S', 'V', 'Y', 'R']
    }

    # Define the initial state and the goal state
    initial_state = ('S', frozenset(['N', 'R']), 0)
    goal_state = ('S', frozenset(), 2)

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
        current_city, remaining_cities, visited_goal_cities = state
        for next_city in graph[current_city]:
            # If the next city is a goal city and we have not visited it twice yet, increment the count of visited goal cities
            if next_city in ['N', 'R'] and visited_goal_cities < 2:
                new_state = (next_city, remaining_cities, visited_goal_cities + 1)
            # If the next city is not a goal city and we have not visited it yet, add it to the set of visited cities
            elif next_city not in remaining_cities and next_city not in ['N', 'R']:
                new_state = (next_city, remaining_cities | {next_city}, visited_goal_cities)
            else:
                continue

            # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
            new_cost = g + 1

            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                visited_costs[new_state] = new_cost
                heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of remaining goal cities to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as we need to visit each remaining goal city at least once
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic, if the city is a remaining goal city
    return len(goal[1]) - len(state[1])

print(a_star())
