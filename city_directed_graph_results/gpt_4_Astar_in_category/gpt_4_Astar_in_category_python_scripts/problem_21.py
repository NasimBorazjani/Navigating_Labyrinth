
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]]

    # Define the city names
    city_names = ['I', 'K', 'D', 'M', 'Y', 'H', 'C', 'R', 'V', 'W', 'Q']

    # Define the initial state and goal state
    initial_state = ('Y', False, False)
    goal_state = ('Y', True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['Y'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        current_city_index = city_names.index(state[0])
        for i in range(len(city_names)):
            # Check if there is a road from the current city to the city at index i
            if adjacency_matrix[current_city_index][i] == 1:
                # Generate the new state
                new_city = city_names[i]
                visited_I = state[1] or new_city == 'I'
                visited_Q = state[2] or new_city == 'Q'
                new_state = (new_city, visited_I, visited_Q)

                # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that we still need to visit
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to any city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if the city is one of the cities we still need to visit, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no cities left to visit in the goal state.
    h = 0
    if not state[1]:
        h += 1
    if not state[2]:
        h += 1
    return h

print(a_star())
