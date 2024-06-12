
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    graph = {
        'J': ['I', 'R', 'M', 'D'],
        'X': ['R', 'T'],
        'U': ['J', 'X', 'T', 'B', 'E'],
        'I': ['U'],
        'R': ['I', 'Y', 'M'],
        'T': ['J', 'I', 'B'],
        'Y': ['I', 'T', 'D'],
        'B': ['X', 'R', 'E'],
        'M': ['I', 'Y'],
        'D': ['X', 'R', 'E'],
        'E': ['J', 'X', 'I', 'M']
    }
    # Define the initial state and the goal state
    initial_state = ('E', 'E', 0, 0)
    goal_state = ('E', 2, 2)

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

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for neighbor in graph[state[0]]:
            # Check if the new state would be valid, ie we can only visit each city once, except for T and Y, which we can visit twice
            if (neighbor not in actions or neighbor in ['T', 'Y']) and (actions.count('T') < 2 or neighbor != 'T') and (actions.count('Y') < 2 or neighbor != 'Y'):
                # Generate the new state
                new_state = (neighbor, neighbor if neighbor in ['T', 'Y'] else state[1], state[2] + 1 if neighbor == 'T' else state[2], state[3] + 1 if neighbor == 'Y' else state[3])
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [neighbor], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each tile from its goal position
    # The heuristic relaxes the constraint that a tile can only be swapped with the empty spot and presumes we can move the tiles to their goal position by swapping them with any of the other tiles
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving a tile to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state.
    h = 0
    # The heuristic is the sum of the number of visits remaining to T and Y
    h += 2 - state[2]
    h += 2 - state[3]
    return h

print(a_star())
