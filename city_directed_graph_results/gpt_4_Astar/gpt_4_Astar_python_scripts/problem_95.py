
import heapq

def a_star():
    # Define the adjacency matrix of the graph
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
                        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
                        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
                        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
                        [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
                        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], 
                        [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0], 
                        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
                        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
                        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]
    # Define the cities
    cities = ['E', 'K', 'G', 'C', 'U', 'A', 'J', 'O', 'N', 'R', 'W', 'M', 'B', 'H', 'Q']
    # Define the initial state and the goal state
    initial_state = ('C', ['E', 'Q'], ['E', 'Q'])
    goal_state = ('C', [], [])
    # Define the visited costs
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Define the queue
    queue = [(0, 0, [], initial_state)]
    # While there are unvisited states
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions
        if state == goal_state:
            return actions
        # Generate all possible actions from the current state
        for i in range(len(cities)):
            if adjacency_matrix[cities.index(state[0])][i] == 1:
                new_state = list(state)
                new_state[0] = cities[i]
                if cities[i] in new_state[1]:
                    new_state[1].remove(cities[i])
                elif cities[i] in new_state[2]:
                    new_state[2].remove(cities[i])
                new_state = tuple(new_state)
                new_cost = g + 1
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, goal_state)
                    heapq.heappush(queue, (new_cost + h, new_cost, actions + [cities[i]], new_state))
    return None

def heuristic(state, goal):
    # The heuristic function can be the number of cities that still need to be visited
    return len(state[1]) + len(state[2])

print(a_star())
