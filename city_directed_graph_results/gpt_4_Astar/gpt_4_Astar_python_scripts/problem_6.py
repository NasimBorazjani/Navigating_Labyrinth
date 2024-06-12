
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries, where the keys of the outer dictionary are the cities and the values are dictionaries with keys as the cities that can be reached from the current city and values as the travel time to that city
    adjacency_matrix = {'F': {'J': 1, 'K': 1, 'M': 1},
                        'I': {'F': 1, 'B': 1},
                        'O': {'J': 1, 'D': 1, 'M': 1, 'B': 1},
                        'J': {'F': 1, 'O': 1},
                        'K': {'O': 1, 'D': 1},
                        'D': {'I': 1, 'O': 1, 'R': 1},
                        'N': {'I': 1, 'R': 1},
                        'R': {'J': 1, 'M': 1},
                        'M': {'F': 1, 'I': 1, 'J': 1},
                        'B': {'F': 1, 'O': 1, 'M': 1}}
    # Define the initial state as a tuple with the current city, the cities visited so far, and the number of times the destination cities have been visited
    initial_state = ('N', frozenset(['N']), frozenset())
    # Define the goal state as a tuple with the current city, the cities visited so far, and the number of times the destination cities have been visited
    goal_state = ('N', frozenset(['N', 'F', 'I', 'O', 'J', 'K', 'D', 'R', 'M', 'B']), frozenset(['F', 'F', 'D', 'D']))

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

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities that can be reached from the current city
        for next_city in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie the city must not have been visited before, unless it is a destination city and it has not been visited twice already
            if (next_city not in state[1] or (next_city in ['F', 'D'] and state[2].count(next_city) < 2)):
                # Generate the new state
                new_state = (next_city, state[1] | {next_city}, state[2] + (next_city if next_city in ['F', 'D'] else ''))
                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [next_city], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of cities that have not been visited yet, plus the number of times the destination cities have not been visited
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once and each destination city must be visited at least twice
    # It is consistent because the cost of moving to a new city is always 1, which is exactly the decrease in the heuristic cost, if the city is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all cities have been visited and the destination cities have been visited twice
    h = len(goal[1] - state[1]) + goal[2].count('F') + goal[2].count('D') - state[2].count('F') - state[2].count('D')
    return h

print(a_star())
