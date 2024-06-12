
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    # Define the city names
    city_names = ['J', 'U', 'X', 'R', 'L', 'Z', 'O', 'F', 'Q', 'C', 'N', 'V', 'M']

    # Define the initial state and goal state
    initial_state = (0, False, False, [False]*13, [city_names.index('J')])
    goal_state = (2, True, True, [False]*13)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[:3] == goal_state:
            return [city_names[i] for i in state[3]]

        # Generate all valid actions from the current state, which includes moving to any of the cities connected to the current city
        for next_city in range(13):
            if adjacency_matrix[state[3][-1]][next_city] == 1 and (not state[2][next_city] or city_names[next_city] in ['Z', 'M']):
                # The actions is valid, generate the new state
                new_state = list(state)
                new_state[3] = list(new_state[3])
                new_state[3].append(next_city)
                new_state[2] = list(new_state[2])
                new_state[2][next_city] = True
                if city_names[next_city] == 'Z':
                    new_state[0] += 1
                if city_names[next_city] == 'M':
                    new_state[1] += 1
                new_state = tuple(new_state)
                # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state 
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, new_state))

    return None

print(a_star())
