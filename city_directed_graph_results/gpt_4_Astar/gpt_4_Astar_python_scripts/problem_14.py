
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the travel time (1 for all cities)
    adjacency_matrix = {'M': {'Z': 1},
                        'U': {'M': 1, 'F': 1, 'P': 1},
                        'B': {'M': 1, 'U': 1, 'V': 1, 'E': 1},
                        'F': {'B': 1, 'H': 1},
                        'V': {'F': 1, 'P': 1},
                        'Z': {'U': 1, 'B': 1, 'V': 1, 'H': 1},
                        'P': {'M': 1, 'V': 1},
                        'N': {'U': 1, 'B': 1, 'Z': 1, 'E': 1},
                        'E': {'M': 1, 'Z': 1},
                        'H': {'M': 1, 'B': 1, 'V': 1, 'Z': 1}}

    # Define the initial state as a tuple with the current city, the cities visited so far (including the current city), and the number of times the destination cities have been visited
    initial_state = ('N', {'N'}, {'M': 0, 'H': 0})

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
        # The goal state is where the destination cities have been visited twice
        if state[2]['M'] == 2 and state[2]['H'] == 2:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is a destination city and it has been visited less than 2 times
            if (next_city not in state[1] or (next_city in ['M', 'H'] and state[2][next_city] < 2)):
                # Generate the new state
                new_state = (next_city, state[1] | {next_city}, state[2].copy())
                # Increment the visit count of the destination cities
                if next_city in ['M', 'H']:
                    new_state[2][next_city] += 1
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
    return None

def heuristic(state):
    # An admissible and consistent heuristic for this problem is the number of destination cities that have not been visited twice
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited destination city must be visited at least once
    # It's consistent because moving to a new city reduces the heuristic cost of the successor node by a max of 1 (if the new city is a destination city that has not been visited twice), which is equal to the cost of reaching the successor node
    return 2 - state[2]['M'] - state[2]['H']

print(a_star())
