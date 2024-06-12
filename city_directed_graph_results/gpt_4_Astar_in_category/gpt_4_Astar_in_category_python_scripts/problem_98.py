
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    city_map = [[0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]]

    # Define the city names
    city_names = ['B', 'X', 'F', 'Q', 'V', 'D', 'A', 'J', 'N', 'M', 'G', 'H', 'K', 'T', 'S']

    # Define the initial state and goal state
    initial_state = (5, False, False, ['D'])
    goal_state = (5, True, True)

    # Define the visited costs
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Define the queue
    queue = [(0, 0, initial_state)]

    while queue:
        _, g, state = heapq.heappop(queue)

        # Unpack the state
        current_city, visited_X, visited_J, path = state

        # Check if the current state is the goal state
        if (current_city, visited_X, visited_J) == goal_state:
            return path

        # Generate all possible actions from the current state
        for next_city in range(len(city_map)):
            # Check if there is a road from the current city to the next city
            if city_map[current_city][next_city] == 1:
                # Check if the next city is X or J
                if city_names[next_city] == 'X':
                    new_visited_X = True
                else:
                    new_visited_X = visited_X

                if city_names[next_city] == 'J':
                    new_visited_J = True
                else:
                    new_visited_J = visited_J

                # Check if the next city has been visited before
                if city_names[next_city] not in path or (new_visited_X and new_visited_J):
                    new_state = (next_city, new_visited_X, new_visited_J, path + [city_names[next_city]])
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, new_state))

    return None

def heuristic(state, goal_state):
    # The heuristic function can be the number of cities that have not been visited yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal
    # It is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal
    return sum(1 for visited in state[1:3] if not visited)

print(a_star())
