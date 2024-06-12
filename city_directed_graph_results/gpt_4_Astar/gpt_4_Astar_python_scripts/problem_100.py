
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
                        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]]
    # Define the cities
    cities = ['I', 'A', 'Y', 'K', 'F', 'H', 'W', 'D', 'L', 'U', 'N', 'R', 'Z', 'V', 'X']
    # Define the initial state and the goal state
    initial_state = ('R', ['N', 'X'], ['N', 'X'])
    goal_state = ('R', [], [])
    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Define the queue
    queue = [(0, 0, [], initial_state)]
    # While there are unvisited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions
        if state == goal_state:
            return actions
        # Generate all possible actions from the current state
        for i in range(len(cities)):
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                new_city = cities[i]
                new_state = (new_city, state[1][:], state[2][:])
                if new_city in new_state[1]:
                    new_state[1].remove(new_city)
                elif new_city in new_state[2]:
                    new_state[2].remove(new_city)
                # If the new state is valid
                if new_state not in visited_costs or g + 1 < visited_costs[new_state]:
                    visited_costs[new_state] = g + 1
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (g + 1 + h, g + 1, actions + [new_city], new_state))
    return None

def heuristic(state, goal_state):
    # The heuristic function is the sum of the number of cities that need to be visited
    return len(state[1]) + len(state[2])

print(a_star())
