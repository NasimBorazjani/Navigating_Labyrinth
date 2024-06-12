
import heapq

def a_star():
    # Define the adjacency matrix of the graph, with each row and column representing a city, and a '1' signifies a direct road from the city of the row to the city of the column
    graph = {
        'G': ['H'],
        'D': ['P'],
        'X': ['G', 'Y', 'W'],
        'N': ['W', 'A', 'H'],
        'Y': ['X', 'N', 'A'],
        'W': ['X'],
        'A': ['G', 'D', 'X', 'V', 'H'],
        'P': ['G', 'Y', 'H'],
        'V': ['G', 'P'],
        'H': ['G', 'D', 'N', 'A', 'P']
    }

    # Define the initial state and the goal state
    initial_state = ('W', False, False, ['W'])
    goal_state = (True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        current_city, visited_A, visited_H, path = state

        # If we have visited both A and H twice, and the current city is either A or H, we have reached the goal state
        if (visited_A, visited_H) == goal_state and (current_city == 'A' or current_city == 'H'):
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in graph[current_city]:
            # If we have not visited the neighbor city before, or the neighbor city is A or H and we have visited it less than 2 times, we can move to the neighbor city
            if (neighbor not in path) or (neighbor == 'A' and not visited_A) or (neighbor == 'H' and not visited_H):
                # Generate the new state
                visited_A_new = visited_A or neighbor == 'A'
                visited_H_new = visited_H or neighbor == 'H'
                new_state = (neighbor, visited_A_new, visited_H_new, path + [neighbor])
                # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities (A and H) not yet visited twice
    # The heuristic relaxes the constraints that we can only move to neighboring cities and that we can only visit each city once (except for A and H), ie It presumes we can move directly to any given city
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is always 1, the decrease in the number of destination cities not yet visited twice
    visited_A, visited_H = state[1], state[2]
    return 2 - visited_A - visited_H

print(a_star())
