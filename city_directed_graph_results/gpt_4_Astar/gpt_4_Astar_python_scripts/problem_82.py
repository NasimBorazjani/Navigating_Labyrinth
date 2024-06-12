
import heapq

def a_star():
    # Define the adjacency matrix of the graph, with the cities as the nodes and the roads as the edges
    # The adjacency matrix is represented as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the key city of the outer dictionary and values as the cost of the edge (1 for all edges in this problem)
    graph = {'C': {'U': 1, 'F': 1, 'B': 1, 'T': 1, 'X': 1, 'L': 1},
             'K': {'C': 1, 'F': 1, 'B': 1, 'N': 1, 'H': 1},
             'U': {'F': 1, 'T': 1, 'L': 1},
             'F': {'K': 1, 'B': 1, 'T': 1, 'R': 1},
             'Q': {'K': 1, 'U': 1, 'F': 1, 'T': 1, 'L': 1},
             'B': {'C': 1, 'Q': 1, 'X': 1},
             'N': {'C': 1, 'F': 1, 'W': 1, 'H': 1},
             'W': {'U': 1, 'L': 1},
             'H': {'Q': 1, 'X': 1, 'R': 1},
             'J': {'C': 1, 'K': 1, 'Q': 1, 'B': 1},
             'T': {'F': 1, 'N': 1, 'R': 1},
             'X': {'K': 1, 'F': 1, 'Q': 1, 'W': 1, 'J': 1},
             'R': {'U': 1, 'B': 1, 'W': 1},
             'L': {'U': 1, 'N': 1, 'W': 1, 'H': 1}}

    # Define the initial state and the goal state of the problem
    # The initial state is a tuple with the current city, the set of visited cities, and the number of times the destination cities have been visited
    initial_state = ('J', frozenset(['J']), frozenset())
    # The goal state is when the current city is 'J', all cities have been visited, and the destination cities 'F' and 'L' have been visited twice
    goal_state = ('J', frozenset(graph.keys()), frozenset(['F', 'F', 'L', 'L']))

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

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        current_city, visited_cities, visited_destinations = state
        for next_city in graph[current_city]:
            # Check if the new state would be valid, ie the next city must not have been visited before, unless it is a destination city and it has been visited less than 2 times
            if (next_city not in visited_cities or (next_city in ['F', 'L'] and visited_destinations.count(next_city) < 2)):
                # The actions is valid, generate the new state
                new_visited_cities = visited_cities | {next_city}
                new_visited_destinations = visited_destinations
                if next_city in ['F', 'L']:
                    new_visited_destinations += (next_city,)
                new_state = (next_city, new_visited_cities, new_visited_destinations)
                # The cost so far is the number of actions taken, as our objective is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal_state):
    # An admissible and consistent heuristic is the number of cities that have not been visited yet
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected to the current city and presumes we can move to any city directly from the current city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a city is always 1, which is exactly the decrease in the number of unvisited cities, if the city is unvisited, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all cities would have been visited in the goal state.
    _, visited_cities, visited_destinations = state
    h = len(goal_state[1] - visited_cities) + len(goal_state[2] - visited_destinations)
    return h

print(a_star())
