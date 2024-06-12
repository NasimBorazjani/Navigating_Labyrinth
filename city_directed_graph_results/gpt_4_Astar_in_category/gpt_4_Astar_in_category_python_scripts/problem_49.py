
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = {
        'W': ['Y', 'K', 'Q'],
        'D': ['A', 'E'],
        'R': ['W', 'C'],
        'A': ['D', 'R', 'Y', 'S', 'N'],
        'Y': ['Q'],
        'F': ['W', 'R', 'S'],
        'C': ['D', 'Y', 'F', 'S', 'N', 'E', 'Q'],
        'S': ['W', 'D', 'Y', 'N'],
        'N': ['D', 'R', 'A', 'F', 'C', 'Q'],
        'E': ['K'],
        'K': ['A', 'F', 'N'],
        'Q': ['D', 'A', 'S', 'N', 'E']
    }

    # Define the initial state and goal state
    initial_state = ('E', False, False, False, False)
    goal_state = ('E', True, True, True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['E'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in adjacency_matrix[state[0]]:
            # Check if the new state would be valid, ie if the city has not been visited before, or if it is one of the destination cities
            if neighbor not in path or neighbor in ['D', 'R']:
                # Generate the new state
                new_state = list(state)
                new_state[0] = neighbor
                # If the city is one of the destination cities, increment the count of visits to that city
                if neighbor == 'D':
                    new_state[1] = not new_state[1]
                elif neighbor == 'R':
                    new_state[2] = not new_state[2]
                new_state = tuple(new_state)
                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [neighbor], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited twice
    # The heuristic relaxes the constraint that we can only visit each city once, and presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is always 1, the decrease in the number of destination cities not yet visited twice
    return sum(goal[1:]) - sum(state[1:])

print(a_star())
