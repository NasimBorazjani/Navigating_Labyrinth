
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = {
        'A': ['M', 'O', 'E', 'G', 'P'],
        'N': ['Q', 'P'],
        'B': ['Z', 'Q', 'G'],
        'M': ['N', 'E'],
        'Z': ['O', 'Q'],
        'O': ['M', 'E', 'Q', 'L'],
        'E': ['A', 'B', 'M', 'Z', 'G', 'P'],
        'Q': ['M'],
        'G': ['N', 'M', 'Q', 'L'],
        'L': ['N', 'Q', 'G', 'P'],
        'P': ['E', 'L']
    }

    # Define the initial state and the goal state
    initial_state = ('B', False, False, ['B'])
    goal_state = ('B', True, True, [])

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, initial_state)]

    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state[:3] == goal_state[:3]:
            return state[3]

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in adjacency_matrix[state[0]]:
            # Check if the new state is valid, ie if the city has not been visited before, or if it is one of the destination cities
            if neighbor not in state[3] or neighbor in ['E', 'N']:
                # Generate the new state
                visited_E = state[1] or neighbor == 'E'
                visited_N = state[2] or neighbor == 'N'
                new_state = (neighbor, visited_E, visited_N, state[3] + [neighbor])

                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities not yet visited
    # The heuristic relaxes the constraint that we can only visit each city once and presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is always 1, the decrease in the number of destination cities not yet visited
    return sum([goal[1] and not state[1], goal[2] and not state[2]])

print(a_star())
