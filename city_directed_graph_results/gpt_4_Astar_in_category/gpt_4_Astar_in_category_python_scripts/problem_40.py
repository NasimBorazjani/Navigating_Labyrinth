
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]]

    # Define the city names
    city_names = ['R', 'L', 'F', 'E', 'D', 'Q', 'G', 'U', 'H', 'T', 'Z', 'A']

    # Define the initial state and goal state
    initial_state = (2, 0, 0, [False]*12, [2])  # The third parameter is the number of times we have visited city R and A
    goal_state = (2, 2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the path required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [2], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return [city_names[i] for i in path]

        # Generate all valid actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(12):
            if adjacency_matrix[state[0]][i] == 1 and not state[3][i] and (i != 0 or state[1] < 2) and (i != 11 or state[2] < 2):
                # The actions is valid, generate the new state
                new_state = list(state)
                new_state[0] = i
                new_state[3] = list(state[3])
                new_state[3][i] = True
                if i == 0:
                    new_state[1] += 1
                if i == 11:
                    new_state[2] += 1
                new_state = tuple(new_state)
                # The cost so far is the number of actions made, as our objective is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [i], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of cities we still need to visit
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to any city
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic estimate, if the city is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the number of cities we still need to visit would be 0 in the goal state.
    return 12 - sum(state[3]) + (2 - state[1]) + (2 - state[2])


print(a_star())
