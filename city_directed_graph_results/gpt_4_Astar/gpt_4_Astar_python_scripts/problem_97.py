
import heapq

def a_star():
    # Define the initial state and the goal state of the puzzle
    initial_state = 'Q'
    goal_state = ['N', 'N', 'Y', 'Y']

    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'R': {'J': 1, 'A': 1},
        'Y': {'R': 1, 'W': 1, 'A': 1, 'O': 1, 'U': 1, 'V': 1, 'X': 1},
        'W': {'E': 1},
        'H': {'Y': 1, 'O': 1, 'E': 1, 'P': 1},
        'J': {'Y': 1, 'W': 1, 'H': 1, 'O': 1, 'U': 1, 'L': 1},
        'A': {'W': 1, 'N': 1, 'E': 1},
        'O': {'R': 1, 'W': 1, 'J': 1, 'Q': 1, 'V': 1},
        'N': {'R': 1, 'Y': 1, 'A': 1, 'E': 1, 'P': 1},
        'U': {'W': 1, 'H': 1},
        'E': {'Y': 1, 'W': 1, 'H': 1, 'O': 1, 'X': 1},
        'Q': {'R': 1, 'O': 1, 'E': 1},
        'L': {'R': 1, 'W': 1, 'A': 1},
        'P': {'Y': 1, 'N': 1, 'U': 1, 'E': 1},
        'V': {'H': 1, 'J': 1, 'L': 1, 'P': 1},
        'X': {'H': 1, 'A': 1, 'N': 1, 'Q': 1, 'V': 1}
    }

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state, goal_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state, goal = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if not goal:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
        for next_city in adjacency_matrix[state]:
            # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
            new_cost = g + 1

            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
            if next_city in goal:
                new_goal = list(goal)
                new_goal.remove(next_city)
                heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], next_city, new_goal))
            elif next_city not in actions:
                heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], next_city, goal))

    return None

print(a_star())
