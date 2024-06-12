
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    city_map = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
                [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    # Define the city names
    city_names = ['S', 'E', 'D', 'Y', 'F', 'B', 'O', 'H', 'U', 'I', 'C', 'Q', 'Z', 'J']

    # Define the initial state and goal state
    initial_state = (6, 0, 0)  # (current city, visited B, visited H)
    goal_state = (6, 2, 2)  # (current city, visited B twice, visited H twice)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [city_names[initial_state[0]]], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for next_city in range(len(city_map)):
            # Check if the next city is connected to the current city
            if city_map[state[0]][next_city] == 1:
                # Check if the next city is B or H, and if it has been visited less than twice
                if (next_city == 5 and state[1] < 2) or (next_city == 7 and state[2] < 2):
                    # Generate the new state
                    new_state = (next_city, state[1] + (next_city == 5), state[2] + (next_city == 7))
                # If the next city is not B or H, and it has not been visited before
                elif next_city not in path and next_city != 5 and next_city != 7:
                    new_state = (next_city, state[1], state[2])
                else:
                    continue

                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [city_names[new_state[0]]], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of times we still need to visit B and H
    # The heuristic relaxes the constraints that we can only visit each city once and that we can only move to cities that are directly connected to the current city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is 1, which is exactly the decrease in the heuristic if we move to B or H
    return goal[1] - state[1] + goal[2] - state[2]


print(a_star())
