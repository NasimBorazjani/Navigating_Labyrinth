
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                        [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0]]

    # Define the city names
    city_names = ['S', 'Z', 'I', 'R', 'P', 'T', 'X', 'B', 'F', 'A', 'L', 'M', 'G', 'N', 'E']

    # Define the initial state and goal state
    initial_state = (4, 0, 0)  # (current city, visited I, visited N)
    goal_state = (4, 2, 2)  # (current city, visited I twice, visited N twice)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element.
    queue = [(0, 0, [initial_state[0]])]  # (priority, cost so far, path)

    while queue:
        _, g, path = heapq.heappop(queue)
        state = path[-1]

        if state == goal_state:
            return [city_names[i] for i in path]

        for i in range(15):  # for each city
            if adjacency_matrix[state[0]][i] == 1:  # if there is a road from current city to city i
                visited_I = state[1] + (i == 2)  # increment visited_I if city i is I
                visited_N = state[2] + (i == 13)  # increment visited_N if city i is N
                new_state = (i, visited_I, visited_N)

                # Check if the new state is valid
                if visited_I <= 2 and visited_N <= 2 and (i not in path or i == 2 or i == 13):
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state]))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of times we still need to visit I and N
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as we need to visit I and N at least as many times as the heuristic estimates
    # This heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal
    return goal[1] - state[1] + goal[2] - state[2]


print(a_star())
