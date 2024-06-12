
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = {
        'I': ['E', 'Z', 'Q'],
        'V': ['H'],
        'F': ['I', 'E', 'A'],
        'E': ['I', 'Y'],
        'Y': ['I', 'F', 'Z', 'Q'],
        'A': ['I', 'V'],
        'Z': ['I', 'F', 'E', 'Q'],
        'T': ['V', 'F', 'E', 'Y', 'A', 'Z'],
        'H': ['I', 'T'],
        'Q': ['Z', 'T', 'H']
    }

    # Define the initial state and the goal state
    initial_state = ('V', False, False, False, False)
    goal_state = ('V', True, True, True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['V'], initial_state)]

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
            if neighbor not in path or (neighbor in ['I', 'Y'] and state[path.index(neighbor) + 1] == False):
                # Generate the new state
                new_state = list(state)
                new_state[0] = neighbor
                if neighbor == 'I':
                    new_state[1] = not new_state[1]
                elif neighbor == 'Y':
                    new_state[2] = not new_state[2]
                new_state = tuple(new_state)
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [neighbor], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited twice
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each destination city must be visited at least twice
    # It's consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city and has not been visited twice yet
    return sum(state[1:] != goal[1:])

print(a_star())
