
import heapq


def initialize():
    # Define the adjacency matrix of the cities and the goal states
    adj_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0]
    ]
    start = 'Y'
    goal_states = {'E': 2, 'M': 2}
    num_cities = 12

    # Initialize the visited costs and the priority queue
    visited_costs = {start: 0}
    queue = [(0, 0, [start], start)]

    return adj_matrix, num_cities, visited_costs, queue, goal_states


def a_star():
    adj_matrix, num_cities, visited_costs, queue, goal_states = initialize()

    while queue:
        _, g, path, state = heapq.heappop(queue)

        # Check if we have reached a goal state
        if all(goal_states[city] <= path.count(city) for city in goal_states):
            return path

        # Generate all possible actions from the current state
        for i in range(num_cities):
            if adj_matrix[state][i] == 1 and path.count(chr(i + 65)) < goal_states.get(chr(i + 65), 1):
                # Compute the new state and the cost
                new_state = chr(i + 65)
                new_cost = g + 1

                # Check if the new state is valid
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the straight-line distance to the goal state
                    h = heuristic(new_state, goal_states)
                    heapq.heappush(queue, (new_cost + h, new_cost, path + [new_state], new_state))

    return None


def heuristic(state, goal_states):
    # The heuristic is the straight-line distance to the goal state
    return sum(abs(ord(state) - ord(city)) for city in goal_states)


print(a_star())
