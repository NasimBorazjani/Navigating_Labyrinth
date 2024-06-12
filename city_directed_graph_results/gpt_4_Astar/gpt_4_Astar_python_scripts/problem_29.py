
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the cost to reach that city
    adjacency_matrix = {'R': {'E': 1, 'D': 1, 'J': 1},
                        'S': {'W': 1, 'G': 1, 'N': 1, 'J': 1},
                        'W': {'R': 1},
                        'B': {'P': 1, 'J': 1},
                        'P': {'S': 1, 'D': 1},
                        'G': {'B': 1},
                        'Q': {'W': 1, 'B': 1, 'P': 1, 'N': 1, 'D': 1},
                        'E': {'R': 1, 'S': 1, 'P': 1, 'G': 1, 'Q': 1},
                        'N': {'P': 1, 'G': 1, 'D': 1},
                        'D': {'W': 1, 'E': 1},
                        'J': {'S': 1, 'P': 1, 'Q': 1}}
    # Define the initial state as a tuple with the current city, the cities visited so far, and the number of times the destination cities have been visited
    initial_state = ('G', set(['G']), {'E': 0, 'S': 0})
    # Define the goal state as a tuple with the current city as 'G', the cities visited so far as all the cities, and the number of times the destination cities have been visited as 2
    goal_state = ('G', set(['R', 'S', 'W', 'B', 'P', 'G', 'Q', 'E', 'N', 'D', 'J']), {'E': 2, 'S': 2})

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path to get to each state in a list; the path to reach the initial state is just the initial city
    queue = [(0, 0, ['G'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path taken to reach the goal state
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is a destination city and it has been visited less than 2 times
            if (next_city not in state[1] or (next_city in ['E', 'S'] and state[2][next_city] < 2)):
                # Generate the new state
                new_state = (next_city, state[1] | set([next_city]), state[2].copy())
                # If the next city is a destination city, increment the count of times it has been visited
                if next_city in ['E', 'S']:
                    new_state[2][next_city] += 1
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the number of destination cities that have not been visited twice yet, as we need to visit each destination city at least once more
                    h = 2 - new_state[2]['E'] + 2 - new_state[2]['S']
                    heapq.heappush(queue, (new_cost + h, new_cost, path + [next_city], new_state))
    return None

print(a_star())
