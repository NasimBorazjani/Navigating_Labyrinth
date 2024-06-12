
import heapq

def a_star():
    # Define the adjacency matrix of the graph, with the cities as the nodes and the roads as the edges
    # The cities are represented as indices of the rows and columns of the adjacency matrix
    # The roads are represented as 1s in the adjacency matrix, with a 1 at the intersection of row i and column j signifying a road from city i to city j
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                        [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0]]
    # Define the initial state and the goal state of the problem
    # The initial state is the city 'A', represented as the index 1
    # The goal state is to visit the cities 'H' and 'W', represented as the indices 12 and 8, twice
    initial_state = (1, (12, 8))
    goal_state = (1, ())
    # Define the number of cities
    num_cities = 14
    # Define the mapping of the city names to their indices
    city_names = ['B', 'A', 'M', 'G', 'V', 'J', 'T', 'N', 'W', 'X', 'K', 'Y', 'H', 'C']

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    # The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            # Convert the indices of the cities in the actions to their names
            return [city_names[action] for action in actions]

        # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
        for next_city in range(num_cities):
            # Check if the move is valid, ie if there is a direct road from the current city to the next city
            if adjacency_matrix[state[0]][next_city] == 1:
                # The move is valid, generate the new state
                # The new state is the next city and the remaining cities to visit
                remaining_cities = list(state[1])
                if next_city in remaining_cities:
                    remaining_cities.remove(next_city)
                elif next_city not in actions:
                    remaining_cities.append(next_city)
                new_state = (next_city, tuple(remaining_cities))
                # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of remaining cities to visit
    # The heuristic relaxes the constraint that we can only move to a city directly connected to the current city and presumes we can move to any of the remaining cities in one move
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving to a city is always 1, which is exactly the decrease in the number of remaining cities to visit, if the city is one of the remaining cities to visit, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no remaining cities to visit in the goal state
    return len(state[1])

print(a_star())
