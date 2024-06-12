
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'I': {'F': 1, 'H': 1, 'W': 1, 'D': 1, 'L': 1, 'U': 1, 'N': 1, 'R': 1, 'Z': 1, 'V': 1},
        'A': {'I': 1, 'K': 1, 'N': 1, 'R': 1, 'Z': 1},
        'Y': {'H': 1, 'W': 1, 'Z': 1, 'V': 1},
        'K': {'D': 1, 'L': 1, 'U': 1, 'N': 1},
        'F': {'A': 1, 'K': 1, 'H': 1, 'D': 1, 'L': 1, 'U': 1, 'N': 1, 'R': 1, 'Z': 1, 'V': 1},
        'H': {'I': 1, 'W': 1, 'L': 1, 'U': 1, 'N': 1, 'R': 1, 'Z': 1, 'V': 1},
        'W': {'I': 1, 'K': 1, 'F': 1, 'D': 1, 'L': 1, 'U': 1, 'N': 1, 'R': 1, 'Z': 1, 'V': 1},
        'D': {'A': 1, 'Y': 1, 'K': 1, 'F': 1, 'H': 1, 'W': 1, 'L': 1, 'U': 1, 'N': 1, 'R': 1, 'Z': 1, 'V': 1},
        'L': {'A': 1, 'Y': 1, 'K': 1, 'F': 1, 'H': 1, 'W': 1, 'D': 1, 'U': 1, 'N': 1, 'R': 1, 'Z': 1, 'V': 1},
        'U': {'A': 1, 'Y': 1, 'K': 1, 'F': 1, 'H': 1, 'W': 1, 'D': 1, 'L': 1, 'N': 1, 'R': 1, 'Z': 1, 'V': 1},
        'N': {'A': 1, 'Y': 1, 'K': 1, 'F': 1, 'H': 1, 'W': 1, 'D': 1, 'L': 1, 'U': 1, 'R': 1, 'Z': 1, 'V': 1},
        'R': {'A': 1, 'K': 1, 'F': 1, 'H': 1, 'W': 1, 'D': 1, 'L': 1, 'U': 1, 'N': 1, 'Z': 1, 'V': 1},
        'Z': {'A': 1, 'K': 1, 'F': 1, 'H': 1, 'W': 1, 'D': 1, 'L': 1, 'U': 1, 'N': 1, 'R': 1, 'V': 1},
        'V': {'A': 1, 'Y': 1, 'F': 1, 'H': 1, 'W': 1, 'D': 1, 'L': 1, 'U': 1, 'N': 1, 'R': 1, 'Z': 1},
        'X': {'Y': 1, 'K': 1, 'F': 1, 'H': 1, 'W': 1, 'D': 1, 'L': 1, 'U': 1, 'N': 1, 'R': 1, 'Z': 1, 'V': 1}
    }

    # Define the initial state, goal state, and other variables
    initial_state = 'R'
    goal_state = ['N', 'X']
    num_visits = 2

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state, num_visits)]

    while queue:
        _, g, actions, current_city, visits_left = heapq.heappop(queue)

        # If we have visited both destination cities twice, return the path
        if visits_left == 0 and current_city in goal_state:
            return actions

        # Generate all possible actions from the current city
        for next_city, road in adjacency_matrix[current_city].items():
            # Check if the next city has not been visited before
            if next_city not in actions:
                new_visits_left = visits_left
                if next_city in goal_state:
                    new_visits_left -= 1
                new_cost = g + road

                if new_cost < visited_costs.get(next_city, float('inf')):
                    visited_costs[next_city] = new_cost
                    heapq.heappush(queue, (new_cost + new_visits_left, new_cost, actions + [next_city], next_city, new_visits_left))

    return None


print(a_star())
