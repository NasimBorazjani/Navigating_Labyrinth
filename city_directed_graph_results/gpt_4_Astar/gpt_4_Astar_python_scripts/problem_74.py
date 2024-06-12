
import heapq

def a_star():
    # Define the adjacency matrix of the graph, with the cities as the nodes and the roads as the edges
    adjacency_matrix = {
        'O': ['Q', 'Z'],
        'M': ['V'],
        'U': ['M', 'L', 'B', 'K'],
        'L': ['O', 'P', 'D', 'A', 'K'],
        'Q': ['L', 'P', 'A', 'S', 'V', 'E'],
        'P': ['U', 'A', 'B', 'Z'],
        'D': ['M', 'U', 'P', 'V'],
        'A': ['M', 'U', 'Q', 'P', 'S', 'Z'],
        'S': ['O', 'M', 'D'],
        'B': ['M', 'L', 'S', 'V'],
        'K': ['M', 'L', 'Q', 'D', 'A', 'S', 'V', 'Z'],
        'V': ['O', 'D', 'Z'],
        'E': ['Q', 'D', 'A', 'B', 'K', 'Z'],
        'Z': ['O', 'U', 'Q', 'D', 'A', 'S', 'K', 'E']
    }
    # Define the initial state and the goal state of the problem
    initial_state = ('M', ['L', 'L', 'Z', 'Z'], ['M'])  # The initial state includes the current city, the cities yet to visit, and the path taken so far
    goal_state = ('M', [], ['M'])  # The goal state is when we are back in city 'M' and have visited all the cities in the list

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path taken to reach the goal state
        if state == goal_state:
            return state[2]

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for next_city in adjacency_matrix[state[0]]:
            # If the next city is in the list of cities yet to visit, remove it from the list
            if next_city in state[1]:
                new_cities_to_visit = list(state[1])
                new_cities_to_visit.remove(next_city)
            else:
                new_cities_to_visit = state[1]

            # If the next city is not in the path taken so far or is one of the destination cities, add it to the path
            if next_city not in state[2] or next_city in ['L', 'Z']:
                new_path = list(state[2])
                new_path.append(next_city)
            else:
                new_path = state[2]

            # Generate the new state
            new_state = (next_city, new_cities_to_visit, new_path)

            # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
            new_cost = g + 1

            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                visited_costs[new_state] = new_cost
                h = heuristic(new_state, goal_state)
                heapq.heappush(queue, (new_cost + h, new_cost, new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of cities yet to visit
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as each city yet to visit must be visited at least once
    # The heuristic is consistent because the cost of moving to a new city is always 1, which is exactly the decrease in the number of cities yet to visit, if the new city is in the list of cities yet to visit
    return len(state[1])


print(a_star())
