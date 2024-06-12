
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    city_map = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]]

    # Define the names of the cities
    city_names = ['S', 'X', 'Y', 'Q', 'O', 'R', 'D', 'V', 'H', 'J', 'F', 'C']

    # Define the initial state and goal state
    initial_state = (3, 0, 0)  # (current city, visited V, visited F)
    goal_state = (3, 2, 2)  # (current city, visited V twice, visited F twice)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [city_names[initial_state[0]]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for new_city in range(len(city_map)):
            # Check if the new city is connected to the current city and if it has not been visited before
            if city_map[state[0]][new_city] == 1 and city_names[new_city] not in path:
                # Generate the new state
                visited_v = state[1]
                visited_f = state[2]
                # If the new city is V or F, increment the visited count
                if city_names[new_city] == 'V':
                    visited_v += 1
                elif city_names[new_city] == 'F':
                    visited_f += 1
                new_state = (new_city, visited_v, visited_f)
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_city]], new_state))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities left to visit
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to any city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the number of cities left to visit, if the city is moved toward is one of the cities left to visit, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as there are no cities left to visit in the goal state.
    return goal[1] - state[1] + goal[2] - state[2]


print(a_star())
