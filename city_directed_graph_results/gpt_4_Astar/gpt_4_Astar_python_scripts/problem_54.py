
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'G': ['T', 'K', 'Y', 'P'],
        'T': ['A', 'E'],
        'M': ['G', 'T'],
        'U': ['G', 'M'],
        'K': ['T', 'U', 'D', 'P', 'I'],
        'Y': ['M', 'U', 'K', 'D'],
        'D': ['M', 'I'],
        'A': ['G', 'U', 'Y', 'D'],
        'P': ['M', 'D', 'S', 'I'],
        'R': ['U', 'E'],
        'E': ['K', 'R'],
        'S': ['T', 'K', 'P'],
        'I': ['U', 'Y', 'E']
    }
    # Define the initial state and the goal state
    initial_state = ('R', frozenset(['A', 'Y']), 2, 2)
    goal_state = ('R', frozenset(), 0, 0)

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

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        current_city, visited_cities, num_A, num_Y = state
        for next_city in graph[current_city]:
            # Check if the new state would be valid, ie we can only visit each city once, except for A and Y which we can visit twice
            if (next_city not in visited_cities or (next_city == 'A' and num_A > 0) or (next_city == 'Y' and num_Y > 0)):
                # Generate the new state
                new_visited_cities = visited_cities | {next_city}
                new_num_A = num_A - 1 if next_city == 'A' else num_A
                new_num_Y = num_Y - 1 if next_city == 'Y' else num_Y
                new_state = (next_city, new_visited_cities, new_num_A, new_num_Y)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities left to visit
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once
    # It's consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is moved toward its goal position
    _, visited_cities, num_A, num_Y = state
    return len(goal[1] - visited_cities) + num_A + num_Y

print(a_star())
